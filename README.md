# Desert Art Gallery — Owner-Controlled Design Kit v2

**Current structural source:** `design/owner-controlled-kit-v2/`  
**Status:** Adopted as the single active structural HTML/CSS implementation source (D-014). This does not approve final brand identity or authorize production application development.

## Authority hierarchy

1. `docs/DECISIONS.md` — explicit owner decisions.
2. Root `AGENTS.md` — permanent agent rules.
3. `docs/DESIGN-AUTHORITY.md` — owner control and closed design scope.
4. `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md` — repository-wide hierarchy/reconciliation policy.
5. Owner-approved design specifications and `docs/PAGE-INVENTORY.md` / `docs/COMPONENT-INVENTORY.md`.
6. Technical guidance that does not conflict.
7. Historical files — audit context only, never active instructions.

## Preview and implementation source

Open `design/owner-controlled-kit-v2/index.html` and the pages under `design/owner-controlled-kit-v2/pages/`. Preserve all original HTML, CSS, responsive rules, script, page/section order, supplied components and disabled states. The files are a non-production structural kit, not a live store or a production app.

## Exact page inventory

1. Homepage — `index.html`
2. Shop / all products — `pages/shop.html`
3. Category / collection — `pages/collection.html`
4. Product detail — `pages/product.html`
5. About DAG — `pages/about.html`
6. Makers — `pages/makers.html`
7. Journal index — `pages/journal.html`
8. Journal article — `pages/article.html`
9. Contact / support — `pages/contact.html`

See `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md` for exact sections and components.

## Brand identity remains owner-controlled

Final colours, typography, type scale/hierarchy, logo/wordmark/descriptor and photography direction remain pending. `styles/tokens-layout-only.css` is system-colour/system-font QA fallback only, not a DAG palette or production theme. Do not infer or populate missing brand tokens.

## Language, content and commerce

Customer-facing content is English-only; Japan-first does not imply Japanese-language UI or settle seller jurisdiction, sales territories, currency, tax/duties, shipping, payments, returns or service commitments.

Never fabricate product, maker, material, dimension, provenance, price, stock, review, contact, policy or delivery information. Existing placeholders stay visibly pending; disabled controls stay disabled. Cart, checkout, account, wishlist, live search/filter/sort, payment, orders, shipping calculation and returns are out of scope.

Do not add pages, sections, navigation, banners, testimonials, badges, widgets, icons, animations, popups, sticky/floating features, chat, newsletter or other UI/functions without explicit owner approval and inventory amendment.

## References and IP

POJ Studio is primary for ecommerce/page structure; Macaroni Shoten is secondary for curation/select-retail character (D-010). Do not clone proprietary HTML/CSS/JS, branded layouts, logos, text, photography, fonts or assets. The v2 DAG kit is the structural implementation source.

## Documentation governance

- `docs/DOCUMENTATION-RECONCILIATION-MATRIX.md` — path-level dispositions.
- `docs/DOCUMENTATION-RECONCILIATION-REPORT.md` — audit findings and evidence.
- `docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md` — completion status and exceptions.
- `docs/DOCUMENTATION-CHANGELOG.md` — dated changes.
- `docs/OWNER-TOKEN-INPUT.md` — pending owner values.

Whenever a decision or source changes, reconcile all relevant tracked documents, prompts, code comments, HTML/CSS/JS, workflows and issue templates. Do not merely add a new document alongside old active instructions.
