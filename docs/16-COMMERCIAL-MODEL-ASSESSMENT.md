# 16 — Commercial Model Assessment

**Status:** Options assessed; owner decision remains unresolved.  
**Decision ID:** U-008 in `docs/DECISIONS.md`.

## Options

| Model | Customer experience | Operational requirements | Main risk | Current fit |
|---|---|---|---|---|
| Direct ecommerce | Fast, familiar purchase path; clear price and availability | Verified product/price/stock, seller disclosures, checkout, payment, shipping, tax/duty, returns, support | Cannot make a reliable promise until cross-border capabilities are known | Strong target experience only for sale-ready items |
| Enquiry-led gallery | Useful for rare, high-value, variable or custom pieces | Prompt enquiry response, accurate manual quotes, clear follow-up and order confirmation | Friction, slower conversion, unclear response expectations | Useful for items whose price, shipping or availability needs human confirmation |
| Hybrid | Direct purchase for ready items; enquiry path for exceptions | Clear eligibility rules and distinct purchase/enquiry states, with shared catalogue and service data | Inconsistent item states and operational complexity if rules are unclear | **Proposed hypothesis for evaluation** |

## Proposed hypothesis (not an owner decision)

Evaluate a **controlled hybrid** model:
- A product is purchasable only when its price, stock/uniqueness, dimensions, material, condition, image set and fulfilment route are verified.
- A product uses an enquiry path only when there is a genuine operational reason (for example, a bespoke request or confirmed need for a manual shipping quote). The reason and expected response process must be clear.
- Do not use enquiry as a substitute for missing basic product information or as a way to obscure price.
- Do not show fake stock counts, urgency labels or a purchase button for unverified items.

This is a recommendation for owner evaluation, not an approved storefront policy. The final model should be selected after mapping the real catalogue and the owner's order-fulfilment process.

## Why not choose a full model yet?

The following are still unresolved: seller legal identity and jurisdiction, destination coverage, base/display currency, payment provider eligibility, export and import handling, shipping rates and delivery commitments, returns/refunds, product readiness and the support process. Those are material requirements, not details to invent in a visual design phase.

## Owner workshop inputs

Before M3, ask the owner to review:
1. Which products are genuinely ready for a customer to buy without manual confirmation?
2. Are any pieces one-of-a-kind, made-to-order, bespoke or variable in a way that changes checkout?
3. Who owns stock accuracy, order acceptance, packing, dispatch and customer support?
4. Can shipping rates and expected delivery be calculated before checkout for the chosen destinations?
5. What happens when an item sells offline while a customer is checking out?
6. What is the operational response time for enquiries and who will handle them?

## Recommendation

Keep the interface architecture flexible enough to support both `Buy` and `Enquire` product states, but do not implement either path in production until U-001 through U-008 and the sale-ready product criteria have been reviewed. Use a prototype to test the journeys in M2; make payments, taxes, shipping and policy claims placeholders only where explicitly labelled as such.
