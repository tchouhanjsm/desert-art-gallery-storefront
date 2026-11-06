# Desert Art Gallery — Permanent Agent Instructions

## 1. Mission
Build Desert Art Gallery (DAG) as a premium, product-led ecommerce and gallery experience rooted in the textiles, objects, material culture and craft identity of Jaisalmer, Rajasthan, with a Japan-first customer focus.

This is a new project. Do not copy or inherit the old storefront's HTML, CSS, layouts, components, design tokens, page structures, content assumptions or visual decisions from:
https://github.com/tchouhanjsm/desert-art-gallery

The legacy repository may be inspected selectively for verified domain knowledge, data structures, operational lessons and proven engineering logic. It is not the visual starting point.

## 2. Instruction hierarchy
When instructions conflict, follow this order:
1. Explicit owner decisions recorded in `docs/DECISIONS.md`.
2. This `AGENTS.md`.
3. `docs/00-PROJECT-CHARTER.md`.
4. Relevant approved brand, design, content and architecture documents.
5. Current milestone in `docs/10-ROADMAP.md`.
6. Task-specific instructions, provided they do not conflict with higher-priority instructions.

If authoritative documents conflict, do not silently choose one. Identify the contradiction, record it and ask one focused owner question only when it blocks safe progress. Otherwise choose a safe, reversible approach and document the assumption.

## 3. Creative and working philosophy
Work with the discipline associated with an excellent Japanese premium-retail and craft studio:
- **Omotenashi:** anticipate customer needs and remove friction.
- **Shokunin:** care deeply about detail, quality and finish.
- **Ma:** use space intentionally to create rhythm, hierarchy and focus.
- **Kanso:** remove unnecessary complexity, never useful information.
- **Kaizen:** observe, test, improve and verify continuously.

These are working and service principles. They are not instructions to imitate Japanese stereotypes, insert Japanese motifs, or use Japanese-language storefront content.

Creative references:
- https://pojstudio.com/
- https://shop.macaro-ni.jp/

Study the principles behind their retail experiences. Do not clone their layouts, assets, text or brand identity.

Permanent principle:

# DO NOT ABANDON MINIMALISM. ABANDON EMPTINESS.

## 4. Confirmed project direction
- Japan-first is the intended customer and market focus.
- All customer-facing content must remain English-only.
- DAG's brand identity must retain its authentic connection to Jaisalmer, Rajasthan, textiles, objects and craft.
- The new repository is the source of truth for the new storefront.
- The old repository's frontend and design instructions are not inherited.
- The owner has approximately 3,000 original product photographs for roughly 300 products. Full image migration and hosting are deferred until the design and frontend foundation is ready.
- Use verified product, maker, material, provenance, price, availability, policy and business information only.

## 5. Japan-first does not authorize invented operational rules
Japan-first describes the intended customer focus. It does not, by itself, settle the seller's legal jurisdiction, exact shipping coverage, tax treatment, duties, payment-provider eligibility, returns obligations, consumer disclosures or fulfillment capabilities.

Do not invent or silently decide:
- Legal seller identity and jurisdiction.
- Sales territories and exclusions.
- Currency and conversion rules.
- Tax and duty treatment.
- Shipping destinations, fees and delivery promises.
- Payment providers or payment methods.
- Returns, refunds and cancellation policy.
- Privacy, consumer-law or other legal disclosures.
- Customer-service contact details or operating commitments.

Research options and explain implications. Record owner-controlled decisions in `docs/DECISIONS.md`.

## 6. Accuracy and anti-hallucination rules
Never fabricate:
- Products, product names or product attributes.
- Prices, discounts or currency conversions.
- Reviews, ratings, rankings or sales figures.
- Inventory quantities or availability.
- Maker identities, craft techniques or provenance.
- Materials, dimensions, condition or care information.
- Awards, certifications or sustainability claims.
- Shipping charges, delivery times or return promises.
- Business addresses, contact details or legal statements.

When information is missing:
1. Search project files and approved sources.
2. State what is verified and what is not.
3. Use clearly labelled design/development placeholders when necessary.
4. Record unresolved content as an owner dependency.
5. Never turn a plausible guess into a fact.

Clearly distinguish verified facts, assumptions, proposals, owner decisions and implemented/tested behaviour.

## 7. Design process
Do not start production frontend implementation before the creative direction and key page prototypes have been reviewed against the acceptance criteria.

Use these states:
Exploration → Proposed → Owner-approved → Implemented → Visually verified.

An AI agent cannot mark its own design proposal as owner-approved.

Do not use the old storefront's screenshots, source styles or layout as the design target. Create a fresh DAG direction informed by the approved references and DAG's own material identity.

Product discovery and presentation are central. Editorial storytelling must support shopping, not replace it.

## 8. Photography rules
- Do not upload, migrate or optimize the 3,000-photo library unless explicitly assigned.
- Do not commit product-photo binaries to Git.
- Do not bulk-download Etsy image URLs during the foundation/design phase.
- Do not use unrelated stock imagery as product representation.
- Use varied, visually deliberate design placeholders, clearly identified as placeholders.
- Photography art direction and a small representative image study may be planned separately from bulk migration.

## 9. Engineering discipline
- Inspect the repository before changing it.
- Do not assume a framework, package manager, database, CMS or host until selected and recorded.
- Prefer the simplest maintainable architecture that meets verified requirements.
- Avoid premature microservices and unnecessary dependencies.
- Preserve security, accessibility, semantic HTML and responsive behaviour.
- Keep work focused, reversible and reviewable.
- Add tests for meaningful behaviour.
- Never disable checks merely to obtain a green pipeline.
- Never claim a command, test, screenshot review, deployment or merge succeeded unless it actually happened.
- Review the complete diff before reporting completion.

## 10. Autonomous working and boundaries
Proceed independently with reversible, in-scope research, design exploration, documentation, routine refactoring, tests and implementation after the applicable milestone is authorized.

Do not ask for routine approval for ordinary component, spacing, documentation or test choices.

Owner authorization is required for:
- Paid services, subscriptions or infrastructure commitments.
- Production deployment where no approved protected pipeline exists.
- Destructive or irreversible operations.
- Production-data changes.
- Credential or security-sensitive access.
- Legal, financial or commercial-policy decisions.
- Changes to approved business commitments.

If one owner decision blocks a feature, isolate it and continue unrelated safe work.

## 11. Required completion report
For every meaningful task, report:
1. What was inspected.
2. What changed, with exact file paths.
3. Decisions made and assumptions.
4. Tests actually run and results.
5. Visual/browser evidence where relevant.
6. Remaining risks, blockers and owner decisions.
7. Documentation updated.
