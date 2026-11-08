# M2-A — Reference-Led Visual Proposal for Desert Art Gallery

**Status: OWNER REVIEW REQUIRED — NOT APPROVED FOR IMPLEMENTATION**  
**Prepared:** 8 November 2026  
**Reference hierarchy:** POJ Studio leads; Macaroni Shoten informs; Jaisalmer gives DAG its identity.

This is one coherent proposal, not a palette competition. It deliberately does not revive P-015/P-016 or copy a reference site's brand assets, proprietary code, exact branded artwork, logo, photography or typeface files. Every DAG HEX value, typeface, size and component treatment below is a design recommendation only. The owner retains final authority over colours, typography, logo/wordmark, descriptor and photography direction.

## 1. What the live references actually show

### POJ Studio — primary reference

Live pages reviewed on 8 November 2026:
- https://pojstudio.com/
- https://pojstudio.com/collections/all
- https://pojstudio.com/products/kohiki-slim-angled-cup

Observed structure and experience:
- A full-width, photography-led campaign hero leads the homepage. Below it, the page alternates concise brand/editorial statements, image-led entry points, press/story material and featured product collections.
- The navigation separates shopping, experience, stories and brand information rather than forcing every content type into one catalogue.
- The Shop All page showed 295 products and 13 pages at review time. It used a two-part collection composition: a left filter/navigation rail and a product grid. Product cards exposed image, name and price, with availability or curated labels on some cards.
- The product page used an approximately half-width gallery and half-width information column on desktop. Portrait product imagery and thumbnails provide several views; maker context is integrated into the product story.
- The site uses a responsive design-system vocabulary: spacing, breakpoints, surface, text, button and border variables. Typography sizes use fluid clamp-based rules. CSS variable names included the --shadow- family prefix; visible weights included 400, 500 and 600.
- Navigation and merchandising controls on POJ (localisation, search, account, cart, filters, sorting, layout toggles, purchase actions and promotional bars) describe POJ's commercial implementation. They are not a DAG feature backlog and are excluded where they are not in DAG's approved scope.

**Measurement limits:** The browser report did not capture exact viewport dimensions. POJ's resolved HEX/RGB values could not be extracted; the actual values sit behind theme variables. Its precise font-family names and font files were not resolved. Therefore no POJ HEX or typeface is presented here as a measured reference value.

### Macaroni Shoten — secondary reference

Live pages reviewed on 8 November 2026:
- https://shop.macaro-ni.jp/
- https://shop.macaro-ni.jp/about
- https://shop.macaro-ni.jp/categories/3902202
- https://shop.macaro-ni.jp/categories/3902214

Observed structure and experience:
- A compact navigation groups the shop into four broad headings: Kitchen, Living, Food and Daily, with subcategory links nested beneath.
- The homepage uses a large lifestyle-image area and short editorial positioning. The About page expands the shop's curation philosophy.
- The shop showed an empty-product state during this review. Therefore current product merchandising, card detail and purchase experience could not be assessed.
- The live DOM inspection reported Yu Mincho (yumin) as the editorial serif family and sans-serif navigation. Reported sizes included 32px for the shop title, 16px for the tagline/menu items, 14px for navigation and 12px for footer text.
- Direct DOM colour readings reported #000000 primary text, #FF6700 orange icon accent, #FECB8B a secondary logo detail, and #CCCCCC for the menu background. Header and modal surfaces were white/light grey.

These are values observed on Macaroni only, not proposed DAG colours. Do not transplant its orange, gold, logo, Japanese copy, font files or menu implementation.

### Reference-to-DAG learning

| Reference observation | DAG adaptation proposed | Explicitly not copied |
|---|---|---|
| POJ's image-led homepage and clear routes into shopping, stories and makers | A strong DAG hero followed by the exact existing three category slots, four curated product slots, material/story split and two story slots | POJ campaign, text, assets, exact nav, press modules, commercial banners |
| POJ collection context, product count and clear product cards | Concise category context and calm, consistent product cards using only verified facts | POJ filters, sorting, swatches, badges, count claims or layout switcher |
| POJ near 50/50 desktop product gallery and information | A clear two-column product-evaluation composition with large portrait image and visible verified facts | POJ product composition, tab content, cart, quantity or related-product modules |
| Macaroni's compact four-group taxonomy | A small, understandable DAG collection structure based on the real catalogue when it is verified | Kitchen/Living/Food/Daily labels and any guessed DAG taxonomy |
| Macaroni's concise editorial treatment | Short, specific editorial introductions connected to real Jaisalmer makers, materials and objects | Japanese wording, copy, logo, assets or exact serif use |

## 2. One proposed DAG visual direction

**Working direction name (proposal label only): “Material in Focus.”**  
A crisp, image-led gallery system with deep mineral blue, bright sun-yellow and clean white. Its character comes from strong editorial typography, confident colour used with restraint, generous image scale and the specificity of genuine Jaisalmer objects and making. The page should feel curated and substantial, not sparse: each section earns its place through a product, material, maker or useful story.

This proposal intentionally avoids beige, grey, ivory, greige and muted terracotta as the palette foundation. The proposed canvas is true white with a cool, almost-blue surface tint; the identity colour is a saturated mineral blue, paired with a vivid saffron accent. The palette is not claimed to be a traditional Jaisalmer palette or a statement about local craft history.

## 3. Proposed colour system — exact values, roles and limits

All entries in this table are **proposed DAG adaptations**, not measured values from POJ/Macaroni and not owner-approved tokens.

| Token / role | Proposed HEX | Intended use |
|---|---|---|
| Canvas / primary surface | #FFFFFF | Main page background and image surround |
| Ink / primary text | #132A3A | Body text, display text, navigation and strong labels |
| Brand / primary action | #174F6B | Primary action surface, selected navigation rule and restrained identity blocks |
| Sun / accent | #E5AD26 | Small graphic markers, category index, fine rules and highlight fills with dark ink text |
| Cool surface | #F3F7F8 | Alternating editorial panels, quiet information surfaces and card groupings |
| Border / divider | #D4E0E5 | Fine separators, image-frame edges and form outlines |

The accent colour is intentionally not used as small text on white. It is a graphic/fill colour with dark-ink text. Primary controls use the deep blue with white text. Do not add gradients, shadows or a second arbitrary accent without owner review.

### Contrast calculation for this proposal only

Calculated from the proposed sRGB hex values:
- #132A3A on #FFFFFF: approximately 14.79:1.
- #174F6B on #FFFFFF: approximately 8.87:1.
- #132A3A on #E5AD26: approximately 7.28:1.
- #132A3A on #F3F7F8: approximately 13.71:1.

These calculations are design checks for the proposal, not a WCAG conformance claim. Actual states, text sizes, opacity, photographs, hover/focus and disabled controls must be rechecked after the owner approves a direction. The #D4E0E5 border is a subtle decorative divider; do not use it alone to communicate an essential control boundary.

## 4. Proposed type system

POJ's exact font files/family names were not resolved in the live inspection. Macaroni's page exposed a Yu Mincho editorial serif and sans-serif navigation. DAG should not copy either reference's actual typeface files.

**Proposed pairing (not approved):**
- Display/editorial: Source Serif 4, weights 500 and 600; 700 only for short hero emphasis if needed. Use for the hero headline, editorial page titles and story/article headings.
- Body and interface: Inter, weights 400, 500 and 600; 700 only for high-priority short labels. Use for paragraphs, product facts, navigation, controls, prices, captions and footer text.
- Fallbacks: Source Serif 4, Georgia, serif for display; Inter, Arial, sans-serif for interface/body. Prefer self-hosted licensed font files if this pairing is approved. Confirm font licence and final file provenance before use.

### Proposed type hierarchy

| Role | Desktop | Mobile | Weight / line-height |
|---|---:|---:|---|
| Hero headline | 56px | 34px | Source Serif 4 600 / 1.08 |
| Page H1 | 44px | 34px | Source Serif 4 600 / 1.12 |
| Section H2 | 32px | 28px | Source Serif 4 600 / 1.18 |
| Card / subsection H3 | 22px | 20px | Inter 600 / 1.25 |
| Body | 16px | 16px | Inter 400 / 1.60 |
| Secondary body | 14px | 14px | Inter 400 / 1.50 |
| Eyebrow / nav label | 11px | 11px | Inter 600 / 1.25; letter spacing 0.09em |
| Caption / metadata | 12px | 12px | Inter 500 / 1.40 |

Use sentence case for editorial headings and normal case for explanatory copy. Avoid making all navigation/body content uppercase. Keep long-form reading measure around 60–72 characters per line where the layout allows.

## 5. Wordmark and logo requirements

No logo, emblem, monogram, descriptor or final wordmark is proposed as an approved design. The recommended brief for a future original identity is:
- A custom typographic wordmark reading “Desert Art Gallery”.
- A secondary “DAG” monogram only if the owner wants one and it remains legible at small sizes.
- No generic camel, fort silhouette, dunes, sunburst, mandala or stock craft icon as a shortcut.
- Supply vector master artwork (SVG and print-ready PDF), horizontal and compact arrangements, one-colour positive/negative variants, clear-space and minimum-size rules, and accessible digital export.
- Keep the descriptor separate from the master wordmark until the owner approves exact wording. Do not invent a tagline.
- Ensure the design remains readable in the supplied desktop and mobile header widths. Confirm ownership and reproduction rights for commissioned artwork.

The text wordmark/descriptor placeholders in D-014 remain placeholders until owner approval. Do not redraw them as an implementation decision.

## 6. Header and navigation proposal

Preserve the exact supplied six navigation destinations: Shop, Collections, About, Makers, Journal, Contact. Do not add Experience, Visit, Interiors, account, cart, currency/language selector or promotion bar.

Desktop composition:
- Wordmark aligned left.
- Six nav links grouped horizontally with clear spacing and strong contrast.
- Existing search presentation only where it exists in the supplied kit; it remains disabled/visual-only.
- Enquire remains only where the supplied page already has it.
- Utility location row and footer preserve their supplied presence/omissions and content placeholders.
- No new sticky state, floating action, dropdown interaction or announcement band.

Mobile composition:
- Wordmark left; existing menu toggle right.
- The six links appear in the existing supplied mobile navigation disclosure.
- The search affordance remains disabled where present. Do not add a search overlay or new control.
- Keep a generous tap area around existing controls without introducing new elements.

## 7. Page compositions within the approved inventory

The page design proposals below refer to existing D-014 slots and sections only. They do not authorize a change to the HTML source kit. The exact page/section counts remain in docs/PAGE-INVENTORY.md and docs/COMPONENT-INVENTORY.md.

### Homepage

Desktop: a generous, wide editorial hero with one genuine, owner-approved image and concise identity-led copy. Below it, the three existing category cards form a clear discovery row; four curated product cards provide an immediate route into the catalogue; the existing split section gives one material/maker story real depth; two journal cards close the page with useful editorial paths. Preserve breathing room but avoid giant empty gaps.

Mobile: one full-width hero image-frame, headline and action stacked; three category doors as compact stacked cards or a controlled two-column arrangement if text remains clear; product cards in a two-column grid only where image and title are readable; editorial split becomes image then text; two story cards stack. Do not drop or invent slots.

### Shop and Collections

Shop desktop: page introduction and three supplied category-link placeholders precede the existing six product cards. Use a consistent card rhythm, image crop and title/price alignment. Do not add a filter sidebar or change disabled Filter/Sort.

Collection desktop: breadcrumb, compact collection title/intro and three existing product cards. Use the same card proportions and typographic hierarchy as Shop.

Mobile: page introduction first, category links as clearly labelled compact cards, two product columns where readable, with stable image frames and short title wrapping. Existing disabled controls remain disabled; no live filtering, sorting, counts or swatches are implied.

### Product Detail

Desktop: approximately 55% gallery / 45% information is proposed as a starting composition inside the existing two-column structure. Use one prominent 4:5 portrait image frame and the three existing square thumbnail frames. Product name, verified price/specification fields and the existing accordions sit in the information column. Keep the Enquire link only where already supplied. Purchase and options stay disabled.

Mobile: stack the main portrait image first, then its three thumbnail frames, then product identity and the verified fact summary. Existing information accordions remain available. Keep the disabled purchase and variant controls visibly disabled; do not imply transaction readiness.

### About and Makers

Use the two existing About editorial splits to connect place/material context to a second concrete aspect of the gallery, without unsupported claims. Use the Makers layout to explain an individual maker only when identity and facts are owner-verified. A placeholder must say information pending; do not invent a maker bio.

### Journal and Stories

Use the six existing Journal story cards and one Article layout. Each card needs a clear editorial title and a relevant, approved image/placeholder. The article page should give the lead image and text enough room for readable long-form reading. Do not add press logos, testimonials or related-story widgets.

### Contact and Support

Keep the Contact structure factual and direct: verified contact details only, a clear support-information hierarchy and the existing disabled enquiry-form concept. Do not activate form submission or invent service hours, response times, returns/shipping commitments or a contact address.

## 8. Photography and image-frame proposal

**Not an approved final photography direction.** The proposed visual treatment is:
- Prefer original DAG photography with accurate colour, natural surface detail, a clear focal object and usable context/scale.
- Use a purposeful mix of full-object, detail/material and contextual views only where genuine images exist.
- Preserve natural colour and texture; avoid excessive saturation, artificial blur, heavy filters or dramatic stock-like grading.
- Do not infer provenance, artisan identity, region, age or technique from appearance alone.
- Use fixed image frames so the layout remains composed before assets arrive. Suggested ratios are hero 16:9, product/category cards 4:5, product main view 4:5, product thumbnails 1:1 and journal lead 16:9. Ratios are proposal values for owner review, not reference measurements.
- Any empty frame must carry a visible label: “ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING”. For a generic layout placeholder use “LAYOUT PLACEHOLDER — NOT A DAG PRODUCT”.
- Do not use generated illustrations, remote Etsy photos, stock images or unrelated images as DAG catalogue photography. No actual sample is present; image validation remains pending.

## 9. Proposed CSS tokens and component specifications

These are a proposal specification only. Do not put them in the active D-014 token file or any production stylesheet before approval.

| Token | Proposed value |
|---|---|
| --dag-color-canvas | #FFFFFF |
| --dag-color-ink | #132A3A |
| --dag-color-brand | #174F6B |
| --dag-color-accent | #E5AD26 |
| --dag-color-surface | #F3F7F8 |
| --dag-color-border | #D4E0E5 |
| --dag-font-display | “Source Serif 4”, Georgia, serif |
| --dag-font-body | Inter, Arial, sans-serif |
| --dag-weight-regular / medium / semibold | 400 / 500 / 600 |
| --dag-space-1 … --dag-space-8 | 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64px |
| --dag-content-max | 1440px |
| --dag-gutter-desktop / mobile | 56px / 20px |
| --dag-section-gap-desktop / mobile | 80px / 48px |
| --dag-radius-card | 0px (proposed restrained, square-edged card frame) |

Component rules:
- Header: consistent baseline, clear focus indicator and no extra controls.
- Navigation: strong text contrast, generous spacing and visible active-page indication without badges.
- Product card: fixed 4:5 frame, image, product title and verified price only; no speculative labels, ratings, stock or swatches.
- Category card: one image frame, concise approved label and optional one-line description only if factual.
- Editorial split: balanced image/text columns with an intentionally clear reading order on mobile.
- PDP gallery: one large 4:5 image, three 1:1 thumbnail slots, obvious selected state only if already supported by prototype behaviour; avoid new carousel behaviour.
- Accordion: simple typographic title, visible focus and readable expanded text; no new accordion categories beyond the supplied four.
- Footer: preserve existing groups and exact link inventory.

## 10. Desktop and mobile visual examples

A separate, self-contained review board accompanies this proposal. It uses labelled image frames only; it is not a prototype, production theme or real catalogue. It demonstrates a desktop homepage/shop/PDP composition and corresponding narrow-screen stacking. The board is stored outside the public repository so the owner can review it without publishing a branded prototype.

## 11. Approval gate and change control

Review the proposal as one direction. The owner may approve it, reject it or request exact changes to individual values and rules. Silence, a CI pass or the existence of this document does not count as approval.

Before implementation, record the owner's exact accepted/rejected changes in docs/DECISIONS.md and update docs/OWNER-TOKEN-INPUT.md. Only then may a private, local, non-transactional prototype be styled for the six authorized M2-E areas. The D-014 structural kit remains unchanged; the prototype must stay outside the public repository and use only approved genuine sample content or clearly labelled placeholders.
