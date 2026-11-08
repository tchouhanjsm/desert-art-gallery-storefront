# 00 — Project Charter

## Purpose
Create a distinctive, trustworthy, premium ecommerce and gallery experience for Desert Art Gallery (DAG), rooted in Jaisalmer, Rajasthan, and the character of its textiles, objects and authentic craft, with a Japan-first customer focus.

The goal is not to modernize the old storefront. The goal is to define and build the right experience from first principles.

## Principal design references

Our principal references are:

- **POJ Studio:** https://pojstudio.com/
- **Macaroni Shoten:** https://shop.macaro-ni.jp/

These are DAG's references for creative and retail study. Study their actual editorial presentation, merchandising, product discovery, navigation, typography, photography and responsive customer experience. Learn from their principles, but do not copy their assets, exact layouts, content or brand identity. DAG must express its own Jaisalmer textile, object and craft identity.

## Owner-confirmed reference hierarchy (D-010)

Reference fidelity is BLEND. POJ Studio is the primary reference for overall ecommerce architecture and page experience. Macaroni Shoten is the secondary reference for select-shop curation and concise editorial retail character. DAG retains its own Jaisalmer identity, product taxonomy, photography and English-only content.

This hierarchy does not select DAG's final palette, typography, visual personality, art direction, technology, commerce model or legal/operational rules. It identifies references for non-proprietary experience study only; it does not authorize importing their navigation, banners, filters, checkout, service features or other UI into the closed D-014 kit.

## Current structural scope (D-014)

The owner has adopted the DAG Owner-Controlled Design Kit v2 as the structural HTML/CSS source for exactly nine pages. The 25-file owner archive is materialized in `design/owner-controlled-kit-v2/`; its SHA-256 is `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`. The 14 original HTML/CSS/JS implementation assets were verified at adoption; PR #9 applies two documented CSS-only accessibility maintenance rules. See `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md` for the closed route and component contract.

D-014 does not approve final brand identity, production application development, a framework/backend/hosting choice, cart/checkout or other commerce functionality, or any new UI beyond the supplied kit.

## Confirmed direction
- Japan-first is the intended customer focus.
- All customer-facing content is English-only.
- DAG's identity is rooted in Jaisalmer/Rajasthan textiles, objects and craft.
- The design system and storefront must be original to DAG.
- Approximately 3,000 original product photographs for roughly 300 products exist; bulk migration and media hosting are deferred.
- Product, maker, material, provenance, price, review, inventory, policy and business claims must be verified.

## Market and operational distinction
Japan-first customer focus does not establish all legal or operational arrangements. Before commerce implementation, confirm:
- Seller's legal entity and jurisdiction.
- Exact sales territories and exclusions.
- Base/display currency.
- Tax and import-duty handling.
- Shipping providers, destinations, charges and delivery commitments.
- Payment-provider availability and supported methods.
- Returns, refunds and cancellations.
- Privacy, consumer and seller disclosures.
- Customer support contact and operating hours.

Do not assume these from design references or from the previous repository.

## Customer and merchandising ambition
The future store should make it easy to understand what DAG offers, discover relevant products, evaluate quality and specifications, understand purchasing conditions and obtain help. Product presentation leads; storytelling deepens product interest. These future-state ambitions do not authorize new features in the D-014 structural kit.

## Success criteria
- Distinctive, product-led visual identity after owner approval.
- Strong catalogue and category discovery.
- Honest, useful product information.
- Thoughtful desktop and mobile experience.
- Clear support and trust information.
- Accessible, secure, maintainable engineering.
- A feasible owner/admin operating model.
- Verified end-to-end commerce only after commercial rules and scope are approved.

## Initial scope exclusions
- Full image-library migration.
- Live payment integration.
- Unapproved tax/shipping/legal rules.
- Publishing unverified brand, maker or product stories.
- Production deployment.
- Selecting vendors or paid infrastructure before requirements review.

## Legacy boundary
The previous repository may be inspected for verified domain knowledge, data structures, operations and proven engineering. Do not reuse its UI, layouts, styles, theme tokens or obsolete instructions.
