# Reference Research Log

Record every significant reference-site review.

**Authority note:** All entries below are observations of third-party reference sites, not DAG design requirements. D-014 and the active root page/component inventories define DAG's current scope. Reference observations about banners, search, cart, filtering, checkout, locale controls, badges, promotions or page sections do not authorize those elements for DAG.

For each entry: date accessed, source URL, page/journey reviewed, specific observation, learning for DAG, what must not be copied and design implication.

## Principal references

- **POJ Studio:** https://pojstudio.com/
- **Macaroni Shoten:** https://shop.macaro-ni.jp/

## Prior inspection notes retained from M1 research (6 November 2026)

### POJ Studio
- Inspected homepage, Shop All, Kintsugi collection and related journal paths on 6 November 2026.
- Observed country/currency and language controls, a tariff/duty notice, distinct Shop/Experiences/Kintsugi/Stories/About areas, category navigation, price/availability filters, sorting, variant labels and Sold out/Preorder states.
- DAG may study the separation of product taxonomy, editorial, maker context and service information. Do not copy POJ taxonomy, UI, text, imagery or page layouts.
- Sources: https://pojstudio.com/ ; https://pojstudio.com/collections/all ; https://pojstudio.com/collections/kintsugi-kit ; https://pojstudio.com/blogs/kintsugi

### Macaroni Shoten
- Inspected https://shop.macaro-ni.jp/ on 6 November 2026. The shop then presented four broad category names (Kitchen, Living, Food, Daily) and an empty-product state.
- Use only as a prompt to consider compact category doors and an everyday-use lens. It was not possible to evaluate active product cards or checkout during that inspection. Do not copy its Japanese-language customer content or identity; DAG remains English-only.

These observations do not prescribe or imply a winner among the current visual territories.


## Updated reference review — 6 November 2026

### POJ Studio — live homepage and retail journeys

Reviewed:
- https://pojstudio.com/
- https://pojstudio.com/collections/tableware-1
- https://pojstudio.com/collections/bestsellers
- https://pojstudio.com/pages/about

Current observations:
- Homepage combines a promotional/duty notice area, broad primary navigation, a seasonal campaign hero, concise brand statement, category/collection entry points, mission content, press, artisan stories, bestseller products and service/company footer links.
- Navigation separates Shop, Experiences, Kintsugi, Stories, Visit and About. Shop has grouped collection/category links; country/currency and English/Japanese language controls are available.
- Tableware content groups products by categories/materials such as ceramics, wood, glass and washi, with short introductions, prices, variant and availability/bestseller/preorder labels.
- Bestsellers exposes product count, sorting, availability and price filters, visible prices and status labels.
- About content connects products with artisan, team and sustainability narratives.
- A commerce-partner case study describes the site as Shopify-based and mentions product metafields/metaobjects, product-page tabs and collection banners. This is third-party implementation context only; it does not authorize DAG to use Shopify or copy the implementation.

DAG learning:
- Keep catalogue discovery and editorial storytelling as distinct but connected routes.
- Use concise collection context, visible product facts and filters only when supported by the catalogue.
- Give makers and craft context room to explain an object's value.
- Treat country, currency, tariffs, shipping and language controls as business decisions; do not copy POJ's settings or publish unapproved delivery/tax claims.

Do not copy POJ's logo, wording, images, exact menu structure, product names, page composition or visual identity.

### Macaroni Shoten — live storefront and category

Reviewed:
- https://shop.macaro-ni.jp/
- https://shop.macaro-ni.jp/categories/3902202
- Historical launch context: https://prtimes.jp/main/html/rd/p/000000069.000005511.html

Current observations:
- The live store has a compact header/search and short Japanese introductory text.
- Visible category taxonomy is Kitchen, Living, Food and Daily, with category-specific sublinks.
- About, contact, privacy and commercial-disclosure paths are present.
- On the access date, the live homepage and Kitchen category both returned an empty-product state. Active product merchandising and checkout could not be assessed.
- The 1 October 2021 launch announcement described a curated selection of Japanese handmade goods and selected food products. This is historical context only, not proof of today's active catalogue.

DAG learning:
- Category discovery can be compact and understandable.
- Base category labels must reflect DAG's actual range and customer use; do not copy Macaroni's labels or Japanese customer content.
- Revisit the live site before any later detailed merchandising comparison because the empty state limits what can be assessed.

## Owner direction and design boundary

The owner rejected the four previous territories and designated POJ Studio and Macaroni Shoten as principal references on 6 November 2026. See D-008 and D-009 in DECISIONS.md and docs/17-REFERENCE-LED-DESIGN-BRIEF.md.

Study their customer-experience principles and retail quality, but produce an original DAG design. Do not copy exact brand identity, layout, writing, imagery, product content or proprietary assets. These observations do not approve a palette, typeface or final visual direction.


## Live reference inspection — 7 November 2026 (D-010 hierarchy)

### POJ Studio — primary ecommerce reference

**Browser inspection viewport:** desktop 1440 × 900. Tablet 768 × 1024 and mobile 390 × 844 screenshots could not be captured in this browser session. No screenshots are committed. The following notes distinguish directly observed desktop structure from unknown responsive behaviour.

Reviewed pages:
- Homepage: https://pojstudio.com/
- Shop All: https://pojstudio.com/collections/all
- Tableware collection: https://pojstudio.com/collections/tableware-1
- Decor collection: https://pojstudio.com/collections/decor
- Variant product: https://pojstudio.com/products/kohiki-rim-elliptical-bowl
- Variant product: https://us.pojstudio.com/products/boro-sashiko-tapestry
- Product detail: https://pojstudio.com/products/cast-iron-furin
- About: https://pojstudio.com/pages/about
- Stories: https://pojstudio.com/pages/stories
- Artisan index: https://pojstudio.com/blogs/artisan

Directly observed in the desktop browser session and text-accessible page content:

**Scope boundary:** The following bullets describe the reference sites only. They are research observations, not DAG requirements or approval to add announcements, country/language controls, search, cart, filtering, reviews, sticky UI or any other reference feature. D-014 and the active DAG inventories define the only current structural scope.
- A rotating announcement region, with distinct promotional and tariff/duty messages on the live reference.
- Main navigation includes Shop and grouped shopping destinations, plus Experiences, Kintsugi, Stories, Visit, About and Interiors. Search, cart, account and locale controls are present.
- Homepage uses a full-width campaign image/hero with a short headline and Shop Now action. Its broader structure includes category/collection pathways, mission, press, stories and featured merchandise.
- Shop All provides category navigation, sorting and availability/price filter content. The desktop product grid showed four cards per row in the browser inspection. Product count is volatile: one inspection returned 295 and a separate indexed page capture returned 296; do not use either as a fixed target.
- Product cards communicate real item states such as sold out, bestseller and available size/colour variants. DAG may use equivalent state patterns only when its underlying data supports them.
- Product pages expose multi-image galleries, product narrative, option controls where present, quantity and purchase action, with supporting maker, dimensions, care or shipping content depending on the product.
- About connects the brand mission and team. Stories/Artisan pages group articles by editorial subject and use category, title and excerpt patterns.

Unknown or not conclusively verified:
- Sticky-header scroll behaviour and exact hover/focus transitions.
- Exact computed CSS measurements, font declarations, content max-widths and breakpoints.
- Exact mobile drawer, filter, grid and gallery interaction at 390px/768px.
- Full carousel/thumbnail interaction on every product page.
- Whether every card swatch pattern is interactive under every product option.

DAG translation:
- POJ supplies the leading ecommerce structure, product discovery and product-detail information hierarchy.
- DAG must use its own categories, verified products, original images, English content and approved commercial facts.
- POJ's Kintsugi, workshops, visit/interiors, Japanese language, country selectors, discounts, shipping thresholds and tariff messages are not DAG features by default.

### Macaroni Shoten — secondary curation reference

Reviewed:
- Home: https://shop.macaro-ni.jp/
- About: https://shop.macaro-ni.jp/about

Browser inspection viewport: desktop approximately 1440 × 900. Tablet and mobile layouts were not directly verified; no resized screenshots are available from this session.

Directly observed:
- The active store displayed an empty-product state across the inspected categories. No live product grid, product cards, PDP variants or checkout could be assessed.
- Header/search/cart access and a slide-in navigation pattern were present.
- Navigation groups Home, About, Category, Contact and external links.
- Broad category names are Kitchen, Living, Food and Daily. Visible subcategory groupings include kitchen supplies, interior goods, housekeeping, food/drinks and daily goods.
- About describes the store as an editorially curated select shop with high-quality handmade items and carefully selected food/lifestyle items.
- Footer/content paths include privacy and Japanese commercial-disclosure information, plus external/social links.

DAG translation:
- Use the select-shop thinking: fewer, more meaningful groups; a clear reason for selection; concise, useful editorial framing.
- Do not copy category labels, Japanese text, BASE platform elements, addresses, social links or legal pages.
- The live empty state limits evidence. Macaroni does not provide a current reference for populated product grids, filters, PDP or checkout.

### Measurement and screenshot limitations

This pass did not produce saved viewport screenshots or computed-style measurements. Desktop observations are documented at the tested viewport; 768px and 390px are reserved as explicit DAG prototype validation viewports. Do not describe inferred mobile behaviour as reference-observed. Future visual review should capture actual DAG screenshots at all three widths and record measured rather than guessed values.

### Reference hierarchy interpretation (D-010)

POJ Studio leads global commerce structure and the shopping journey. Macaroni Shoten informs the curated selection model. Neither reference supplies DAG's brand identity or product content. The hierarchy does not approve a DAG palette, typography, art direction or production theme.
