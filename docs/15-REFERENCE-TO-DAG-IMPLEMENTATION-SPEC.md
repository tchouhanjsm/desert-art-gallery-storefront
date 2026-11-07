# 15 — Reference-to-DAG Implementation Specification

**Status:** Owner-approved reference hierarchy; implementation specification ready for responsive prototyping after the remaining visual-identity gate is satisfied.  
**Reference fidelity:** BLEND.  
**Primary reference:** POJ Studio — ecommerce structure and page experience.  
**Secondary reference:** Macaroni Shoten — select-shop curation and editorial retail character.  
**Owner decision:** D-010, confirmed 7 November 2026.  
**Customer-facing language:** English only.  
**Brand/content identity:** Desert Art Gallery, rooted in Jaisalmer, Rajasthan.  
**Full photo-library migration:** Deferred.

> This document approves the reference hierarchy and defines the experience to study and prototype. It does not approve DAG's final colours, fonts, image art direction, logo, page styling, commerce model, product taxonomy, technology stack or legal/commercial policies.

## 1. The selected reference relationship

The owner selected a blend of the two references, with POJ Studio as the primary reference. This hierarchy is confirmed and must not be reopened unless the owner changes it.

### POJ Studio — primary ecommerce and visual-structure reference

https://pojstudio.com/

Use POJ as the principal reference for:
- Overall storefront architecture and page hierarchy.
- Global shell, announcement area, header, navigation and grouped shop menus.
- Homepage campaign/hero, category discovery, editorial storytelling and featured merchandise.
- Shop-all and collection navigation, filters, sorting and product-grid behaviour.
- Product-card information hierarchy, product-state labels and variant cues.
- Product-detail image galleries, narrative, options, quantity and purchase-action placement.
- Maker/artisan information, product details and care content.
- Stories, About, supporting information and footer structure.
- Interaction patterns across desktop and mobile, where directly observable.

The 7 November 2026 inspection observed a campaign-led homepage, grouped Shop navigation, separate editorial and supporting destinations, collection shortcuts, mission/press/story modules and featured merchandise. The Shop All page exposes category navigation, availability and price filter controls in its text-accessible page content, a sort selector and visible product/status information. Product pages demonstrate a narrative, gallery, option controls where applicable, quantity and purchase action, plus supporting maker, detail, care or shipping information.

The hierarchy and patterns are the reference. POJ's Japanese subject matter and business-specific features are not DAG requirements.

### Macaroni Shoten — secondary curation and select-retail reference

https://shop.macaro-ni.jp/

Use Macaroni Shoten to understand:
- The character of a carefully edited select shop.
- A compact and understandable category system.
- Grouping products by meaningful areas of daily life.
- Concise editorial expression of selection, usefulness and quality.
- The way a store's editorial identity can support product curation.

Its About page describes an editorially curated selection of high-quality handmade goods and carefully selected food/lifestyle products. The visible category groups are Kitchen, Living, Food and Daily, with subcategories under Kitchen, Living and Food.

**Current-state limitation:** On 7 November 2026, the live storefront showed an empty-product state across the inspected categories. Do not claim to have evaluated a populated product grid, product-card states, variants or checkout there. Macaroni is the secondary curation reference, not evidence for a live ecommerce product-page system.

### What “blend” means for DAG

This is not a 50/50 copy exercise and is not permission to clone either website.

- **POJ Studio leads** overall ecommerce architecture, page hierarchy, navigation, homepage structure, shop/collection, product card, product detail, maker/story and supporting retail experience.
- **Macaroni Shoten informs** select-shop philosophy, category grouping, lifestyle-oriented curation and concise editorial retail character.
- **DAG owns** its brand identity, Jaisalmer connection, actual products, photography, content, taxonomy, language and final visual decisions.

A DAG page may use a POJ-like interaction pattern or information hierarchy while using an entirely DAG-specific composition, product set, image treatment, typography and colours selected by the owner.

Do not use POJ's Kintsugi, Japanese artisan, Japanese-language, country selector, workshop, visit, interiors, free-shipping thresholds or other business-specific features as DAG features unless DAG actually offers an equivalent. Do not copy Macaroni's Japanese labels, product assortment or category names. Translate only the underlying retail logic into verified DAG categories.

## 2. Research record and evidence boundary

Live inspection date: **7 November 2026**.

### 2.1 POJ Studio pages inspected

| Page | URL | Evidence captured |
|---|---|---|
| Homepage | https://pojstudio.com/ | Announcement area, main navigation, campaign hero, category/collection pathways, mission, press, stories, featured products and footer links. |
| Shop All | https://pojstudio.com/collections/all | Category shortcuts, sort control, availability and price filter text, product count snapshot, product states and product-card information. |
| Tableware collection | https://pojstudio.com/collections/tableware-1 | Collection introduction, contextual grouping and product merchandising. |
| Decor collection | https://pojstudio.com/collections/decor | Editorial grouping of product families and collection shortcuts. |
| Variant product | https://pojstudio.com/products/kohiki-rim-elliptical-bowl | Size/colour options, variable price, quantity and add-to-cart placement, supporting information sections. |
| Variant product | https://us.pojstudio.com/products/boro-sashiko-tapestry | Multi-image gallery, size options and clear source-market difference. |
| Product detail | https://pojstudio.com/products/cast-iron-furin | Multi-image gallery, product narrative, add-to-cart, maker information, dimensions and care. |
| About | https://pojstudio.com/pages/about | Mission, team and artisan/press narrative. |
| Stories index | https://pojstudio.com/pages/stories | Editorial categories and article-card pattern. |
| Artisan index | https://pojstudio.com/blogs/artisan | Maker/story index and editorial grouping. |

### 2.2 POJ observations

**Homepage and global shell**
- The inspected desktop page shows a rotating announcement area with a promotional message and a separate tariff/duty information message. Those are POJ's own commercial statements and must not be copied.
- The primary header exposes Shop, Experiences, Kintsugi, Stories, Visit, About and Interiors. Shop expands into grouped category, bestseller and Kintsugi destinations.
- Search, cart, account, language and country/currency controls are present in the wider site shell.
- The initial hero is a large image-led campaign with a headline and shopping action. Below it, the homepage connects collection discovery, mission, press, stories and featured merchandise.
- The full lower footer includes company, shop, customer-support, legal and newsletter destinations.

**Shop and collection**
- Shop All exposes a category hierarchy, sort selection and availability/price filter content. A category/collection page shares the general product-grid structure.
- The inspected desktop grid presented four product cards per row. Card information includes image, product name, price, and, when relevant, status labels or variant cues.
- Examples of observed card states include sold out, bestseller, size-variant and colour choices. These are not DAG labels until their underlying business facts and definitions exist.
- The text-accessible product count differed between page captures (295 in the browser inspection and 296 in a later indexed page result). The number is time- and capture-dependent and is not a design requirement.

**Product detail**
- The variant examples expose choice controls, a quantity stepper and a clearly positioned purchase action.
- The inspected product content includes a descriptive narrative and supporting sections such as Description, Made By, Shipping, Dimensions and Care, depending on the product.
- A multi-image gallery is present. Thumbnail/carousel interaction was not fully established for every product; do not invent a specific gesture model from a static page read.
- Product-level price and delivery messages can vary by market/locale. A US storefront product URL displayed a US-market price while the Japanese storefront displays yen. DAG's display currency and market rules remain unresolved.

**About and stories**
- POJ connects mission, people, maker context, products and stories. Its editorial categories include Artisan, Inspiration and Kintsugi.
- The design learning is the relationship between product information and supporting editorial, not POJ's Japanese craft subject matter, artisan biographies or claims.

### 2.3 Macaroni Shoten pages inspected

| Page | URL | Evidence captured |
|---|---|---|
| Homepage | https://shop.macaro-ni.jp/ | Compact shop shell, hero/editorial message, search/menu/cart access, empty-product state and category tree. |
| About | https://shop.macaro-ni.jp/about | Select-shop description and hero/editorial presentation. |
| Category tree | available through home navigation | Kitchen, Living, Food and Daily, with visible subcategory links. |

The live shop showed no listed products. Its visible navigation uses a slide-in menu, with Home, About, Category, Contact and Link destinations; search is available within the navigation experience. The About content describes the store as an editorially curated select shop. It is useful evidence for the curation model and concise retail presentation only.

### 2.4 Viewport and measurement limitations

- POJ's browser inspection was completed at desktop 1440 × 900.
- Macaroni's browser inspection was completed at desktop approximately 1440 × 900.
- The browser session could not reliably resize and capture screenshots at 768 × 1024 or 390 × 844. Tablet/mobile page behaviour is therefore **not directly verified** in this research pass.
- The text-accessible pages provide structural evidence, but no verified computed CSS, font-family declarations, content-container widths, exact spacing tokens or breakpoint values were extracted.
- No reference-site screenshot files are stored in the repository. Do not claim screenshot evidence or measured pixel values that were not captured.
- Before a rendered DAG prototype is accepted, inspect its actual implementation at 1440, 768 and 390 CSS-pixel viewport widths and record real observations. The values are test viewports, not mandated CSS breakpoints.

### 2.5 Evidence discipline

For future reference reviews, record:
- Exact page URL and date accessed.
- Actual viewport size.
- Screenshot evidence only where captured.
- Directly observed layout/behaviour.
- Approximate visual estimate, explicitly labelled.
- Unknown or inaccessible behaviour.
- DAG adaptation.
- Reference-specific content or business features that must not be copied.

## 3. Global site shell

### 3.1 Announcement / utility bar

**Reference pattern:** POJ uses a narrow announcement region for changing notices and information.

**DAG specification**
- Render a slim announcement strip only when there is an approved, current message.
- No fabricated discount, free shipping, delivery, tax, tariff, promotion or urgency message.
- Hide the entire strip when there is no approved message; no empty permanent band.
- If dismissible, provide a labelled close control and preserve dismissal for the appropriate session/persistence period selected during implementation.
- If multiple notices exist, use accessible controls and avoid automatically changing text faster than a customer can read it.
- Do not allow an announcement to obscure the primary navigation or keyboard focus.

**Acceptance:** No unapproved message is visible; an absent message produces no empty strip; a visible message is readable and dismissible when designed to be.

### 3.2 Header and primary navigation

**Reference pattern:** POJ uses a prominent Shop hierarchy, with separate high-level destinations, plus search and cart. Macaroni demonstrates a compact shell with a slide-in navigation system.

**DAG specification**
- Logo/wordmark links to home.
- Shop is the principal route to product discovery.
- Search and cart are available from the global shell.
- Account and wishlist appear only if implemented, justified and supported by a real customer function.
- Desktop Shop navigation may use grouped columns or a mega-menu. Its entries must come from approved DAG categories and collections.
- Other top-level destinations may include About, Stories/Journal and Contact when those pages have real content.
- Never add an empty category or invented collection merely to fill the menu.
- Header scroll behaviour (static, sticky, overlay or compacting) is an exploration/prototype decision. Compare usability and visual hierarchy rather than assuming POJ's exact behaviour.
- Keep all customer-facing labels in English.

**Interaction and accessibility**
- Native links for navigation; disclosure buttons for submenus.
- Keyboard users can open/close menus and move through links in a predictable tab order.
- Escape closes an open menu and returns focus to its trigger.
- Outside click closes overlays where appropriate.
- Focus remains visible; menu state is exposed to assistive technology.
- Do not rely on hover alone to reveal essential destinations.

### 3.3 Desktop mega-menu

- Group links by approved product category, curated collection and, only where relevant, editorial discovery.
- A featured image or editorial tile may be shown only when a real, approved asset and destination exist.
- Keep labels concise and scannable.
- No POJ-specific columns (Kintsugi, Experiences, Visit, Interiors) are copied by default.
- No final column count, dimensions, colours or type styling is selected here.

**Acceptance:** The menu makes the approved DAG catalogue easy to enter, does not expose empty categories, and works by mouse, keyboard and touch.

### 3.4 Mobile navigation

- Use an accessible menu button and a drawer or disclosure pattern.
- Preserve the main hierarchy: Shop, approved category/collection groups, Stories/About and support.
- Search and cart remain discoverable.
- Avoid deeply nested menus; use progressive disclosure for a small number of levels.
- Lock background scrolling only when the drawer is modal; restore scroll and focus on close.
- Support Escape, outside click where appropriate, screen-reader labels and visible focus.

**Acceptance:** A customer can open, navigate and close the menu using touch and keyboard without losing context.

### 3.5 Footer

- Group destinations into Shop, About/Stories, Help/Customer Care and Policies.
- Include only verified contact/business details.
- Newsletter signup requires a real consent-managed submission workflow and privacy information; otherwise omit it.
- Shipping, returns, terms, privacy and seller disclosures are shown only when approved content exists.
- Do not include Macaroni's BASE links/social handles or POJ-specific contact/press links.
- Avoid repeating the entire main navigation or adding empty footer columns.

## 4. Page-by-page implementation specification

Each page contract below defines the purpose, reference influence, structure, behaviour, dependencies and acceptance criteria. The final visual treatment must use the owner's later-approved DAG direction.

### Page 1 — Homepage

**Customer purpose:** Understand what DAG offers, establish confidence in the gallery's point of view and enter a meaningful catalogue pathway.

**Reference:** POJ homepage structure and discovery routes; Macaroni's edited/select-shop philosophy.

**Desktop structure**
1. Optional approved announcement.
2. Global header.
3. Editorial hero/current collection.
4. Primary category and collection pathways.
5. Featured products or curated edit.
6. DAG curation/brand statement.
7. Verified maker, material or craft story.
8. Journal/editorial discovery.
9. Additional product/collection discovery only if supported.
10. Verified customer-support/reassurance information.
11. Footer.

**Tablet/mobile structure**
- Preserve the hierarchy but reflow sections to the viewport.
- Hero copy and primary action remain early in the page.
- Category entry points remain visible and tappable.
- Featured products use a readable grid or intentional horizontal rail; avoid clipped cards.
- Editorial modules stack in a clear order.
- No fixed desktop split proportion is mandated.

**Components and interactions**
- Hero module with one primary shopping CTA and optional secondary discovery action.
- Category/collection cards and text links.
- Product cards using the shared product-card contract.
- Story/maker teaser cards.
- Optional campaign/announcement state only when content is approved.

**Data dependencies**
- Approved DAG wordmark and visual direction.
- Real category/collection taxonomy.
- Verified product records and images, or unmistakably labelled prototype placeholders.
- Approved story and maker content.
- Approved promotional copy, if any.

**Accessibility**
- One page-level H1.
- Descriptive link labels and meaningful image alt text.
- No text embedded only in images.
- Keyboard-operable carousels if used; reduced-motion support.

**Acceptance**
A first-time visitor can identify what DAG sells, locate a meaningful shopping route and understand the next action from the opening view. Placeholder content is visibly identified as illustrative.

### Page 2 — Shop / All Products

**Customer purpose:** Browse the full published catalogue and narrow the result set.

**Reference:** POJ Shop All; Macaroni's compact select-shop grouping.

**Desktop structure**
- Page title and concise factual introduction.
- Category/collection shortcuts.
- Truthful result count when sourced from published results.
- Filter region and sort/view controls.
- Responsive product grid.
- Pagination or load-more when required.
- Clear loading, empty and no-results states.

**Tablet/mobile structure**
- Filter controls become a clear drawer or disclosure panel where a persistent sidebar would constrain the grid.
- Sort remains easy to reach.
- Product columns are determined by card readability and image proportions at each viewport; do not hard-code the reference's four-column layout to all devices.
- Selected filters remain visible and removable.

**Filters and sorting**
- Only expose filters backed by consistent catalogue fields and enough values to be useful.
- Candidate facets include category, material, size, colour, price and availability only after the data exists and is approved.
- Never infer stock, price or material facets from free-form tags without a verified mapping.
- Sorting options must correspond to actual indexed data. Do not display popularity/bestseller sorting without sales or editorial evidence.
- Filter changes update results and result count. Provide reset/clear-all behaviour.

**Components**
- Breadcrumbs, result heading, filter drawer/sidebar, sort selector, active-filter chips, product grid, pagination/load-more, empty state.

**Dependencies**
- Approved category taxonomy.
- Published product records with reliable price, availability and relevant facets.
- Search/index strategy selected during technical architecture.

**Accessibility**
- Form controls have labels and announced state.
- Results update is announced without moving focus unexpectedly.
- Filter drawer traps/restores focus only when modal.

**Acceptance**
Customers can browse and refine a real dataset; result counts and sort/filter states are truthful; mobile browsing remains legible.

### Page 3 — Category landing page

**Customer purpose:** Introduce a validated top-level product group and guide customers into relevant subcategories or collections.

**Reference:** POJ category/shop structure; Macaroni's clear broad category doors.

**Structure**
- Breadcrumb.
- Category name and concise factual introduction.
- Optional lead image.
- Relevant subcategory or collection links.
- Optional product highlights.
- Entry to the category product results.

**Responsive behaviour**
- Desktop can use grouped link modules and a lead image.
- Tablet/mobile stack category doors and maintain clear tap targets.
- Avoid duplicating the entire Shop All filter system above the fold.

**Dependencies**
- Owner-approved taxonomy derived from actual DAG products.
- Verified category descriptions and permitted images.

**Acceptance**
A customer understands what is included and can enter a relevant collection without encountering empty or misleading groupings.

### Page 4 — Collection page

**Customer purpose:** Browse a deliberately curated group with a clear reason for its selection.

**Reference:** POJ collection context and merchandising; Macaroni editorial selection philosophy.

**Structure**
- Breadcrumbs.
- Collection title and concise editorial introduction.
- Optional collection image/banner.
- Relevant product count, filters and sorting when supported.
- Product grid.
- Related story or collection only when genuinely connected.

**DAG adaptation**
- Keep category (what type of product it is) distinct from collection (why these products are grouped).
- Collection logic may be material, use, form, colour, maker, theme or editorial selection, but only if the product relationship is documented and approved.
- Do not copy POJ's Fall Series, Kintsugi, Bestseller or other collection labels as DAG collections.

**Acceptance**
The customer can understand the collection's editorial idea and browse genuine related products.

### Page 5 — Product detail page

**Customer purpose:** Evaluate a specific item, understand its verified attributes and choose the valid next action.

**Reference:** POJ product detail pages, including gallery, variant selection, maker, details/care and shipping sections.

**Desktop structure**
- Breadcrumb.
- Product gallery and product information in a balanced two-region layout.
- Product name, price or approved enquiry state.
- Factual short summary.
- Options/variants when they genuinely exist.
- Quantity where appropriate.
- Availability.
- Primary action according to the approved commerce model.
- Supporting product facts, maker/story and care sections.
- Related items only where an actual relationship exists.

**Tablet/mobile structure**
- Product name/price/action remain close to the image gallery in reading order.
- Gallery supports swipe/previous/next where implemented, visible controls and accessible labels.
- Variant and quantity controls remain usable without horizontal overflow.
- A sticky mobile purchase action is optional and must not obscure content or accessibility controls.

**Gallery**
- Primary and supporting views in a deliberate sequence.
- Zoom/lightbox only if the image resolution supports it.
- No fabricated details or scale cues.
- Alt text describes visible product/image content, not assumed material or provenance.
- Placeholder galleries must be clearly labelled as illustrative.

**Product information**
- Show only available, verified sections: description, material, dimensions, condition, included items, options, origin, maker, technique, care.
- Do not render empty accordions.
- Distinguish verified maker from supplier, curator or reseller.
- Source descriptions are not automatically approved public product copy.

**Trust and fulfilment**
- Show shipping, duties, returns and delivery details only after their legal/operational approval.
- Do not copy POJ's thresholds or duties wording.

**Acceptance**
A customer can inspect the imagery, understand verified product facts and available options, and see an honest next action and purchasing conditions.

### Page 6 — Search results

**Customer purpose:** Find a known item or discover products using relevant terms.

**Reference:** POJ's global search access and shop discovery.

**Requirements**
- Search is reachable from every page.
- Search overlay/page supports clear open, submit, close and clear actions.
- Predictive suggestions only when useful and based on real catalogue data.
- Results reuse the same product-card component as Shop/collection.
- Include empty, no-results, loading and error states.
- Recent/popular searches only when supported by actual data.
- Query is preserved when returning from a result where appropriate.

**Responsive/accessibility**
- Search remains keyboard accessible.
- Label and instructions are explicit; Escape closes an overlay and restores focus.
- Mobile search input is not obscured by the keyboard.

**Acceptance**
Search returns consistent real results and communicates no-results/error states honestly.

### Page 7 — Cart

**Customer purpose:** Review selected items and amend the cart before checkout.

**Reference:** POJ's persistent cart access and conventional product commerce clarity.

**Requirements**
- Each line item shows image, name, selected options, quantity and authoritative price/line total.
- Quantity update and remove controls.
- Subtotal and only verified additional-cost messaging.
- Clear empty-cart state with route back to shopping.
- Preserve cart state appropriately and handle changed/unavailable items honestly.
- No fabricated free-shipping progress bar, countdown, savings or urgency.

**Responsive/accessibility**
- Line items reflow without losing price or action visibility.
- Quantity updates are keyboard accessible and announced.
- Error messages identify the affected line item.

**Acceptance**
Cart totals reconcile with authoritative item pricing and every line can be changed or removed.

### Page 8 — Checkout

**Customer purpose:** Complete an order with an accurate total and clear seller/delivery/payment conditions.

**Reference:** Use POJ's clarity around product and shipping information, not its specific operational rules.

**Gate:** Do not implement a real checkout until seller jurisdiction, sales territory, currency, tax/duties, shipping, payments, returns and order operations have been approved.

**Required steps when authorized**
- Contact and delivery details.
- Destination-appropriate address fields.
- Shipping options and charges from approved configuration.
- Tax/duty handling from the approved legal/technical model.
- Supported payment methods only.
- Order review, final total and clear confirmation.
- Validation, retry, failure and duplicate-submission protection.
- Server-side price/availability revalidation and idempotency.

**Acceptance**
No customer can submit an order with a guessed total, unsupported payment method or unverified fulfilment promise.

### Page 9 — Maker / Artisan profile

**Customer purpose:** Understand a verified person or organization connected to a product.

**Reference:** POJ maker/artisan information and story structure.

**Requirements**
- Name and role only when confirmed and approved for publication.
- Portrait/process imagery only with rights and consent.
- Verified location and context.
- Verifiable materials and techniques.
- Related products connected through a documented relationship.
- Clearly distinguish maker, workshop, supplier, curator and gallery.
- Do not invent biography, quotations, lineage or awards.
- If no verified maker identity exists, use a material/product story instead of fabricating a profile.

**Acceptance**
Every claim and image has an approved source/permission; linked products have a genuine relationship.

### Page 10 — About DAG

**Customer purpose:** Understand what DAG is, what it selects and its verified connection to Jaisalmer/Rajasthan.

**Reference:** POJ About/mission structure; Macaroni's concise curation statement.

**Requirements**
- Clear statement of the gallery's offer.
- Verified Jaisalmer/Rajasthan connection.
- Curatorial point of view, once owner-approved.
- Team/founder details only if supplied and approved.
- Links to real products, makers and stories.
- Avoid generic luxury, heritage or sustainability claims without evidence.

**Acceptance**
The About page communicates DAG's identity accurately without borrowing the references' biography or story.

### Page 11 — Journal / Stories index

**Customer purpose:** Discover useful editorial content connected to products, materials, use or verified craft context.

**Reference:** POJ Stories/Artisan/Inspirational categories.

**Requirements**
- Feature story with image/title hierarchy.
- Consistent article cards with title, short excerpt and metadata only when verified.
- Editorial categories such as material notes, maker stories, care or object context only where content exists.
- Filters/search only when volume justifies them.
- Relevant product links only with a genuine relationship.

**Acceptance**
Editorial discovery is useful and supports shopping rather than replacing or obstructing it.

### Page 12 — Journal / Story article

**Customer purpose:** Read an accurate story or useful guide in a clear editorial format.

**Requirements**
- Title, introduction and author/date/category only when verified.
- Lead image and body image sequence with rights/credits.
- Readable text measure, headings and captions.
- Source notes or credits when applicable.
- Related product/maker links only when genuine.
- No fabricated quotations, sources, dates or historical claims.

**Acceptance**
Article content is accessible, scannable, properly credited and based on approved material.

### Page 13 — Contact / Customer support

**Customer purpose:** Reach a real support channel or ask a product-related question.

**Requirements**
- Contact method actually monitored by DAG.
- Form only if submission handling, storage, notification and privacy controls are implemented.
- Product enquiry can carry product reference/name and customer question.
- No invented response-time guarantee.
- Shipping, returns and FAQ links only to approved content.
- Do not invent addresses, email, phone, hours or contact staff.

**Accessibility**
- Explicit labels, error summary, field-level errors and success state.
- Do not clear entered text after a recoverable error.
- Consent wording only when required for actual data handling.

**Acceptance**
Submissions reach a monitored destination, data is handled according to an approved privacy approach, and no false contact commitment is shown.

### Page 14 — Curated collection / About the selection

**Customer purpose:** Understand the curatorial logic behind a specific group of objects and continue into the relevant products.

**Reference:** Macaroni Shoten's select-shop philosophy, supported by POJ editorial collection presentation.

**Requirements**
- Explain the editorial basis of the collection.
- Group items by a verified relationship such as material, use, form, craft or documented edit.
- Clearly distinguish collection from product category.
- Use concise editorial text and strong imagery.
- Link to actual products and categories.
- Do not invent a collection theme to make the page feel populated.

**Acceptance**
The customer can explain why the products belong together and can browse them directly.

### Page 15 — Account (conditional)

Do not build an account area merely because POJ exposes login.
- Determine whether accounts are needed and what customer jobs they solve.
- Consider guest checkout.
- If implemented, provide real order/profile functions and account recovery.
- Protect personal data and sessions.
- Do not expose account links that lead to unsupported functionality.

### Page 16 — Wishlist (conditional)

- Implement only after persistence and customer value are established.
- Define guest vs signed-in persistence.
- Provide add/remove and empty states.
- Keep product availability and price current when shown.
- Never imply a reservation or stock hold unless the commerce system implements it.

### Page 17 — Shipping, delivery and returns information (conditional)

- Publish only after destination coverage, actual fulfilment, fees, expected timelines and returns/refunds/cancellations are approved.
- Separate known facts from conditions and exceptions.
- Use plain English and clear customer-facing terminology.
- Do not use POJ's threshold, destination, country selector or tariff language as DAG commitments.

### Page 18 — Legal, privacy and seller information (conditional)

- Publish only after the seller identity/jurisdiction and applicable disclosure requirements have been confirmed and content reviewed.
- Explain actual data collection, retention and customer rights.
- Do not copy Macaroni's or POJ's legal pages.
- Never show a draft or placeholder policy as final.

## 5. Reusable component contracts

The following are semantic component responsibilities, not a chosen framework or final visual style.

| Component | Responsibility | Required states / behaviour |
|---|---|---|
| SiteAnnouncement | Optional approved notice | Hidden, visible, dismissed; no empty band. |
| SiteHeader | Wordmark, primary links and global actions | Default, open navigation, scrolled/compact only if selected, focus-visible. |
| ShopMegaMenu | Desktop grouped discovery | Closed/open, keyboard/touch, focus return. |
| MobileNavDrawer | Mobile navigation | Closed/open, nested disclosure, Escape/close, scroll/focus management. |
| SearchDialog | Global search entry | Closed/open, typing, suggestions if supported, loading, empty, error, close. |
| Breadcrumbs | Orient customer in hierarchy | Semantic list, current page identified. |
| CollectionCard | Enter a real collection/category | Default and focus; only approved image/text. |
| ProductCard | Product summary and PDP destination | Default, focus, sold-out/preorder only when real, variant cues only when useful. |
| ProductGrid | Responsive product layout | Loading, results, empty, error. |
| FilterPanel / FilterDrawer | Narrow results | Selected, applied, cleared, disabled, loading; keyboard accessible. |
| SortControl | Reorder results | Selected option, disabled/loading. |
| ProductGallery | Inspect product imagery | Selected image, next/previous, optional zoom, mobile touch, keyboard support. |
| VariantSelector | Choose actual sellable options | Unselected, selected, unavailable, validation error. |
| QuantityStepper | Adjust quantity when allowed | Minimum/maximum, disabled, validation state. |
| ProductDetails | Render verified facts and story sections | Only populated sections; accessible disclosure if collapsed. |
| MakerCard | Link to verified maker story | Only verified names, claims and permitted images. |
| StoryCard | Link to editorial article | Verified title/excerpt/metadata. |
| CartLineItem | Review/edit cart contents | Quantity update, remove, price changed, unavailable/error. |
| CheckoutStep | Gather/order review data | Idle, validation error, submitting, retry, complete. |
| ContactForm | Customer enquiry | Idle, invalid, submitting, success, error. |
| SiteFooter | Support/company/policy navigation | Approved links only; optional consent-managed subscription. |

## 6. CSS and frontend architecture specification

This section defines structure and responsibilities only. It does **not** select the production framework, CSS methodology, values or visual tokens.

### 6.1 Architecture boundaries
- Use semantic HTML and progressive enhancement.
- Keep global shell, page compositions and reusable commerce/editorial components separate.
- Use page-specific styles only when a pattern is genuinely page-specific.
- Do not copy POJ source code, CSS, class names, assets or markup.
- Do not reuse the previous DAG repository frontend or theme.
- Do not select a framework, build tool, CMS, database or hosting provider in this specification.
- Production implementation starts after the relevant design and technical-architecture decisions.

### 6.2 Token contract after visual approval

Define semantic tokens only after the owner selects the visual direction:
- Colour roles: page background, elevated surface, primary text, secondary text, border, interactive accent, status colours.
- Typography roles: display, heading, body, UI, caption/metadata.
- Type sizes and line heights: responsive and content-led.
- Spacing scale: consistent steps with documented usage.
- Layout: content maximums, page gutters, text measure and grid gaps.
- Shape/surface: border, radius, shadow and image treatment.
- Motion: transition duration/easing and reduced-motion behaviour.
- Component states: hover, focus, selected, disabled, loading, error and success.

No HEX values, font family or default production token is selected here.

### 6.3 CSS organization

When the stack is selected, keep responsibilities clearly separated:
1. Reset/base and typography defaults.
2. Owner-approved design tokens.
3. Layout primitives and responsive containers.
4. Global site shell.
5. Shared product, collection, editorial and form components.
6. Page composition.
7. State and accessibility styling.

Prefer explicit component/state classes over selectors tightly coupled to DOM depth. Avoid scattered overrides and duplicate token definitions.

### 6.4 Responsive layout contract

Test at:
- Desktop: 1440 CSS px.
- Tablet: 768 CSS px.
- Mobile: 390 CSS px.

These are validation viewports, not fixed breakpoint declarations. Choose actual CSS breakpoints after testing where content and controls need to reflow.

At every viewport verify:
- No horizontal page overflow.
- Navigation can be used without hover.
- Product names, prices, options and actions remain legible.
- Image crop preserves the relevant product.
- Filters and drawers are reachable and closable.
- Form controls are usable with touch and keyboard.
- Focus indicators remain visible.
- No sticky UI obscures content or action controls.

### 6.5 Image system

- Preserve source aspect ratio unless a deliberate crop is approved.
- Define consistent image roles: hero, collection lead, product primary, product detail, editorial lead and thumbnail.
- Do not force every image into one ratio if the object itself needs another presentation.
- Use object-fit and object-position rules at component level, with per-image adjustment only when necessary.
- Use descriptive alt text and empty alt only for purely decorative imagery.
- Never represent an unrelated stock image as a DAG product.
- Defer bulk photo-library migration and hosting.

### 6.6 Interaction states

Every interactive component must define:
- Default.
- Hover (where pointer input exists).
- Focus-visible.
- Active/pressed.
- Selected/current.
- Disabled/unavailable.
- Loading/submitting.
- Error.
- Success/confirmation.
- Empty/no-results where relevant.

Use real buttons for actions and links for navigation. Escape should close modal/drawer experiences. Focus must return to the trigger. Honour reduced-motion preferences.

## 7. Responsive and interaction matrix

| Area | Desktop | Tablet | Mobile | Accessibility and fallback |
|---|---|---|---|---|
| Header | Full navigation and grouped Shop menu | Condensed links or accessible disclosure after testing | Menu drawer plus search/cart access | Keyboard, Escape, focus restore; no hover-only dependency. |
| Announcement | Single narrow message or rotating notices | Same content with wrapping tested | Collapse or concise line; no overlap | Pausable/dismissible where moving; no empty state. |
| Shop filters | Sidebar or filter disclosure | Compact panel/drawer | Modal drawer/disclosure | Labels, selected state, clear/reset, focus management. |
| Product grid | Column count chosen for usable card width | Reduce columns as required | One/two columns only if card remains readable | Semantic list/grid, meaningful headings and card links. |
| Product gallery | Main image with optional thumbnails | Compact thumbnails or previous/next | Touch-friendly swipe or stacked images | Buttons, alt text, keyboard access; swipe not sole method. |
| Product options | Inline choices | Wrap options | Full-width/tappable options | Labels, selected/unavailable state, clear errors. |
| Cart | Page or side panel only if practical | Stacked line items | Stacked items and totals | Announce quantity/price updates. |
| Checkout | Form sections and order summary | Stacked form/summary | Single-column progressive flow | Error summary, labels, secure submission, idempotency. |
| Editorial | Multi-column story layout | Reflow | Single-column readable measure | Correct heading hierarchy, captions, image text alternatives. |
| Footer | Grouped columns | Reduced columns | Stacked disclosures/links | Logical reading order, contrast/focus. |

No responsive interaction should be specified as directly observed from POJ or Macaroni when it was not verified at that viewport.

## 8. Brand identity requirements

### Confirmed
- Brand name: Desert Art Gallery.
- Rooted in Jaisalmer, Rajasthan.
- Japan-first intended customer-market focus.
- English-only customer-facing content.
- Original DAG identity; reference patterns are not copied.

### Proposed requirements for owner review
- Positioning should communicate a curated gallery/store, not a generic marketplace.
- Brand personality should balance product clarity, editorial depth and commercial honesty.
- The brand promise must be grounded in actual product sourcing, quality control and fulfilment capabilities.
- Wordmark/logo should work in header, mobile, footer, packaging and communication contexts.
- Graphic language should support product imagery rather than compete with it.
- Packaging and digital communications should share a consistent owner-approved system.
- Photography should show actual products faithfully and allow inspection of material, surface, scale and condition where available.

### Awaiting owner input
- Final positioning and promise.
- Logo/wordmark choice or brief.
- Palette and typography.
- Photography mood and image-treatment rules.
- Voice and vocabulary.
- Packaging/digital communication direction.

Do not invent brand history, maker stories, craft techniques, provenance, material claims or heritage claims.

## 9. Customer and commercial requirements

Confirmed:
- Japan-first is the intended primary customer-market focus.
- Customer-facing site content is English-only.

Still unresolved and not implied by the reference decision:
- Seller legal identity and jurisdiction.
- Exact sales territories.
- Base/accounting and display currency.
- Tax and import duties.
- Shipping destinations, rates and delivery commitments.
- Payment providers and methods.
- Returns, refunds and cancellations.
- Privacy and seller/legal disclosures.
- Direct ecommerce, enquiry-led or hybrid commerce model.

Use the market research as hypotheses for validation, not verified DAG customer demand. Test English-language comprehension with Japan-based participants without silently introducing Japanese customer-facing copy. Do not hard-code payment/localization behaviours from POJ.

## 10. Photography and catalogue rules

- Approximately 3,000 original photographs for roughly 300 products are recorded as available in the project charter; full migration and hosting remain deferred.
- Do not upload, bulk-migrate, optimise, download or commit the library during this reference/specification phase.
- Use intentional placeholders only when no approved product sample exists. Make them visibly illustrative.
- Use a representative 10–20 product/photo sample when supplied and approved.
- Never invent product names, prices, specs, materials, dimensions, condition, maker, provenance, review, availability or care instructions.
- Preserve source evidence, owner verification, rights status and public approval as separate states.
- Do not publish external Etsy image URLs as DAG product images by default.

## 11. M2 prototype gate and delivery sequence

The reference hierarchy is confirmed, but it does not close the M1 visual-identity gate.

Before moving from this specification to rendered M2 page prototypes:
1. Owner chooses, combines, requests revisions or rejects the four current visual territories, or asks for a new set.
2. Record the explicit visual decision and exact approved foundations in DECISIONS.md.
3. Confirm the initial customer-validation cohort and research approach.
4. Supply or approve a representative product/photo sample, or explicitly permit clearly labelled illustrative placeholders for the prototype.
5. Confirm which page journeys should be tested first. Do not implement real cart/checkout/policy promises while U-001 through U-008 remain unresolved.

After the above, prototype the homepage, Shop/collection, product detail, About/Makers, Journal and Contact at the required viewports. Cart/checkout should remain non-transactional concepts until the commercial gate is met.

## 12. Explicitly out of scope

- Pixel-perfect cloning or reuse of either reference's assets, brand identity, copy, product data or proprietary code.
- Final DAG palette, typography, photography art direction or production visual personality.
- Production CSS token values or global theme.
- Production application/framework selection.
- Database, CMS, payment provider or hosting selection.
- Live checkout, payment, tax, shipping or returns implementation.
- Bulk photo migration.
- Real product import or publication.
- Invented product, maker, customer or business claims.

## 13. Acceptance

This specification is accepted as an implementation brief when a separate design/frontend agent can understand:
1. The confirmed primary/secondary reference hierarchy.
2. The page purpose and structure for every required customer route.
3. What belongs to POJ's structural influence and Macaroni's curation influence.
4. The DAG-specific data, content and commercial dependencies.
5. Responsive and interaction requirements.
6. Reusable component responsibilities.
7. Accessibility and empty/loading/error states.
8. The owner-controlled visual identity gate.
9. The unapproved commercial and technical decisions.
10. What may be prototyped next and what must remain blocked.

**POJ Studio leads the ecommerce experience. Macaroni Shoten informs the curation. DAG remains original.**

**DO NOT ABANDON MINIMALISM. ABANDON EMPTINESS.**
