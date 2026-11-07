# 10 — Project Roadmap

**Current milestone:** M1 — reference hierarchy confirmed and complete page-by-page implementation specification delivered. Visual identity and customer-validation gates remain open; no final visual direction is approved.

## M0 — Repository and governance foundation
**Status: Completed.**
- Install root-level project foundation.
- Establish permanent agent rules, charter, design philosophy, decision register and AI protocol.
- Add automated documentation/link checks and CI validation.

## M1 — Customer, brand and reference-led creative strategy
**Status: Research and proposal package delivered; owner review pending.**
- Preserve evidence-led Japan-first customer/market research and define validation hypotheses.
- Compare direct-purchase, enquiry-led and hybrid commercial models without making an owner decision.
- Follow D-010: POJ Studio is the primary ecommerce/page-structure reference; Macaroni Shoten is the secondary select-shop/curation reference.
- Record dated observations, exact page URLs, viewport limitations and current live-site state.
- Translate useful retail principles into DAG-specific requirements without cloning either site.
- Prepare a source-neutral catalogue intake kit so product facts, evidence and image references can be checked before any application or database is selected.
- Record the historical Etsy export field mapping and preserve source-row identity, raw SKU ambiguity and remote image references separately from local media.
- Present four new, materially different DAG visual territories. The earlier P-015 set remains rejected and archived.
- Provide exact palette values, typography families/weights/licensing, layout and art-direction specifications.
- Render desktop and mobile examples with accessibility/contrast notes.
- Present neutral trade-offs; do not recommend, rank, score, select or imply a default.
- Ask the owner to choose, combine, request revisions or reject all options. Stop before final tokens or production styling.

Deliverables: [Japan-first customer research](14-JAPAN-FIRST-CUSTOMER-RESEARCH.md), [commercial model assessment](16-COMMERCIAL-MODEL-ASSESSMENT.md), [reference-to-DAG implementation specification](15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md), [reference research log](REFERENCE-RESEARCH-LOG.md), [reference-led design brief](17-REFERENCE-LED-DESIGN-BRIEF.md), [four visual specifications](18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md), [rendered desktop/mobile board](../design/explorations/reference-led-directions.html), [catalogue intake and fact-verification standard](20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md), [Etsy source export mapping](21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md), and [owner decision register](DECISIONS.md).

Exit: the owner explicitly chooses, combines, requests revisions or rejects the four new visual proposals and confirms the initial customer-validation focus. D-010 confirms the reference hierarchy only; it does not satisfy the visual identity gate. The implementation specification may guide later prototypes, but M2 production-style page prototypes remain blocked until the owner approves a visual direction. Real cart/checkout/policy implementation remains gated by the unresolved commercial decisions.

## M2 — Responsive page prototypes
Only after owner visual selection:
- Homepage.
- Shop and category.
- Product detail.
- About and Makers.
- Journal.
- Contact.
- Cart/checkout concepts, subject to business-rule decisions.
- Responsive states and meaningful interactions.

Exit: owner reviews rendered prototypes on mobile, tablet and desktop; visual system is owner-approved.

## M3 — Business and technical architecture
- Confirm seller jurisdiction and sales territories.
- Confirm operational/commercial model.
- Evaluate payment, shipping, tax and returns requirements.
- Define catalogue, content, media and owner operations.
- Evaluate technology and hosting without premature commitments.
- Assess legacy engineering for selective reuse, never frontend/design copying.

## M4 — Application foundation
Begin only after design and architecture approval. Bootstrap the chosen application, approved design system, routes, data boundaries, tests and CI.

## M5 — Catalogue, content and media
Integrate verified catalogue data, establish media mapping, and integrate original photography only when authorized.

## M6 — Commerce and merchant operations
Subject to approved business rules, implement purchase/enquiry, checkout, payments, tax/shipping, orders, fulfilment, support and owner/admin operations.

## M7 — Launch readiness
Security, accessibility, performance, SEO, backup/restore, monitoring, incident plan, deployment and owner acceptance.

Do not skip milestones to generate visible code. See the mandatory owner gate in 14-OWNER-CONTROLLED-VISUAL-DIRECTION.md: **THE AI PROPOSES. THE OWNER CHOOSES. THE AI IMPLEMENTS.**
