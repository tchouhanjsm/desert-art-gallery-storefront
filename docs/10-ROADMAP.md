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

- **M2-A — proposal ready, visual approval pending:** One reference-led visual proposal is prepared in docs/27. POJ Studio is primary, Macaroni Shoten secondary; no proposed colours/type/logo/photo direction is approved or applied. The owner retains final authority.
- **M2-B — cohort accepted:** Seven Japan-based qualitative participants are approved as a research plan (3 home/interior, 2 craft/material, 1 trade/design, 1 gift/considered-purchase). The full operations plan is docs/28. Recruitment, external contact, consent/data handling, recording, incentives and spend remain separately unauthorized.
- **M2-C — placeholder approach accepted, evidence pending:** Use clearly labelled layout placeholders and image-frame compositions. Product-image validation remains pending until approximately 10–20 genuine photos and verified product information are supplied. No full photography-library migration.
- **M2-D — journey order accepted:** Discover identity → browse products/categories/collections → evaluate product/images/verified specifications → explore makers/materials/editorial → contact/support. Mobile is cross-cutting across every journey. Automated testing passed; owner visual walkthrough and human usability acceptance remain separate.
- **M2-E — private prototypes conditionally authorized:** Exactly six local/private non-transactional areas: Homepage; Shop and Collections; Product Detail; About and Makers; Journal and Stories; Contact and Support. This is a six-area grouping across the unchanged nine-page D-014 kit. The shared shell appears only as already supplied. Begin branded implementation only after explicit M2-A visual approval. Keep prototype files out of the public repository.

### Owner review sequence
1. Review the single proposal in docs/27 and record exact accept/revise/reject decisions.
2. After M2-A approval, build the six private prototype areas using the approved visual tokens and D-014's exact page/section inventory.
3. Use labelled placeholders until the genuine product sample and verified facts are available.
4. Run responsive and accessibility automation; prepare the owner walkthrough in docs/26.
5. Record owner visual feedback separately from any future participant usability evidence.

### Completed automated structural evidence
- [DAG Project Quality run #90](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483703448): PASS, 101/101 Python tests and repository audits.
- [DAG Structural Kit Browser Review run #17](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483703451): PASS, 45/45 route/viewport, 25/25 journey/viewport, 54 keyboard sequences, reduced motion and 18 screenshots.
- [Browser artifact](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483703451/artifacts/13617914179).

These checks assess structural automation only. They do not validate customer demand, conduct human usability testing or constitute owner visual acceptance.

## Technical and commercial work

Preserve existing catalogue intake, photo audit, Etsy mapping, research and merchant documentation where valid. Do not select a production framework, database, CMS, hosting provider, payment provider, currency, sales territory, tax treatment, shipping terms, return policy or commercial model by inference.

## Explicit exclusions

No additional routes, sections, components, banners, testimonials, badges, reviews, widgets, icons, animations, popups, sticky/floating UI, chat/newsletter/social modules or new navigation. No cart, checkout, account, wishlist, live search/filter/sort, variants, payment, order operations, shipping calculation or returns workflow.

## Roadmap update rule

Update this roadmap only when an actual owner decision, evidence-backed milestone, implementation or validation result changes. State what is complete, incomplete and blocked without anticipating future results.
