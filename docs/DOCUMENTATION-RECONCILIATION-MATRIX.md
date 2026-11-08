# Documentation Reconciliation Matrix — Design Kit v2

**Review date:** 2026-11-07  
**Branch:** `feat/owner-design-kit-v2-reconciliation`  
**Review basis:** Complete tracked tree on the feature branch plus owner archive `DAG-owner-controlled-design-kit-v2.zip`, SHA-256 `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`.

Disposition definitions: **RETAIN** = remains valid without material change; **UPDATE** = reconciled with D-014; **SUPERSEDE** = active instruction replaced by a higher-authority source; **ARCHIVE** = preserved as historical, non-operative evidence; **REMOVE** = deleted because obsolete or misleading.

| Tracked path / group | Disposition | Reconciliation outcome |
|---|---|---|
| `AGENTS.md`, `README.md` | UPDATE | Root authority, verified source path, nine-page baseline, closed scope, English-only content and owner identity boundaries documented. |
| `HANDOFF-PROMPT.md` | UPDATE | New root handoff enforces D-014 and discloses source/validation requirements. |
| `design/README.md` | UPDATE | Clarifies kit source, owner approval and historical design assets. |
| `design/owner-controlled-kit-v2/` (25 files) | UPDATE / RETAIN | All 25 installed. PR #8 verified the original 14 HTML/CSS/JS files against the ZIP. PR #9 amends only styles/components.css and styles/layout.css for focus visibility and reduced motion; the other 12 implementation assets remain byte-identical. |
| `design/approved/.gitkeep`, `design/prototypes/.gitkeep` | RETAIN | Empty governed locations; no branded design identity or production prototype is approved. |
| `design/explorations/m1-territory-study.html` | ARCHIVE | Original retained at `docs/historical/visual-proposals/m1-territory-study.html`. |
| `design/explorations/visual-directions.html` and P-015 SVG renders | ARCHIVE | Rejected P-015 board and four desktop/mobile SVGs preserved under `docs/historical/visual-proposals/`; active paths removed. |
| `design/explorations/reference-led-directions.html` | ARCHIVE | Superseded P-016 board retained under `docs/historical/visual-proposals/`; active path removed. |
| `docs/00-PROJECT-CHARTER.md`, `docs/01-DESIGN-PHILOSOPHY.md`, `docs/02-BRAND-IDENTITY.md` | UPDATE | Current D-014 scope and pending brand-identity decisions documented; Japanese-inspired service principles do not imply Japanese UI. |
| `docs/03-CREATIVE-DIRECTION.md`, `docs/04-VISUAL-DESIGN-SYSTEM.md`, `docs/05-ART-DIRECTION-AND-PHOTOGRAPHY.md` | UPDATE | No AI-selected colours, fonts, logo, photo art direction or unlisted UI. Layout-only tokens are QA fallback only. |
| `docs/06-CONTENT-STRATEGY.md` | RETAIN | Verified-facts-first and English-only policy remains compatible; no unsupported claim or structural feature is authorized. |
| `docs/07-INFORMATION-ARCHITECTURE.md` | UPDATE | Current nine-page route list and excluded interactions aligned to D-014. |
| `docs/08-TECHNICAL-ARCHITECTURE.md` | UPDATE | Checkout/account/search references qualified as future discovery only and outside current kit; no stack is selected. |
| `docs/09-QUALITY-AND-ACCEPTANCE.md`, `docs/10-ROADMAP.md`, `docs/13-DESIGN-REVIEW-PROTOCOL.md` | UPDATE | Structural review, owner gates, test evidence and no-production boundaries aligned to source kit. |
| `docs/11-CUSTOMER-AND-MERCHANDISING-STRATEGY.md`, `docs/12-MERCHANT-OPERATIONS.md`, `docs/16-COMMERCIAL-MODEL-ASSESSMENT.md` | RETAIN | Business hypotheses and unresolved commercial choices remain context, not approved operating policy or UI scope. |
| `docs/14-JAPAN-FIRST-CUSTOMER-RESEARCH.md` | UPDATE | Explicitly distinguishes market research from design authority; customer-facing language remains English-only. |
| `docs/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md` | SUPERSEDE | Active-path instructions reduced to owner-only identity input and links to controlling D-014 policy; full previous file archived. |
| `docs/15-CREATIVE-DIRECTION-OPTIONS.md`, `docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md` | ARCHIVE | Active paths are non-operative stubs; original content preserved under `docs/historical/superseded/`. |
| `docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md` | SUPERSEDE | Active path is a concise D-010 reference note; original research preserved under `docs/historical/superseded/`. |
| `docs/17-REFERENCE-LED-DESIGN-BRIEF.md`, `docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md` | ARCHIVE | Active paths are historical stubs; full previous proposal specs preserved under `docs/historical/superseded/`. |
| `docs/19-PHOTO-LIBRARY-AUDIT.md`, `docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md`, `docs/21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md` | RETAIN | Valid data-ingestion, evidence and photo-audit preparation retained; private catalogue/export/media remain outside Git. |
| `docs/22-CUSTOMER-VALIDATION-PLAYBOOK.md` | UPDATE | Research gates and prototype tasks aligned to D-014; no recruitment or fieldwork claimed. |
| `docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md` | UPDATE | Former six-page scope replaced with nine-page D-014 structural baseline and five explicit open owner gates. Old version archived. |
| `docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md` | ADD | Records the PR #9 source-level accessibility changes, preserved boundaries and browser/assistive-technology checks still outstanding. |
| `docs/ADR-TEMPLATE.md`, `docs/REFERENCE-RESEARCH-LOG.md` | RETAIN | Ongoing decision and dated-reference evidence documents remain compatible. |
| `docs/AI-BOOTSTRAP-PROMPT.md`, `docs/AI-WORKING-PROTOCOL.md`, `docs/UPDATE-VISUAL-OWNER-GATE-PROMPT.md` | UPDATE | Stale option-selection and AI authority removed; prompts now follow root authority and closed scope. |
| `docs/DECISIONS.md`, `docs/OWNER-INPUT-REGISTER.md`, `docs/OWNER-TOKEN-INPUT.md` | UPDATE | D-014 added; D-013 superseded; P-015 rejected; P-016 historical; owner inputs remain pending. |
| `docs/DESIGN-AUTHORITY.md`, `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`, `docs/PAGE-INVENTORY.md`, `docs/COMPONENT-INVENTORY.md` | UPDATE | Active owner authority, source hierarchy and exact nine-page/closed-component contract established. |
| `docs/M1-OWNER-REVIEW.md`, `templates/prototypes/m2-owner-entry-decision.md` | SUPERSEDE / ARCHIVE | Active paths are short historical stubs or v2-gate worksheet; original six-route/M1 source preserved in history. |
| `docs/historical/**` | RETAIN | Superseded source docs, old M1/M2 package and rejected visual boards/renders retained with non-operative labels. |
| `scripts/validate_project.py`, `scripts/audit_m2_readiness.py`, scripts/audit_kit_accessibility.py | UPDATE | Enforce D-014, exact 25-file kit inventory, current implementation blob hashes, relative page links, source-level accessibility support and five open owner gates. |
| `scripts/audit_photo_library.py`, catalogue/Etsy validation and reconciliation scripts | RETAIN | Independent data-quality tooling preserved. |
| `tests/test_project_validation.py`, `tests/test_visual_review_quality.py`, `tests/test_m2_prototype_readiness.py`, `tests/test_m2_readiness_audit.py` | UPDATE | Tests target v2 identity inputs, source/inventory scope and open owner gates, not historical option sets or former six-route scope. |
| `tests/test_kit_accessibility.py` | ADD | Guards nine-page semantic structure, navigation state, source focus/reduced-motion rules and supplied disabled-control labels. |
| Catalogue, photo-audit, Etsy, research and privacy-template tests | RETAIN | Independent checks retained; update only for an actual contract change. |
| `.github/workflows/project-quality.yml` | RETAIN | Existing pull-request workflow runs the updated source validator, M2 gate audit and complete unittest suite. |
| `.github/ISSUE_TEMPLATE/.gitkeep`, `.github/workflows/.gitkeep` | RETAIN | Empty repository scaffolding. |

## Source archive integrity

The uploaded ZIP contains exactly 25 files: 9 HTML pages, 4 CSS files, 1 JavaScript file and 11 kit-local governance/README/handoff documents. All 25 are installed under `design/owner-controlled-kit-v2/`. The SHA-256 of the uploaded ZIP is:

`64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`

At D-014 adoption (PR #8), all 14 original HTML/CSS/JS assets were compared using Git's blob SHA-1 formula and exact byte length; every expected SHA and size matched. PR #9 amends only two existing CSS files for focus visibility and reduced-motion support. The other 12 implementation assets remain byte-identical to the ZIP. The validator now enforces current reviewed hashes and the exact 25-path kit inventory. The 11 kit-local documents were aligned to the root hierarchy and are not claimed as byte-identical source assets.

The source kit was installed and byte-verified at PR #8 adoption. PR #9 amends two CSS files for accessibility; the other 12 implementation assets remain byte-identical and the current validator checks all 14 reviewed hashes. Brand identity, production application, commercial/legal decisions, customer research recruitment and unlisted functionality remain unapproved.

## PR #8 validation history and current review

The preceding checklist was completed for PR #8. PR #8 merged after PR workflow run #63 and main-branch push run #64 both passed. PR #9 adds a separate source-level accessibility audit and tests; its own validation status is maintained on the current pull request. Rendered browser, keyboard traversal and assistive-technology checks remain outstanding and are explicitly not claimed as complete.


## 2026-11-08 accessibility maintenance disposition

The v2 source directory remains the only active structural source. The follow-up is a permitted accessibility maintenance amendment, not a new visual direction or component inventory change. Only the shared focus treatment and reduced-motion rule changed; no HTML page, route, section, navigation destination, label, placeholder or disabled state changed. See docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md for the source review and outstanding browser acceptance.
