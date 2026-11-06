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

## Current visual proposals — no owner choice recorded

### P-015 — Four visual territories
Status: PROPOSED
Proposal: Present four materially different exploratory directions for comparison: Graphic Atelier, Future Relics, Living Garden and Modern Folk Pop. Exact palette/font/layout/contrast specifications are in `docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md`; desktop/mobile examples are in `design/explorations/visual-directions.html` and `design/explorations/rendered/`.
Owner decision required: Choose one, combine named elements, request revisions or reject all four. No winner is designated. No direction is recommended, ranked, selected or approved. This record does not confer visual authority on the AI.
Date: 2026-11-06

The former Material Archive / Collected Colour synthesis remains a historical AI proposal only. It is not a default, preferred direction or owner approval. Do not implement it unless the owner explicitly selects its elements in a new recorded decision.
