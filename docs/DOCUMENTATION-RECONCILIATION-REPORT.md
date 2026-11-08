# Repository-Wide Documentation Reset — Audit Report

**Audit date:** 2026-11-08  
**Repository:** `tchouhanjsm/desert-art-gallery-storefront`  
**Audited baseline:** `main` at `a4b665f81433e98cd78469e0a1bc1bb81a3528df`  
**Owner archive:** `DAG-owner-controlled-design-kit-v2.zip`  
**Archive SHA-256:** `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`  
**Tracked baseline:** 140 paths.

## Executive result

The supplied archive is the same 25-file owner-controlled kit already adopted under D-014. The repository contains the complete source kit at `design/owner-controlled-kit-v2/`; this reset does not re-extract, re-theme or redesign it.

PR #8 adopted D-014 (structural scope only). PR #9 subsequently added two documented CSS-only accessibility maintenance rules: visible keyboard focus using `currentColor` and a reduced-motion override for the existing smooth-scroll rule. The nine HTML pages and the other 12 implementation assets remain unchanged. The project validator enforces the current 14 implementation-asset hashes and the closed 25-file kit inventory.

The audit found stale active-state wording in `design/README.md` and `docs/AI-BOOTSTRAP-PROMPT.md`, an incomplete seven-level source hierarchy that bundled two distinct levels, and a reference-spec title that conflated D-010 reference credit with the superseded page-by-page implementation proposal. These active paths have been corrected. Nine superseded owner-review/visual-proposal Markdown files now carry a mandatory archival banner. The original contents remain preserved underneath.

The reset leaves all owner decisions, pending identity values, commercial/legal unknowns, customer research gates, and D-014 structural boundaries unchanged. No production application code, product facts, brand tokens, page/section/component additions or commerce behaviour are introduced.

## 1. Archive and implementation verification

The uploaded archive SHA-256 matches the D-014 adoption archive:

`64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`

Package contents: 25 files — nine HTML pages, four CSS files, one JavaScript file and eleven kit-local governance/readme/handoff documents.

The 14 original implementation assets were verified at PR #8 adoption against the owner archive using Git blob SHA-1 and file size. PR #9 changes only two existing CSS assets for accessibility support. The source validator checks the current hash of all 14 implementation assets and the exact kit path inventory.

No owner archive content was changed by this documentation reset.

## 2. Authority hierarchy established

The repository now states the requested hierarchy without collapsing levels 5 and 6:

1. Explicit owner-approved decisions — `docs/DECISIONS.md`.
2. Root `AGENTS.md`.
3. `docs/DESIGN-AUTHORITY.md`.
4. `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`.
5. Owner-approved design specifications.
6. Current page and component inventories — `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`.
7. Technical and implementation documentation only where compatible with levels 1–6.
8. Historical documents as audit context only; never current instructions.

Root `AGENTS.md`, `README.md`, root handoff and AI bootstrap are aligned to this order. The root agent policy explicitly extends the check to nested prompts/READMEs, source comments, HTML/CSS/JS, theme/token files, workflows, issue templates and technical guides.

## 3. Repository-wide tracked-file audit

The audit enumerated all 140 tracked paths in the baseline, including files outside `docs/`: root/nested READMEs and handoffs, the complete owner kit, historical visual HTML/SVG assets, scripts, tests, GitHub workflow/issue-template scaffolding and catalogue/research CSV templates.

The exhaustive per-path disposition table is in `docs/DOCUMENTATION-RECONCILIATION-MATRIX.md`.

| Disposition | Count in 140-path baseline |
|---|---:|
| UPDATE | 24 |
| RETAIN | 85 |
| SUPERSEDE | 7 |
| ARCHIVE | 24 |
| REMOVE | 0 |
| **Total** | **140** |

Two new paths are added by this reset: `scripts/audit_documentation_consistency.py` and `tests/test_documentation_consistency.py`. Therefore the branch tree will contain 142 paths after commit. The matrix lists those two separately and does not misrepresent them as part of the 140-path baseline.

### Main active documents updated

- `AGENTS.md` — exact eight-level hierarchy; repository-wide governance requirements.
- `README.md` — exact hierarchy and confirmed kit materialization/archive identity.
- `HANDOFF-PROMPT.md` — read order and governance rule.
- `design/README.md` — removed stale “once materialized” status.
- `docs/DESIGN-AUTHORITY.md` — explicit level-3 role and non-operative archive rule.
- `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md` — exact eight levels, separated specifications and inventories.
- `docs/AI-BOOTSTRAP-PROMPT.md` — removed false materialization blocker and specified hierarchy-first audit.
- `docs/00-PROJECT-CHARTER.md` — D-010 references clarified as principles, not a feature backlog.
- `docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md` — active path clarified as D-010 reference-credit note only; former page-by-page implementation spec superseded and archived.

### Owner decisions checked and retained

`docs/DECISIONS.md` was inspected and left unchanged because it already correctly records:

- D-007: owner controls identity; old four-option AI generation process superseded.
- D-008/P-015: four earlier visual territories rejected.
- D-010: POJ Studio primary, Macaroni Shoten secondary reference hierarchy; no implied feature authority.
- D-013: former six-route scope superseded by D-014.
- D-014: exact nine-page structural scope only; no brand identity or production authorization.
- P-016: superseded, historical only.

`docs/OWNER-INPUT-REGISTER.md` and `docs/OWNER-TOKEN-INPUT.md` were inspected and left unchanged because their owner inputs remain correctly open/pending. No new owner decision was invented to make the reset appear complete.

## 4. Retired visual instructions and historical archive

Active paths for P-015/P-016 and former M1/M2 materials remain short superseded stubs or gated records; the former detailed material remains under `docs/historical/`.

Nine Markdown files under `docs/historical/superseded/` now begin with:

**HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT.**

Their original bodies are preserved for audit, but their old proposals, option-selection instructions, page/feature lists and approval workflow are non-operative. Historical board HTML and eight SVG renders remain archived without deletion.

No old beige/ivory/sand/terracotta-first mandate, legacy font pairing, Japanese-language storefront instruction, old layout implementation or fabricated catalogue example is revived as active guidance.

## 5. Automated regression protection

Added `scripts/audit_documentation_consistency.py`, which:

- Enumerates tracked files with `git ls-files`.
- Scans active text/source files across the repository, not just `docs/`.
- Checks historical/superseded content for an explicit archival banner.
- Flags selected stale active directives with file/line context.
- Checks the required governance paths and the eight-level hierarchy order.
- Separates historical mentions (which remain necessary in decision/audit records) from active instructions.

Added `tests/test_documentation_consistency.py` for repository-wide audit behaviour and archive-scope checks.

Updated `scripts/validate_project.py` to enforce the eight-level source order, prevent the known stale kit-materialization statements and require archival banners for all superseded Markdown files.

Updated `.github/workflows/project-quality.yml` to run the new consistency audit as part of existing PR/push validation. Existing source integrity, M2 readiness, accessibility source and Markdown-link audits remain enabled.

## 6. Internal links and implementation references

The existing `scripts/audit_documentation_links.py` remains the active Markdown link checker. It scans active Markdown files, follows local relative links, rejects path escapes and excludes the historical archive from active-link enforcement. The CI workflow continues to run it.

Current page, component and source-kit references were inspected against D-014. The active design reference path is now a D-010 credit note, not an outdated page-by-page implementation instruction. Historical implementation detail links resolve to archived paths.

## 7. Retained technical and business knowledge

Catalogue intake, Etsy source mapping/reconciliation, photo-library audit, merchant operations, commercial-model research, customer research templates, privacy/consent templates, test suites and local utilities remain in the repository. They were not deleted merely because they predate D-014. Their retention does not convert proposals into production schemas, operating policy, research authorization or UI requirements.

## 8. Scope and limitations

This is a documentation/governance reset only. It does not:

- Approve brand colours, typography, type scale, logo/wordmark/descriptor or photography direction.
- Add or remove D-014 pages, sections, components, navigation destinations or controls.
- Enable disabled Search, Filter/Sort, variant, purchase or enquiry concepts.
- Add product records, claims, imagery or business facts.
- Authorize participant recruitment, research spending, production application development, technology selection, commerce functionality or deployment.
- Claim screen-reader, WCAG conformance, final colour contrast or owner visual approval. PR #11's separate Chromium automation covers the nine-page responsive matrix and browser interactions but does not replace those approvals.

## 9. Validation status

The final branch commit and GitHub Actions result are recorded after the PR is created. The following checks are required in CI:

- `python3 scripts/validate_project.py`
- `python3 scripts/audit_m2_readiness.py`
- `python3 scripts/audit_kit_accessibility.py`
- `python3 scripts/audit_documentation_consistency.py`
- `python3 scripts/audit_documentation_links.py`
- `python3 -m unittest discover -s tests -v`

No test is marked PASS in this report until GitHub Actions actually runs on the final PR head.


## 10. Post-baseline reconciliation — merged PR #11

The original exhaustive matrix is anchored to the 140 tracked paths at baseline commit
`a4b665f81433e98cd78469e0a1bc1bb81a3528df`. PR #11 subsequently merged at
`95079bbb5ccf6aaf888d4523a5adfda582ab448c` and added three tracked QA paths:

- `.github/workflows/kit-browser-review.yml` — RETAIN; dedicated Chromium workflow.
- `requirements-browser.txt` — RETAIN; isolated Playwright test dependency.
- `scripts/kit_browser_review.py` — RETAIN; structural browser QA runner.

PR #11 also updated existing paths: `AGENTS.md`, `README.md`,
`design/owner-controlled-kit-v2/styles/responsive.css`,
`docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md`,
`docs/DOCUMENTATION-CHANGELOG.md`,
`docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`, and
`scripts/validate_project.py`. Their current status is reconciled with the eight-level
authority and the current three-CSS-maintenance history in this branch.

The current main tree after PR #11 contains 143 tracked paths. PR #10 adds
`scripts/audit_documentation_consistency.py` and
`tests/test_documentation_consistency.py`; after this reset merges, the tree will contain
145 tracked paths. The matrix above preserves the exact 140-path baseline totals and adds
individual dispositions for all three later PR #11 additions.

### PR #11 implementation and browser evidence

PR #11 introduced a dedicated Playwright/Chromium review of all nine supplied pages at
390, 430, 768, 1280 and 1440 CSS-pixel widths (45 route/viewport combinations). The first run
identified a real Product Detail mobile overflow at 390px and 430px caused by automatic
minimum thumbnail grid tracks. The existing mobile CSS was corrected without changing HTML,
the three thumbnail slots, routes, sections, components or supplied JavaScript.

The final PR #11-head browser workflow run #5 passed 45/45 route/viewport combinations.
Reduced-motion, keyboard focus and mobile navigation checks passed; no horizontal overflow,
browser page errors or failed local assets were reported. The run published 18 full-page
screenshots and JSON/Markdown summaries as a CI artifact. The project-quality workflow run
#74 also passed. This automated evidence does not claim screen-reader, WCAG, contrast or owner
visual approval.
