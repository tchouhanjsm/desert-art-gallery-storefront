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
Status: SUPERSEDED IN PART BY D-014
Decision: The owner alone controls and approves DAG's final palette, typography, visual personality and photography art direction. The former process instruction requiring the AI to generate at least four rendered alternatives is superseded: D-014 adopts the owner-supplied structural kit and does not commission a new AI-generated direction exercise. The owner must provide or explicitly approve all foundational identity values before branded styling. No historical palette or type pairing may be used as a default.
Consequences: Record exact owner-provided values in `docs/OWNER-TOKEN-INPUT.md` and this decision register. The principle of exclusive owner approval remains active; the old multi-option process does not.
Date: 2026-11-06; process superseded 2026-11-07

### D-008 — Reject the four proposed visual territories
Status: CONFIRMED
Decision: The owner explicitly rejected all four territories in P-015 on 6 November 2026: Graphic Atelier, Future Relics, Living Garden and Modern Folk Pop. None is selected, preferred, approved, a default or an active candidate. The full P-015 package is retained as historical evidence only.
Owner instruction: "My DAG visual direction decision: reject."
Consequences: P-015 is archived as rejected historical evidence. D-014 defines the current structural source; do not revive P-015 concepts, palettes or font pairings.
Date: 2026-11-06

### D-009 — POJ Studio and Macaroni Shoten as principal design references
Status: CONFIRMED
Decision: The owner names https://pojstudio.com/ and https://shop.macaro-ni.jp/ as the principal references for the next DAG creative and retail design study and asks whether DAG can be designed exactly like them. Use both as close references for customer experience, editorial retail quality, product discovery, merchandising and information hierarchy. The DAG deliverable must remain original: do not clone either site's identity, source assets, copy, product imagery or pixel-for-pixel page composition. This reference instruction does not select a final DAG palette, typography, art direction or page layout.
Owner instruction: "shop.macaro-ni.jp/ and pojstudio.com - can we design exactly as it it."
Consequences: D-010 records the confirmed reference hierarchy. This reference decision does not authorize new features or visual identity selection. D-014 and the current inventories govern structure.
Date: 2026-11-06

### D-010 — Reference fidelity and hierarchy
Status: CONFIRMED
Decision: DAG's reference fidelity is BLEND. POJ Studio is the primary reference for overall ecommerce architecture, global navigation, homepage composition, Shop/collection discovery, product cards, product detail, maker/story and supporting retail experience. Macaroni Shoten is the secondary reference for select-shop curation, category grouping, lifestyle-oriented selection and concise editorial retail character. DAG must remain an original Jaisalmer-rooted brand with its own products, content, imagery, taxonomy and English-only customer-facing experience.
Owner instruction (7 November 2026): "Reference fidelity: BLEND. Primary reference: POJ Studio. Secondary reference: Macaroni Shoten."
Boundaries: This decision confirms the reference relationship only. It does not approve a DAG colour palette, font pairing, visual personality, photography art direction, final layout, category taxonomy, commerce model, technology stack or any POJ/Macaroni feature that DAG does not actually offer. Do not clone source code, proprietary CSS, exact composition, copy, products, photography or brand identity.
Consequences: Use `docs/REFERENCE-RESEARCH-LOG.md` for dated observations. D-014 and the active `docs/PAGE-INVENTORY.md` / `docs/COMPONENT-INVENTORY.md` govern DAG's current structure. Owner-only identity approval remains active; the former AI-generated option procedure in D-007 is superseded.
Date: 2026-11-07

### D-011 — Mixed genuine-photograph and labelled-placeholder evidence approach
Status: CONFIRMED
Decision: The owner directs the future M2 visual/customer-experience prototype to use a mixed image-evidence approach: genuine DAG sample photographs where product/image identity, factual mapping, rights/permissions and prototype-use approval are verified; explicitly labelled illustrative placeholders for missing product images, additional views or visual states.
Boundaries: This confirms the evidence approach only. It does not mean a real image sample has been supplied or cleared. M2-C remains open until the representative sample is supplied and approved. No unrelated stock imagery, generated art or remote Etsy image is to be represented as a genuine DAG product photograph. No bulk migration, public publication or photo binary commit is authorized.
Date: 2026-11-07

### D-012 — Mobile is a cross-journey acceptance dimension
Status: CONFIRMED
Decision: Mobile testing is required across every selected customer journey; mobile recovery is not a separate journey. Journey acceptance must not be granted on desktop-only evidence. Review mobile widths alongside the tablet and desktop viewport matrix.
Boundaries: This sets the responsive testing rule only. It does not prioritize or select any of the five candidate customer journeys; M2-D remains open for the owner's journey order.
Date: 2026-11-07

### D-013 — Six-route prototype scope
Status: SUPERSEDED BY D-014
Decision: The earlier six-route non-production prototype scope and its shared-shell assumptions are superseded by the owner-supplied nine-page structural kit in D-014.
Boundaries: This historical decision is retained for audit context only. It does not define current routes, sections or components.
Date: 2026-11-07

### D-014 — Owner-controlled Design Kit v2 is the structural source
Status: CONFIRMED — STRUCTURAL SCOPE ONLY
Decision: Adopt the owner-supplied DAG Owner-Controlled Design Kit v2 as the sole active structural HTML/CSS source. Its exact nine HTML pages, CSS files, responsive styles, supplied prototype script, page order, sections and component inventory define the closed structural scope.
Boundaries: This does not approve final brand colours, typography, type hierarchy/scale, logo, wordmark, descriptor, photography direction/cropping, final customer-facing copy, product facts or production application behaviour. `tokens-layout-only.css` is system/browser QA fallback only, not a DAG palette or production theme. Preserve supplied markup, styles, responsive rules, component structure, placeholders and disabled controls. Do not add pages, sections, shell items, features or functionality. Production application development, commerce behaviour, technical stack selection, public deployment and owner-only business/legal decisions remain unauthorised.
Consequences: The active page and component inventories are `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`. The former six-page M2 scope is superseded. Brand token inputs remain pending. Japan-first remains distinct from customer-facing language; the storefront remains English-only.
Date: 2026-11-07

### D-015 — Bounded M2 structural journey-review authorization
Status: CONFIRMED — LIMITED NON-PRODUCTION REVIEW SCOPE
Owner instruction (8 November 2026): "Achieve all the M2 (A-E) in one go."
Decision recorded for execution: authorize a bounded M2 structural journey-review implementation using only the nine pages and existing components, links and disabled states in D-014, with automated Chromium route and journey checks at the five established review widths. The acceptance scope is recorded in docs/25-M2-DECISION-AND-REVIEW-PACK.md.
Boundaries: This authorization covers repository-side review tooling, private non-production structural journey checks and evidence reporting only. It does not approve or invent brand values, logo/wordmark, final copy, product facts, catalogue taxonomy, image rights, public photo publication, public or participant research, recruitment, incentives/spending, new pages/sections/components, new interaction behaviour, commerce features, production app development, technology/hosting selection or public deployment. Search, filters/sort, product options, purchase and contact submission remain disabled.
Consequences: M2-E is authorized for the exact bounded review scope. M2-A and M2-C remain blocked on owner-controlled inputs/evidence; M2-B and M2-D have recommendations and automation prepared but owner adoption and any external research remain outstanding. No supplied kit HTML/CSS/JS asset is changed by this authorization.
Date: 2026-11-08


### D-016 — Owner authorization for M2 visual proposal, research preparation and private prototypes
Status: CONFIRMED — PROPOSAL REVIEW AND CONDITIONAL PRIVATE-PROTOTYPE AUTHORIZATION
Owner instruction (8 November 2026): the owner confirms the M2-A reference hierarchy, adopts the seven-person qualitative research cohort, approves the mixed placeholder/image-frame approach, approves the five customer-journey priorities, and authorizes private non-transactional prototypes for six named areas.

M2-A — Visual direction:
- POJ Studio is the primary reference for overall website/ecommerce composition, navigation, product grids, product detail and customer experience. Macaroni Shoten is secondary for curation, category grouping and editorial retail character. Jaisalmer remains DAG's source of identity.
- Prepare one coherent, evidence-led visual proposal with exact proposed HEX roles, reference typography observations, proposed typefaces/weights/hierarchy, logo/wordmark requirements, header, homepage, shop/grid, PDP, photography treatment, CSS tokens/components and desktop/mobile examples.
- The four rejected P-015 territories remain rejected. Do not create another arbitrary palette set or reuse historic directions.
- Every colour/type/logo/descriptor/photo value in the proposal is a proposal only. The owner retains final approval. No production token, theme or branded prototype may be finalized or applied before explicit owner visual approval.

M2-B — Initial customer-validation cohort:
- The initial Japan-based qualitative cohort is accepted as a research plan: 3 home/interior shoppers interested in textiles or décor; 2 craft/material enthusiasts; 1 trade/design professional; 1 gift or considered-purchase shopper.
- These are research contexts and hypotheses, not validated personas or a representative sample.
- Prepare eligibility, objectives, interview questions, recruitment options, consent/privacy workflow and indicative cost ranges.
- This decision does not authorize recruitment, external contact, participant-data collection, recording, participant incentives or any spend. Those require a separate explicit authorization.

M2-C — Product and image evidence:
- Use clearly labelled illustrative layout placeholders and image-frame compositions to demonstrate intended ratios and gallery structure.
- Do not invent catalogue products, use generated artwork as DAG product photography, or represent placeholders as genuine products.
- Product-image validation remains pending until the owner supplies approximately 10–20 genuine product photographs and associated verified product information.
- Prepare intake and fact-verification only. No full photography-library migration is authorized.

M2-D — Customer-journey priority:
1. Discover Desert Art Gallery and understand its identity.
2. Browse products, categories and collections.
3. Evaluate a product, its images and verified specifications.
4. Explore makers, materials and editorial stories.
5. Contact the gallery and obtain useful information.
Mobile responsiveness and usability are cross-cutting acceptance requirements for every journey, not a sixth journey. Automated testing does not equal human usability acceptance.

M2-E — Private prototype authorization:
Authorize private/local, non-transactional HTML/CSS prototypes for exactly these six areas:
1. Homepage.
2. Shop and Collections.
3. Product Detail.
4. About and Makers.
5. Journal and Stories.
6. Contact and Support.
The global header, navigation, search presentation, shared components and footer are included only where already relevant to those areas. The six areas are review groupings over the unchanged nine-page D-014 structural inventory; they do not add or remove routes, sections or components.

This authorization is conditional: branded prototype implementation may begin only after the owner explicitly approves the M2-A visual proposal. The prototypes must remain local/private and outside the public repository. Existing non-transactional concept states may be shown only if needed to explain the journey; cart/checkout concepts must never imply live purchases or commercial commitments.

Explicit exclusions remain: production application development; live payments/orders; real shipping or tax calculations; external participant recruitment; public deployment; paid services/subscriptions; migration of the full product-photography library; new pages, sections, widgets, promotional content or unapproved interactions; and unapproved changes to identity or commercial model. No technology, seller jurisdiction, currency, fulfilment, tax, payment or returns policy is approved by D-016.

Relationship to D-015: D-015 records the earlier limited structural journey-review authorization and its completed automation. D-016 adds the owner's later, more specific M2 decision and conditionally authorizes six private non-transactional prototype areas after visual approval. D-015 remains valid historical authority for the completed structural review; it is not the ceiling for the newly authorized private prototype phase.

Consequences:
- M2-B cohort and M2-D journey order are owner-approved as plans/priorities; neither is evidence of demand or human usability acceptance.
- M2-A remains awaiting explicit visual approval; the proposal itself is not approved identity.
- M2-C remains pending actual owner-supplied sample and evidence.
- M2-E private prototypes are authorized only after M2-A visual approval, with the exact six-area and non-production boundaries above.
Date: 2026-11-08

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
Status: SUPERSEDED — HISTORICAL ONLY

Basis: D-009 and the former reference-led design study.

Proposal package delivered before the owner supplied the v2 structural kit: Porcelain Index, Bordeaux Editions, Blue Current and Citron Signal, with palette, typography, layout and photography proposals. The complete original board and specifications are preserved under `docs/historical/visual-proposals/` and `docs/historical/superseded/` for audit only.

Disposition: These are not approved options, current candidates, defaults or implementation instructions. Do not revive, rank, blend or reuse their values. D-014 is structural adoption only; the owner still controls all final identity inputs. The former request for an AI-generated option selection process is superseded by D-014 and D-007's updated status.

Date: 2026-11-06

The former Material Archive / Collected Colour synthesis remains a historical AI proposal only. It is not a default, preferred direction or owner approval. Do not implement it unless the owner explicitly selects its elements in a new recorded decision.
