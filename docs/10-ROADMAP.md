# 10 — Project Roadmap

**Current milestone:** M1 — reference hierarchy confirmed, page specification delivered and M2 entry/acceptance pack prepared. Visual identity and customer-validation gates remain open; M2 has not started and no final visual direction is approved.

## M0 — Repository and governance foundation
**Status: Completed.**
- Install root-level project foundation.
- Establish permanent agent rules, charter, design philosophy, decision register and AI protocol.
- Add automated documentation/link checks and CI validation.

## M1 — Customer, brand and reference-led creative strategy
**Status: Reference, research and preparation packages delivered; owner decisions and field validation pending.**
- Preserve evidence-led Japan-first customer/market research and define validation hypotheses.
- Prepare a customer-validation playbook, neutral discovery interview guide, prototype usability guide and blank anonymized research templates. Do not claim field validation until sessions have actually been conducted.
- Compare direct-purchase, enquiry-led and hybrid commercial models without making an owner decision.
- Follow D-010: POJ Studio is the primary ecommerce/page-structure reference; Macaroni Shoten is the secondary select-shop/curation reference.
- Record dated observations, exact page URLs, viewport limitations and current live-site state.
- Translate useful retail principles into DAG-specific requirements without cloning either site.
- Prepare a source-neutral catalogue intake kit so product facts, evidence and image references can be checked before any application or database is selected.
- Record the historical Etsy export field mapping and preserve source-row identity, raw SKU ambiguity and remote image references separately from local media.
- Present four new, materially different DAG visual territories. The earlier P-015 set remains rejected and archived.
- Provide exact palette values, typography families/weights/licensing, layout and art-direction specifications.
- Render desktop and mobile examples with accessibility/contrast notes.
- Keep the owner-review board semantically accessible and regression-check every documented contrast ratio without changing owner-controlled design proposals.
- Present neutral trade-offs; do not recommend, rank, score, select or imply a default.
- Ask the owner to choose, combine, request revisions or reject all options. Stop before final tokens or production styling.

Deliverables: [Japan-first customer research](14-JAPAN-FIRST-CUSTOMER-RESEARCH.md), [commercial model assessment](16-COMMERCIAL-MODEL-ASSESSMENT.md), [reference-to-DAG implementation specification](15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md), [reference research log](REFERENCE-RESEARCH-LOG.md), [reference-led design brief](17-REFERENCE-LED-DESIGN-BRIEF.md), [four visual specifications](18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md), [rendered desktop/mobile board](../design/explorations/reference-led-directions.html), [catalogue intake and fact-verification standard](20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md), [Etsy source export mapping](21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md), [customer validation playbook](22-CUSTOMER-VALIDATION-PLAYBOOK.md), and [owner decision register](DECISIONS.md).

Exit: the owner explicitly chooses, combines, requests revisions or rejects the four new visual proposals and identifies the initial Japan-first customer segment focus. Japan-first itself is confirmed by D-003. M2-B asks only which segment hypotheses to research; method, recruitment route, consent and spending remain separately gated. D-010 confirms the reference hierarchy only; it does not satisfy the visual identity gate. M2 production-style page prototypes remain blocked until the owner approves a visual direction. No field validation is claimed. Real cart/checkout/policy implementation remains gated by unresolved commercial decisions.

## M2 — Responsive page prototypes
**Readiness preparation:** The [M2 entry and acceptance pack](23-M2-PROTOTYPE-ENTRY-AND-ACCEPTANCE.md), separate M2-A visual-review bundle supplied to the owner, and blank [owner-entry decision worksheet](../templates/prototypes/m2-owner-entry-decision.md) and blank [prototype review template](../templates/prototypes/prototype-review.csv) are prepared. M2 execution has not started. The separate owner-review bundle contains all four territories across homepage, Shop/collection and product-detail at desktop/mobile sizes; none is selected or recommended.

The read-only `python3 scripts/audit_m2_readiness.py` command checks cross-document gate consistency. Open gates are expected; confirmed records still require explicit owner authorization before the first route begins.

**Entry gate:** Only after owner visual selection and the remaining inputs recorded in the M2 pack:
- Homepage.
- Shop and category.
- Product detail.
- About and Makers.
- Journal.
- Contact.
- Shared global shell on all six routes: announcement/status strip, header, primary/category navigation, search disclosure and footer.
- Reusable presentation components: breadcrumbs, page/section headings, category tiles, product cards, filter/sort concepts, product gallery, product-facts rows, maker/story modules, editorial cards, support blocks and action patterns.
- Cart/checkout concepts, subject to business-rule decisions.
- Responsive states and meaningful interactions; mobile testing is cross-cutting across every journey, not a standalone journey.
- Review all six route areas against the M2 pack, including 390, 430, 768, 1280 and 1440 px widths.

Exit: owner reviews the complete six-route experience and shared shell on mobile, tablet and desktop; every selected journey has mobile and desktop evidence; visual system is owner-approved.

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
