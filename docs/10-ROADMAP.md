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

## M2 combined delivery — structural review and decision package

D-015 records the owner's 8 November 2026 instruction as authorization for the exact bounded, non-production structural review. The active branch implements five customer journeys at 390, 430, 768, 1280 and 1440px, while retaining the nine-route responsive review and existing keyboard checks. The journey review does not alter the owner kit's HTML/CSS/JS files or enable disabled controls.

- **M2-A — blocked on owner input:** no brand colours, type families/weights/hierarchy, wordmark/logo/descriptor or photo direction have been supplied/approved. The system-token fallback and historic proposals cannot be reused.
- **M2-B — recommendation prepared:** first qualitative cohort proposed as home/interior shoppers with textile/craft interest, alongside craft/material enthusiasts and a small trade/gift contrast. No interviews, recruitment, incentives or external data collection are claimed.
- **M2-C — blocked on source evidence:** no owner-supplied 10–20 product photo/fact sample is present. The private intake validator now distinguishes prototype-use permission from public publication approval and enforces rights evidence and completed photo-audit checks.
- **M2-D — automation implemented:** five structural journeys and five viewport widths create 25 journey/viewport checks. Journey order is recommended, not represented as an owner-approved customer priority. Human usability evaluation remains separate.
- **M2-E — authorized for bounded review:** D-015 permits only the non-production review described in the M2 pack. It does not authorize final brand styling, external participant studies, new UI scope, production application work or deployment.

See docs/25-M2-DECISION-AND-REVIEW-PACK.md for segment reasoning, exact journey order, market evidence, sample acceptance and remaining owner input.

## Owner gates retained

- **Brand identity:** exact colours, typography, logo/wordmark/descriptor and photography direction remain pending owner input. The system-token fallback is QA only.
- **Customer validation:** Japan-first segments and journey priority remain to be confirmed; no fieldwork is represented as complete.
- **Product/photo evidence:** only owner-approved genuine sample photographs with verified mapping and rights may be used; label placeholders for missing views (D-011).
- **Responsive journey acceptance:** mobile/tablet/desktop must be tested across every selected journey (D-012).
- **Next-phase authorization:** D-014 alone does not authorize added prototype scope or production development.

### M2 implementation validation status

The M2 branch's GitHub Actions checks are required before this package is considered technically green. Do not claim the new journey matrix or expanded sample validator passed until those final-head runs have completed.

## Technical and commercial work

Preserve existing catalogue intake, photo audit, Etsy mapping, research and merchant documentation where valid. Do not select a production framework, database, CMS, hosting provider, payment provider, currency, sales territory, tax treatment, shipping terms, return policy or commercial model by inference.

## Explicit exclusions

No additional routes, sections, components, banners, testimonials, badges, reviews, widgets, icons, animations, popups, sticky/floating UI, chat/newsletter/social modules or new navigation. No cart, checkout, account, wishlist, live search/filter/sort, variants, payment, order operations, shipping calculation or returns workflow.

## Roadmap update rule

Update this roadmap only when an actual owner decision, evidence-backed milestone, implementation or validation result changes. State what is complete, incomplete and blocked without anticipating future results.
