# Repository-Wide Documentation Reconciliation Matrix

**Review date:** 2026-11-09
**Decision update:** D-017 — M2-A Revision 2 visual direction approved for private prototype  
**Audited baseline:** `main` at `a4b665f81433e98cd78469e0a1bc1bb81a3528df` (PR #9 merge)  
**Owner archive:** `DAG-owner-controlled-design-kit-v2.zip`  
**Owner archive SHA-256:** `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`  
**Tracked baseline:** 140 files, enumerated from the Git index using `git ls-files` and the GitHub recursive tree API.

## Disposition definitions

- **RETAIN** — inspected and compatible; no content change required.
- **UPDATE** — active file changed to correct authority, current repository state, scope or validation evidence.
- **SUPERSEDE** — active path remains as a concise non-operative notice or gated worksheet; former operative content is replaced by higher authority.
- **ARCHIVE** — preserved for audit/provenance only and explicitly labelled non-operative.
- **REMOVE** — deleted as obsolete or misleading. None was required in this reset because the old material could be preserved without remaining an active instruction.

## Path-by-path disposition

| Tracked path | Disposition | Review finding / reason |
|---|---|---|
| `.github/ISSUE_TEMPLATE/.gitkeep` | RETAIN | Empty issue-template scaffold; no contradictory instruction. |
| `.github/workflows/.gitkeep` | RETAIN | Empty workflow scaffold; no contradictory instruction. |
| `.github/workflows/project-quality.yml` | UPDATE | Add repository-wide contextual documentation-consistency audit to existing PR/push quality workflow. |
| `AGENTS.md` | UPDATE | Exact eight-level hierarchy; enumerate and reconcile nested prompts, source comments, code, workflows and templates; preserve closed D-014 scope. |
| `HANDOFF-PROMPT.md` | UPDATE | Directs agents to the precise eight-level hierarchy and path-level reconciliation evidence. |
| `README.md` | UPDATE | Exact eight-level hierarchy and confirmed owner archive/source status. |
| `design/README.md` | UPDATE | Remove stale “once materialized” language; identify the currently installed source and verified archive. |
| `design/approved/.gitkeep` | RETAIN | Empty owner-approved brand-asset area; no identity asset is approved. |
| `design/explorations/.gitkeep` | RETAIN | Empty active exploration area; retired proposal boards are not active here. |
| `design/owner-controlled-kit-v2/HANDOFF-PROMPT.md` | RETAIN | Kit-local handoff remains subordinate to root authority and aligned with D-014. |
| `design/owner-controlled-kit-v2/README.md` | RETAIN | Kit overview and limitations remain aligned; owner-supplied package preserved. |
| `design/owner-controlled-kit-v2/docs/COMPONENT-INVENTORY.md` | RETAIN | Owner-supplied kit inventory preserved. |
| `design/owner-controlled-kit-v2/docs/DESIGN-AUTHORITY.md` | RETAIN | Kit-local authority preserved beneath root authority. |
| `design/owner-controlled-kit-v2/docs/DOCUMENTATION-CHANGELOG.md` | RETAIN | Owner-supplied kit provenance preserved. |
| `design/owner-controlled-kit-v2/docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md` | RETAIN | Kit-local source evidence retained. |
| `design/owner-controlled-kit-v2/docs/DOCUMENTATION-RECONCILIATION-PROMPT.md` | RETAIN | Kit-local prompt remains subordinate; root hierarchy controls. |
| `design/owner-controlled-kit-v2/docs/DOCUMENTATION-SOURCE-OF-TRUTH.md` | RETAIN | Kit-local governance preserved; root policy is authoritative. |
| `design/owner-controlled-kit-v2/docs/OWNER-TOKEN-INPUT.md` | RETAIN | Blank owner-only token inputs; no palette or typeface invented. |
| `design/owner-controlled-kit-v2/docs/PAGE-INVENTORY.md` | RETAIN | Nine-page owner source inventory preserved. |
| `design/owner-controlled-kit-v2/docs/REFERENCE-CREDIT-AND-IP.md` | RETAIN | Reference/IP rules remain compatible with D-010 and root scope. |
| `design/owner-controlled-kit-v2/index.html` | RETAIN | Owner-supplied Home structure preserved; no markup changes in this reset. |
| `design/owner-controlled-kit-v2/pages/about.html` | RETAIN | Owner-supplied About structure preserved. |
| `design/owner-controlled-kit-v2/pages/article.html` | RETAIN | Owner-supplied Article structure preserved. |
| `design/owner-controlled-kit-v2/pages/collection.html` | RETAIN | Owner-supplied Collection structure preserved. |
| `design/owner-controlled-kit-v2/pages/contact.html` | RETAIN | Owner-supplied Contact structure and disabled form concept preserved. |
| `design/owner-controlled-kit-v2/pages/journal.html` | RETAIN | Owner-supplied Journal structure preserved. |
| `design/owner-controlled-kit-v2/pages/makers.html` | RETAIN | Owner-supplied Makers structure preserved. |
| `design/owner-controlled-kit-v2/pages/product.html` | RETAIN | Owner-supplied Product structure and disabled purchase control preserved. |
| `design/owner-controlled-kit-v2/pages/shop.html` | RETAIN | Owner-supplied Shop structure and disabled controls preserved. |
| `design/owner-controlled-kit-v2/scripts/prototype.js` | RETAIN | Supplied minimal prototype script preserved. |
| `design/owner-controlled-kit-v2/styles/components.css` | RETAIN | Existing D-014 kit CSS including the documented PR #9 focus rule preserved; this reset adds no styling. |
| `design/owner-controlled-kit-v2/styles/layout.css` | RETAIN | Existing D-014 kit CSS including the documented PR #9 reduced-motion rule preserved. |
| `design/owner-controlled-kit-v2/styles/responsive.css` | RETAIN | Owner-supplied responsive rules preserved. |
| `design/owner-controlled-kit-v2/styles/tokens-layout-only.css` | RETAIN | System/browser QA fallback remains non-brand; no production palette selected. |
| `design/prototypes/.gitkeep` | RETAIN | Empty governed prototype location; no production prototype authorized. |
| `docs/00-PROJECT-CHARTER.md` | UPDATE | Verify D-014 materialization and clarify D-010 reference hierarchy does not add features to the closed kit. |
| `docs/01-DESIGN-PHILOSOPHY.md` | RETAIN | Current philosophy is compatible with owner-controlled identity and D-014 boundaries. |
| `docs/02-BRAND-IDENTITY.md` | RETAIN | Brand identity inputs remain pending and owner-controlled. |
| `docs/03-CREATIVE-DIRECTION.md` | RETAIN | No active AI-selected identity direction; D-014 governs structure. |
| `docs/04-VISUAL-DESIGN-SYSTEM.md` | RETAIN | Layout-only fallback remains QA-only; no production token set is approved. |
| `docs/05-ART-DIRECTION-AND-PHOTOGRAPHY.md` | RETAIN | Owner approval, genuine-photo evidence and placeholder boundaries remain intact. |
| `docs/06-CONTENT-STRATEGY.md` | RETAIN | English-only and verified-facts-first guidance remains aligned. |
| `docs/07-INFORMATION-ARCHITECTURE.md` | RETAIN | Current nine-page information architecture is aligned to the kit inventory. |
| `docs/08-TECHNICAL-ARCHITECTURE.md` | RETAIN | Technology choices and production architecture remain unresolved and outside D-014. |
| `docs/09-QUALITY-AND-ACCEPTANCE.md` | RETAIN | Acceptance guidance preserves disabled states and distinguishes static from browser checks. |
| `docs/10-ROADMAP.md` | RETAIN | Roadmap preserves D-014 and open owner gates; no new production milestone is authorized by this reset. |
| `docs/11-CUSTOMER-AND-MERCHANDISING-STRATEGY.md` | RETAIN | Business hypotheses remain context, not implementation authority. |
| `docs/12-MERCHANT-OPERATIONS.md` | RETAIN | Operational guidance retained; unresolved operational commitments remain gated. |
| `docs/13-DESIGN-REVIEW-PROTOCOL.md` | RETAIN | Review protocol remains within D-014 and owner approval boundaries. |
| `docs/14-JAPAN-FIRST-CUSTOMER-RESEARCH.md` | RETAIN | Japan-first research context remains separate from English-only UI and owner authorization. |
| `docs/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md` | SUPERSEDE | Active-path stub is non-operative; P-015/P-016 cannot be reactivated from this path. |
| `docs/15-CREATIVE-DIRECTION-OPTIONS.md` | SUPERSEDE | Active-path stub retires the old option workflow; no palette/type option is active. |
| `docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md` | SUPERSEDE | Active-path stub retires P-015 specifications; original file remains archived. |
| `docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md` | UPDATE | Distinguish confirmed D-010 reference hierarchy note from the superseded page-by-page implementation proposal. |
| `docs/16-COMMERCIAL-MODEL-ASSESSMENT.md` | RETAIN | Commercial model remains exploratory and is not converted into policy or UI scope. |
| `docs/17-REFERENCE-LED-DESIGN-BRIEF.md` | SUPERSEDE | Active-path stub marks former brief historical; D-010 reference credit remains, not an option-generation instruction. |
| `docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md` | SUPERSEDE | Active-path stub marks P-016 proposals historical; no proposal values become defaults. |
| `docs/19-PHOTO-LIBRARY-AUDIT.md` | RETAIN | Read-only photo-audit knowledge preserved; no bulk migration or publication authorized. |
| `docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md` | RETAIN | Intake/fact-verification guidance retained without approving production schema or facts. |
| `docs/21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md` | RETAIN | Export-mapping/reconciliation knowledge retained; no source export or import approved. |
| `docs/22-CUSTOMER-VALIDATION-PLAYBOOK.md` | RETAIN | Research playbook remains gated by M2-B/C/D/E; no recruitment is authorized here. |
| `docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md` | RETAIN | Current D-014 nine-page pack and five open owner gates remain authoritative. |
| `docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md` | RETAIN | PR #9 source-level accessibility record preserved; browser and assistive-tech checks remain outstanding. |
| `docs/ADR-TEMPLATE.md` | RETAIN | Decision-record template remains compatible with repository governance. |
| `docs/AI-BOOTSTRAP-PROMPT.md` | UPDATE | Historical audit note: the stale source-materialization blocker was removed; the active prompt requires the exact authority sequence and repository-wide reconciliation. |
| `docs/AI-WORKING-PROTOCOL.md` | RETAIN | Existing engineering workflow remains subordinate to root authority and inventories. |
| `docs/COMPONENT-INVENTORY.md` | RETAIN | Nine-page component inventory remains the closed structure baseline. |
| `docs/DECISIONS.md` | RETAIN | D-001–D-014 and P-015/P-016 statuses were verified; no new owner design decision is invented. |
| `docs/DESIGN-AUTHORITY.md` | UPDATE | Explicitly designate level 3, confirm current archive state and reiterate that historical content is non-operative. |
| `docs/DOCUMENTATION-CHANGELOG.md` | UPDATE | Record the 2026-11-08 repository-wide reset and audit tooling. |
| `docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md` | UPDATE | Replace prior grouped/PR #8 checklist with current per-file audit, this reset’s validation and remaining browser checks. |
| `docs/DOCUMENTATION-RECONCILIATION-MATRIX.md` | UPDATE | Replace previous grouped matrix with this 140-row current tracked-path matrix. |
| `docs/DOCUMENTATION-RECONCILIATION-REPORT.md` | UPDATE | Record current baseline, archive verification, exact paths, findings, scan method and real CI evidence. |
| `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md` | UPDATE | Split owner-approved specs and inventories into separate levels; define the exact eight-level hierarchy. |
| `docs/M1-OWNER-REVIEW.md` | SUPERSEDE | Active path is a non-operative historical stub; full review is retained in the archive. |
| `docs/OWNER-INPUT-REGISTER.md` | RETAIN | Owner gates remain open as recorded; no owner responses inferred. |
| `docs/OWNER-TOKEN-INPUT.md` | RETAIN | Brand inputs remain pending; no palette, typography or logo is selected. |
| `docs/PAGE-INVENTORY.md` | RETAIN | Nine-page inventory remains the single active route baseline. |
| `docs/REFERENCE-RESEARCH-LOG.md` | RETAIN | Dated research retained as evidence; it cannot add features or override D-014. |
| `docs/UPDATE-VISUAL-OWNER-GATE-PROMPT.md` | RETAIN | Owner-gate prompt remains constrained by root decisions and D-014. |
| `docs/historical/README.md` | RETAIN | Archive index explains historical, non-operative status. |
| `docs/historical/superseded/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md` | ARCHIVE | Original owner-control process preserved with mandatory non-operative banner; old multi-option instruction is not active. |
| `docs/historical/superseded/15-CREATIVE-DIRECTION-OPTIONS.md` | ARCHIVE | Historical proposals retained with mandatory non-operative banner. |
| `docs/historical/superseded/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md` | ARCHIVE | Rejected P-015 palette/type specifications retained with mandatory banner. |
| `docs/historical/superseded/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md` | ARCHIVE | Former reference-led implementation detail retained with mandatory banner; D-010 remains only as the reference hierarchy decision. |
| `docs/historical/superseded/17-REFERENCE-LED-DESIGN-BRIEF.md` | ARCHIVE | Former reference-led creative brief retained with mandatory non-operative banner. |
| `docs/historical/superseded/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md` | ARCHIVE | P-016 visual proposal specification retained with mandatory non-operative banner. |
| `docs/historical/superseded/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE-v1-six-route.md` | ARCHIVE | Superseded six-route M2 pack retained with mandatory non-operative banner. |
| `docs/historical/superseded/M1-OWNER-REVIEW.md` | ARCHIVE | Former M1 review retained with mandatory non-operative banner. |
| `docs/historical/superseded/m2-owner-entry-decision-v1-six-route.md` | ARCHIVE | Former six-route M2 worksheet retained with mandatory non-operative banner. |
| `docs/historical/visual-proposals/m1-territory-study.html` | ARCHIVE | Original M1 visual exploration preserved for traceability only with a non-operative HTML comment banner. |
| `docs/historical/visual-proposals/reference-led-directions.html` | ARCHIVE | Original P-016 board preserved for traceability only with a non-operative HTML comment banner; no candidate is active. |
| `docs/historical/visual-proposals/rendered/future-relics-desktop.svg` | ARCHIVE | Rejected P-015 desktop render preserved for traceability only. |
| `docs/historical/visual-proposals/rendered/future-relics-mobile.svg` | ARCHIVE | Rejected P-015 mobile render preserved for traceability only. |
| `docs/historical/visual-proposals/rendered/graphic-atelier-desktop.svg` | ARCHIVE | Rejected P-015 desktop render preserved for traceability only. |
| `docs/historical/visual-proposals/rendered/graphic-atelier-mobile.svg` | ARCHIVE | Rejected P-015 mobile render preserved for traceability only. |
| `docs/historical/visual-proposals/rendered/living-garden-desktop.svg` | ARCHIVE | Rejected P-015 desktop render preserved for traceability only. |
| `docs/historical/visual-proposals/rendered/living-garden-mobile.svg` | ARCHIVE | Rejected P-015 mobile render preserved for traceability only. |
| `docs/historical/visual-proposals/rendered/modern-folk-pop-desktop.svg` | ARCHIVE | Rejected P-015 desktop render preserved for traceability only. |
| `docs/historical/visual-proposals/rendered/modern-folk-pop-mobile.svg` | ARCHIVE | Rejected P-015 mobile render preserved for traceability only. |
| `docs/historical/visual-proposals/visual-directions.html` | ARCHIVE | Rejected P-015 visual board preserved for traceability only with a non-operative HTML comment banner. |
| `scripts/audit_documentation_consistency.py` | UPDATE | New tracked-tree audit flags stale active directives and checks the eight-level hierarchy; historic references are handled separately. |
| `scripts/audit_documentation_links.py` | RETAIN | Existing Markdown internal-link audit retained; run in CI. |
| `scripts/audit_kit_accessibility.py` | RETAIN | Existing D-014 static accessibility audit retained. |
| `scripts/audit_m2_readiness.py` | RETAIN | Existing five-open-gate M2 readiness audit retained. |
| `scripts/audit_photo_library.py` | RETAIN | Existing read-only photo audit utility retained. |
| `scripts/build_etsy_review_bundle.py` | RETAIN | Existing private/local review-bundle utility retained; no import/publication authorized. |
| `scripts/create_etsy_reconciliation_worklist.py` | RETAIN | Existing source-export reconciliation utility retained. |
| `scripts/preview_etsy_export.py` | RETAIN | Existing read-only export preview utility retained. |
| `scripts/validate_catalogue_intake.py` | RETAIN | Existing local catalogue validation utility retained; not a production schema approval. |
| `scripts/validate_project.py` | UPDATE | Enforce current source, exact eight-level hierarchy and archival labels in addition to D-014 asset hashes. |
| `scripts/verify_etsy_review_bundle.py` | RETAIN | Existing verification utility retained. |
| `templates/catalogue/README.md` | RETAIN | Blank catalogue-intake instructions remain; no source data is committed. |
| `templates/catalogue/etsy-image-sources.csv` | RETAIN | Blank Etsy image-source template retained. |
| `templates/catalogue/product-facts.csv` | RETAIN | Blank product-facts template retained. |
| `templates/catalogue/product-images.csv` | RETAIN | Blank product-image mapping template retained. |
| `templates/catalogue/product-source-records.csv` | RETAIN | Blank product-source evidence template retained. |
| `templates/catalogue/products.csv` | RETAIN | Blank product intake template retained. |
| `templates/prototypes/README.md` | RETAIN | Prototype template guidance remains gated by owner approval. |
| `templates/prototypes/m2-owner-entry-decision.md` | SUPERSEDE | Worksheet remains a decision-capture aid; current M2 acceptance pack and owner decision register supersede former six-route assumptions. |
| `templates/prototypes/prototype-review.csv` | RETAIN | Blank prototype review template retained; no study authorized. |
| `templates/research/README.md` | RETAIN | Research templates retained; no recruitment/spend authorization inferred. |
| `templates/research/discovery-interview-guide.md` | RETAIN | Interview template retained as gated preparation only. |
| `templates/research/finding-synthesis.csv` | RETAIN | Blank synthesis template retained. |
| `templates/research/participant-screener.csv` | RETAIN | Blank screener template retained; recruitment remains gated. |
| `templates/research/prototype-usability-guide.md` | RETAIN | Usability guide retained as preparation; no prototype study authorized. |
| `templates/research/research-session-notes.csv` | RETAIN | Blank research notes template retained. |
| `templates/research/session-opening-and-consent.md` | RETAIN | Consent template retained; no sessions or recruitment authorized. |
| `templates/research/task-observations.csv` | RETAIN | Blank task-observation template retained. |
| `tests/test_catalogue_intake.py` | RETAIN | Existing catalogue-intake regression tests unchanged. |
| `tests/test_customer_validation_templates.py` | RETAIN | Existing customer-validation template tests unchanged. |
| `tests/test_etsy_export_preview.py` | RETAIN | Existing export-preview regression tests unchanged. |
| `tests/test_etsy_reconciliation_worklist.py` | RETAIN | Existing reconciliation-worklist tests unchanged. |
| `tests/test_etsy_review_bundle.py` | RETAIN | Existing review-bundle tests unchanged. |
| `tests/test_etsy_review_bundle_verification.py` | RETAIN | Existing review-bundle verification tests unchanged. |
| `tests/test_documentation_consistency.py` | UPDATE | New regression tests for tracked-file audit scope, hierarchy and non-operative historical handling. |
| `tests/test_kit_accessibility.py` | RETAIN | Existing nine-page accessibility-source tests unchanged. |
| `tests/test_m2_prototype_readiness.py` | RETAIN | Existing M2 D-014 scope regression tests unchanged. |
| `tests/test_m2_readiness_audit.py` | RETAIN | Existing open-gate audit tests unchanged. |
| `tests/test_photo_library_audit.py` | RETAIN | Existing photo-audit tests unchanged. |
| `tests/test_project_validation.py` | RETAIN | Existing project validator tests remain compatible; validator gained governance assertions. |
| `tests/test_visual_review_quality.py` | RETAIN | Existing owner-identity pending-state tests unchanged. |

## Totals

| Disposition | Count |
|---|---:|
| UPDATE | 24 |
| RETAIN | 85 |
| SUPERSEDE | 7 |
| ARCHIVE | 24 |
| REMOVE | 0 |
| **Total tracked paths in reviewed baseline** | **140** |

This table is exhaustive for the 140-path baseline enumerated before this reset. The two newly added paths (`scripts/audit_documentation_consistency.py` and `tests/test_documentation_consistency.py`) are listed explicitly above; after their addition, the branch contains 142 tracked paths.


## Post-baseline paths added by merged PR #11

The exhaustive disposition table above remains anchored to the 140-path baseline at
`a4b665f81433e98cd78469e0a1bc1bb81a3528df`. PR #11 subsequently merged a focused
browser-QA batch, adding the following three tracked paths. Existing PR #11 modifications
to AGENTS, README, the source-of-truth policy, changelog, structural accessibility review,
responsive CSS and project validator are reconciled in the merged PR #10 branch content.

| Tracked path | Disposition | Reconciliation outcome |
|---|---|---|
| `.github/workflows/kit-browser-review.yml` | RETAIN | Dedicated Chromium QA workflow for all nine supplied routes and five responsive review widths; produces CI evidence only and adds no product functionality. |
| `requirements-browser.txt` | RETAIN | Isolated pinned Playwright dependency used only by browser QA; it is not a storefront runtime dependency. |
| `scripts/kit_browser_review.py` | RETAIN | Browser QA runner checks routes, viewport overflow, navigation state, keyboard focus, reduced-motion behaviour, local assets and screenshot evidence without changing the kit structure. |

After PR #11, main contained 143 tracked paths. PR #10 adds the two audit implementation files
listed explicitly in the original matrix; the resulting tracked tree contains 145 paths. The
140-path disposition totals above describe the original baseline only and are not silently
re-labelled as the post-PR #11 total.


## M2 D-016 reconciliation overlay — 8 November 2026

The following paths were reconciled to the owner's new M2-A–E decisions. This overlay supplements the baseline path inventory above; it does not alter the D-014 kit file inventory or imply that proposed identity values are approved.

| Path | Disposition | Reconciliation |
|---|---|---|
| docs/DECISIONS.md | UPDATE | Add D-016; retain D-015 as authority for completed structural QA and clarify conditional prototype scope. |
| docs/27-M2-A-REFERENCE-LED-VISUAL-PROPOSAL.md | ADD | One reference-led DAG proposal; all colour, type, logo, descriptor and photo values pending owner approval. |
| docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md | ADD | Approved seven-person cohort; operations prepared; fieldwork and costs not authorized. |
| docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md | ADD | Six-area owner walkthrough mapped to the unchanged nine-page kit; human acceptance pending. |
| docs/OWNER-INPUT-REGISTER.md; docs/OWNER-TOKEN-INPUT.md | UPDATE | Reflect cohort/journey decisions and proposal review; keep all final identity values pending. |
| docs/REFERENCE-RESEARCH-LOG.md | UPDATE | Add live 8 November observations, measurement limitations and IP boundaries. |
| docs/22-CUSTOMER-VALIDATION-PLAYBOOK.md; docs/25-M2-DECISION-AND-REVIEW-PACK.md; docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md; docs/10-ROADMAP.md | UPDATE | Reconcile gate statuses and the owner-approved cohort, journey order and conditional six-area prototype authorization. |
| AGENTS.md; README.md; docs/DESIGN-AUTHORITY.md; docs/DOCUMENTATION-SOURCE-OF-TRUTH.md; docs/02-BRAND-IDENTITY.md; docs/04-VISUAL-DESIGN-SYSTEM.md | UPDATE | Permit only the separate private prototype under D-016, after visual approval; preserve D-014 source assets and pending identity status. |
| docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md; docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md | UPDATE | Add placeholder/image-frame rules and owner journey priority; preserve photo evidence and human-review gates. |
| scripts/audit_m2_readiness.py; tests/test_m2_readiness_audit.py; tests/test_m2_prototype_readiness.py | UPDATE | Enforce new gate statuses and D-016 boundaries with regression coverage. |
| docs/DOCUMENTATION-CHANGELOG.md | UPDATE | Record all D-016, proposal, research and prototype walkthrough changes. |

The D-014 owner kit assets, active PAGE-INVENTORY and COMPONENT-INVENTORY are RETAINED unchanged. The owner token input remains pending; no production tokens are written.


## M2 private prototype review-readiness overlay — 8 November 2026

| Path | Disposition | Reconciliation |
|---|---|---|
| scripts/validate_private_prototype.py | ADD | Local-only validator enforces private root, D-016 scope, M2-A decision/proposal hash, image evidence and non-transactional boundaries. |
| scripts/private_prototype_browser_review.py | ADD | Local-only Playwright runner, blocks external hosts, reviews nine pages × five widths and stores screenshots/reports outside repository. |
| schemas/private-prototype-manifest.schema.json | ADD | Machine-readable contract for the pending/approved visual decision reference and private asset ledger. |
| templates/private-prototype-manifest.template.json | ADD | Deliberately pending private manifest; cannot pass until M2-A approval and supporting assets/evidence are supplied. |
| tests/test_private_prototype_validator.py | ADD | Regression tests for private-root policy, approval hash, scope, placeholders, genuine-photo evidence, transaction/network rejection and browser-entry gate. |
| docs/29-M2-PRIVATE-PROTOTYPE-VALIDATION-AND-REVIEW.md | ADD | Local operating guide and limitations for the private prototype validation/review pipeline. |
| AGENTS.md; README.md; docs/23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md; docs/10-ROADMAP.md; docs/DOCUMENTATION-CHANGELOG.md | UPDATE | Document current readiness tooling and retain explicit M2-A implementation gate. |

The owner-controlled D-014 HTML/CSS/JS assets, page/component inventories and QA-only token fallback are retained unchanged. The M2-A visual proposal is updated to record D-017 approval for private prototype use. The private prototype itself and its assets/reports remain outside the public repository.


## M2 owner walkthrough record-support overlay — 10 November 2026

| Path | Disposition | Reconciliation |
|---|---|---|
| scripts/validate_owner_walkthrough.py | ADD | Validates a private owner-authored D-016 walkthrough record, six area decisions, five viewport reviews and route/component-scoped revision requests; summary excludes free text. |
| schemas/owner-walkthrough-record.schema.json | ADD | Documents the exact record shape and closed D-016 area, D-014 route and viewport inventories. |
| templates/owner-walkthrough-record.template.json | ADD | Blank/pending private template; contains no owner feedback, product information, imagery or local paths. |
| tests/test_owner_walkthrough.py | ADD | Regression coverage for incomplete/accepted/revision/rejected states, decision gates, malformed records, route scope, symlinks and output privacy. |
| docs/33-M2-OWNER-WALKTHROUGH-RECORD-VALIDATION.md | ADD | Local operating guide and acceptance limitations for the owner walkthrough record helper. |
| README.md; docs/10-ROADMAP.md; docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md; docs/29-M2-PRIVATE-PROTOTYPE-VALIDATION-AND-REVIEW.md; docs/DOCUMENTATION-CHANGELOG.md; docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md | UPDATE | Record the private walkthrough helper and keep owner visual acceptance, M2-C evidence and M2-B fieldwork gates explicitly pending. |


## M2-C photo-audit integrity overlay — 10 November 2026

| Path | Disposition | Reconciliation |
|---|---|---|
| scripts/audit_photo_library.py | UPDATE | Bind the optional JSON summary to the exact CSV inventory bytes with SHA-256. |
| scripts/validate_catalogue_intake.py | UPDATE | Verify the inventory digest and reject cross-run or malformed report pairs. |
| tests/test_photo_library_audit.py; tests/test_catalogue_intake.py | UPDATE | Cover digest emission, missing digest and same-count cross-run report substitution. |
| docs/19-PHOTO-LIBRARY-AUDIT.md; docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md; docs/32-M2-C-PRIVATE-CATALOGUE-READINESS-REPORT.md | UPDATE | Document exact-pair integrity and regeneration rules. |
| README.md; docs/10-ROADMAP.md; docs/DOCUMENTATION-CHANGELOG.md; docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md | UPDATE | Record this implementation and preserve the owner-supplied sample and approval gates. |


## M2-B fieldwork authorization-preflight overlay — 10 November 2026

| Path | Disposition | Reconciliation |
|---|---|---|
| scripts/validate_m2b_fieldwork_authorization.py | ADD | Fail-closed preflight for the eight written D-016 fieldwork approvals, fixed cohort, supporting details and owner confirmation. It does not initiate research. |
| schemas/m2b-fieldwork-authorization.schema.json | ADD | Closed schema for the private owner-authored authorization record. |
| templates/m2b-fieldwork-authorization.template.json | ADD | Deliberately pending record with the fixed approved seven-person cohort and eight pending approvals. |
| tests/test_m2b_fieldwork_authorization.py | ADD | Regression coverage for all approval gates, data/consent/spend/schedule blockers, invalid records and private-output protections. |
| docs/35-M2-B-FIELDWORK-AUTHORIZATION-GATE.md | ADD | Private preflight operating guide, status meanings and authorization limitations. |
| docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md | UPDATE | Link the preflight and keep all eight owner approvals and participant-level consent requirements pending. |
| README.md; docs/10-ROADMAP.md; docs/DOCUMENTATION-CHANGELOG.md; docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md | UPDATE | Record implementation and separate tooling readiness from actual fieldwork authorization. |