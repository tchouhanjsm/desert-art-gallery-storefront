# Design Authority and Change Control

## Governing rule

**DAG Owner-Controlled Design Kit v2 is the sole active structural HTML/CSS implementation source.** Its original HTML pages, CSS files, responsive styles, structural components, page order and component inventory must be preserved as supplied. Do not redesign, silently restyle, expand or reinterpret the kit.

The kit is structurally adopted (D-014). This does **not** approve final brand identity. Final brand colours, typography, logo/wordmark/descriptor and photography art direction remain owner-controlled and pending.

## Owner-controlled identity

The owner alone approves exact brand colours, typefaces/weights/hierarchy/type scale, logo/wordmark/descriptor, photography direction/crop and customer-facing copy or factual claims. Do not select or infer missing values.

`styles/tokens-layout-only.css` uses system canvas colours and system fonts only for layout QA. It is not a DAG palette, neutral brand identity or production theme.

## Closed implementation scope

Use only the nine routes and exact structures in `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`. Do not add, remove, rearrange or reinterpret pages, sections, header/footer items, navigation destinations, components, controls or functionality without an explicit owner decision and inventory amendment.

The kit's own kit-only notice, utility location row, wordmark/header, navigation, action area and footer are supplied structural content. They are not permission to add other banners or shell elements.

Do not add unlisted pages/sections, promotions, testimonials, reviews, badges, widgets, icons, animation, chat, newsletter/social modules, popups, floating/sticky features, search/filter/sort/variant/purchase/cart/checkout/account/wishlist or commerce behaviour.

Existing disabled/visual-only controls remain disabled. Do not invent or implement behaviour from their appearance.

## Content and language integrity

- Customer-facing content is English-only. Japan-first does not authorize Japanese or bilingual storefront UI.
- Never fabricate products, names, attributes, prices, discounts, reviews, stock, availability, makers, materials, dimensions, condition, provenance, care, awards, certifications, sustainability claims, contact details, policies or delivery promises.
- Preserve supplied placeholder wording and disabled states until verified content/behaviour and owner approval exist.
- Use only owner-approved DAG assets. Do not represent unrelated stock, generated or remote Etsy imagery as genuine DAG photography.

## Reference and IP

D-010: POJ Studio is the primary ecommerce/page-structure reference; Macaroni Shoten is secondary for curation/select-retail character. Learn non-proprietary principles only. Do not copy protected source code, CSS, layouts, text, imagery, logos, fonts or branded artwork.

## Documentation governance

The repository-wide source hierarchy is in `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`. Every prompt, README, source comment, workflow and issue template must comply. Historical proposals must be labelled **HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT** and must never be used as defaults or instructions.

## Permitted maintenance

Fix genuine defects, semantic/accessibility issues, responsive mechanics, security, maintainability and documentation consistency only where the v2 inventory, content, visual contract and behaviour are preserved. Maintenance is not permission for visible additions or redesign.

Any required scope change needs a written problem statement, exact affected page/component, customer and visual/functional impact, data requirements, risks, alternatives, acceptance criteria and explicit owner approval recorded in `docs/DECISIONS.md`.

No production application development is authorized by structural kit adoption.
