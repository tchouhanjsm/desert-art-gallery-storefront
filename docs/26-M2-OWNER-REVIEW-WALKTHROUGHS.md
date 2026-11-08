# M2 — Owner Review Walkthroughs for the Six Private Prototype Areas

**Status: WALKTHROUGH PLAN READY — VISUAL PROPOSAL APPROVAL REQUIRED BEFORE BRANDED PROTOTYPES**  
**Decision:** D-016 (8 November 2026)

This document turns the owner's six authorized prototype areas into a review sequence. It is not a claim that a branded prototype exists. The six areas are groupings of the existing nine D-014 pages and do not change the page, section or component inventory.

## 1. Area-to-page map

| Owner-authorized review area | Existing D-014 page(s) | Review objective |
|---|---|---|
| 1. Homepage | index.html | Understand DAG identity and find the next relevant path |
| 2. Shop and Collections | pages/shop.html; pages/collection.html | Understand available category grouping and move into a collection |
| 3. Product Detail | pages/product.html | Evaluate image coverage and verified product information |
| 4. About and Makers | pages/about.html; pages/makers.html | Understand gallery context and maker/material stories |
| 5. Journal and Stories | pages/journal.html; pages/article.html | Explore editorial context and a complete story |
| 6. Contact and Support | pages/contact.html | Find accurate support/contact information and understand what is not yet offered |

Global header, existing navigation, search presentation, shared components and footer are reviewed in the context of each area, not as new prototype sections. Preserve the exact supplied page-specific presence and omissions.

## 2. Owner walkthrough sequence and checks

### 1 — Discover DAG
1. Start at the top of the Homepage at desktop width.
2. Read the brand identity and hero message.
3. Identify the three existing category entry points.
4. Locate a featured product and one story route.
5. Repeat on mobile, noting reading order, crop, text fit and navigation clarity.

Owner checks: Is the gallery identity clear within the first viewport? Is the relationship to Jaisalmer specific and factual? Does the page feel curated and substantial rather than empty? Is the primary route obvious without extra promotional elements?

### 2 — Browse products, categories and collections
1. Use Shop and the exact existing category links.
2. Open the Collection page.
3. Compare the way card images, labels and verified facts support scanning.
4. Repeat on mobile and tablet, checking card width, title wrapping and image crops.

Owner checks: Are categories understandable from actual catalogue evidence? Are product cards consistent? Are placeholders clearly labelled? Are disabled Filter/Sort controls unmistakably non-functional? No taxonomy, filter or sort behaviour should be invented.

### 3 — Evaluate a product
1. Open Product Detail from an existing product card/link.
2. Review the main image frame and three existing thumbnails.
3. Check factual attributes, units and evidence references.
4. Open the existing Description, Materials and specifications, Maker and provenance, and Care accordions.
5. Check that option and purchase controls remain disabled.

Owner checks: Can a reviewer understand the item without invented copy? Are unknown facts visibly pending? Does the image set demonstrate scale, material and condition where genuine evidence exists? Does the gallery remain legible on mobile?

### 4 — Explore makers, materials and stories
1. Review About and its two existing editorial split sections.
2. Continue to Makers.
3. Follow Journal to an Article.
4. Check that every maker/material/origin statement is evidence-backed, and all missing content remains labelled.

Owner checks: Does editorial detail add useful depth without unsupported heritage or sustainability claims? Does image/text order work on narrow screens? Is long-form text readable?

### 5 — Contact and obtain useful information
1. Review the Contact information panel.
2. Find the supplied Enquire link only where present.
3. Inspect the disabled enquiry-form concept without submitting anything.
4. Review the footer support links and factual contact details.

Owner checks: Is the route obvious? Are only confirmed contact details shown? Does the page avoid invented response times, shipping, tax, return, payment or service commitments? Is disabled form behaviour clear?

## 3. Responsive review dimensions

Every journey and every area must be reviewed at all five existing QA widths:
- 390 CSS px — narrow mobile.
- 430 CSS px — large mobile.
- 768 CSS px — tablet.
- 1280 CSS px — laptop/desktop.
- 1440 CSS px — wide desktop.

These are review widths, not new breakpoint requirements. Check layout order, overflow, card columns, image-frame stability, readable line lengths, nav disclosure and focus visibility. Automated Chromium coverage already exercises the five existing structural journeys at these widths; a human owner walkthrough remains separate.

## 4. Product/image evidence display rules

Until the owner supplies and approves a private sample:
- Use neutral image frames with visible text: “ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING”.
- Use “LAYOUT PLACEHOLDER — NOT A DAG PRODUCT” for a non-product layout tile.
- Label every missing angle/view rather than silently reusing one image.
- Show image ratios and gallery composition without importing any of the ~3,000-image library.
- Never generate fictitious products, prices, maker identities, specifications or reviews.
- Generated artwork must not be represented as DAG catalogue photography.

A 10–20 product sample is expected from the owner. Image validation remains pending until genuine product photos, verified product information, source reconciliation, image-rights evidence and private prototype-use permissions are supplied and checked.

## 5. Owner acceptance record

For each area, record:
- Decision: accept / request revision / reject.
- Desktop review: 1280 and 1440.
- Mobile/tablet review: 390, 430 and 768.
- Visual hierarchy and density.
- Image ratio/crop and placeholder clarity.
- Content/factual evidence gaps.
- Navigation clarity and shared-shell consistency.
- Keyboard/focus and disabled-state clarity.
- Exact requested changes and the relevant component/page.

These owner-led walkthroughs are not participant usability research. Human usability acceptance remains pending. Owner visual sign-off of a prototype is not customer usability research. Human customer usability testing requires a separate research protocol and the explicit M2-B fieldwork authorization. No user testing or customer usability validation is claimed by these walkthroughs.

## 6. Prototype implementation gate

Only after the owner explicitly approves the M2-A reference-led visual proposal:
- Create a private/local prototype outside the public repository.
- Implement exactly the six areas mapped above using the D-014 route/section inventory and the approved visual tokens.
- Include shared shell only as already represented in the source pages.
- Use labelled placeholders until real sample assets are accepted.
- Keep all controls non-transactional. No payment/order, shipping/tax or live enquiry processing.
- Perform responsive, keyboard and reduced-motion checks; present screenshots and a reproducible owner walkthrough.
- Record changes and outstanding decisions; do not deploy publicly or choose a production stack.

