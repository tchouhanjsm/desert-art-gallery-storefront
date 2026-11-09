# 10 — Roadmap

## Completed milestone — D-014 structural kit adoption

The owner-approved DAG Owner-Controlled Design Kit v2 is materialized at `design/owner-controlled-kit-v2/`. All 25 files are present. At adoption (PR #8), all 14 original HTML/CSS/JS files were byte-verified against the supplied ZIP by Git blob SHA-1 and exact file size. PR #9 amends two CSS files for accessibility maintenance and PR #11 amends the existing mobile responsive stylesheet for the Product Detail thumbnail-grid defect; three CSS assets now carry documented maintenance and the other 11 implementation assets remain byte-identical. PR #12 changes repository QA scripts/tests only, not the owner-supplied kit assets. The source-integrity validator enforces the closed file inventory and current reviewed source hashes.

This milestone adopts structure only. It does not approve brand identity, production styling, production app development, commerce functionality, hosting or technology choices.

### Completed evidence
1. All 25 source kit files materialized under the agreed path.
2. All 14 original implementation assets byte-verified.
3. All nine page paths and relative CSS/JS references validated by `scripts/validate_project.py`.
4. Active docs/prompts and old visual proposal paths reconciled to D-014.
5. Page/component inventories corrected against the supplied source.
6. CI validators and relevant tests updated for the new authority.
7. Repository reconciliation report, matrix, changelog and checklist committed.

## Completed maintenance delivery — accessibility and browser assurance (PR #9, PR #11 and PR #12)

The follow-up maintenance patch is limited to the supplied kit's existing CSS and does not alter the nine HTML pages, structure, copy, controls, disabled states, responsive breakpoints or token values:
- styles/components.css adds an explicit :focus-visible outline using currentColor; no brand colour is introduced.
- styles/layout.css respects prefers-reduced-motion by disabling the existing smooth-scroll behaviour.
- The static accessibility audit now uses a standard-library HTML parser to check page titles, accessible names, labels, image alternatives, unique IDs, sequential heading hierarchy, ARIA ID relationships and positive `tabindex` values.
- Regression fixtures cover valid labelled markup and failures such as duplicate IDs, missing names, empty links and dangling ARIA references.
- Chromium browser QA covers live DOM semantics and native Enter/Space operation of the existing mobile navigation disclosure, including `aria-expanded` and focus retention. It remains isolated from the storefront runtime.
- No owner-supplied HTML, CSS or JavaScript was changed by PR #12; no page, section, navigation item, component or visible control was added or removed.

### Validation completed — PR #12
- [DAG Project Quality run #79](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42466004185) — PASS: project/source integrity, M2 owner-gate consistency, static accessibility semantics, repository-wide documentation consistency, Markdown links and **89/89 Python tests**.
- [DAG Structural Kit Browser Review run #7](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42466004123) — PASS: **45/45** route/viewport combinations, **54** mobile keyboard-operation sequences, reduced-motion review and **18** full-page screenshots with JSON/Markdown summaries.
- These results provide automated structural and browser evidence only; they are not screen-reader testing, WCAG certification, colour-contrast approval or owner visual sign-off.

## M2 owner decisions and next delivery gates — D-016

The owner has now confirmed the M2-A through M2-E decisions. The previous PR #13 structural-review automation remains complete; D-016 defines the current owner-approved plan and conditional private-prototype scope.

- **M2-A — approved under D-017:** Revision 2 “Material in Focus” is approved for private prototype implementation: palette, Source Serif 4 / Inter pairing, hierarchy, layout values, photography principles and all nine page compositions. Final logo artwork, descriptor wording, copy and genuine product-image evidence remain separate.
- **M2-B — cohort accepted:** Seven Japan-based qualitative participants are approved as a research plan (3 home/interior, 2 craft/material, 1 trade/design, 1 gift/considered-purchase). The full operations plan is docs/28. Recruitment, external contact, consent/data handling, recording, incentives and spend remain separately unauthorized.
- **M2-C — placeholder approach accepted, evidence pending:** Use clearly labelled layout placeholders and image-frame compositions. Product-image validation remains pending until approximately 10–20 genuine photos and verified product information are supplied. No full photography-library migration.
- **M2-D — journey order accepted and automated review implemented:** Discover identity → browse products/categories/collections → evaluate product/images/verified specifications → explore makers/materials/editorial → contact/support. Mobile is cross-cutting across every journey. The new private journey runner passes 25/25 combinations across all five review widths. Owner visual walkthrough and human usability acceptance remain separate.
- **M2-E — private prototype implementation authorized:** D-017 satisfies the visual approval condition. Build exactly six local/private non-transactional areas: Homepage; Shop and Collections; Product Detail; About and Makers; Journal and Stories; Contact and Support. This is a six-area grouping across the unchanged nine-page D-014 kit. Keep prototype files out of the public repository.

### Owner review sequence
1. D-017 records approval of the Revision 2 proposal and the exact approved visual baseline.
2. **Complete:** Build the six private prototype areas using the approved values and D-014's exact nine-page/section inventory; keep all prototype files outside the public repository.
3. Use labelled placeholders until the genuine product sample and verified facts are available.
4. **Complete:** Run local static validation, responsive/accessibility review (45/45), and the five-journey review (25/25); prepare the owner walkthrough in docs/26.
5. **Pending:** Record owner visual feedback separately from any future participant usability evidence.

### Completed automated structural evidence
- [DAG Project Quality run #90](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483703448): PASS, 101/101 Python tests and repository audits.
- [DAG Structural Kit Browser Review run #17](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483703451): PASS, 45/45 route/viewport, 25/25 journey/viewport, 54 keyboard sequences, reduced motion and 18 screenshots.
- [Browser artifact](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483703451/artifacts/13617914179).

These checks assess structural automation only. They do not validate customer demand, conduct human usability testing or constitute owner visual acceptance.

## Completed delivery — M2-E private prototype and M2-D five-journey automation

Following PR #13's merge, the next bulk engineering slice adds the private-prototype validation pipeline without bypassing the M2-A approval gate:
- `scripts/validate_private_prototype.py` validates an external private prototype root, exact D-014 routes and D-016 six-area map, M2-A owner-decision reference and proposal SHA-256, image asset ledger, placeholder labels, rights/prototype-use references, semantic page structure and prohibited network/transaction behaviour.
- `schemas/private-prototype-manifest.schema.json` and `templates/private-prototype-manifest.template.json` provide a machine-readable manifest contract. The template is deliberately pending until the owner supplies a visual approval decision.
- `scripts/private_prototype_browser_review.py` performs local-only Chromium review at 390, 430, 768, 1280 and 1440px, including screenshots and JSON/Markdown summaries outside the public repository. It blocks external browser requests and will not run until the static gate passes.
- `scripts/private_prototype_journey_review.py` runs the five owner-approved customer journeys at all five widths (25 combinations), covering page transitions, product accordions, disabled commerce controls, and the disabled non-submitting enquiry concept. It renders the exact local HTML/CSS/JS in-memory, resolves clicked relative links with the browser URL algorithm, and writes JSON/Markdown summaries outside the repository.
- Regression tests cover owner approval/hash matching, routes/groupings, placeholders, genuine-photo evidence, private path boundaries, disabled forms, network APIs and transaction paths.

**M2-E private prototype implementation is complete as a local review artifact; M2-D automated journey coverage is complete.** The actual nine-page Revision 2 prototype remains outside the public repository. Current automated evidence: 45/45 route/viewport checks, 18 screenshots, and 25/25 five-journey/viewport checks. No genuine product/photo sample has been supplied; owner visual acceptance and human usability acceptance remain pending.

### PR #14 continuation — private review assurance hardening

The same PR extends the readiness gate without starting prototype styling:
- The manifest validator now fails closed on non-integer schema versions, malformed approval states, non-calendar dates, unsupported approval/asset metadata fields, unnormalized asset paths and non-string genuine-photo evidence references.
- It rejects inline event handlers, link `ping` beacons, form-associated submission overrides, service-worker/worker registration and cross-context messaging APIs in addition to the existing transaction/network restrictions.
- The local Chromium runner rejects symlinked prototype roots, checks the viewport meta tag and records browser-console errors, failed requests and unsuccessful HTTP resource responses as review failures.
- Regression coverage adds eleven tests for malformed metadata, path normalization, inline event handlers, worker/network overrides, approval-date validation, SVG references, image-type submit controls and review-root boundaries.

The continuation was implemented and validated at PR #14 head `ac0d7474401c77c1eb8a805f65f8fac1e344624f`. [DAG Project Quality run #143](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42511940719) passed source/foundation, M2 gate, accessibility, documentation consistency and Markdown link audits, with **136/136 Python tests** passing. The private Chromium review was not run because no approved private prototype exists; it remains a local-only step after M2-A approval. These controls still do not certify arbitrary script safety, owner approval, customer usability or production readiness.

## Technical and commercial work

Preserve existing catalogue intake, photo audit, Etsy mapping, research and merchant documentation where valid. Do not select a production framework, database, CMS, hosting provider, payment provider, currency, sales territory, tax treatment, shipping terms, return policy or commercial model by inference.

## Explicit exclusions

No additional routes, sections, components, banners, testimonials, badges, reviews, widgets, icons, animations, popups, sticky/floating UI, chat/newsletter/social modules or new navigation. No cart, checkout, account, wishlist, live search/filter/sort, variants, payment, order operations, shipping calculation or returns workflow.

## Roadmap update rule

Update this roadmap only when an actual owner decision, evidence-backed milestone, implementation or validation result changes. State what is complete, incomplete and blocked without anticipating future results.


## Completed local implementation — Revision 4 content evidence and semantics

The private prototype now differentiates all existing image slots by their intended evidence role (homepage, category, catalogue product, product gallery view, place/material, maker portrait, Journal story and Article lead). Every frame remains explicitly illustrative and pending; no image is presented as genuine DAG photography. The exact slot counts remain unchanged across all nine D-014 routes.

Product Detail retains the same four facts but exposes them as a semantic description list; each value and price/currency remains pending owner verification. Existing breadcrumbs on Collection, Product Detail and Article are labelled navigation landmarks with a current item. Article introduction, publication date, authorship and source credits remain pending. Mobile fact rows wrap without horizontal overflow.

Local Revision 4 evidence: 45/45 route/viewport render checks across 390, 430, 768, 1280 and 1440px; 18 screenshots; zero horizontal overflow; 34/34 image slots with visible/accessibility labels; 3/3 breadcrumb routes; four semantic product fact pairs; all product accordions/disabled controls retained. The journey runner is extended to re-check content-evidence slots and semantic page states on every rendered journey page. These remain automated checks, not owner sign-off or participant usability acceptance.


## M2-C implementation — private catalogue intake readiness reporting

The source-neutral intake validator was hardened to reject symlinked catalogue/audit inputs, photo-audit summaries with traversal errors or Boolean candidate counts, and status=ok image-audit rows without a recognized format and lowercase 64-character SHA-256 digest.

Added scripts/build_catalogue_readiness_report.py. It reuses the existing five-CSV validator and completed photo-audit inventory, then writes private JSON/Markdown reports with aggregate intake coverage and per-product blockers for owner-reconciled source rows, product-level private-use approval, verified/prototype-approved fact evidence, rights-cleared/prototype-approved primary image evidence, and draft/in-review publication state. The report excludes product copy, prices, source-export values and image binaries; output paths cannot overlap the public repository or catalogue source directory and existing reports are not overwritten.

This completes the readiness-reporting tooling only. The real 10–20 product/photo sample, verified facts, source reconciliation and image-rights/prototype-use evidence remain owner-supplied inputs and have not been fabricated or staged in Git.
