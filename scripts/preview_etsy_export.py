#!/usr/bin/env python3
"""Read-only preflight for a private Etsy Listings Download CSV.

No product records are imported, normalized, published or written back to the source file.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit

REQUIRED_HEADERS = {"TITLE", "DESCRIPTION", "PRICE", "CURRENCY_CODE", "QUANTITY"}
IMAGE_HEADER = re.compile(r"^IMAGE(?:[1-9]|10)$")
VARIATION_HEADER = re.compile(r"^VARIATION [1-3] (?:TYPE|NAME|VALUES)$")
MAX_SOURCE_BYTES = 100 * 1024 * 1024


def allowed_etsy_image_url(value: str) -> bool:
    if not value or len(value) > 2048:
        return False
    try:
        parsed = urlsplit(value)
        return (
            parsed.scheme == "https"
            and parsed.hostname is not None
            and parsed.hostname.lower() == "i.etsystatic.com"
            and parsed.username is None
            and parsed.password is None
            and parsed.port is None
            and parsed.path.startswith("/")
        )
    except ValueError:
        return False


def normalize_title(value: str) -> str:
    return " ".join(value.casefold().split())


def preview_etsy_export(source_path: Path) -> tuple[dict[str, object], list[dict[str, object]], bool]:
    source_path = source_path.expanduser().resolve()
    if not source_path.is_file() or source_path.is_symlink():
        raise ValueError("Source CSV must be an existing regular file, not a symbolic link.")

    size = source_path.stat().st_size
    if size > MAX_SOURCE_BYTES:
        raise ValueError(f"Source CSV exceeds the {MAX_SOURCE_BYTES // (1024 * 1024)} MB safety limit.")

    source_bytes = source_path.read_bytes()
    digest = hashlib.sha256(source_bytes).hexdigest()
    try:
        source_text = source_bytes.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValueError("Source CSV must be UTF-8 or UTF-8 with BOM.") from exc

    issues: list[dict[str, object]] = []
    previews: list[dict[str, object]] = []
    fatal = False
    reader = csv.reader(io.StringIO(source_text, newline=""))
    try:
        headers = next(reader)
    except StopIteration:
        headers = []
    normalized_headers = [value.strip().upper() for value in headers]
    header_counts = Counter(normalized_headers)
    duplicate_headers = sorted(name for name, count in header_counts.items() if name and count > 1)
    image_headers = [name for name in normalized_headers if IMAGE_HEADER.fullmatch(name)]
    missing_headers = sorted(REQUIRED_HEADERS - set(normalized_headers))

    if not headers:
        issues.append({"row": None, "field": "header", "code": "empty_file"})
        fatal = True
    if duplicate_headers:
        issues.append({"row": 1, "field": "header", "code": "duplicate_headers", "count": len(duplicate_headers)})
        fatal = True
    if missing_headers:
        issues.append({"row": 1, "field": "header", "code": "missing_required_headers", "count": len(missing_headers)})
        fatal = True
    if not image_headers:
        issues.append({"row": 1, "field": "header", "code": "missing_image_columns"})
        fatal = True

    if fatal:
        summary = {
            "source_filename": source_path.name,
            "source_sha256": digest,
            "source_bytes": size,
            "headers": normalized_headers,
            "source_rows": 0,
            "fatal_structure_error": True,
            "issues": issues,
            "read_only": True,
            "imported": False,
        }
        return summary, previews, True

    variations = [name for name in normalized_headers if VARIATION_HEADER.fullmatch(name)]
    column_index = {name: index for index, name in enumerate(normalized_headers)}
    sku_values: list[str] = []
    title_values: list[str] = []
    row_warnings: dict[int, int] = {}
    currency_counts: Counter[str] = Counter()
    quantity_counts: Counter[str] = Counter()
    image_reference_count = 0
    invalid_image_url_count = 0
    populated_variation_rows = 0
    empty_sku_rows = 0
    empty_title_rows = 0
    empty_description_rows = 0
    source_row_number = 0

    for cells in reader:
        if not cells or not any(cell.strip() for cell in cells):
            continue
        source_row_number += 1
        row_issues = 0
        if len(cells) != len(normalized_headers):
            issues.append({
                "row": source_row_number,
                "field": "row",
                "code": "column_count_mismatch",
                "expected": len(normalized_headers),
                "actual": len(cells),
            })
            row_issues += 1

        values = {
            name: (cells[index].strip() if index < len(cells) else "")
            for name, index in column_index.items()
        }
        title = values.get("TITLE", "")
        description = values.get("DESCRIPTION", "")
        sku = values.get("SKU", "")
        price = values.get("PRICE", "")
        currency = values.get("CURRENCY_CODE", "")
        quantity = values.get("QUANTITY", "")

        if not title:
            empty_title_rows += 1
            issues.append({"row": source_row_number, "field": "TITLE", "code": "blank_title"})
            row_issues += 1
        if not description:
            empty_description_rows += 1
            issues.append({"row": source_row_number, "field": "DESCRIPTION", "code": "blank_description"})
            row_issues += 1
        if not sku:
            empty_sku_rows += 1
        else:
            sku_values.append(sku.casefold())
        if title:
            title_values.append(normalize_title(title))

        if bool(price) != bool(currency):
            issues.append({"row": source_row_number, "field": "PRICE/CURRENCY_CODE", "code": "price_currency_pair_incomplete"})
            row_issues += 1
        if currency:
            currency_counts[currency] += 1
            if not re.fullmatch(r"[A-Z]{3}", currency):
                issues.append({"row": source_row_number, "field": "CURRENCY_CODE", "code": "currency_format_review"})
                row_issues += 1
        if quantity:
            quantity_counts[quantity] += 1
            if not re.fullmatch(r"(?:0|[1-9][0-9]*)", quantity):
                issues.append({"row": source_row_number, "field": "QUANTITY", "code": "quantity_format_review"})
                row_issues += 1

        row_image_count = 0
        row_invalid_image_count = 0
        for field in image_headers:
            url = values.get(field, "")
            if not url:
                continue
            image_reference_count += 1
            row_image_count += 1
            if not allowed_etsy_image_url(url):
                invalid_image_url_count += 1
                row_invalid_image_count += 1
                issues.append({"row": source_row_number, "field": field, "code": "image_url_host_review"})
                row_issues += 1

        has_variations = any(values.get(field, "") for field in variations)
        if has_variations:
            populated_variation_rows += 1

        if row_issues:
            row_warnings[source_row_number] = row_issues
        previews.append({
            "source_data_row_number": source_row_number,
            "source_record_ref": f"etsy:{digest}:row:{source_row_number}",
            "source_title_raw": title,
            "source_sku_raw": sku,
            "source_price_raw": price,
            "source_currency_raw": currency,
            "source_quantity_raw": quantity,
            "populated_image_slots": row_image_count,
            "invalid_image_urls": row_invalid_image_count,
            "has_variation_values": has_variations,
            "row_review_required": bool(row_issues),
        })

    sku_counts = Counter(sku_values)
    duplicate_sku_values = {sku for sku, count in sku_counts.items() if count > 1}
    duplicate_sku_rows = sum(count for count in sku_counts.values() if count > 1)
    title_counts = Counter(title_values)
    repeated_title_groups = sum(1 for count in title_counts.values() if count > 1)
    repeated_title_rows = sum(count for count in title_counts.values() if count > 1)
    for row in previews:
        sku = str(row["source_sku_raw"]).casefold()
        title = normalize_title(str(row["source_title_raw"]))
        row["source_sku_duplicate"] = bool(sku and sku in duplicate_sku_values)
        row["source_sku_occurrences"] = sku_counts.get(sku, 0) if sku else 0
        row["title_occurrences"] = title_counts.get(title, 0) if title else 0

    summary: dict[str, object] = {
        "source_filename": source_path.name,
        "source_sha256": digest,
        "source_bytes": size,
        "headers": normalized_headers,
        "source_rows": source_row_number,
        "currency_counts": dict(sorted(currency_counts.items())),
        "quantity_counts": dict(sorted(quantity_counts.items())),
        "empty_sku_rows": empty_sku_rows,
        "duplicate_sku_groups": len(duplicate_sku_values),
        "duplicate_sku_rows": duplicate_sku_rows,
        "empty_title_rows": empty_title_rows,
        "empty_description_rows": empty_description_rows,
        "distinct_title_count": len(title_counts),
        "repeated_title_groups": repeated_title_groups,
        "repeated_title_rows": repeated_title_rows,
        "image_reference_count": image_reference_count,
        "invalid_image_url_count": invalid_image_url_count,
        "variation_columns": variations,
        "populated_variation_rows": populated_variation_rows,
        "category_column_present": any(name in {"CATEGORY", "CATEGORY_NAME", "SECTION", "SECTION_NAME"} for name in normalized_headers),
        "listing_id_column_present": any(name in {"LISTING_ID", "LISTINGID"} for name in normalized_headers),
        "rows_requiring_review": len(row_warnings),
        "issue_count": len(issues),
        "issues": issues,
        "fatal_structure_error": False,
        "read_only": True,
        "imported": False,
    }
    return summary, previews, False


def _write_json(summary: dict[str, object], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with destination.open("x", encoding="utf-8") as handle:
        handle.write(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")


def _write_rows(rows: list[dict[str, object]], destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "source_data_row_number", "source_record_ref", "source_title_raw", "source_sku_raw",
        "source_sku_duplicate", "source_sku_occurrences", "title_occurrences",
        "source_price_raw", "source_currency_raw", "source_quantity_raw",
        "populated_image_slots", "invalid_image_urls", "has_variation_values", "row_review_required",
    ]
    with destination.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Read-only Etsy Listings Download preflight. No products or images are imported."
    )
    parser.add_argument("source_csv", type=Path, help="Private Etsy Listings Download CSV")
    parser.add_argument("--json", dest="json_path", type=Path, help="Optional private JSON summary path (never overwritten)")
    parser.add_argument("--rows-csv", type=Path, help="Optional private row-level review CSV path (never overwritten)")
    args = parser.parse_args(argv)

    try:
        source = args.source_csv.expanduser().resolve()
        destinations = [
            path.expanduser().resolve()
            for path in (args.json_path, args.rows_csv)
            if path is not None
        ]
        if len({str(path).casefold() for path in destinations}) != len(destinations):
            parser.error("--json and --rows-csv must use different output paths")
        if any(path == source for path in destinations):
            parser.error("Report output paths must not overwrite the source CSV")
        for path in destinations:
            if path.exists():
                parser.error(f"Report already exists; choose a new path: {path}")

        summary, previews, fatal = preview_etsy_export(source)
        if args.json_path:
            _write_json(summary, args.json_path.expanduser().resolve())
        if args.rows_csv:
            _write_rows(previews, args.rows_csv.expanduser().resolve())
    except (OSError, ValueError, csv.Error) as exc:
        print(f"Etsy source preflight failed: {exc}", file=sys.stderr)
        return 2

    print("Etsy source preflight: " + ("FAILED" if fatal else "READ-ONLY PREVIEW"))
    print(f"- Source rows: {summary.get('source_rows', 0)}")
    print(f"- Source SHA-256: {summary.get('source_sha256', '')}")
    print(f"- Duplicate SKU groups: {summary.get('duplicate_sku_groups', 0)}")
    print(f"- Repeated title groups: {summary.get('repeated_title_groups', 0)}")
    print(f"- Image URL references: {summary.get('image_reference_count', 0)}")
    print(f"- Invalid image URL references: {summary.get('invalid_image_url_count', 0)}")
    print(f"- Rows requiring review: {summary.get('rows_requiring_review', 0)}")
    print("- Imported: false")
    return 1 if fatal else 0


if __name__ == "__main__":
    raise SystemExit(main())
