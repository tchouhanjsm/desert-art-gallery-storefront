# M2 — Structural Kit Review and Prototype Entry

**Status:** D-014's nine-page structural kit remains unchanged. D-016 records the owner's M2-A–E scope and D-017 records approval of the Revision 2 visual direction for the six-area local/private prototype. The seven-person Japan research cohort and five-journey priority remain approved as plans; genuine product evidence remains pending. No production or public deployment is authorized.

## Governing baseline

D-014 establishes the exact nine-page structural baseline. Use only `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`. D-011 mixed genuine-photo/labelled-placeholder evidence and D-012 mobile-across-every-journey remain active. D-013's six-page scope is superseded.

| Gate | Required owner input / evidence | Current status |
|---|---|---|
| M2-A — Visual identity | Review the single reference-led proposal and explicitly approve/revise colours, typography, logo/wordmark/descriptor and photo direction. | **Revision 2 visual direction approved under D-017 for the local/private prototype** — production use and remaining identity/content inputs retain separate gates |
| M2-B — Customer research | Approved seven-person Japan-based cohort; separately approve route, consent, data handling, moderator, recording and any costs before fieldwork. | **Cohort approved as a plan; fieldwork authorization pending** — no recruitment, contact or collection |
| M2-C — Product/photo evidence | Use labelled placeholders and image frames until owner supplies 10–20 genuine product photos and verified information; keep intake/fact checks ready. | **Placeholder approach approved; sample pending** — no image validation or full-library migration |
| M2-D — Responsive journeys | Five owner-prioritized journeys; evaluate each on mobile, tablet and desktop; retain human owner and usability acceptance. | **Priority approved; automation passed; human review pending** — automation is not usability validation |
| M2-E — Private prototype authorization | Exactly six local/private non-transactional areas under D-016; D-017 records M2-A approval and permits branded private implementation. | **Private prototype implementation authorized** — no production, public deployment or new UI scope |

## Private prototype authorization under D-016

D-016 authorizes private/local, non-transactional HTML/CSS prototypes for exactly six areas:
1. Homepage — index.html.
2. Shop and Collections — pages/shop.html and pages/collection.html.
3. Product Detail — pages/product.html.
4. About and Makers — pages/about.html and pages/makers.html.
5. Journal and Stories — pages/journal.html and pages/article.html.
6. Contact and Support — pages/contact.html.

Global header, supplied navigation, search presentation, shared components and footer are included only where relevant. These six review groupings do not replace or expand the exact nine-page D-014 structural inventory.

**Start gate:** branded prototype implementation begins only after the owner explicitly approves the single M2-A visual proposal. Build locally/private and keep all implementation outside this public repository. Use only the proposed/approved layout within current page and component inventories. Until genuine 10–20 product sample records and images are supplied and verified, use clearly labelled image frames and layout placeholders.

Allowed: responsive layout implementation, shared component demonstrations and non-transactional interaction demonstrations within the six areas. Cart/checkout concepts may be represented only when needed to explain the journey, never as a live transaction or approved commercial commitment.

Excluded: production application, live payment/orders, shipping/tax calculations, external recruitment, public deployment, paid services/subscriptions, full photography-library migration, new pages/sections/widgets/promotional content/interactions, or unapproved brand/commercial model changes. Search/filter/sort, variant, purchase and enquiry submission remain disabled.

D-015 remains the decision record for the completed repository-side structural review and its automated checks. D-016 extends the authorized scope only to the six private prototype areas after M2-A visual approval.

## Private prototype entry and automated review gate

The next implementation-readiness phase is governed by [29 — M2 Private Prototype Validation and Review](29-M2-PRIVATE-PROTOTYPE-VALIDATION-AND-REVIEW.md). The repository now contains a manifest schema/template, a private-root validator and a local-only Chromium runner. The tools require:
- A private prototype directory outside this public repository.
- An explicit owner decision approving M2-A, cross-referenced by the manifest.
- A SHA-256 match to the exact approved visual-proposal revision.
- The unchanged nine-page D-014 map and exact six D-016 groupings.
- A complete local image ledger with exact visible placeholder labels or genuine-photo rights, product-mapping and separate prototype-use evidence.
- Local-only assets and code; no external network calls, persistence, transaction endpoints, active form controls or POST operations.

The local browser runner checks all nine routes at five viewport widths, reduced-motion, landmarks, image loading, accessible names, keyboard focus and disabled forms. It writes 18 screenshots and review summaries to a local output directory outside the repository. No private prototype or screenshot is uploaded to CI/GitHub. Current M2-A approval is still pending, so no actual prototype run is claimed and the existing template remains `pending`.

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

The M2 branch adds **25 journey/viewport checks** (five bounded journeys × five viewport widths). Their successful final-head results are recorded in the PR #13 evidence section below.

## PR #13 — Final M2 browser and quality acceptance evidence

On PR #13's final code head before the documentation-only evidence sync:

- [DAG Project Quality run #89](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483463438) — PASS: **101/101 Python tests**, foundation/source-integrity checks, M2 disposition audit, accessibility source audit, documentation consistency and Markdown links.
- [DAG Structural Kit Browser Review run #16](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483463352) — PASS: **45/45** route/viewport checks, **25/25** journey/viewport checks, **54** mobile Enter/Space focus-retention sequences, reduced-motion check and **18** full-page screenshots. The artifact contains JSON/Markdown summaries: [CI artifact](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483463352/artifacts/13619045256).

This automated evidence verifies the bounded structural review only. It does not replace owner visual sign-off, participant usability research, screen-reader testing, WCAG certification or acceptance of genuine product content/photos.

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
4. M2-A visual approval is recorded under D-017; implement the six authorized private prototype areas outside the public repository.
5. Until the 10–20 genuine sample is supplied, use labelled image frames and layout placeholders; do not claim image validation.
6. Keep M2-B fieldwork separately blocked until recruitment, consent/privacy, data handling and cost are authorized.
7. Conduct the owner-led six-area visual walkthrough and record requested changes; do not equate automation with human usability acceptance.

**No production application development, technology selection or public deployment is authorized by this pack.**
