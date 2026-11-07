# Repository-Wide Reconciliation Report — DAG Design Kit v2

**Review date:** 2026-11-07  
**Branch:** `feat/owner-design-kit-v2-reconciliation`  
**Status:** Source kit materialized and byte-verified; governance and core validation aligned. Final internal-link/stale-language checks and PR CI remain to be confirmed.

## Source and integrity evidence

Owner archive: `DAG-owner-controlled-design-kit-v2.zip`  
Archive SHA-256: `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`

The archive contains exactly **25 files**:
- 9 HTML pages.
- 4 CSS files.
- 1 JavaScript prototype file.
- 11 README, handoff, authority, inventory and governance documents.

All 25 are installed under `design/owner-controlled-kit-v2/`. The 14 HTML/CSS/JS assets have been compared against the original archive by Git blob SHA-1 and file size. All 14 match exactly. CI now enforces the expected blob hashes and the exact 25-file inventory in `scripts/validate_project.py`.

The 11 kit-local governance/readme files are reconciled to D-014 and the repository-root authority hierarchy; they are not claimed to be byte-identical to their v1-era source text. The original HTML/CSS/JS asset bytes remain unchanged.

## Confirmed structural baseline

D-014 adopts the v2 kit as the sole active structural source for exactly nine pages: Home, Shop, Collection, Product detail, About, Makers, Journal index, Journal article and Contact. See `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`.

Preserve source markup, CSS, responsive rules, prototype script, page/section order, existing components, placeholders and disabled states. This is a non-production structural kit.

## Owner-controlled decisions and product boundaries

- Final brand colours, typography families/weights/hierarchy/type scale, logo/wordmark/descriptor and photography art direction/crops remain owner-controlled and pending.
- `tokens-layout-only.css` is browser/system QA fallback only, not a DAG palette or production theme.
- Customer-facing content remains English-only. Japan-first is not an instruction to create Japanese-language UI.
- Never fabricate products, makers, materials, dimensions, provenance, prices, stock, reviews, availability, contact details, policies or delivery promises.
- Use only approved product imagery with verified product mapping, permissions and publication approval; retain labelled placeholders where evidence is missing (D-011).
- Mobile review remains required across every selected journey (D-012).
- D-013's former six-page prototype scope is superseded by D-014's nine-page structure.
- P-015 remains rejected. P-016 and Material Archive / Collected Colour are historical only.
- D-010 remains the reference hierarchy: POJ Studio primary for ecommerce/page structure; Macaroni Shoten secondary for curation/select-shop character. Do not copy protected source code, CSS, copy, imagery, logos, fonts or exact branded compositions.
- No additional UI, components, routes, production app, commerce workflows or technology choices are authorized.

## Repository changes on this branch

### Authority, decisions and inventories
- Updated root `AGENTS.md` and `README.md` to reflect materialized D-014 source and owner-controlled identity boundaries.
- Added `docs/DESIGN-AUTHORITY.md` and `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`.
- Updated `docs/DECISIONS.md` with D-014 and marked D-013 superseded.
- Updated `docs/OWNER-INPUT-REGISTER.md` and added `docs/OWNER-TOKEN-INPUT.md`.
- Added the exact page and component inventories.
- Added matrix, report, checklist and changelog.

### Active documentation and prompts updated
- `docs/01-DESIGN-PHILOSOPHY.md`
- `docs/03-CREATIVE-DIRECTION.md`
- `docs/04-VISUAL-DESIGN-SYSTEM.md`
- `docs/05-ART-DIRECTION-AND-PHOTOGRAPHY.md`
- `docs/07-INFORMATION-ARCHITECTURE.md`
- `docs/08-TECHNICAL-ARCHITECTURE.md`
- `docs/09-QUALITY-AND-ACCEPTANCE.md`
- `docs/10-ROADMAP.md`
- `docs/13-DESIGN-REVIEW-PROTOCOL.md`
- `docs/14-JAPAN-FIRST-CUSTOMER-RESEARCH.md` (scope clarification)
- `docs/22-CUSTOMER-VALIDATION-PLAYBOOK.md`
- `docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md`
- `docs/AI-BOOTSTRAP-PROMPT.md`
- `docs/AI-WORKING-PROTOCOL.md`
- `docs/UPDATE-VISUAL-OWNER-GATE-PROMPT.md`
- `templates/prototypes/m2-owner-entry-decision.md`
- `design/README.md`

### Superseded and historical material
- Replaced active-path P-015/P-016 documents with clear historical stubs; preserved their full original Markdown files under `docs/historical/superseded/`.
- Moved the old visual boards and all eight desktop/mobile proposal SVGs from `design/explorations/` to `docs/historical/visual-proposals/`.
- Preserved the previous M1 visual review and six-route M2 pack/worksheet under the historical directory.
- The active exploration folder now contains only its empty placeholder.

### Validators and tests
- Reworked `scripts/validate_project.py` to enforce D-014 authority, exact 25-file inventory, 14 original asset blob hashes, English page language and local page/stylesheet/script references.
- Reworked `scripts/audit_m2_readiness.py` to audit five open owner gates against the nine-page baseline.
- Updated project, visual identity and M2 tests to test the active v2 scope rather than old proposal boards or six-route assumptions.
- The existing workflow `.github/workflows/project-quality.yml` still runs the project validator, owner-gate audit and complete Python unittest suite.

## Retained technical/business knowledge

Existing photo audit, catalogue intake, Etsy export mapping/reconciliation, customer research templates, merchant operations, commercial-model assessment, reference research log, ADR template, and independent catalogue/photo/Etsy tests remain in the repository. They are not promoted into approved production architecture or commercial policy.

## Validation status

- [x] Owner ZIP SHA-256 recorded.
- [x] ZIP contains 25 source entries.
- [x] All 25 paths materialized under the agreed Git path.
- [x] All 14 HTML/CSS/JS assets verified byte-for-byte using Git blob hashes.
- [x] Old visual proposal boards and renders removed from active exploration paths and retained historically.
- [x] Validator and M2 audit updated to D-014.
- [ ] Final contextual stale-instruction search across all tracked relevant files.
- [ ] Final Markdown internal-link validation.
- [ ] Branch validator, owner-gate audit and unit test suite green in GitHub Actions.
- [ ] PR review and merge.

## Remaining caution

The source kit is now materialized and the original implementation asset bytes are verified. That does not approve brand styling, content publication, customer research recruitment, a production app, or any commerce capability. Owner gates and remaining CI results must remain explicit.
