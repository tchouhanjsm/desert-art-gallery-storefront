# 19 — Non-Destructive Photo Library Audit

## Purpose and status

A small, dependency-free Python utility to inventory a selected DAG photo sample or the existing photo folder before any media architecture, migration or hosting decision.

The owner has approximately 3,000 original photographs for roughly 300 products. This tool does **not** authorize bulk migration. Start with the documented 10–20 image sample when available; scanning the full library is optional and can wait until the owner explicitly requests it.

## Safety contract

The scanner is read-only with respect to source media. It does not rename, edit, rotate, re-encode, compress, move, upload or delete images. It writes only the CSV/JSON reports at the destination paths provided. Existing report files are never overwritten; choose fresh output paths for each run. Keep reports outside the source photo folder and outside Git unless explicitly sanitized and approved; file names and relative folder names may disclose internal information.

It does not extract EXIF/GPS metadata, infer product identities, match filenames to SKUs, assess image aesthetics, detect near-duplicates, decide which image is best or publish anything. Exact duplicates mean byte-identical SHA-256 matches only.

## Inventory fields

The CSV report contains relative path, filename, extension, detected format, file size, dimensions, aspect ratio, megapixels, SHA-256 checksum, exact-duplicate group, status and warning codes. The optional JSON summary contains candidate count, format totals, bytes, duplicate counts, review count, skipped symlinks and a `read_only` marker.

## Format support and limitations

Format detection covers JPEG, PNG, GIF, WebP, BMP, TIFF, SVG and HEIC/AVIF signatures/extensions. Dimension parsing is implemented for JPEG, PNG, GIF, WebP and BMP. TIFF, SVG and HEIC/AVIF are inventoried but their dimensions are marked for manual review. A malformed/truncated candidate or an extension/content mismatch is also marked for review. The parser reads a bounded header and streams file hashes; it does not load complete images into memory.

No minimum resolution is assumed. Supply `--min-megapixels` only when the owner or a later media brief establishes a threshold appropriate to intended crops and output sizes.

## Run locally

From the repository root:

```bash
python scripts/audit_photo_library.py "/path/to/a-small-approved-sample" \
  --csv "/path/to/private-reports/dag-photo-audit.csv" \
  --json "/path/to/private-reports/dag-photo-audit-summary.json"
```

To scan the full folder later, pass that folder instead. Do not use the entire library as the first review sample unless requested.

Optional resolution review threshold (example only, not a DAG acceptance rule):

```bash
python scripts/audit_photo_library.py "/path/to/sample" \
  --min-megapixels 1.0 \
  --csv "/path/to/private-reports/dag-photo-audit.csv"
```

The CSV destination is required. Both report paths must be outside the source directory, and CSV/JSON must use different destinations. Existing files are not overwritten; select new report names for each run. The command exits with code 0 for a complete scan, code 1 when one or more directories could not be traversed (reports are written with scan_complete=false), or code 2 for invalid/unreadable inputs or report-writing errors. Directory traversal failures are included in the JSON summary and printed as warnings; an incomplete scan must not be treated as a complete inventory. Source files are never modified.

## Validation

Unit tests use synthetic image headers and temporary directories. They cover PNG/JPEG/GIF/WebP/BMP dimensions, extension/content mismatch, corrupt candidates, exact duplicate detection, source immutability, symlink skipping, existing-report collision protection, non-finite thresholds, incomplete directory traversal reporting, report output and invalid input paths. Tests do not require real DAG images or third-party dependencies.

## What remains for a real sample

Once the owner supplies 10–20 representative original image files, review the report alongside a human visual inspection. Decide separately:
1. Whether source filenames and folder structure carry useful product/SKU information.
2. How the owner identifies each product and its approved lead/detail/context image order.
3. Rights/consent and publication approval status.
4. Crop/aspect-ratio and responsive derivative requirements after visual direction selection.
5. Whether any exact duplicates or corrupted files require manual action.

The tool does not make those editorial, product or commercial decisions.


## CSV/JSON pair integrity

When the JSON summary is requested, the scanner records inventory_csv_sha256: the SHA-256 digest of the exact CSV bytes written by that same run. The catalogue validator checks this digest before using the inventory. This prevents a CSV from one scan being paired with a different summary merely because both scans contain the same number of files. Keep the pair together and regenerate both outputs together after any audit rerun; do not hand-edit either file.
