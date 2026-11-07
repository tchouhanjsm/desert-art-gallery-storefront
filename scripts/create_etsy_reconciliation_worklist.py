#!/usr/bin/env python3
"""Create an editable, unassigned reconciliation worklist from a verified Etsy bundle."""
from __future__ import annotations
import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from verify_etsy_review_bundle import verify_review_bundle

VARIATION_HEADER = re.compile(r"^VARIATION [1-3] (?:TYPE|NAME|VALUES)$")
WORKLIST_FIELDS = [
    "source_record_ref", "source_file_sha256", "source_data_row_number",
    "source_title_raw", "source_sku_raw", "source_sku_duplicate",
    "source_sku_occurrences", "title_occurrences", "source_price_raw",
    "source_currency_raw", "source_quantity_raw", "source_materials_raw",
    "source_tags_raw", "source_variations_raw", "image_source_count",
    "proposed_dag_product_id", "identity_match_basis",
    "identity_evidence_reference", "owner_reconciliation_status", "reviewer_notes",
]

def _git_root(path: Path) -> Path | None:
    current = path if path.is_dir() else path.parent
    for candidate in (current, *current.parents):
        marker = candidate / ".git"
        if marker.exists() or marker.is_symlink():
            return candidate
    return None

def create_reconciliation_worklist(bundle_path: Path, output_path: Path) -> dict[str, object]:
    supplied_bundle = bundle_path.expanduser()
    if supplied_bundle.is_symlink():
        raise ValueError("Bundle directory must not be a symbolic link.")
    bundle = supplied_bundle.resolve()
    valid, errors = verify_review_bundle(bundle)
    if not valid:
        raise ValueError("Review bundle failed verification: " + "; ".join(errors))

    expanded_output = output_path.expanduser()
    if expanded_output.is_symlink():
        raise ValueError("Worklist output must not be a symbolic link.")
    output = expanded_output.resolve()
    if output.is_relative_to(bundle):
        raise ValueError("Editable worklist must be outside the immutable source bundle.")
    if _git_root(output.parent):
        raise ValueError("Private worklist output must be outside every Git working tree.")
    if output.exists():
        raise ValueError(f"Worklist output already exists; choose a new path: {output}")
    output.parent.mkdir(parents=True, exist_ok=True)
    if _git_root(output.parent):
        raise ValueError("Private worklist output must be outside every Git working tree.")

    summary = json.loads((bundle / "source-summary.json").read_text(encoding="utf-8"))
    raw_records = []
    with (bundle / "source-rows.jsonl").open("r", encoding="utf-8") as handle:
        for line in handle:
            raw_records.append(json.loads(line))
    with (bundle / "source-row-review.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        review_rows = list(csv.DictReader(handle))
    with (bundle / "image-source-references.csv").open("r", encoding="utf-8-sig", newline="") as handle:
        image_rows = list(csv.DictReader(handle))

    review_by_ref = {row["source_record_ref"]: row for row in review_rows}
    image_counts = Counter(row["source_record_ref"] for row in image_rows)
    source_digest = str(summary["source_sha256"])

    with output.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=WORKLIST_FIELDS)
        writer.writeheader()
        for record in raw_records:
            record_ref = str(record["source_record_ref"])
            raw_fields = record["source_fields"]
            normalized = {str(name).strip().upper(): value for name, value in raw_fields.items()}
            review = review_by_ref[record_ref]
            variations = {
                name: value for name, value in raw_fields.items()
                if VARIATION_HEADER.fullmatch(str(name).strip().upper())
            }
            writer.writerow({
                "source_record_ref": record_ref,
                "source_file_sha256": source_digest,
                "source_data_row_number": record["source_data_row_number"],
                "source_title_raw": normalized.get("TITLE", ""),
                "source_sku_raw": normalized.get("SKU", ""),
                "source_sku_duplicate": review.get("source_sku_duplicate", "False"),
                "source_sku_occurrences": review.get("source_sku_occurrences", "0"),
                "title_occurrences": review.get("title_occurrences", "0"),
                "source_price_raw": normalized.get("PRICE", ""),
                "source_currency_raw": normalized.get("CURRENCY_CODE", ""),
                "source_quantity_raw": normalized.get("QUANTITY", ""),
                "source_materials_raw": normalized.get("MATERIALS", ""),
                "source_tags_raw": normalized.get("TAGS", ""),
                "source_variations_raw": json.dumps(variations, ensure_ascii=False, sort_keys=True),
                "image_source_count": image_counts.get(record_ref, 0),
                "proposed_dag_product_id": "",
                "identity_match_basis": "",
                "identity_evidence_reference": "",
                "owner_reconciliation_status": "unreviewed",
                "reviewer_notes": "",
            })
    return {
        "output_path": str(output),
        "source_rows": len(raw_records),
        "image_reference_rows": len(image_rows),
        "source_sha256": source_digest,
    }

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create an editable private reconciliation worksheet from a verified Etsy review bundle."
    )
    parser.add_argument("bundle_dir", type=Path, help="Private Etsy review bundle directory")
    parser.add_argument("output_csv", type=Path, help="New private CSV output path outside the bundle and Git")
    args = parser.parse_args(argv)
    try:
        result = create_reconciliation_worklist(args.bundle_dir, args.output_csv)
    except (OSError, ValueError, csv.Error, json.JSONDecodeError) as exc:
        print(f"Etsy reconciliation worklist failed: {exc}", file=sys.stderr)
        return 2
    print("Etsy reconciliation worklist: CREATED")
    print(f"- Output: {result['output_path']}")
    print(f"- Source rows: {result['source_rows']}")
    print(f"- Image references: {result['image_reference_rows']}")
    print("- Product IDs assigned: false")
    print("- Owner review state: unreviewed")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
