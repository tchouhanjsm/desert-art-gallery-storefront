# Decision Register

This file is the durable record of owner-approved decisions and unresolved questions.

Statuses: CONFIRMED, PROPOSED, UNRESOLVED, REJECTED, SUPERSEDED.

## Confirmed

### D-001 — New repository is the source of truth
Status: CONFIRMED
Decision: Build the new storefront in `desert-art-gallery-storefront`. The previous repository is a selective engineering/business reference only. Its frontend, styles and design decisions are not inherited.
Date: 2026-11-06

### D-002 — Customer-facing language
Status: CONFIRMED
Decision: All customer-facing storefront content is English-only.
Date: 2026-11-06

### D-003 — Japan-first customer focus
Status: CONFIRMED
Decision: Japan is the intended primary customer-market focus. This is distinct from seller jurisdiction, exact sales territories and operating/legal arrangements, which require separate confirmation.
Date: 2026-11-06

### D-004 — Creative references
Status: CONFIRMED
Decision: Study POJ Studio and Macaroni Shoten for editorial retail, merchandising and customer experience. Do not clone either.
References: https://pojstudio.com/ ; https://shop.macaro-ni.jp/
Date: 2026-11-06

### D-005 — Brand roots
Status: CONFIRMED
Decision: DAG retains its Jaisalmer, Rajasthan textile, object and craft identity. Claims must be verified.
Date: 2026-11-06

### D-006 — Photography migration deferred
Status: CONFIRMED
Decision: Approximately 3,000 original photographs across roughly 300 products exist. Bulk migration and hosting are deferred. Do not commit the photo library to Git.
Date: 2026-11-06

### D-007 — Owner controls visual identity selection
Status: CONFIRMED
Decision: The AI agent must not unilaterally choose DAG's final palette, typography, visual style or art direction. It must present at least four materially distinct rendered alternatives with exact values and neutral trade-offs, then wait for the owner to choose. The previous beige/grey/ivory/terracotta direction must not be used as an automatic default.
Date: 2026-11-06

### D-008 — Reject the four proposed visual territories
Status: CONFIRMED
Decision: The owner explicitly rejected all four territories in P-015 on 6 November 2026: Graphic Atelier, Future Relics, Living Garden and Modern Folk Pop. None is selected, preferred, approved, a default or an active candidate. The full P-015 package is retained as historical evidence only.
Owner instruction: "My DAG visual direction decision: reject."
Consequences: Build a fresh visual review around the references named in D-009. Do not reuse the rejected palettes or type pairings as a default.
Date: 2026-11-06

### D-009 — POJ Studio and Macaroni Shoten as principal design references
Status: CONFIRMED
Decision: The owner names https://pojstudio.com/ and https://shop.macaro-ni.jp/ as the principal references for the next DAG creative and retail design study and asks whether DAG can be designed exactly like them. Use both as close references for customer experience, editorial retail quality, product discovery, merchandising and information hierarchy. The DAG deliverable must remain original: do not clone either site's identity, source assets, copy, product imagery or pixel-for-pixel page composition. This reference instruction does not select a final DAG palette, typography, art direction or page layout.
Owner instruction: "shop.macaro-ni.jp/ and pojstudio.com - can we design exactly as it it."
Consequences: Use docs/17-REFERENCE-LED-DESIGN-BRIEF.md to prepare new owner-review options. Keep the visual approval gate active.
Date: 2026-11-06

### D-010 — Reference fidelity and hierarchy
Status: CONFIRMED
Decision: DAG's reference fidelity is BLEND. POJ Studio is the primary reference for overall ecommerce architecture, global navigation, homepage composition, Shop/collection discovery, product cards, product detail, maker/story and supporting retail experience. Macaroni Shoten is the secondary reference for select-shop curation, category grouping, lifestyle-oriented selection and concise editorial retail character. DAG must remain an original Jaisalmer-rooted brand with its own products, content, imagery, taxonomy and English-only customer-facing experience.
Owner instruction (7 November 2026): "Reference fidelity: BLEND. Primary reference: POJ Studio. Secondary reference: Macaroni Shoten."
Boundaries: This decision confirms the reference relationship only. It does not approve a DAG colour palette, font pairing, visual personality, photography art direction, final layout, category taxonomy, commerce model, technology stack or any POJ/Macaroni feature that DAG does not actually offer. Do not clone source code, proprietary CSS, exact composition, copy, products, photography or brand identity.
Consequences: Follow docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md for the page-by-page implementation specification and docs/REFERENCE-RESEARCH-LOG.md for dated evidence. Preserve the separate owner-controlled visual-identity gate in D-007.
Date: 2026-11-07

## Unresolved owner decisions

### U-001 — Seller jurisdiction and legal identity
Status: UNRESOLVED
Question: What is the legal seller entity and jurisdiction?
Impacts: tax, consumer obligations, payment eligibility, privacy and disclosures.

### U-002 — Exact sales territories
Status: UNRESOLVED
Question: Will DAG sell only to Japan, to Japan and India, or to additional international destinations?
Impacts: shipping, duties, tax, payment, returns and support.

### U-003 — Currency and pricing
Status: UNRESOLVED
Question: What is the base accounting currency and which display currencies are required?
Impacts: price management, conversion, rounding and checkout.

### U-004 — Shipping and fulfilment
Status: UNRESOLVED
Question: Which carriers, destinations, rates, delivery promises and fulfilment workflows are feasible?

### U-005 — Payment methods
Status: UNRESOLVED
Question: Which providers and methods are supported by the seller jurisdiction and target markets?

### U-006 — Returns, refunds and cancellations
Status: UNRESOLVED
Question: What policy is approved and legally applicable?

### U-007 — Customer segments
Status: UNRESOLVED
Question: Which customer segments and purchase motivations should research prioritize?

### U-008 — Commercial model
Status: UNRESOLVED
Question: Direct ecommerce, enquiry-led gallery or hybrid? Compare before implementation.

### U-009 — Brand positioning and promise
Status: PROPOSED
Question: What precise promise can DAG make, supported by verified capabilities?

### U-010 — Technology and hosting
Status: UNRESOLVED
Question: Select after requirements and options are documented.

## Decision record format
For each new decision, record ID, date, status, context, options, decision, rationale, consequences, affected docs/code and owner confirmation.

## Rejected historical visual proposal package

### P-015 — Four visual territories
Status: REJECTED

Proposal history: Graphic Atelier, Future Relics, Living Garden and Modern Folk Pop were presented with exact palette/font specifications and desktop/mobile explorations in the earlier review.

Owner decision: The owner explicitly rejected all four on 6 November 2026: "My DAG visual direction decision: reject."

Consequences: None of the four proposals may be treated as selected, preferred, ranked, blended by the AI, a default or an active candidate. No winner exists; the entire P-015 package is rejected. Retain the assets and specifications as historical audit material only. Do not use their palettes, type pairings or preview compositions as a starting default.

### P-018 — Etsy source export mapping and remote-image reconciliation
Status: PROPOSED

Proposal: Add a source-snapshot mapping for Etsy Listings Download data, using the immutable source-file SHA-256 and logical data-row number as the row identity because the documented export has no listing ID and contains repeated titles. Preserve raw duplicate/blank SKUs, source descriptions/prices/materials/tags/quantity/variations and IMAGE1–IMAGE10 URLs in separate private intake tables. Keep remote URLs separate from local assets; no download or import is authorized by this proposal.

Evidence boundary: The mapping references the historical audit written in the earlier `desert-art-gallery` repository on 4 November 2026 (527 rows and other reported observations). The original export is not tracked in the new storefront repository and has not been re-audited in this task. A current source file must be provided privately before import preview or row reconciliation.

Boundaries: No raw Etsy export, populated source manifest, image URL, price, category, product or downloaded media is committed to Git. This does not approve a production import, taxonomy, currency, pricing, inventory, legal/commerce policy, backend or visual system.

Date: 2026-11-07

### P-017 — Draft source-neutral catalogue intake contract
Status: PROPOSED

Proposal: Prepare a private product-data intake package that separates product identity, factual evidence, public approval and image rights/publication approval. Blank templates and a local standard-library validator are provided in `templates/catalogue/` and `scripts/validate_catalogue_intake.py`; the draft standard is documented in `docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md`.

Boundaries: This is not an approved production schema, category taxonomy, currency policy, commerce model or backend design. No product records are included in the repository. The owner must review the fields and workflow before this contract is treated as authoritative.

Date: 2026-11-06

### P-016 — New reference-led DAG design exploration
Status: PROPOSED

Basis: D-009 and docs/17-REFERENCE-LED-DESIGN-BRIEF.md.

Proposal package delivered: [Porcelain Index], [Bordeaux Editions], [Blue Current] and [Citron Signal], each with exact HEX palettes, type families/weights/licensing, page composition and photography direction, neutral trade-offs and contrast notes. Desktop/mobile renders are presented in design/explorations/reference-led-directions.html; detailed specifications are in docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md. The four territories are proposals only, not recommendations or approvals.

Owner action: Review the new options when presented and choose one, combine explicit elements, request revisions or reject all. No recommendation or winner is designated. No production tokens or theme may be finalized before the new explicit owner choice is recorded.

Date: 2026-11-06

The former Material Archive / Collected Colour synthesis remains a historical AI proposal only. It is not a default, preferred direction or owner approval. Do not implement it unless the owner explicitly selects its elements in a new recorded decision.
