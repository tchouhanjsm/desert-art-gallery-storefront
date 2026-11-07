# Current Page Inventory — DAG Owner-Controlled Design Kit v2

**Status:** Active structural contract (D-014). Transcribed from the nine supplied HTML files. It defines exact route/section scope only; it does not approve brand tokens, copy, product facts or production behaviour.

| # | Source | Page | Exact supplied top-level content |
|---:|---|---|---|
| 1 | `index.html` | Homepage | Hero; category discovery grid (3 slots); selected/curated product grid (4 slots); brand/material feature split; Journal/story preview (2 slots). |
| 2 | `pages/shop.html` | Shop / all products | Page intro; catalogue toolbar with disabled filter/sort; 3 category-link placeholders; product grid (6 placeholder cards). |
| 3 | `pages/collection.html` | Category / collection | Breadcrumbs; compact page intro; disabled filter/sort toolbar; product grid (3 placeholder cards). |
| 4 | `pages/product.html` | Product detail | Breadcrumbs; main gallery and 3 thumbnails; product information; disabled option and purchase controls; enquiry link; 4 detail accordions. |
| 5 | `pages/about.html` | About DAG | Page intro; editorial split; reverse editorial split. |
| 6 | `pages/makers.html` | Makers | Page intro; maker profile layout. |
| 7 | `pages/journal.html` | Journal index | Page intro; story-card grid (6 placeholder cards). |
| 8 | `pages/article.html` | Journal article | Breadcrumb; article header; lead image; article body. |
| 9 | `pages/contact.html` | Contact / support | Page intro; contact information panel; disabled enquiry-form concept. |

## Shared shell

All nine pages use the supplied shared shell. Preserve page-specific omissions exactly as present in HTML:

- Kit-only preview notice.
- Utility location row.
- Text wordmark and descriptor placeholder.
- Primary navigation exactly as supplied: Shop, Collections, About, Makers, Journal, Contact.
- Mobile navigation toggle.
- Disabled/visual-only search action where present.
- Enquiry action where supplied.
- Shared footer groups.
- Supplied `prototype.js`.

Do not add announcement bars, navigation entries, account/cart controls or any other shell item.

## Responsive contract

Use the supplied `styles/responsive.css`. Review at 390, 430, 768, 1280 and 1440 CSS-pixel widths. These are review widths, not permission to invent or change breakpoints.

## Explicitly not present

No Cart, Checkout, account, wishlist, payment, shipping calculation, returns workflow, order creation, inventory reservation, live search/filter/sort, functional variants, purchase submission or enquiry backend.

## Scope control

This is a closed nine-page route and section inventory. No page, section, route, navigation destination or component may be added, removed or rearranged without explicit owner approval and a recorded inventory amendment.
