# M2-C — Photo-Audit Pair Integrity

**Status:** Implemented in PR #16. The genuine product/photo sample remains owner-supplied and pending.  
**Purpose:** Ensure that a private photo-audit CSV inventory and its JSON summary are one evidence pair before catalogue intake or readiness reporting uses them.

## Integrity contract

When audit_photo_library.py writes a JSON summary, it first completes the CSV inventory and records the SHA-256 digest of those exact CSV bytes as inventory_csv_sha256. The summary is then written separately. The validator recalculates the CSV digest and requires an exact match.

This detects accidental cross-run pairing even when two scans have the same candidate count. Missing, malformed or mismatched digests are rejected. The CSV and summary are not edited or repaired by the validator; generate a fresh pair from the photo-audit command.

## Run

    python3 scripts/audit_photo_library.py "/PATH/TO/PRIVATE/APPROVED-SAMPLE" \
      --csv "$HOME/Documents/DAG-private-reports/photo-audit.csv" \
      --json "$HOME/Documents/DAG-private-reports/photo-audit-summary.json"

Then pass those exact two files together to the catalogue validator or readiness report. Keep both files, the source photographs and all intake CSVs private and outside Git. If the source sample changes or the audit is rerun, create a new pair and supply both outputs from that run.

## What the digest establishes—and what it does not

The digest establishes that the summary references the exact CSV file supplied to the catalogue validator. It does not prove that the photo source was complete, that the scan was performed by a trusted reviewer, that a file depicts a particular product, or that DAG has legal rights to use it. Those checks remain separate: complete/read-only scan metadata, human product mapping, factual evidence, rights evidence and owner prototype-use approval.
