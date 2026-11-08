# M2 — Structural Kit Review and Prototype Entry

**Status:** D-014's nine-page structural scope remains the only active UI baseline. PR #12 has been merged and its final-head CI evidence is recorded below. This M2 branch adds five automated customer-journey scenarios and a strict private sample validator; it does not change any owner-supplied HTML, CSS or JavaScript asset. D-015 authorizes only the bounded structural, non-production review recorded in docs/25-M2-DECISION-AND-REVIEW-PACK.md. M2-A and M2-C still require owner inputs/evidence; M2-B and M2-D recommendations still need owner adoption for external research/priority; M2-E is authorized only for the bounded review scope.

## Governing baseline

D-014 establishes the exact nine-page structural baseline. Use only `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`. D-011 mixed genuine-photo/labelled-placeholder evidence and D-012 mobile-across-every-journey remain active. D-013's six-page scope is superseded.

| Gate | Required owner input / evidence | Current status |
|---|---|---|
| M2-A — Brand identity | Exact owner-approved colours, type families/weights/hierarchy/type scale, logo/wordmark/descriptor and photography direction/crop rules; record in docs/OWNER-TOKEN-INPUT.md and DECISIONS.md. | **Blocked on owner input** — no brand tokens or identity assets have been supplied/approved; do not infer historic palette/type |
| M2-B — Customer segment / journey | Confirm the initial Japan-first research cohort and prioritized customer tasks; approve recruitment route, consent handling and any spending separately. | **Recommendation prepared; owner adoption pending** — proposed primary context is home/interior buyers with textile/craft interest; no recruitment or fieldwork |
| M2-C — Product/photo evidence | Owner-supplied 10–20 real product records and mapped original photos; verify product facts, image identity, rights and separate prototype-use permission. | **Blocked on sample/evidence** — no original product sample/export/photo set is present in the active project inputs |
| M2-D — Responsive journey coverage | Confirm journey order; cover mobile/tablet/desktop for each journey (D-012). | **Execution matrix implemented; owner priority/human acceptance pending** — five journeys × five widths are covered by automated Chromium checks |
| M2-E — Next-phase authorization | Exact prototype/review scope, acceptance criteria and non-production boundary. | **Authorized for bounded structural review only** under D-015; no branded prototype expansion, external research or production work is authorized |

## Bounded M2 review scope authorized by D-015

The owner instruction dated 8 November 2026 authorizes the following repository-side work, only:

- Exercise five existing structural journeys: Home → Shop → Collection; Shop → Collection → Product; Product information/disabled-state review; About → Makers → Journal → Article; Product → Enquire → Contact.
- Review all nine supplied routes at 390, 430, 768, 1280 and 1440 CSS-pixel widths.
- Exercise only interactions already present in the kit: mobile navigation, product information accordions and links. Purchase, variant, search, filter/sort and contact submission remain disabled.
- Record machine-readable and Markdown summaries, failures and screenshots as CI artifacts.
- Keep the prototype local/non-production and preserve the D-014 source asset boundary.

This is not a branded visual prototype approval, usability study with participants, production application authorization, or public deployment permission. The exact scope, M2 disposition and owner handoff are detailed in docs/25-M2-DECISION-AND-REVIEW-PACK.md.

## Nine-page baseline

1. `index.html` — Home: hero; three category slots; four curated product slots; brand/material feature split; two journal/story slots.
2. `pages/shop.html` — Shop: intro; disabled filter/sort toolbar; category links; product grid.
3. `pages/collection.html` — Collection: compact intro; disabled filter/sort toolbar; product grid.
4. `pages/product.html` — Product: breadcrumbs; gallery plus three thumbnails; facts; disabled option/purchase controls; enquiry link; Description, Materials and specifications, Maker and provenance, Care accordions.
5. `pages/about.html` — About: intro and two editorial splits, second reverse.
6. `pages/makers.html` — Makers: intro and maker profile.
7. `pages/journal.html` — Journal: intro and five story cards.
8. `pages/article.html` — Article: article header, lead image and body.
9. `pages/contact.html` — Contact: intro, contact-information panel and disabled enquiry-form concept.

Shared shell elements are limited to the kit-only notice, utility location row, text wordmark/descriptor placeholder, six supplied navigation destinations, mobile navigation toggle, disabled Search where present, Enquire where supplied and supplied footer groups. Preserve page-specific omissions exactly.

## Latest structural browser assurance

PR #12 final-head evidence (already merged):
- [DAG Project Quality run #81](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42466218616) — PASS, **89/89 Python tests**.
- [DAG Structural Kit Browser Review run #8](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42466218645) — PASS, **45/45 route/viewport checks**, **54** mobile Enter/Space navigation sequences, reduced-motion check and 18 screenshots.

The M2 branch extends browser review with **25 journey/viewport checks** (five bounded journeys × five viewport widths). Its final results are not claimed until the new PR's GitHub Actions runs complete.

## Closed behaviour and content boundary

Keep existing disabled controls disabled. There is no cart, checkout, account, wishlist, live search/filter/sort, variant selection, purchase action, payment, order operation, inventory reservation, shipping calculation, returns workflow or enquiry backend. Do not add banners, testimonials, badges, reviews, widgets, popups, chat, newsletter/social, extra navigation, sticky/floating UI, animation or other sections/components.

Customer-facing language remains English-only. Japan-first does not authorize Japanese UI. Never fabricate products, makers, materials, dimensions, prices, provenance, stock, reviews, ratings, contact information, policies or delivery claims.

## Responsive review

Review the supplied layout at 390, 430, 768, 1280 and 1440 CSS-pixel widths. These are review widths, not permission to invent or change breakpoints. PR #11 corrected the Product Detail thumbnail-grid overflow at 390px and 430px. PR #12's latest Chromium run passed all 45 route/viewport combinations, with no horizontal overflow, browser page errors or failed local document/style/script assets. It also passed 54 Enter/Space mobile navigation sequences across the nine pages and three mobile/tablet widths, checking disclosure state and focus retention. The run uploaded 18 full-page screenshots plus JSON/Markdown summaries; see the linked workflow and current evidence in `docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md`. Do not restyle the kit or add functionality to resolve a visual defect without owner approval when it changes the visual contract.

## Static accessibility maintenance already applied

- All nine pages retain lang=en, exactly one main landmark with id=main-content, exactly one h1 and the supplied mobile navigation toggle with aria-expanded, aria-controls and its text label.
- The supplied sort, variant and enquiry controls remain disabled and retain their existing labels.
- styles/components.css provides a visible :focus-visible outline using currentColor; no palette or token value was selected.
- styles/layout.css disables existing smooth scrolling when prefers-reduced-motion: reduce is active.
- No skip-link component, page, section, navigation destination, control or interaction was added. The current closed inventory remains authoritative.

PR #12 adds a structural HTML parser audit for document titles, accessible names, form labels, image alternatives, unique IDs, sequential heading levels, ARIA ID relationships and positive `tabindex`, plus regression fixtures for valid and deliberately malformed markup. The successful Chromium run provides browser-rendered responsive and keyboard evidence for the current pages. Screen-reader behaviour, touch-target adequacy, zoom/reflow and WCAG conformance remain unverified.

## Entry and acceptance sequence

1. Complete: the 25 source-kit files are materialized; the 14 original implementation assets were byte-verified at D-014 adoption. Current source hashes are enforced by scripts/validate_project.py.
2. Complete at source level: validate all page links, relative stylesheet/script paths, English language, main landmarks, heading count, menu state, focus CSS and reduced-motion support.
3. Complete for the current structural baseline: PR #12 Chromium run [#42466004123](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42466004123) passed 45/45 route/viewport combinations at 390, 430, 768, 1280 and 1440 CSS-pixel widths; 54 mobile keyboard-operation sequences and reduced-motion review also passed. The run uploaded 18 full-page screenshots and JSON/Markdown summaries.
4. Resolve owner gates M2-A through M2-E before any branded prototype/customer study that depends on them.
5. Use only verified product facts and owner-cleared sample photographs; label placeholders clearly.
6. Obtain explicit owner acceptance before advancing to production design or application work.

**No production application development, technology selection or public deployment is authorized by this pack.**
