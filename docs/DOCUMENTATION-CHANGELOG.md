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


## 2026-11-08 — Repository-wide documentation reset

- Re-verified the uploaded owner archive SHA-256: `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`; it matches the PR #8 adoption archive.
- Enumerated the complete 140-file tracked baseline, including root/nested prompts, HTML/CSS/JS, workflow/template paths, scripts, tests and CSV templates.
- Replaced the bundled seven-level hierarchy with the exact eight-level order, separating owner-approved specifications and current page/component inventories.
- Updated root `AGENTS.md`, `README.md`, handoff, design README, design authority, source policy, project charter and AI bootstrap prompt.
- Corrected the stale “kit not yet materialized” language and clarified that D-010 references do not authorize POJ/Macaroni features.
- Clarified the active reference-spec path as a D-010 credit/reference note only; former page-by-page implementation guidance remains superseded.
- Added mandatory non-operative banners to all nine Markdown files under `docs/historical/superseded/`, preserving their source content beneath the banners.
- Added a per-path reconciliation matrix and refreshed the report/checklist against the 140-file baseline.
- Added tracked-tree-aware stale-instruction audit, regression tests and GitHub Actions workflow step.
- Preserved the decision register, open owner inputs, kit files, technical/business knowledge and all production/brand scope boundaries unchanged.
- No extra page, section, component, brand token, catalogue data, product fact, commerce behaviour or production application code was added.

Validation outcome for this reset is recorded only after the final PR head's GitHub Actions run completes.

## 2026-11-08 — Chromium browser review and mobile gallery correction
- Added a dedicated Playwright/Chromium workflow covering all nine owner-controlled pages at the five required responsive review widths (45 route/viewport combinations).
- Added runtime checks for stylesheet loads, document overflow, page landmarks, mobile navigation state, keyboard focus visibility, browser page errors and reduced-motion behaviour.
- Added mobile/desktop full-page screenshots and JSON/Markdown run summaries as CI artifacts.
- The first browser run found a 684px Product Detail gallery caused by three 220px automatic thumbnail grid tracks at 390px and 430px viewports.
- Corrected the existing mobile CSS grid to use shrinkable tracks and square thumbnail sizing; retained all three existing thumbnail slots and made no HTML or component changes.
- Updated the current implementation asset hash and recorded browser/assistive-technology validation boundaries.
