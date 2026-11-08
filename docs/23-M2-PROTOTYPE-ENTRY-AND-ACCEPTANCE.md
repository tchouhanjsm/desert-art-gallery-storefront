# M2 — Structural Kit Review and Prototype Entry

**Status:** The owner-supplied nine-page structural scope is recorded in D-014 and materialized at design/owner-controlled-kit-v2/ (25 files). PR #8 verified all 14 original HTML/CSS/JS assets against the owner archive. PR #9 adds two CSS-only accessibility maintenance rules documented in docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md; all nine HTML pages remain unchanged. M2 customer validation and any later prototype work remain owner-gated.

## Governing baseline

D-014 establishes the exact nine-page structural baseline. Use only `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`. D-011 mixed genuine-photo/labelled-placeholder evidence and D-012 mobile-across-every-journey remain active. D-013's six-page scope is superseded.

| Gate | Required owner input / evidence | Current status |
|---|---|---|
| M2-A — Brand identity | Exact owner-approved colours, typography/weights/hierarchy, logo/wordmark/descriptor and photography direction; documented in `docs/OWNER-TOKEN-INPUT.md` and `DECISIONS.md`. | Open — structural kit is not identity approval |
| M2-B — Customer segment / journey | Confirm initial Japan-first customer segment and prioritized customer tasks before recruiting or running sessions. | Open — no fieldwork is complete |
| M2-C — Product/photo evidence | Owner-approved representative real sample with verified product/image mapping and rights/permissions; labelled placeholders for missing views/states (D-011). | Open — sample and rights approval outstanding |
| M2-D — Responsive journey coverage | Owner confirms journey order; evaluate mobile/tablet/desktop across every selected journey (D-012). | Open — mobile is a required dimension, not a separate journey |
| M2-E — Next-phase authorization | Explicit owner authorization for the exact prototype/review work, acceptance criteria and non-production boundary. | Open — D-014 alone does not authorize expansion or production implementation |

Open gates block only dependent work. They do not block safe documentation maintenance, source-kit verification, accessibility review of the supplied markup or factual catalogue preparation.

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

## Closed behaviour and content boundary

Keep existing disabled controls disabled. There is no cart, checkout, account, wishlist, live search/filter/sort, variant selection, purchase action, payment, order operation, inventory reservation, shipping calculation, returns workflow or enquiry backend. Do not add banners, testimonials, badges, reviews, widgets, popups, chat, newsletter/social, extra navigation, sticky/floating UI, animation or other sections/components.

Customer-facing language remains English-only. Japan-first does not authorize Japanese UI. Never fabricate products, makers, materials, dimensions, prices, provenance, stock, reviews, ratings, contact information, policies or delivery claims.

## Responsive review

Review the supplied layout at 390, 430, 768, 1280 and 1440 CSS-pixel widths. These are review widths, not permission to invent or change breakpoints. Record observed clipping, overflow, navigation access, image behaviour, focus visibility and reading order. Do not restyle the kit or add functionality to resolve a visual defect without owner approval when it changes the visual contract.

## Static accessibility maintenance already applied

- All nine pages retain lang=en, exactly one main landmark with id=main-content, exactly one h1 and the supplied mobile navigation toggle with aria-expanded, aria-controls and its text label.
- The supplied sort, variant and enquiry controls remain disabled and retain their existing labels.
- styles/components.css provides a visible :focus-visible outline using currentColor; no palette or token value was selected.
- styles/layout.css disables existing smooth scrolling when prefers-reduced-motion: reduce is active.
- No skip-link component, page, section, navigation destination, control or interaction was added. The current closed inventory remains authoritative.

These are static source checks only. Actual browser rendering, keyboard traversal, screen-reader behaviour and responsive review at all specified widths remain unverified until run.

## Entry and acceptance sequence

1. Complete: the 25 source-kit files are materialized; the 14 original implementation assets were byte-verified at D-014 adoption. Current source hashes are enforced by scripts/validate_project.py.
2. Complete at source level: validate all page links, relative stylesheet/script paths, English language, main landmarks, heading count, menu state, focus CSS and reduced-motion support.
3. Still required: run rendered browser review at 390, 430, 768, 1280 and 1440 CSS-pixel widths; record clipping, overflow, focus, navigation, image behaviour and reading order.
4. Resolve owner gates M2-A through M2-E before any branded prototype/customer study that depends on them.
5. Use only verified product facts and owner-cleared sample photographs; label placeholders clearly.
6. Obtain explicit owner acceptance before advancing to production design or application work.

**No production application development, technology selection or public deployment is authorized by this pack.**
