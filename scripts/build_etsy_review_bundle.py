#!/usr/bin/env python3
"""Build a private, read-only review bundle from an Etsy CSV export."""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import sys
from pathlib import Path

from preview_etsy_export import (
    IMAGE_HEADER,
    allowed_etsy_image_url,
    preview_etsy_export,
    _write_json,
    _write_rows,
)

IMAGE_REFERENCE_FIELDS = [
    "source_record_ref",
    "source_data_row_number",
    "source_image_field",
    "source_image_url",
    "source_url_status",
    "local_asset_id",
    "rights_status",
    "publication_status",
]


def _git_root(path: Path) -> Path | None:
    current = path if path.is_dir() else path.parent
    for candidate in (current, *current.parents):
        marker = candidate / ".git"
        if marker.exists() or marker.is_symlink():
            return candidate
    return None


def validate_private_destination(source: Path, destination: Path) -> Path:
    if destination.expanduser().is_symlink():
        raise ValueError("Bundle destination must not be a symbolic link.")
    source_path = source.expanduser().resolve()
    source_directory = source_path.parent
    output = destination.expanduser().resolve()
    if output == source_directory or output.is_relative_to(source_directory):
        raise ValueError("Bundle destination must be outside the source CSV directory.")
    if source_directory.is_relative_to(output):
        raise ValueError("Bundle destination must not contain the source CSV directory.")
    if _git_root(output.parent):
        raise ValueError("Bundle destination must be outside every Git working tree.")
    if output.exists():
        raise ValueError(f"Bundle destination already exists; choose a new path: {output}")
    return output


def build_private_review_bundle(source: Path, destination: Path) -> dict[str, object]:
    """Preserve raw rows and remote image references without assigning products."""
    source_input = source.expanduser()
    if source_input.is_symlink():
        raise ValueError("Source CSV must not be a symbolic link.")
    source_path = source_input.resolve()
    if not source_path.is_file():
        raise ValueError("Source CSV must be an existing regular file.")

    summary, previews, fatal = preview_etsy_export(source_input)
    if fatal:
        raise ValueError("Cannot create a review bundle from an export with fatal header errors.")

    output = validate_private_destination(source_path, destination)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.mkdir(exist_ok=False)

    source_text = source_path.read_bytes().decode("utf-8-sig")
    reader = csv.reader(io.StringIO(source_text, newline=""))
    raw_headers = next(reader)
    normalized_headers = [header.strip().upper() for header in raw_headers]
    image_columns = [
        (index, header)
        for index, header in enumerate(normalized_headers)
        if IMAGE_HEADER.fullmatch(header)
    ]
    preview_by_row = {
        int(record["source_data_row_number"]): record
        for record in previews
    }

    image_count = 0
    with (output / "source-rows.jsonl").open("x", encoding="utf-8") as raw_handle, (
        output / "image-source-references.csv"
    ).open("x", encoding="utf-8-sig", newline="") as image_handle:
        image_writer = csv.DictWriter(image_handle, fieldnames=IMAGE_REFERENCE_FIELDS)
        image_writer.writeheader()
        source_row_number = 0
        for cells in reader:
            if not cells or not any(cell.strip() for cell in cells):
                continue
            source_row_number += 1
            preview = preview_by_row[source_row_number]
            raw_fields = {
                header: cells[index] if index < len(cells) else ""
                for index, header in enumerate(raw_headers)
            }
            raw_handle.write(json.dumps({
                "source_system": "etsy",
                "source_file_sha256": summary["source_sha256"],
                "source_data_row_number": source_row_number,
                "source_record_ref": preview["source_record_ref"],
                "row_review_required": preview["row_review_required"],
                "source_fields": raw_fields,
                "extra_cells": cells[len(raw_headers):],
            }, ensure_ascii=False) + "\n")

            for index, field in image_columns:
                raw_url = cells[index] if index < len(cells) else ""
                url = raw_url.strip()
                if not url:
                    continue
                image_writer.writerow({
                    "source_record_ref": preview["source_record_ref"],
                    "source_data_row_number": source_row_number,
                    "source_image_field": field,
                    "source_image_url": url,
                    "source_url_status": (
                        "allowed_source_host" if allowed_etsy_image_url(url) else "review_required"
                    ),
                    "local_asset_id": "",
                    "rights_status": "unknown",
                    "publication_status": "not_approved",
                })
                image_count += 1

    bundle_summary = dict(summary)
    bundle_summary.update({
        "raw_source_headers": raw_headers,
        "bundle_format": "dag-etsy-private-review-bundle-v1",
        "contains_raw_source_fields": True,
        "image_source_rows_written": image_count,
        "product_assignments_created": False,
        "image_downloaded": False,
    })
    _write_json(bundle_summary, output / "source-summary.json")
    _write_rows(previews, output / "source-row-review.csv")

    readme = """PRIVATE DAG ETSY SOURCE REVIEW BUNDLE
=======================================

This package contains private raw source-row values and image URL references.
Treat it as sensitive business data. Keep the entire directory outside Git,
public/shared folders and customer-facing systems.

Files:
- source-summary.json: source SHA-256, structure checks and warning summary.
- source-row-review.csv: compact row index, duplicate indicators and review flags.
- source-rows.jsonl: complete raw source fields, preserving original headers and
  exact text values, including multiline descriptions.
- image-source-references.csv: one row per populated IMAGE1-IMAGE10 reference.
- README.txt: data-handling and approval boundaries.

Important boundaries:
- No product ID, catalogue row, SKU normalization or product match is created.
- No title-based or SKU-based product assignment is performed.
- No image is downloaded, copied, transformed or hotlinked.
- An allowed URL host is only a preflight check; it is not proof the URL is live,
  DAG owns the image, or publication is permitted.
- Every image starts with rights_status=unknown and publication_status=not_approved.
- Price, quantity, materials, tags and descriptions remain raw source values;
  they are not verified product facts, current inventory or approved public copy.
- No currency conversion, tax, markup, shipping promise or product taxonomy is inferred.
- The original source CSV is not modified.

Next manual step: reconcile each source row to a real product identity using
independent evidence, then separately verify factual claims and image rights.
Do not feed this package directly into a production import.
"""
    with (output / "README.txt").open("x", encoding="utf-8") as handle:
        handle.write(readme)

    bundle_files = [
        "README.txt",
        "source-summary.json",
        "source-row-review.csv",
        "source-rows.jsonl",
        "image-source-references.csv",
    ]
    manifest = {
        "manifest_format": "dag-etsy-review-bundle-manifest-v1",
        "files": [
            {
                "path": name,
                "bytes": (output / name).stat().st_size,
                "sha256": hashlib.sha256((output / name).read_bytes()).hexdigest(),
            }
            for name in bundle_files
        ],
    }
    _write_json(manifest, output / "bundle-manifest.json")

    return {
        "bundle_directory": str(output),
        "source_rows": int(summary["source_rows"]),
        "image_source_rows": image_count,
        "source_sha256": str(summary["source_sha256"]),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Create a private raw-source Etsy review bundle; no products or images are imported."
    )
    parser.add_argument("source_csv", type=Path, help="Private Etsy Listings Download CSV")
    parser.add_argument("bundle_dir", type=Path, help="New private output directory outside Git and the source directory")
    args = parser.parse_args(argv)

    try:
        result = build_private_review_bundle(args.source_csv, args.bundle_dir)
    except (OSError, ValueError, csv.Error) as exc:
        print(f"Etsy review bundle failed: {exc}", file=sys.stderr)
        return 2

    print("Private Etsy review bundle: CREATED")
    print(f"- Directory: {result['bundle_directory']}")
    print(f"- Source rows: {result['source_rows']}")
    print(f"- Image references: {result['image_source_rows']}")
    print("- Product assignments created: false")
    print("- Images downloaded: false")
    print("- Integrity manifest: bundle-manifest.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
