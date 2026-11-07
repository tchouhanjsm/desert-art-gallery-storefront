#!/usr/bin/env python3
"""Read-only integrity and structural verifier for a private Etsy review bundle."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

from preview_etsy_export import IMAGE_HEADER, allowed_etsy_image_url

MANIFEST_FORMAT = "dag-etsy-review-bundle-manifest-v1"
BUNDLE_FORMAT = "dag-etsy-private-review-bundle-v1"
EXPECTED_FILES = {
    "README.txt",
    "source-summary.json",
    "source-row-review.csv",
    "source-rows.jsonl",
    "image-source-references.csv",
    "bundle-manifest.json",
}
IMAGE_FIELDS = [
    "source_record_ref",
    "source_data_row_number",
    "source_image_field",
    "source_image_url",
    "source_url_status",
    "local_asset_id",
    "rights_status",
    "publication_status",
]
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


def verify_review_bundle(bundle_path: Path) -> tuple[bool, list[str]]:
    errors: list[str] = []
    supplied = bundle_path.expanduser()
    if supplied.is_symlink():
        return False, ["Bundle directory must not be a symbolic link."]
    bundle = supplied.resolve()
    if not bundle.is_dir():
        return False, ["Bundle path must be an existing directory."]

    actual_names = {item.name for item in bundle.iterdir()}
    if actual_names != EXPECTED_FILES:
        missing = sorted(EXPECTED_FILES - actual_names)
        extra = sorted(actual_names - EXPECTED_FILES)
        if missing:
            errors.append("Missing expected files: " + ", ".join(missing))
        if extra:
            errors.append("Unexpected files present: " + ", ".join(extra))

    for name in EXPECTED_FILES:
        path = bundle / name
        if path.is_symlink():
            errors.append(f"Symbolic-link bundle member is not allowed: {name}")
        elif not path.is_file():
            errors.append(f"Expected regular file is missing: {name}")
    if errors:
        return False, errors

    try:
        manifest = json.loads((bundle / "bundle-manifest.json").read_text(encoding="utf-8"))
        if manifest.get("manifest_format") != MANIFEST_FORMAT:
            errors.append("Unsupported or missing bundle manifest format.")
        entries = manifest.get("files")
        if not isinstance(entries, list):
            errors.append("Manifest files field must be a list.")
            entries = []
        entry_names = [entry.get("path") for entry in entries if isinstance(entry, dict)]
        payload_names = EXPECTED_FILES - {"bundle-manifest.json"}
        if len(entry_names) != len(set(entry_names)) or set(entry_names) != payload_names:
            errors.append("Manifest must contain each expected payload file exactly once.")

        for entry in entries:
            if not isinstance(entry, dict):
                errors.append("Manifest contains a non-object file entry.")
                continue
            name = entry.get("path")
            if name not in payload_names:
                errors.append(f"Manifest contains an invalid payload path: {name!r}")
                continue
            expected_digest = entry.get("sha256")
            expected_size = entry.get("bytes")
            if not isinstance(expected_digest, str) or not SHA256_RE.fullmatch(expected_digest):
                errors.append(f"Manifest has an invalid SHA-256 for {name}.")
                continue
            content = (bundle / name).read_bytes()
            if not isinstance(expected_size, int) or expected_size != len(content):
                errors.append(f"Byte length mismatch for {name}.")
            if hashlib.sha256(content).hexdigest() != expected_digest:
                errors.append(f"SHA-256 mismatch for {name}.")
        if errors:
            return False, errors

        summary = json.loads((bundle / "source-summary.json").read_text(encoding="utf-8"))
        if summary.get("bundle_format") != BUNDLE_FORMAT:
            errors.append("Unsupported review bundle format.")
        source_hash = summary.get("source_sha256")
        if not isinstance(source_hash, str) or not SHA256_RE.fullmatch(source_hash):
            errors.append("Source SHA-256 is missing or malformed.")
        if summary.get("read_only") is not True:
            errors.append("Summary must assert read_only=true.")
        for field in ("imported", "product_assignments_created", "image_downloaded"):
            if summary.get(field) is not False:
                errors.append(f"Summary must assert {field}=false.")

        raw_records: list[dict[str, object]] = []
        with (bundle / "source-rows.jsonl").open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                try:
                    raw_records.append(json.loads(line))
                except json.JSONDecodeError:
                    errors.append(f"Invalid JSON in source-rows.jsonl line {line_number}.")

        row_by_ref: dict[str, dict[str, object]] = {}
        for index, record in enumerate(raw_records, start=1):
            record_ref = record.get("source_record_ref")
            expected_ref = f"etsy:{source_hash}:row:{index}"
            if record.get("source_data_row_number") != index or record_ref != expected_ref:
                errors.append(f"Source row identity mismatch at logical row {index}.")
            if record.get("source_file_sha256") != source_hash:
                errors.append(f"Source file hash mismatch at logical row {index}.")
            if record.get("source_system") != "etsy":
                errors.append(f"Unexpected source system at logical row {index}.")
            if not isinstance(record.get("source_fields"), dict):
                errors.append(f"Raw source fields are not an object at logical row {index}.")
            if isinstance(record_ref, str):
                if record_ref in row_by_ref:
                    errors.append(f"Duplicate source row reference: {record_ref}")
                row_by_ref[record_ref] = record

        if summary.get("source_rows") != len(raw_records):
            errors.append("Source row count does not match source-summary.json.")

        with (bundle / "source-row-review.csv").open("r", encoding="utf-8-sig", newline="") as handle:
            review_rows = list(csv.DictReader(handle))
        if len(review_rows) != len(raw_records):
            errors.append("Compact row review count does not match raw source rows.")
        for index, row in enumerate(review_rows, start=1):
            if row.get("source_record_ref") != f"etsy:{source_hash}:row:{index}":
                errors.append(f"Compact row review identity mismatch at logical row {index}.")

        image_keys: set[tuple[str, str]] = set()
        with (bundle / "image-source-references.csv").open("r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != IMAGE_FIELDS:
                errors.append("Image-reference CSV columns do not match the expected contract.")
            image_rows = list(reader)

        for index, image in enumerate(image_rows, start=1):
            record_ref = image.get("source_record_ref", "")
            field = image.get("source_image_field", "")
            key = (record_ref, field)
            if key in image_keys:
                errors.append(f"Duplicate image source reference: {record_ref}/{field}")
            image_keys.add(key)
            record = row_by_ref.get(record_ref)
            if record is None:
                errors.append(f"Image reference {index} points to an unknown source row.")
                continue
            try:
                row_number = int(image.get("source_data_row_number", ""))
            except ValueError:
                row_number = -1
            if row_number != record.get("source_data_row_number"):
                errors.append(f"Image reference {index} has a mismatched source row number.")
            if not IMAGE_HEADER.fullmatch(field):
                errors.append(f"Image reference {index} uses an unsupported image field.")
            fields = record.get("source_fields", {})
            raw_value = fields.get(field, "") if isinstance(fields, dict) else ""
            url = image.get("source_image_url", "")
            if not raw_value or str(raw_value).strip() != url:
                errors.append(f"Image reference {index} does not match its raw source field.")
            expected_status = "allowed_source_host" if allowed_etsy_image_url(url) else "review_required"
            if image.get("source_url_status") != expected_status:
                errors.append(f"Image URL status mismatch for reference {index}.")
            if image.get("local_asset_id") != "":
                errors.append(f"Local asset assignment is not allowed in reference {index}.")
            if image.get("rights_status") != "unknown":
                errors.append(f"Image rights must remain unknown in reference {index}.")
            if image.get("publication_status") != "not_approved":
                errors.append(f"Image publication must remain unapproved in reference {index}.")
            if "product_id" in image:
                errors.append("Image source references must not contain product_id.")

        if summary.get("image_source_rows_written") != len(image_rows):
            errors.append("Image source row count does not match source-summary.json.")

    except (OSError, UnicodeDecodeError, json.JSONDecodeError, csv.Error) as exc:
        errors.append(f"Could not read bundle: {exc}")
    return not errors, errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Verify a private DAG Etsy review bundle without modifying it.")
    parser.add_argument("bundle_dir", type=Path, help="Private review bundle directory")
    args = parser.parse_args(argv)
    valid, errors = verify_review_bundle(args.bundle_dir)
    if valid:
        print("Etsy review bundle integrity: PASS")
        print("- Manifest checksums: valid")
        print("- Source-row identities: valid")
        print("- Image references: consistent")
        print("- Product assignments: none")
        print("- Image rights/publication: unapproved")
        return 0
    print("Etsy review bundle integrity: FAILED", file=sys.stderr)
    for error in errors:
        print(f"- {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
