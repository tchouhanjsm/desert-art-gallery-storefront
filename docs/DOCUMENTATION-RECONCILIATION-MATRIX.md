# Documentation Reconciliation Matrix — Design Kit v2

**Review date:** 2026-11-07  
**Branch:** `feat/owner-design-kit-v2-reconciliation`  
**Review basis:** Tracked GitHub tree on the branch plus the owner-supplied `DAG-owner-controlled-design-kit-v2.zip` (SHA-256 `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`).

Disposition definitions: **RETAIN** = remains active without material change; **UPDATE** = reconcile against v2; **SUPERSEDE** = active instruction replaced by a higher-authority source; **ARCHIVE** = preserve as historical, non-operative evidence; **REMOVE** = delete because it is redundant, unsafe or misleading.

| Tracked path / group | Disposition | Reason / action |
|---|---|---|
| `AGENTS.md`, `README.md` | UPDATE | Establish the authority hierarchy, v2 structural boundaries, English-only content, owner-only brand decisions and no-production boundary. |
| `design/README.md` | UPDATE | Explain design folder governance and historical-vs-active paths. |
| `design/approved/.gitkeep`, `design/prototypes/.gitkeep` | RETAIN | Empty governed destinations; no approved branded prototype exists. |
| `design/explorations/m1-territory-study.html` | ARCHIVE | Earlier visual territory work is not an active source. |
| `design/explorations/visual-directions.html` and its rendered SVGs | ARCHIVE | P-015 package was explicitly rejected. |
| `design/explorations/reference-led-directions.html` | ARCHIVE | P-016 alternatives are superseded as active candidates; they do not confer brand approval. |
| `docs/00-PROJECT-CHARTER.md` | UPDATE | Reflect the current nine-page structural contract and explicit owner gates. |
| `docs/01-DESIGN-PHILOSOPHY.md`, `docs/02-BRAND-IDENTITY.md` | UPDATE | Retain DAG principles while removing inferred palette/type defaults. |
| `docs/03-CREATIVE-DIRECTION.md`, `docs/04-VISUAL-DESIGN-SYSTEM.md`, `docs/05-ART-DIRECTION-AND-PHOTOGRAPHY.md` | UPDATE | Reconcile visual authority; no AI-selected colours, fonts, logos or photography direction. |
| `docs/06-CONTENT-STRATEGY.md`, `docs/07-INFORMATION-ARCHITECTURE.md` | UPDATE | Align page/section structure to the exact nine-page inventory; content remains verified and English-only. |
| `docs/08-TECHNICAL-ARCHITECTURE.md` | RETAIN | No framework, database, CMS, hosting or production stack is selected; preserve as non-binding technical research. |
| `docs/09-QUALITY-AND-ACCEPTANCE.md` | UPDATE | Test supplied structure, semantics, responsiveness and factual placeholders without inventing functionality. |
| `docs/10-ROADMAP.md` | UPDATE | Move v2 structural review ahead of branded prototype work; keep field research, commercial and technical choices gated. |
| `docs/11-CUSTOMER-AND-MERCHANDISING-STRATEGY.md`, `docs/12-MERCHANT-OPERATIONS.md` | RETAIN | Business hypotheses and operational context remain useful; do not convert them into approved policies. |
| `docs/13-DESIGN-REVIEW-PROTOCOL.md` | UPDATE | Review against the closed v2 inventory and owner-controlled identity. |
| `docs/14-JAPAN-FIRST-CUSTOMER-RESEARCH.md` | RETAIN | Research preparation remains relevant; no recruitment or fieldwork is represented as complete. |
| `docs/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md` | SUPERSEDE | Replace obsolete multi-option selection protocol with D-014 structural authority and pending owner token inputs. |
| `docs/15-CREATIVE-DIRECTION-OPTIONS.md`, `docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md` | ARCHIVE | P-015 was rejected; P-016 is historical only. |
| `docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md` | SUPERSEDE | Historical POJ/Macaroni research remains reference context; the v2 kit and current inventories govern structure. |
| `docs/16-COMMERCIAL-MODEL-ASSESSMENT.md` | RETAIN | Direct/enquiry/hybrid options remain unresolved, not implementation instructions. |
| `docs/17-REFERENCE-LED-DESIGN-BRIEF.md`, `docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md` | ARCHIVE | Previous reference-led identity options are no longer active candidates; brand identity remains unapproved. |
| `docs/19-PHOTO-LIBRARY-AUDIT.md`, `docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md`, `docs/21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md` | RETAIN | Preserve useful audit/ingestion knowledge; no raw exports, private source data or media are authorized in Git. |
| `docs/22-CUSTOMER-VALIDATION-PLAYBOOK.md` | UPDATE | Keep the research protocol but align prototype tasks to current v2 routes; fieldwork remains unperformed. |
| `docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md` | UPDATE | Supersede the old six-route/feature-rich shell assumptions with the nine-page structural contract; keep owner gates. |
| `docs/ADR-TEMPLATE.md`, `docs/REFERENCE-RESEARCH-LOG.md` | RETAIN | Continue using for documented technical decisions and dated reference evidence. |
| `docs/AI-BOOTSTRAP-PROMPT.md`, `docs/AI-WORKING-PROTOCOL.md`, `docs/UPDATE-VISUAL-OWNER-GATE-PROMPT.md` | UPDATE | Remove stale option-selection instructions and enforce root authority/inventory boundaries. |
| `docs/DECISIONS.md`, `docs/OWNER-INPUT-REGISTER.md` | UPDATE | Record D-014, supersede D-013, retain unresolved owner identity and commercial gates. |
| `docs/DESIGN-AUTHORITY.md`, `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`, `docs/PAGE-INVENTORY.md`, `docs/COMPONENT-INVENTORY.md` | UPDATE | Adopted as core active governance and inventory references. |
| `docs/M1-OWNER-REVIEW.md` | ARCHIVE | Prior visual review package is closed; no option is selected. |
| `scripts/validate_project.py`, `scripts/audit_m2_readiness.py` | UPDATE | Replace assertions tied to rejected proposal boards and the former six-page contract. |
| `scripts/audit_photo_library.py`, Etsy review/reconciliation/preview/validation scripts | RETAIN | Preserve independent data-quality tools; no production application scope change. |
| Catalogue, research and prototype CSV/Markdown templates | RETAIN | Preserve blank operational/research templates and privacy safeguards. |
| `templates/prototypes/m2-owner-entry-decision.md` | SUPERSEDE | Prior worksheet assumes the former six-route prototype scope; keep historical copy only. |
| `tests/test_project_validation.py`, `tests/test_visual_review_quality.py`, M2 readiness tests | UPDATE | Test v2 authority, route/component contract, disabled states and owner gates rather than superseded proposals. |
| Catalogue, photo audit, Etsy, customer research tests | RETAIN | Keep independent coverage; update only where a documented v2 source path changes. |
| `.github/workflows/project-quality.yml` | UPDATE | Keep meaningful governance, source-integrity and unit checks; avoid tests that enforce retired design options. |
| `.github/ISSUE_TEMPLATE/.gitkeep`, `.github/workflows/.gitkeep` | RETAIN | Empty repository scaffolding. |

## Source package status

The uploaded archive contains 25 entries: 14 HTML/CSS/JS implementation assets and 11 governance/inventory documents. The archive was inspected and its 14 implementation asset digests were checked locally against the extracted source in the prior staging pass. **The extracted kit directory is not yet present in the current GitHub branch tree.** Therefore the kit is not marked installed or byte-verified in GitHub in this reconciliation. This is an explicit release blocker, not an assumed completion.
