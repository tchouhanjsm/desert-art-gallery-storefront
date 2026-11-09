# Design Authority and Change Control

## Authority and governing rule

This document is level 3 in the root authority hierarchy defined in `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`. It is subordinate only to explicit owner decisions and root `AGENTS.md`; it governs lower-level specifications and implementation documentation.

## Governing rule

**DAG Owner-Controlled Design Kit v2 is the sole active structural HTML/CSS implementation source.** Its original HTML pages, CSS files, responsive styles, structural components, page order and component inventory must be preserved as supplied. Do not redesign, silently restyle, expand or reinterpret the kit.

The kit is structurally adopted (D-014) and materialized in `design/owner-controlled-kit-v2/`. The archive SHA-256 is `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`; the 14 original implementation assets were checked at adoption and PR #9's two CSS maintenance amendments are hash-pinned by the project validator. This does **not** approve final brand identity. Under D-017, the owner approved the exact Revision 2 palette, Source Serif 4 / Inter typography, hierarchy, spacing, page compositions and placeholder/frame ratios for the D-016 local/private non-transactional prototype only. The proposal's SHA-256 is recorded in docs/DECISIONS.md and the prototype manifest. Final logo/wordmark artwork, descriptor, genuine photo art direction/crops and all production theme/application styling remain owner-controlled and pending.

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

This document is level 3 in the exact eight-level hierarchy. Every root/nested prompt, README, source comment, workflow, issue template, HTML/CSS/JS file and technical guide must comply. A lower-level artifact may explain implementation detail but may not create brand, route, component or feature authority. Historical proposals must carry the prefix **HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT** and must never be used as defaults or instructions.

The owner archive was re-supplied for the repository-wide reset and independently verified: it contains 25 files and its SHA-256 matches D-014 adoption. Do not duplicate or redesign the kit to satisfy a documentation task.

## Permitted maintenance

Fix genuine defects, semantic/accessibility issues, responsive mechanics, security, maintainability and documentation consistency only where the v2 inventory, content, visual contract and behaviour are preserved. Maintenance is not permission for visible additions or redesign.

Any scope change beyond the D-016 six-area private prototype needs a written problem statement, exact affected page/component, customer and visual/functional impact, data requirements, risks, alternatives, acceptance criteria and explicit owner approval recorded in docs/DECISIONS.md. Do not add unlisted sections, widgets, promotion or interactions within the prototype.

D-016 separately authorizes local/private, non-transactional prototypes for exactly six review areas after M2-A visual approval. Such files must remain outside this public repository and map to the unchanged nine-page D-014 inventory. This narrow private-prototype authorization is not production application development or permission to deploy publicly.
