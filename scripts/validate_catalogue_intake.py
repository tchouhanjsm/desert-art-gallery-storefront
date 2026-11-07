#!/usr/bin/env python3
"""Validate a draft, source-neutral DAG catalogue intake package (stdlib only).

This validates local preparation CSVs. It does not import, publish, or modify product data.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
from dataclasses import dataclass
from decimal import Decimal
from pathlib import Path, PurePosixPath, PureWindowsPath
from urllib.parse import urlsplit

HEADERS = {
    "products.csv": [
        "product_id", "source_record_ref", "sku", "title_en",
        "short_description_en", "description_en", "category_candidate",
        "publication_status", "availability_status", "price_amount",
        "price_currency", "price_evidence_reference", "internal_notes",
    ],
    "product-facts.csv": [
        "product_id", "fact_key", "fact_value", "unit",
        "verification_status", "evidence_reference", "public_approval",
    ],
    "product-images.csv": [
        "product_id", "asset_id", "source_relative_path", "image_role",
        "sort_order", "rights_status", "publication_status", "alt_text_en",
    ],
    "product-source-records.csv": [
        "product_id", "source_system", "source_file_sha256", "source_data_row_number",
        "source_record_ref", "source_record_id", "source_sku_raw", "source_title_raw",
        "source_price_raw", "source_currency_raw", "source_quantity_raw",
        "source_materials_raw", "source_tags_raw", "source_variations_raw",
        "reconciliation_status", "internal_notes",
    ],
    "etsy-image-sources.csv": [
        "product_id", "source_record_ref", "source_image_field", "source_image_url",
        "local_asset_id", "rights_status", "download_status", "owner_review_status",
        "internal_notes",
    ],
}
PUBLICATION_STATES = {"draft", "in_review", "approved_for_publication", "published", "archived"}
AVAILABILITY_STATES = {"not_verified", "available", "unavailable", "made_to_order"}
FACT_VERIFICATION_STATES = {"unverified", "source_documented", "owner_verified"}
PUBLIC_APPROVAL_STATES = {"not_reviewed", "approved", "do_not_publish"}
IMAGE_ROLES = {"primary", "detail", "scale", "context", "packaging", "other"}
IMAGE_RIGHTS_STATES = {"unknown", "cleared", "restricted"}
IMAGE_PUBLICATION_STATES = {"pending", "approved", "blocked"}
SOURCE_RECONCILIATION_STATES = {"not_reviewed", "needs_reconciliation", "owner_reconciled"}
SOURCE_SYSTEM = re.compile(r"^[a-z0-9][a-z0-9_-]{0,39}$")
SOURCE_FILE_SHA256 = re.compile(r"^[0-9a-f]{64}$")
SOURCE_DATA_ROW_NUMBER = re.compile(r"^[1-9][0-9]*$")
ETSY_IMAGE_FIELD = re.compile(r"^IMAGE(?:[1-9]|10)$")
ETSY_IMAGE_DOWNLOAD_STATES = {"not_attempted", "downloaded", "blocked"}
ETSY_IMAGE_REVIEW_STATES = {"pending", "accepted", "rejected"}
CURRENCY_CODE = re.compile(r"^[A-Z]{3}$")
DECIMAL_AMOUNT = re.compile(r"^(?:0|[1-9][0-9]*)(?:\.[0-9]+)?$")


@dataclass(frozen=True)
class Issue:
    file: str
    row: int | None
    message: str

    def __str__(self) -> str:
        location = self.file if self.row is None else f"{self.file}:{self.row}"
        return f"{location}: {self.message}"


def _value(row: dict[str, str], field: str) -> str:
    value = row.get(field, "")
    return value.strip() if isinstance(value, str) else ""


def _read_rows(root: Path, filename: str, issues: list[Issue]) -> list[tuple[int, dict[str, str]]]:
    path = root / filename
    if not path.is_file() or path.is_symlink():
        issues.append(Issue(filename, None, "required CSV file is missing or is a symbolic link"))
        return []
    rows: list[tuple[int, dict[str, str]]] = []
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.reader(handle)
            try:
                actual_headers = next(reader)
            except StopIteration:
                issues.append(Issue(filename, 1, "file is empty; expected the documented header row"))
                return []
            if actual_headers != HEADERS[filename]:
                issues.append(Issue(
                    filename, 1,
                    "header row does not match the template; use the exact columns and order documented in docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md",
                ))
                return []
            for line_number, values in enumerate(reader, start=2):
                if not values or not any((value or "").strip() for value in values):
                    continue
                if len(values) != len(actual_headers):
                    issues.append(Issue(filename, line_number, f"expected {len(actual_headers)} columns, found {len(values)}"))
                    continue
                rows.append((line_number, dict(zip(actual_headers, values))))
    except (OSError, UnicodeError, csv.Error) as exc:
        issues.append(Issue(filename, None, f"could not read CSV ({type(exc).__name__})"))
    return rows


def _validate_relative_path(value: str) -> bool:
    if not value or "\\" in value:
        return False
    posix = PurePosixPath(value)
    windows = PureWindowsPath(value)
    if posix.is_absolute() or windows.is_absolute() or windows.drive:
        return False
    return all(part not in {"", ".", ".."} for part in value.split("/"))



PHOTO_AUDIT_HEADERS = {"relative_path", "detected_format", "status", "sha256", "duplicate_group"}


def _load_photo_audit(csv_path: Path, summary_path: Path) -> tuple[dict[str, dict[str, str]], list[Issue]]:
    issues: list[Issue] = []
    csv_file = csv_path.expanduser().resolve()
    summary_file = summary_path.expanduser().resolve()

    for label, path in (("photo-audit.csv", csv_file), ("photo-audit-summary.json", summary_file)):
        if path.is_symlink() or not path.is_file():
            issues.append(Issue(label, None, "required photo-audit report is missing, unreadable or a symbolic link"))
    if issues:
        return {}, issues

    try:
        summary = json.loads(summary_file.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        issues.append(Issue("photo-audit-summary.json", None, f"could not read summary ({type(exc).__name__})"))
        return {}, issues

    if not isinstance(summary, dict):
        issues.append(Issue("photo-audit-summary.json", None, "summary must be a JSON object"))
        return {}, issues
    if summary.get("read_only") is not True:
        issues.append(Issue("photo-audit-summary.json", None, "summary is not marked read_only=true"))
    if summary.get("scan_complete") is not True:
        issues.append(Issue("photo-audit-summary.json", None, "photo audit is incomplete; run a complete read-only scan before cross-checking"))
    if not isinstance(summary.get("image_candidates"), int) or summary.get("image_candidates") < 0:
        issues.append(Issue("photo-audit-summary.json", None, "image_candidates must be a non-negative integer"))

    inventory: dict[str, dict[str, str]] = {}
    try:
        with csv_file.open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None or not PHOTO_AUDIT_HEADERS.issubset(set(reader.fieldnames)):
                issues.append(Issue("photo-audit.csv", 1, f"required columns are {sorted(PHOTO_AUDIT_HEADERS)}"))
                return {}, issues
            for row_number, row in enumerate(reader, start=2):
                relative_path = (row.get("relative_path") or "").strip()
                if not _validate_relative_path(relative_path):
                    issues.append(Issue("photo-audit.csv", row_number, "relative_path is empty or unsafe"))
                    continue
                if relative_path in inventory:
                    issues.append(Issue("photo-audit.csv", row_number, f"duplicate relative_path {relative_path!r}"))
                    continue
                status = (row.get("status") or "").strip()
                if status not in {"ok", "review", "unreadable"}:
                    issues.append(Issue("photo-audit.csv", row_number, f"unsupported audit status {status!r}"))
                    continue
                inventory[relative_path] = {
                    "detected_format": (row.get("detected_format") or "").strip(),
                    "status": status,
                    "sha256": (row.get("sha256") or "").strip(),
                    "duplicate_group": (row.get("duplicate_group") or "").strip(),
                }
    except (OSError, UnicodeError, csv.Error) as exc:
        issues.append(Issue("photo-audit.csv", None, f"could not read inventory ({type(exc).__name__})"))
        return {}, issues

    candidate_count = summary.get("image_candidates")
    if isinstance(candidate_count, int) and candidate_count != len(inventory):
        issues.append(Issue(
            "photo-audit-summary.json", None,
            f"image_candidates ({candidate_count}) does not match inventory CSV rows ({len(inventory)})",
        ))
    return inventory, issues

def _is_allowed_etsy_image_url(value: str) -> bool:
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


def validate_catalogue_directory(directory: Path, photo_audit_csv: Path | None = None, photo_audit_summary: Path | None = None) -> list[Issue]:
    root = directory.expanduser().resolve()
    if not root.exists() or not root.is_dir():
        return [Issue(".", None, "input path does not exist or is not a directory")]

    issues: list[Issue] = []
    product_rows = _read_rows(root, "products.csv", issues)
    fact_rows = _read_rows(root, "product-facts.csv", issues)
    image_rows = _read_rows(root, "product-images.csv", issues)
    source_record_rows = _read_rows(root, "product-source-records.csv", issues)
    etsy_image_source_rows = _read_rows(root, "etsy-image-sources.csv", issues)
    photo_inventory: dict[str, dict[str, str]] | None = None
    if photo_audit_csv is not None and photo_audit_summary is not None:
        photo_inventory, audit_issues = _load_photo_audit(photo_audit_csv, photo_audit_summary)
        issues.extend(audit_issues)
    elif photo_audit_csv is not None or photo_audit_summary is not None:
        issues.append(Issue("photo-audit", None, "--photo-audit-csv and --photo-audit-summary must be provided together"))

    products: dict[str, dict[str, str]] = {}
    seen_skus: dict[str, int] = {}
    for line, row in product_rows:
        product_id = _value(row, "product_id")
        if not product_id:
            issues.append(Issue("products.csv", line, "product_id is required"))
            continue
        if product_id in products:
            issues.append(Issue("products.csv", line, f"duplicate product_id {product_id!r}"))
            continue
        products[product_id] = row

        if not _value(row, "title_en"):
            issues.append(Issue("products.csv", line, "title_en is required; keep customer-facing content in English"))
        publication = _value(row, "publication_status")
        if publication not in PUBLICATION_STATES:
            issues.append(Issue("products.csv", line, f"publication_status must be one of {sorted(PUBLICATION_STATES)}"))
        availability = _value(row, "availability_status")
        if availability not in AVAILABILITY_STATES:
            issues.append(Issue("products.csv", line, f"availability_status must be one of {sorted(AVAILABILITY_STATES)}"))

        sku = _value(row, "sku")
        if sku:
            key = sku.casefold()
            if key in seen_skus:
                issues.append(Issue("products.csv", line, f"sku {sku!r} duplicates row {seen_skus[key]}"))
            else:
                seen_skus[key] = line

        amount = _value(row, "price_amount")
        currency = _value(row, "price_currency")
        price_evidence = _value(row, "price_evidence_reference")
        if any((amount, currency, price_evidence)):
            if not (amount and currency and price_evidence):
                issues.append(Issue(
                    "products.csv", line,
                    "price_amount, price_currency and price_evidence_reference must be supplied together; leave all blank when price is unresolved",
                ))
            else:
                if not DECIMAL_AMOUNT.fullmatch(amount):
                    issues.append(Issue("products.csv", line, "price_amount must be a non-negative plain decimal (no symbols or grouping separators)"))
                else:
                    parsed_amount = Decimal(amount)
                    if not parsed_amount.is_finite():
                        issues.append(Issue("products.csv", line, "price_amount must be finite"))
                if not CURRENCY_CODE.fullmatch(currency):
                    issues.append(Issue("products.csv", line, "price_currency must be a three-letter uppercase currency code"))

    source_records: dict[str, dict[str, str]] = {}
    seen_source_rows: set[tuple[str, str, str]] = set()
    for line, row in source_record_rows:
        product_id = _value(row, "product_id")
        if not product_id or product_id not in products:
            issues.append(Issue("product-source-records.csv", line, f"product_id {product_id!r} does not exist in products.csv"))
        source_system = _value(row, "source_system").lower()
        if not SOURCE_SYSTEM.fullmatch(source_system):
            issues.append(Issue("product-source-records.csv", line, "source_system must be a lowercase source key such as etsy"))
        file_hash = _value(row, "source_file_sha256")
        if not SOURCE_FILE_SHA256.fullmatch(file_hash):
            issues.append(Issue("product-source-records.csv", line, "source_file_sha256 must be a lowercase 64-character SHA-256 digest"))
        data_row = _value(row, "source_data_row_number")
        if not SOURCE_DATA_ROW_NUMBER.fullmatch(data_row):
            issues.append(Issue("product-source-records.csv", line, "source_data_row_number must be a positive logical data-row number"))
        record_ref = _value(row, "source_record_ref")
        expected_ref = f"{source_system}:{file_hash}:row:{data_row}"
        if not record_ref or record_ref != expected_ref:
            issues.append(Issue("product-source-records.csv", line, f"source_record_ref must equal {expected_ref!r}"))
        if not _value(row, "source_title_raw"):
            issues.append(Issue("product-source-records.csv", line, "source_title_raw is required to support manual reconciliation"))
        reconciliation = _value(row, "reconciliation_status")
        if reconciliation not in SOURCE_RECONCILIATION_STATES:
            issues.append(Issue("product-source-records.csv", line, f"reconciliation_status must be one of {sorted(SOURCE_RECONCILIATION_STATES)}"))
        identity = (source_system, file_hash, data_row)
        if identity in seen_source_rows:
            issues.append(Issue("product-source-records.csv", line, f"duplicate source snapshot row {identity!r}"))
        seen_source_rows.add(identity)
        if record_ref:
            if record_ref in source_records:
                issues.append(Issue("product-source-records.csv", line, f"duplicate source_record_ref {record_ref!r}"))
            else:
                source_records[record_ref] = row
        if product_id in products and _value(products[product_id], "source_record_ref") != record_ref:
            issues.append(Issue("product-source-records.csv", line, "products.csv source_record_ref must match this source-record row"))
    for product_id, product in products.items():
        product_ref = _value(product, "source_record_ref")
        if product_ref and product_ref not in source_records:
            issues.append(Issue("products.csv", None, f"source_record_ref {product_ref!r} has no matching product-source-records.csv row"))

    approved_primary_images: set[str] = set()
    seen_asset_links: set[tuple[str, str]] = set()
    seen_sort_orders: set[tuple[str, str]] = set()
    for line, row in fact_rows:
        product_id = _value(row, "product_id")
        if not product_id or product_id not in products:
            issues.append(Issue("product-facts.csv", line, f"product_id {product_id!r} does not exist in products.csv"))
        if not _value(row, "fact_key"):
            issues.append(Issue("product-facts.csv", line, "fact_key is required"))
        if not _value(row, "fact_value"):
            issues.append(Issue("product-facts.csv", line, "fact_value is required; omit unknown facts instead of guessing"))
        verification = _value(row, "verification_status")
        if verification not in FACT_VERIFICATION_STATES:
            issues.append(Issue("product-facts.csv", line, f"verification_status must be one of {sorted(FACT_VERIFICATION_STATES)}"))
        evidence = _value(row, "evidence_reference")
        if verification in {"source_documented", "owner_verified"} and not evidence:
            issues.append(Issue("product-facts.csv", line, "documented/verified facts require an evidence_reference"))
        public_approval = _value(row, "public_approval")
        if public_approval not in PUBLIC_APPROVAL_STATES:
            issues.append(Issue("product-facts.csv", line, f"public_approval must be one of {sorted(PUBLIC_APPROVAL_STATES)}"))
        if public_approval == "approved" and (verification != "owner_verified" or not evidence):
            issues.append(Issue("product-facts.csv", line, "public approval requires owner_verified status and an evidence_reference"))

    for line, row in image_rows:
        product_id = _value(row, "product_id")
        if not product_id or product_id not in products:
            issues.append(Issue("product-images.csv", line, f"product_id {product_id!r} does not exist in products.csv"))
        asset_id = _value(row, "asset_id")
        if not asset_id:
            issues.append(Issue("product-images.csv", line, "asset_id is required"))
        else:
            asset_link = (product_id, asset_id)
            if asset_link in seen_asset_links:
                issues.append(Issue("product-images.csv", line, f"duplicate product_id/asset_id pair {asset_link!r}"))
            seen_asset_links.add(asset_link)

        source_path = _value(row, "source_relative_path")
        if not _validate_relative_path(source_path):
            issues.append(Issue("product-images.csv", line, "source_relative_path must be a normalized relative path without '..', drive letters or absolute roots"))
        role = _value(row, "image_role")
        if role not in IMAGE_ROLES:
            issues.append(Issue("product-images.csv", line, f"image_role must be one of {sorted(IMAGE_ROLES)}"))
        order = _value(row, "sort_order")
        if not order.isdigit() or int(order) < 1:
            issues.append(Issue("product-images.csv", line, "sort_order must be a positive integer"))
        elif product_id:
            sort_key = (product_id, order)
            if sort_key in seen_sort_orders:
                issues.append(Issue("product-images.csv", line, f"sort_order {order} is duplicated for product_id {product_id!r}"))
            seen_sort_orders.add(sort_key)
        rights = _value(row, "rights_status")
        if rights not in IMAGE_RIGHTS_STATES:
            issues.append(Issue("product-images.csv", line, f"rights_status must be one of {sorted(IMAGE_RIGHTS_STATES)}"))
        publication = _value(row, "publication_status")
        if publication not in IMAGE_PUBLICATION_STATES:
            issues.append(Issue("product-images.csv", line, f"publication_status must be one of {sorted(IMAGE_PUBLICATION_STATES)}"))
        alt_text = _value(row, "alt_text_en")
        if photo_inventory is not None and _validate_relative_path(source_path):
            audited = photo_inventory.get(source_path)
            if audited is None:
                issues.append(Issue("product-images.csv", line, "source_relative_path was not found in the completed photo-audit inventory"))
            elif publication == "approved":
                if audited["status"] != "ok":
                    issues.append(Issue("product-images.csv", line, f"an approved image must have photo-audit status=ok (found {audited['status']})"))
                if audited["duplicate_group"]:
                    issues.append(Issue("product-images.csv", line, "an approved image is byte-identical to another asset and requires manual review"))
        if publication == "approved":
            if rights != "cleared":
                issues.append(Issue("product-images.csv", line, "an approved image requires rights_status=cleared"))
            if not alt_text:
                issues.append(Issue("product-images.csv", line, "an approved image requires alt_text_en"))
            if role == "primary" and product_id:
                approved_primary_images.add(product_id)

    local_asset_pairs = seen_asset_links
    seen_etsy_image_fields: set[tuple[str, str]] = set()
    for line, row in etsy_image_source_rows:
        product_id = _value(row, "product_id")
        if not product_id or product_id not in products:
            issues.append(Issue("etsy-image-sources.csv", line, f"product_id {product_id!r} does not exist in products.csv"))
        record_ref = _value(row, "source_record_ref")
        source_record = source_records.get(record_ref)
        if source_record is None:
            issues.append(Issue("etsy-image-sources.csv", line, f"source_record_ref {record_ref!r} does not exist in product-source-records.csv"))
        elif _value(source_record, "source_system").lower() != "etsy":
            issues.append(Issue("etsy-image-sources.csv", line, "Etsy image references must link to an etsy source record"))
        elif _value(source_record, "product_id") != product_id:
            issues.append(Issue("etsy-image-sources.csv", line, "product_id does not match the linked source record"))
        image_field = _value(row, "source_image_field").upper()
        if not ETSY_IMAGE_FIELD.fullmatch(image_field):
            issues.append(Issue("etsy-image-sources.csv", line, "source_image_field must be IMAGE1 through IMAGE10"))
        image_key = (record_ref, image_field)
        if image_key in seen_etsy_image_fields:
            issues.append(Issue("etsy-image-sources.csv", line, f"duplicate source image field {image_key!r}"))
        seen_etsy_image_fields.add(image_key)
        source_url = _value(row, "source_image_url")
        if not _is_allowed_etsy_image_url(source_url):
            issues.append(Issue("etsy-image-sources.csv", line, "source_image_url must be HTTPS on the exact i.etsystatic.com host without credentials or a port"))
        rights = _value(row, "rights_status")
        if rights not in IMAGE_RIGHTS_STATES:
            issues.append(Issue("etsy-image-sources.csv", line, f"rights_status must be one of {sorted(IMAGE_RIGHTS_STATES)}"))
        download = _value(row, "download_status")
        if download not in ETSY_IMAGE_DOWNLOAD_STATES:
            issues.append(Issue("etsy-image-sources.csv", line, f"download_status must be one of {sorted(ETSY_IMAGE_DOWNLOAD_STATES)}"))
        review = _value(row, "owner_review_status")
        if review not in ETSY_IMAGE_REVIEW_STATES:
            issues.append(Issue("etsy-image-sources.csv", line, f"owner_review_status must be one of {sorted(ETSY_IMAGE_REVIEW_STATES)}"))
        local_asset_id = _value(row, "local_asset_id")
        if download == "downloaded":
            if not local_asset_id:
                issues.append(Issue("etsy-image-sources.csv", line, "downloaded source image requires local_asset_id"))
            elif (product_id, local_asset_id) not in local_asset_pairs:
                issues.append(Issue("etsy-image-sources.csv", line, "local_asset_id must match a product-images.csv asset for this product"))
        elif local_asset_id:
            issues.append(Issue("etsy-image-sources.csv", line, "local_asset_id must remain blank until download_status=downloaded"))
        if review == "accepted" and (rights != "cleared" or download != "downloaded" or not local_asset_id):
            issues.append(Issue("etsy-image-sources.csv", line, "an accepted source image requires cleared rights and a downloaded local asset mapping"))

    for product_id, row in products.items():
        if _value(row, "publication_status") in {"approved_for_publication", "published"} and product_id not in approved_primary_images:
            issues.append(Issue(
                "products.csv", None,
                f"product_id {product_id!r} is approved/published but has no approved primary image in product-images.csv",
            ))

    return issues


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a draft DAG product intake package without modifying source CSV files."
    )
    parser.add_argument("directory", type=Path, help="Folder containing products.csv, product-facts.csv and product-images.csv")
    parser.add_argument("--photo-audit-csv", type=Path, help="Optional private CSV inventory produced by audit_photo_library.py")
    parser.add_argument("--photo-audit-summary", type=Path, help="JSON summary from the same complete photo-audit run; required with --photo-audit-csv")
    args = parser.parse_args(argv)
    if bool(args.photo_audit_csv) != bool(args.photo_audit_summary):
        parser.error("--photo-audit-csv and --photo-audit-summary must be used together")
    issues = validate_catalogue_directory(args.directory, args.photo_audit_csv, args.photo_audit_summary)
    if issues:
        print(f"Catalogue intake validation: FAILED ({len(issues)} issue(s))")
        for issue in issues:
            print(f"- {issue}")
        return 1
    print("Catalogue intake validation: PASS")
    print("- Required CSV templates and cross-file references are valid")
    if args.photo_audit_csv:
        print("- Product image paths match a complete, read-only photo-audit inventory")
    print("- No catalogue content was imported or modified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
