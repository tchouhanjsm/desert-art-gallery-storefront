# Current Component Inventory — DAG Owner-Controlled Design Kit v2

**Status:** Active closed structural inventory transcribed from supplied HTML/CSS/JS. It describes existing structure and disabled states, not final brand appearance or a production component library.

## Shared shell

- Kit-only preview notice (not a marketing/announcement banner).
- Utility location row with DAG/Jaisalmer text placeholder.
- Text wordmark and descriptor placeholder.
- Primary navigation exactly: Shop, Collections, About, Makers, Journal, Contact.
- Mobile navigation toggle with supplied aria state.
- Search action disabled/visual-only where present.
- Enquiry link/action where supplied.
- Footer with supplied brand/location placeholder and Shop, Discover and Support groups.
- `prototype.js`: mobile navigation toggle and current-year text only.

## Homepage — `index.html`

- Hero copy and hero media placeholder.
- Primary collection action and About link.
- Category discovery grid: exactly 3 slots.
- Curated product grid: exactly 4 slots.
- One brand/material feature split.
- Journal/story preview grid: exactly 2 slots.

## Shop — `pages/shop.html`

- Page intro.
- Catalogue toolbar with pending count and disabled Filter/Sort affordances.
- Category links: exactly 3 placeholders.
- Product grid: exactly 6 structural placeholder cards.

## Collection — `pages/collection.html`

- Breadcrumbs.
- Compact page intro.
- Disabled Filter/Sort toolbar.
- Product grid: exactly 3 structural placeholder cards.

## Product detail — `pages/product.html`

- Breadcrumbs.
- Main gallery and exactly 3 thumbnail slots.
- Product information column with pending price/description fields.
- Disabled variant control.
- Disabled purchase action placeholder.
- Enquiry link.
- Four accordions: Description; Materials and specifications; Maker and provenance; Care.

## About and Makers

- About: page intro and 2 editorial split sections; second uses reverse ordering.
- Makers: page intro and maker profile layout with image/text placeholders.

## Journal and Article

- Journal: page intro and story-card grid (6 placeholders).
- Article: breadcrumb, article header, lead-image placeholder and article body.

## Contact

- Page intro and contact-information panel with real details pending.
- Disabled enquiry-form concept; do not enable without an approved endpoint/privacy workflow and explicit authorization.

## Closed inventory and interactions

Do not add badges, testimonials, reviews, ratings, banners, announcement bars, newsletter, social feeds, animations, popups, sticky bars, chat, new icons, extra navigation, recommendation/related modules or other components/functions not listed above.

Disabled/visual-only controls must stay disabled. Never infer functionality from labels or appearance. No commerce, payment, cart, checkout, account, wishlist, live search/filter/sort, purchase, shipping calculation, returns, order or inventory workflow is included.
