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
For each new decision:
- ID.
- Date.
- Status.
- Context.
- Options considered.
- Decision.
- Rationale.
- Consequences.
- Documents/code affected.
- Owner confirmation where required.

## M1 proposals — awaiting owner review

### P-011 — Creative direction recommendation
Status: PROPOSED
Proposal: Use **Material Archive** as the brand and composition foundation, with the product-discovery clarity and catalogue energy of **Collected Colour**. The preliminary palettes and rules are in `docs/15-CREATIVE-DIRECTION-OPTIONS.md`; the side-by-side exploratory sheet is `design/explorations/m1-territory-study.html`.
Owner decision required: Select Territory A, Territory B or the recommended synthesis before M2. No palette or typography token is approved yet.
Date: 2026-11-06

### P-012 — Brand positioning direction
Status: PROPOSED
Proposal: Position DAG as a considered gallery of textiles and objects connected to Jaisalmer, Rajasthan, presented with accurate product and material information. This is not approved public-facing copy.
Owner decision required: Confirm strategic direction and verify any public claims before publication.
Date: 2026-11-06

### P-013 — Commercial-model hypothesis
Status: PROPOSED
Proposal: Evaluate a controlled hybrid model: direct purchase for sale-ready items with verified price, stock and fulfilment; enquiry for genuinely bespoke or manually quoted exceptions. This does not resolve U-008.
Owner decision required: Select the commercial model after reviewing the real product readiness and operations.
Date: 2026-11-06

### P-014 — Initial customer-validation focus
Status: PROPOSED
Proposal: Test home/interior buyers, craft/material enthusiasts, gift buyers and trade/design professionals as hypotheses, without treating them as validated personas.
Owner decision required: Prioritize the first interview cohort and initial 10–20 product-photo sample.
Date: 2026-11-06
