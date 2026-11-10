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


## 2026-11-08 — PR #10 rebase, validator and audit correction
- Reconciled PR #10 onto main after PR #11 merged, preserving PR #11's responsive Product Detail fix and Chromium QA workflow.
- Replaced the brittle checklist phrase assertion with a semantic materialization-evidence check; the exact kit inventory remains independently validated.
- Added non-operative archival banners to the three historical visual-proposal HTML boards.
- Prevented the tracked-file auditor from treating its own regex definitions as active repository instructions.
- Clarified a historical audit explanation in the path matrix so it is not misclassified as a live directive.
- GitHub Actions DAG Project Quality run #77 passed on PR #10 head `1f11b0eca7be4f34b2088cb94f94bdb041936a2a`: foundation, five owner gates, kit accessibility, repository-wide consistency, Markdown links and unit tests.


## 2026-11-08 — PR #12 semantic and keyboard QA hardening
- Replaced the order-sensitive kit accessibility regex checks with a standard-library HTML parser covering page language/title, landmark and heading structure, accessible names, form labels, image alternatives, unique IDs, ARIA relationships and positive tabindex.
- Added parser regression tests for valid semantics and deliberately malformed markup.
- Extended Chromium review to validate rendered DOM semantics on all nine pages at the five required viewport widths.
- Added 54 mobile Enter/Space keyboard-operation sequences across the nine pages at 390px, 430px and 768px, checking the existing disclosure state and focus retention without changing runtime JavaScript.
- Confirmed CI success: Project Quality run #79 passed 89 Python tests; Chromium Browser Review run #7 passed 45/45 route/viewport combinations and uploaded 18 screenshots plus JSON/Markdown summaries.
- Recorded the result in the M2 entry pack, roadmap and structural accessibility review. D-014 and M2-A through M2-E owner gates remain unchanged.


## 2026-11-08 — Combined M2 A–E decision and structural journey review
- Recorded D-015 from the owner's instruction to achieve M2 A–E, narrowly authorizing the bounded non-production structural journey-review scope.
- Added a consolidated M2 decision/review pack separating owner-controlled inputs, proposed customer research, missing source evidence, responsive journey order and the limits of D-015 authorization.
- Proposed (not owner-validated) a first Japan qualitative cohort centred on home/interior shoppers with textile/craft interest, with craft/material enthusiasts and small trade/gift contrasts.
- Added five Playwright journey scenarios across five responsive widths; the nine-page viewport checks, mobile keyboard operations and disabled commerce states remain in scope.
- Extended private catalogue intake templates/validation so product facts and images require distinct prototype-use approval/evidence, and image rights clearance evidence is recorded separately from public publication approval.
- Added an M2-specific 10–20 product/photo-audit validation mode. No private catalogue data, customer data or product photographs were added to Git.
- M2-A and M2-C remain blocked on owner-supplied identity inputs and product/photo evidence; no recruitment, customer fieldwork, branded theme, production feature or deployment was started.

## 2026-11-08 — M2 source reconciliation and image-rights evidence hardening
- Required every product in a private M2 sample to trace to an owner-reconciled source-export row.
- Added rights_evidence_reference to Etsy source-image records and required it whenever source-image rights are marked cleared.
- Added regression coverage for missing source reconciliation and missing Etsy-image rights evidence.
- Updated the owner input queue, catalogue intake rules, M2 decision pack and roadmap.

## 2026-11-08 — M2 A–E final-head validation
- Final PR #13 Project Quality run #88 passed all source/foundation, M2 disposition, accessibility, documentation consistency and Markdown link audits; all 101 Python tests passed.
- Final PR #13 Chromium Browser Review run #15 passed 45/45 route/viewport checks, 25/25 journey/viewport checks, 54 keyboard-operation sequences and reduced-motion; 18 screenshots plus JSON/Markdown summaries were uploaded.
- Recorded the final CI evidence in the M2 acceptance pack, decision pack, roadmap and accessibility review.
- Retained M2-A and M2-C as owner-evidence blockers; M2-B/M2-D human/owner approval remains separate from automation; D-015 remains limited to non-production structural review.

## 2026-11-08 — M2 final evidence links synchronized
- Updated the M2 acceptance, decision, roadmap and accessibility documents to link to final documentation-sync validation: Project Quality run #89 and Chromium Browser Review run #16.
- Removed the obsolete note that journey CI was still pending.


## 2026-11-08 — Owner M2 decisions, reference-led visual proposal and conditional private prototype scope

- Recorded D-016: POJ Studio primary, Macaroni Shoten secondary, Jaisalmer as DAG identity source; one coherent visual proposal requested with owner approval pending.
- Added docs/27-M2-A-REFERENCE-LED-VISUAL-PROPOSAL.md with live reference observations, measured/unmeasured findings, one exact proposed HEX system, proposed typography/hierarchy, wordmark requirements, six-area compositions, image-frame ratios, CSS tokens/components and desktop/mobile examples.
- Added docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md for the owner-approved seven-person Japan qualitative cohort, screening, objectives, neutral interview prompts, recruitment options, consent/privacy safeguards and indicative incentive/vendor costs. No recruitment, contact, personal-data collection, recording or spending is authorized.
- Added docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md mapping exactly six owner review areas to the unchanged nine-page D-014 kit and preparing desktop/mobile owner acceptance.
- M2-C now explicitly uses labelled layout placeholders and image frames pending approximately 10–20 genuine owner-supplied product photos and verified facts; no full photo-library migration.
- M2-D owner-approved five-journey priority replaces the previous recommendation-only state. Mobile remains cross-cutting; automated tests are explicitly not human usability acceptance.
- M2-E authorizes exactly six local/private non-transactional prototype areas only after M2-A visual approval. Prototype implementation must stay outside the public repository; no production app, public deployment, live transactions, recruitment or spending is authorized.
- Reconciled README, AGENTS, design authority, source-of-truth, owner registers, M2 pack, roadmap, catalogue intake, accessibility review and brand/visual system guidance.
- Updated M2 readiness audit and regression tests to enforce D-016, the visual-approval gate, seven-person cohort, placeholder boundaries and six-area private prototype scope. D-014 HTML/CSS/JS assets and the current token fallback remain unchanged.


## 2026-11-08 — M2 private prototype entry gate and local browser review
- Added a private prototype manifest schema and pending template for D-016's unchanged nine-page/six-area scope.
- Added a local validator that refuses prototype roots inside the public repository; cross-checks a numbered M2-A owner decision and the exact approved proposal SHA-256; enforces page/area inventory, visible placeholder labels, genuine-photo rights, verified product mapping and separate private prototype-use evidence.
- The static validator rejects remote resources, external embed/base/meta-refresh navigation, unsafe paths/symlinks, network APIs, browser persistence, active form controls, POST methods, form endpoints and transactional destinations.
- Added a local-only Playwright/Chromium review runner. It runs only after the static gate passes, blocks non-loopback requests, checks nine routes at five viewport widths and writes screenshots plus JSON/Markdown summaries outside both the public repository and prototype source.
- Added regression coverage for approval state/hash, exact routes/areas, placeholder and genuine-photo evidence, remote/network/transaction rejection, private-root constraints and browser-entry gating.
- No private prototype, product sample, genuine photographs, customer data or screenshots are committed. M2-A visual approval remains pending; D-014 kit assets and QA token fallback remain unchanged.

## 2026-11-09 — PR #14 private prototype review hardening
- Tightened the private manifest validator to fail closed on malformed types, unknown approval/asset fields, non-normalized asset paths and invalid calendar dates; kept the JSON schema, pending template and runtime checks aligned.
- Rejected inline event handlers, link ping beacons, form-associated submission overrides, background worker registration and cross-context messaging APIs in the non-transactional prototype scope. Added local-only checks for inline SVG image/symbol references and prohibited image-type submit controls.
- Hardened local browser review against symlinked prototype roots and added viewport-meta, browser-console, failed-request and HTTP resource-status evidence.
- Added eleven regression tests for new bypasses and malformed manifest conditions, including inline SVG resource references and image-type submit controls.
- Kept M2-A visual approval pending and made no changes to D-014 source assets, brand tokens, photography, catalogue records or private prototype files.
- Expanded final PR #14 continuation head `ac0d7474401c77c1eb8a805f65f8fac1e344624f` passed [DAG Project Quality run #143](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42511940719), including **136/136 Python tests**; the local private-prototype Chromium review was correctly not run without an approved prototype.


## 2026-11-09 — M2-A Revision 2 approval and private prototype authorization
- Recorded owner approval of Revision 2 “Material in Focus” as D-017, including the six exact colour roles, Source Serif 4 / Inter typography direction, type hierarchy, layout values, image-frame ratios and nine-page desktop/mobile compositions.
- Pinned the approved review-board artifact by SHA-256: 097ec2fd8fda3c64c8b478e846b3311caec95dc0cb20a22cf8a6c532f81bdeeb.
- Updated the M2-A proposal and owner token register with the approved private-prototype baseline; final logo artwork, descriptor wording, verified copy, sample photography and rights evidence remain separately pending.
- Confirmed that D-017 satisfies D-016's M2-A gate and authorizes only the six-area local/private, non-transactional prototype across the unchanged nine-page D-014 inventory.
- Reconciled the agent instructions, README, design authority, M2 roadmap, decision pack, walkthrough and prototype validation runbook. D-014 source HTML/CSS/JS and page/component inventories remain unchanged.


## 2026-11-09 — M2-E private prototype build and M2-D five-journey review
- Built the Revision 2 “Material in Focus” prototype outside the public repository, preserving the exact nine D-014 routes and six D-016 review areas.
- Kept the prototype non-transactional; product image frames and unverified product, maker, contact and editorial facts remain visibly pending.
- Completed the local responsive review: 45/45 route/viewport checks across 390, 430, 768, 1280 and 1440 CSS-pixel widths; 18 mobile/desktop screenshots retained in the private review package.
- Added scripts/private_prototype_journey_review.py for the five owner-prioritized M2-D customer journeys, with Playwright checks at all five viewport widths (25/25 passed).
- Journey checks cover the homepage-to-shop/product path; shop-to-collection/product path; product gallery, accordions and disabled purchase/options; About-to-Makers-to-Journal-to-Article; and product enquiry-to-Contact with disabled fields and no write endpoint.
- Added privacy-boundary and route/viewport regression tests. Review output remains outside the public repository and private prototype source.
- Updated the owner walkthrough, private-prototype runbook and roadmap. Owner visual acceptance and human customer usability acceptance remain outstanding.


## 2026-11-09 — M2 private prototype implementation revision 3
- Aligned the private prototype CSS with the exact D-017 palette, type hierarchy, spacing, content width, gutters and image-frame ratios; removed off-palette placeholder treatments, gradients and shadows.
- Added current-page/current-section semantics to the existing six navigation destinations without changing the route inventory.
- Refined the existing mobile navigation disclosure: Escape closes and restores focus to the toggle, destination selection closes the menu, and resizing to desktop clears the expanded state.
- Balanced the third existing homepage category card within the two-column mobile grid; no category, page, section or component was added.
- Extended the local/private journey runner with a D-017 CSS gate, explicit current-navigation mapping and responsive navigation interaction checks.
- Latest local/private evidence: 45/45 route/viewport checks, 18 screenshots, 25/25 journey/viewport checks and 125 responsive navigation disclosure checks. Ten Python regression tests pass.
- The actual prototype, its screenshots and review reports remain outside GitHub. No real product photography or verified catalogue facts were supplied; owner visual acceptance and human usability acceptance remain pending.


## 2026-11-09 — M2 private prototype implementation revision 4
- Differentiated the 34 existing image-frame slots by content evidence role across the nine routes; every visible and accessible label states that owner-approved source/photo/product mapping is pending.
- Converted the four Product Detail fact rows to semantic description-list pairs without adding or fabricating product details; price/currency remain pending.
- Upgraded the existing Collection, Product Detail and Article breadcrumbs to labelled navigation landmarks with the current page identified.
- Clarified Article introduction, publication date, authorship and source credits as pending owner verification.
- Improved narrow-screen wrapping for product-fact label/value pairs.
- Local private QA passed 45/45 route/viewport checks at 390/430/768/1280/1440px, 18 screenshots, zero horizontal overflow, 34/34 image slots, three breadcrumb landmarks and unchanged disabled controls.
- Extended the public journey runner to validate route-specific image evidence labels, fixed slot counts, breadcrumb semantics, semantic product facts and pending editorial metadata on every rendered page in the owner journeys.
- Private prototype content, images and captures remain outside GitHub. Owner visual acceptance and human customer usability acceptance remain pending.


## 2026-11-09 — M2-C private catalogue intake readiness report
- Hardened catalogue/photo-audit input boundaries: reject symlinked source directories and audit report files; require photo-audit traversal error count zero; reject Boolean-as-integer candidate counts; require recognized image formats and valid lowercase SHA-256 digests on audit rows marked ok.
- Added scripts/build_catalogue_readiness_report.py. It reuses the existing CSV and completed photo-audit validators and creates local/private JSON and Markdown readiness reports with aggregate coverage and per-product blockers.
- The report identifies separate product, fact, source reconciliation, image rights and private prototype-use gates, and confirms products remain draft/in_review. It excludes source titles, descriptions, prices, raw export values and image binaries.
- Added regression tests for audit integrity weaknesses, symlink handling, successful M2 readiness reporting, underfilled samples, per-product approval blockers, private output paths and no-overwrite behaviour.
- The report is a private operational aid only. No genuine 10–20 product/photo sample or real catalogue facts/rights evidence were provided; M2-C sample acceptance remains blocked on owner inputs.


## 2026-11-10 — M2 owner walkthrough record validation support
- Added a deliberately pending private JSON template and schema for the six D-016 owner-review areas and five established viewport widths.
- Added scripts/validate_owner_walkthrough.py to validate the owner-authored record, enforce the existing five observation dimensions, and require route/component-scoped requests for revision/rejection.
- Added private JSON/Markdown readiness summaries that contain decision and viewport counts only; free-text owner feedback is excluded.
- Enforced private repository boundaries, symlink rejection, no-overwrite behaviour and owner-only report-file permissions where supported.
- Added regression coverage for accepted, incomplete, revision, rejection, malformed, wrong-route, symlink and private-output cases.
- This makes the existing owner review easier to capture and audit; it does not perform the review or claim owner approval. The actual walkthrough, M2-C product/photo evidence and separately authorized research fieldwork remain pending.
