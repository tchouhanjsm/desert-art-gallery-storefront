# Documentation Changelog

## 2026-11-07 — Owner-controlled DAG Design Kit v2 reconciliation
- Added the root authority hierarchy and repository-wide documentation reconciliation policy.
- Installed all 25 owner-supplied v2 kit files under `design/owner-controlled-kit-v2/`.
- Verified all 14 original HTML/CSS/JS assets against the supplied ZIP by Git blob SHA-1 and exact byte length.
- Reconciled the 11 kit-local README, handoff, authority and inventory documents to the root D-014 hierarchy.
- Corrected the root nine-page and component inventories against the supplied HTML; the Journal now records six story-card placeholders and Collection three product-card placeholders.
- Recorded D-014 as structural adoption only and superseded D-013's former six-route scope.
- Marked P-016 historical only; retained P-015's explicit rejected status.
- Retired the active P-015/P-016 boards and preserved the original boards, renders and superseded documents under `docs/historical/`.
- Replaced the six-route M2 acceptance pack and worksheet with the D-014 nine-page contract and open owner gates.
- Updated root prompts, active design/quality/roadmap docs, validators and affected tests.
- Preserved pending owner identity inputs and no-production/no-additions boundaries.
- Added source-integrity validation for the exact 25-file inventory and 14 original asset hashes.

## PR #8 validation outcome
- PR workflow run #63 passed before merge; main-branch push run #64 passed after merge.
- Source integrity, active Markdown links, M2 gate consistency and the complete test suite were green for the PR #8 baseline.
- PR #9 is a separate accessibility-maintenance follow-up; see the 2026-11-08 entry and structural accessibility review.


## 2026-11-08 — D-014 kit accessibility maintenance
- Added an authored keyboard focus-visible outline using currentColor to the existing shared component stylesheet; no palette or colour token was introduced.
- Added a reduced-motion override for the existing smooth-scroll rule; no animation or interaction was added.
- Preserved the nine HTML pages, structure, labels, placeholders, disabled states, supplied script and responsive breakpoints.
- Added a read-only nine-page accessibility source audit and regression tests.
- Corrected stale kit-materialization statements in the root M2 pack and handoff; documented current source integrity and static-review limits.
- Added docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md and reconciled the roadmap, quality guide, README, authority docs and checklist.
- Kept brand colours, typography, photography direction and all M2 owner gates unchanged.
