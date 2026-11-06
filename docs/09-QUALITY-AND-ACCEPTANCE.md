# 09 — Quality and Acceptance

## Product/design quality
- Customers understand what DAG offers.
- Product discovery is prominent and useful.
- Every section has a purpose.
- Whitespace is intentional.
- Product facts are truthful and legible.
- Desktop and mobile are deliberately composed.
- The experience is distinct to DAG, not a clone or generic template.
- Customer-facing content is English-only.

## Visual review
At minimum review 390px, 430px, 768px, 1280px and 1440px.
Review full rendered pages, not just the first viewport:
- Homepage.
- Shop and category.
- Product detail.
- About, Makers and Journal.
- Contact/support.
- Cart and checkout when implemented.

Record route, viewport and date for screenshots. A screenshot capture does not prove it was visually inspected.

## Owner-controlled visual decision gate

**THE AI PROPOSES. THE OWNER CHOOSES. THE AI IMPLEMENTS.**

Before final visual identity or production styling:
- Present at least four genuinely distinct territories, not four neutral variations.
- Provide exact HEX values/roles, font families/weights and licensing caveats, layout/component rules, photography direction and contrast notes for each.
- Provide rendered desktop and mobile examples for every option.
- State neutral trade-offs; do not recommend, rank, score, select, badge or imply a default winner.
- Ask the owner to choose one, combine specified elements, request revisions or reject all.
- Stop. No final tokens, theme defaults, production CSS/design system or application styling until the explicit owner choice is recorded in `DECISIONS.md`.

The prior Material Archive / Collected Colour proposal is historical only and must not be resumed as a default. See [14 — Owner-Controlled Visual Direction](14-OWNER-CONTROLLED-VISUAL-DIRECTION.md).

## Accessibility
Target WCAG 2.2 AA where applicable. Test keyboard access, visible focus, semantic structure, form labels, accessible names, contrast, reduced motion and responsive touch targets.

## Performance and SEO
Set measurable Core Web Vitals budgets after selecting the stack and realistic media strategy. Validate metadata, canonical URLs, sitemap, robots rules and product structured data only when accurate catalogue information exists.

## Functional quality
Test navigation, links, search, filters, variants, cart, forms, validation, loading/empty/error/success states and critical customer journeys.

## Engineering quality
Run the chosen stack's actual formatting, lint, type-check, unit/integration, build and browser tests. Do not invent scripts or claim unrun tests passed.

## Content integrity
No unverified prices, reviews, stock, maker claims, business details, delivery promises, legal/tax claims or fabricated product content.

## Definition of done
A task is complete only when acceptance criteria are met, affected routes/states are checked, tests are run, changes are reviewed, docs are updated and remaining limitations are disclosed.

## Creative-direction acceptance gate

Before production UI implementation, verify:
- At least four materially distinct visual directions were shown.
- Options are not all beige, grey, ivory or muted earth palettes.
- Exact palette values and typography were provided for each.
- Actual rendered examples were provided for desktop and mobile.
- The owner explicitly selected or combined a direction.
- The selected direction is recorded in `DECISIONS.md`.
- Production tokens reflect only the owner's selection.

If any condition is missing, the visual identity is not approved and production design-system implementation must not proceed.
