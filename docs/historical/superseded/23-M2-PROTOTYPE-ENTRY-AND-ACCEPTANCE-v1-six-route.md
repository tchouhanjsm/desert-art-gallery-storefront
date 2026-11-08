**HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT.** This file is preserved for audit traceability only. All instructions, proposal choices, page/component guidance and links below are non-operative; they do not override the current eight-level authority hierarchy, D-014, or the active page/component inventories.

---

# 23 — M2 Prototype Entry and Acceptance Pack

**Status:** Prepared for execution; M2 has not started.  
**Depends on:** Owner approval of the visual direction and the remaining inputs below.  
**Authority:** This pack operationalizes the M2 entry gate in [15 — Reference-to-DAG Implementation Specification](15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md). It does not override that specification or the owner decision register.

> **No visual selection, no production-style prototype.** The four current territories remain proposals. This pack is a direction-neutral execution contract, not a wireframe, page design, production theme or approval to start M2.

## 1. Entry gate — all conditions must be recorded

| Gate | Required evidence | Status before M2 |
|---|---|---|
| M2-A — Visual identity | Owner explicitly selects one territory, combines named elements, or requests a revised set and then selects. Record exact approved foundations in `docs/DECISIONS.md`. | Open — no territory selected |
| M2-B — Japan-first customer-segment focus | Owner selects the initial segment hypothesis/hypotheses to research. Japan-first is already confirmed by D-003; method, recruitment route, consent and spending remain separate approvals. | Open — segment selection pending |
| M2-C — Mixed product/photo evidence | Use genuine owner-supplied DAG sample photos only after product identity, factual mapping, rights/permissions and prototype-use approval; use clearly labelled illustrative placeholders for missing views/states. | Open — real sample and image-level clearance pending |
| M2-D — Journey priority | Owner ranks the five customer journeys. Mobile/tablet/desktop are mandatory review dimensions of every journey, not separate journeys. | Open — priority pending |
| M2-E — Complete non-production prototype scope | Confirm six routes plus shared global header, navigation, search, footer and reusable presentation components. Keep all behaviour non-transactional. | Open — full shared-shell scope confirmation required |

A reference choice (D-010) is not a visual-identity choice. Do not treat the four P-016 proposals as selected, combine them on the owner's behalf, or use any historical rejected palette or type pairing as a fallback.

When M2-A is approved, record the exact selected colours, typography, visual personality, image treatment and any explicit combinations in the decision register before implementing tokens. Do not infer missing values from a proposal title or its preview.

### Owner decision capture

Use the blank [M2 Owner Entry Decision Record](../templates/prototypes/m2-owner-entry-decision.md) to capture the owner's M2-A through M2-E outcomes. It deliberately starts with every gate open and every choice unchecked. A completed worksheet is not, by itself, approval: transfer confirmed outcomes and exact evidence references into docs/DECISIONS.md and docs/OWNER-INPUT-REGISTER.md before changing a gate's authoritative status.

### Automated gate audit

Run `python3 scripts/audit_m2_readiness.py` to compare each M2-A through M2-E status across the owner-input register, this acceptance table and the worksheet outcome table. Aligned open gates are reported as **BLOCKED (expected)** and do not fail CI. Conflicting statuses, missing owner-input rows, or confirmed gates without a valid decision-register reference fail the audit. Even when every gate is confirmed, the report still requires separate owner authorization for the first route; it does not start M2.

## 2. First prototype route set

The first responsive prototype scope is limited to the six route areas below. This is a scope map, not a chosen navigation taxonomy or a decision about final URL paths.

| Route area | Customer task to evaluate | Required evidence in the prototype | Must remain absent unless verified/approved |
|---|---|---|---|
| Homepage | Understand what DAG offers and find a useful route into discovery. | Clear DAG identity; owner-approved introduction; paths to real approved collections or clearly labelled prototype placeholders; visible support route. | Invented product range, campaign claims, popularity, awards, stock or maker claims. |
| Shop / Category / Collection | Browse and understand the grouping; narrow choices only where useful. | Owner-approved category/collection labels; visible product identity and price only when verified; result/empty state; filters and sorting only where supported by real catalogue fields. | Invented taxonomy, result counts, filters, bestseller labels or availability. |
| Product detail | Understand a specific object and identify the facts that are present, missing or unclear. | Approved image sequence or clearly labelled placeholders; verified facts only; price/options/availability only when supplied and approved; maker/story links only when evidence supports them. | Guessed dimensions, materials, condition, origin, care, maker, provenance, review, price or inventory. |
| About / Makers | Understand DAG's verified identity and any approved maker context. | Owner-approved company description and individually verified maker facts/permissions. | Invented brand history, relationships, artisan names, techniques, social-impact or heritage claims. |
| Journal / Stories | Discover useful editorial context and return to a relevant route. | Approved article content, author/date only when verified, links only to relevant approved products or collections. | Fabricated articles, quotes, author identities or product relationships. |
| Contact / Support | Find a usable contact route and understand what happens after sending a message. | Owner-confirmed contact method; labelled form fields if a form is approved; clear validation, success and error states. | Invented contact details, response-time promises, support hours or privacy commitments. |


### Shared global shell — required on every route

The same shell is in scope on all six pages: a global announcement/status strip with no unapproved promise; DAG brand header/wordmark; responsive primary and category navigation including mobile menu state; search entry/disclosure (visual only, no live catalogue backend); and a global footer with Discover, About and Support groupings. Contact, policy, shipping and service details remain unconfigured until verified and owner-approved.

### Reusable presentation components

The six routes share a content container, title/heading hierarchy, breadcrumbs, section headings and dividers, focus/link/action patterns, category/collection tiles, product cards and factual state labels, filters/sort presentation and empty states, product gallery/thumbnails, product-fact rows, maker/material context modules, editorial/story cards, related-item cards, support/contact blocks and (only if separately approved) contact-form field and validation-state patterns. This is a design inventory only; it does not authorize a production component library or application.

### M2-C mixed image evidence rule

The approved evidence approach is mixed: use genuine DAG photographs supplied by the owner where the exact product/image identity, fact mapping, rights/permissions and prototype-use approval are confirmed; use visibly labelled illustrative placeholders where a real item, image angle or state is missing. Never present unrelated stock, generated art or remote Etsy images as genuine DAG photography. Do not invent product facts. No genuine sample photo was present in the checked-in repositories when this pack was prepared; M2-C stays open until 10–20 representative product/photo records and the relevant approvals are supplied. Keep original media and private rights evidence outside Git; no bulk photo migration or public publication is authorized.

### Cart and checkout boundary

Cart and checkout are not part of the first operational build. If a journey review requires them, show only a clearly labelled, non-transactional concept. No payment submission, order creation, tax/duty calculation, delivery promise, inventory reservation, returns promise or live customer-account action is permitted while the relevant commercial decisions remain unresolved (U-001–U-008).


### M2-B — Initial Japan-first customer segment hypotheses

Japan-first is already established by D-003. The owner decision here is only which contexts to include in the initial discovery focus. These are hypotheses, not validated personas, market-size segments or claims about Japanese shoppers; they can overlap.

| Segment hypothesis | Recent shopping context | Research questions to explore |
|---|---|---|
| Home and interior buyers | Researched or bought textiles, furnishings or objects for their home or a space they are shaping. | Scale, colour, texture, use, care, visual fit and image completeness. |
| Craft and material enthusiasts | Sought objects for material, construction, craft practice, cultural context or documented provenance. | Which material/process facts matter and what evidence supports them. |
| Gift and considered-purchase buyers | Selected a considered object/textile for another person, an occasion or a meaningful purchase. | Suitability, presentation, seller confidence and information needed before deciding. |
| Trade and design professionals | Specified or sourced objects/textiles for interior, hospitality, styling or professional projects. | Dimensions, specifications, quantity/repeatability and enquiry needs. |

The owner may select one or more without ranking. Segment choice does not authorize a research method, sample size, recruitment provider, consent/recording, incentives or spending. Those remain separate approvals; no recruitment or expenditure is authorized by M2-B selection alone.

## 3. Journey scenarios

Use these task scenarios to assess comprehension and navigation once the owner confirms their priority. They are not claims about validated customer behaviour.

1. **Discover:** From the homepage, explain what DAG offers and choose a route into the catalogue.
2. **Browse:** Enter an approved category/collection and explain what items belong there.
3. **Evaluate:** Open a product and identify the facts that are present, missing or unclear.
4. **Contextualize:** Find a related approved maker/story article, then return to the product or collection.
5. **Get support:** Find the confirmed contact route and explain what the next step communicates.
**Mobile is a required test dimension across every selected journey, not a separate journey.** Review each selected task on mobile (390 px and 430 px), tablet (768 px) and desktop (1280 px and 1440 px); desktop-only evidence cannot pass a journey.

Do not ask participants to validate the owner's visual identity choice. Do not run Stage B usability sessions until the approved prototype and the playbook's entry conditions are satisfied.

## 4. Responsive review matrix

Review each in-scope route at all five widths specified in [09 — Quality and Acceptance](09-QUALITY-AND-ACCEPTANCE.md):

| Viewport width | Review intent |
|---:|---|
| 390 px | Narrow mobile layout and touch interactions |
| 430 px | Larger mobile layout and text wrapping |
| 768 px | Tablet reflow and navigation behaviour |
| 1280 px | Desktop navigation and catalogue density |
| 1440 px | Wide desktop content measure and image balance |

These are validation widths, not fixed CSS breakpoints. Determine breakpoints from content behaviour after the approved design is implemented. At every width record the route, viewport, date, reviewer role, observed result and evidence reference in the blank [prototype review template](../templates/prototypes/prototype-review.csv).

## 5. Shared acceptance checklist

A route is reviewable only when the relevant criteria below can be demonstrated.

### Content integrity
- All customer-facing content is English-only.
- Product, maker, material, provenance, dimensions, condition, price, stock and care facts are verified or visibly labelled as placeholders.
- Image rights/publication state is respected; no Etsy remote image URL is treated as a local, rights-cleared product asset.
- No customer-facing delivery, tax, duties, payments, returns, refund, cancellation or legal promise is invented.
- Placeholder copy cannot be mistaken for a real product or operating business commitment.

### Information architecture and interaction
- Each page has one clear primary customer task and a visible route to the next useful step.
- Navigation works without hover and remains operable by keyboard and touch.
- Links navigate; buttons perform actions. No inert control is styled or described as functional.
- Search, sort, filters, variants and quantity controls appear only if they are in the approved prototype scope and have a defined data contract.
- Empty, loading, error, disabled, selected and success states are represented where the interaction requires them.
- Drawers/dialogs support close controls, Escape where appropriate, and focus return.

### Accessibility and responsive behaviour
- Semantic landmarks and a logical heading hierarchy are present.
- Controls have labels and accessible names; keyboard order and visible focus are usable.
- Text and interactive states meet the approved WCAG 2.2 AA target, with exceptions documented rather than hidden.
- Motion respects `prefers-reduced-motion`.
- Touch targets and spacing remain usable.
- No horizontal page overflow; content, images and controls reflow without overlap.
- Sticky elements do not cover essential content or actions.
- Images have meaningful alternative text, or empty alt when purely decorative.

### Review evidence
- Capture the full relevant route, not only the hero or first viewport.
- A screenshot proves capture only; record a separate visual-review result.
- Log each failed criterion with severity, route, viewport, reproducible steps and an issue reference.
- Retest fixed issues at the affected width and one adjacent width.
- Do not claim owner acceptance until the owner has reviewed and accepted the rendered prototype.

## 6. Required handoff for each route

The implementation/review package for each route must include:

1. Route purpose and prioritized customer task.
2. Content/data inventory with verified, placeholder and owner-input states separated.
3. Component inventory mapped to the approved component contracts in document 15.
4. Interaction and state inventory.
5. Responsive captures at the five required widths.
6. Keyboard, focus, contrast, reduced-motion and semantic review notes.
7. Open issue list and retest evidence.
8. Explicit owner review outcome: pending, changes requested or accepted.

Do not mark a route complete merely because markup exists or screenshots were captured.

## 7. Prototype review record template

The CSV under `templates/prototypes/` is intentionally header-only. Use neutral reviewer roles and issue references; do not add participant names, email addresses, phone numbers, addresses, recordings or identifiable research notes to this repository. Participant evidence belongs in the private research workflow under document 22.

## 8. Out of scope for this pack

- Any visual-territory selection or production token creation.
- A wireframe or rendered page prototype.
- Production framework, runtime, build tool, CMS, database or hosting choice.
- Real product import, photo migration or image hosting.
- Live search, account, wishlist, cart, checkout, payment or order operations.
- Commercial/legal policy authoring.
- Participant recruitment, research spending or Stage B sessions.

**Exit condition:** M2 begins only when all applicable entry gates in section 1 are recorded and the owner authorizes the first route scope. Until then, this pack is prepared, not executed.
