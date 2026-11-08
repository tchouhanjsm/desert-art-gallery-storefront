# Design Assets and Source Governance

The active structural HTML/CSS source is materialized at `design/owner-controlled-kit-v2/` under D-014. The owner archive contains 25 files and has SHA-256 `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`. PR #8 verified all 14 original HTML/CSS/JS assets; PR #9 records two narrow CSS accessibility maintenance amendments and the current hashes are enforced by `scripts/validate_project.py`. Do not re-extract, redesign or reinterpret the active kit as part of documentation work.

- `approved/` is reserved for owner-approved brand assets with decision ID and date.
- `prototypes/` is reserved for explicitly authorized review prototypes.
- `explorations/` is not an active source for the rejected or superseded visual proposals.

P-015 was rejected. P-016 is historical only. Previous visual proposal boards and specifications have been moved to `docs/historical/` for audit context. **HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT.**

No current palette, typography, logo/wordmark/descriptor or photography art direction has been approved. Do not put unapproved material in `approved/`.
