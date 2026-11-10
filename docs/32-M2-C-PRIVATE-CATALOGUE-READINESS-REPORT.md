# M2-C — Private Catalogue Intake Readiness Reporting

**Status:** Reporting and validator-hardening implementation complete. Actual sample acceptance remains pending owner-supplied evidence.  
**Scope:** Private, read-only catalogue preparation; no production data model or commerce contract is approved.

## Implemented

- Hardened catalogue input directory and photo-audit report symlink rejection.
- Tightened photo-audit summary validation: candidate count must be a real non-negative integer (not a Boolean), traversal-error count must be present and zero, and scan completeness/read-only flags remain mandatory.
- Required every photo-audit row marked ok to carry a recognized detected image format and a lowercase 64-character SHA-256 digest.
- Added scripts/build_catalogue_readiness_report.py, which reuses the existing catalogue intake validator and photo-audit inventory.
- Added private JSON and Markdown reports with product/fact/image/source counts, clean-photo-audit counts and per-product blockers for the separate product, fact, source reconciliation, image-rights and prototype-use approval gates.
- Kept source titles, descriptions, prices, raw source-export values and image binaries out of the report.
- Enforced output paths outside both the public repository and catalogue source directory; report generation refuses to overwrite existing outputs and never modifies intake CSVs or images.

## Local command

    python scripts/build_catalogue_readiness_report.py "/path/to/private/catalogue-intake" \
      --output-dir "/path/to/private-reports/catalogue-readiness" \
      --photo-audit-csv "/path/to/private-reports/dag-photo-audit.csv" \
      --photo-audit-summary "/path/to/private-reports/dag-photo-audit-summary.json" \
      --m2-sample

The command writes catalogue-readiness.json and catalogue-readiness.md. A structurally valid M2 sample returns exit code 0. A blocked/incomplete sample still produces a blocker report and returns exit code 1.

## Regression coverage

- Accept a valid ten-product private sample and produce a READY report.
- Report an underfilled nine-product sample as BLOCKED without copying product copy.
- Explain product/fact/image approval blockers independently.
- Reject symlinked catalogue/photo-audit sources, positive traversal errors, Boolean photo candidate counts and missing/invalid SHA-256 evidence.
- Reject output paths inside the source catalogue or repository; refuse overwrite of existing reports.

## Current owner evidence gate

The code and reporting workflow are ready. No real owner-supplied 10–20 product/photo sample, verified facts, reconciled source records, per-product prototype-use approvals or image-rights evidence were supplied in this milestone. M2-C sample acceptance remains pending. All populated CSVs, source exports, photographs and generated readiness reports must remain private and outside Git.


## Photo-audit report pairing hardening

The photo-audit scanner now writes inventory_csv_sha256 into its optional JSON summary after the CSV is complete. The catalogue intake loader verifies that the supplied CSV bytes match this digest before using the inventory. This closes the same-candidate-count cross-run pairing gap: a CSV and summary from different scans cannot be combined merely because both contain the same number of image records. Missing, malformed or mismatched digests fail closed. Regenerate and keep each CSV/JSON pair together.
