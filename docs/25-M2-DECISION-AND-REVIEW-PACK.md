# M2 — Combined Owner Decision and Structural Review Pack

**Review date:** 8 November 2026  
**Governing decision:** D-014 (structural kit only)  
**Bounded review authorization:** D-015  
**Purpose:** Bring M2-A through M2-E into one coordinated decision, evidence and acceptance package without inventing owner choices or source assets.

## Executive disposition

M2 can progress substantially in one coordinated engineering pass, but not every gate can honestly be closed by an AI or code change. M2-A requires the owner's actual identity values; M2-C requires the owner's original catalogue/photo sample and rights evidence. This package prepares both workflows and closes the engineering work that does not depend on those inputs.

| Gate | Work delivered in this pass | Honest state |
|---|---|---|
| M2-A — Brand identity | Audited exact required owner inputs and linked the controlled token register. | **Blocked on owner-supplied identity** |
| M2-B — Customer segment and research | Reviewed market context; proposed an initial qualitative cohort and study focus. | **Recommendation ready; owner adoption and fieldwork authorization pending** |
| M2-C — Product/photo evidence | Extended private intake fields and added a strict 10–20 product sample validator with rights, photo-audit and separate prototype-use checks. | **Evidence workflow ready; sample absent** |
| M2-D — Responsive journey coverage | Defined five journeys and added 25 automated journey/viewport checks on top of the 45 route/viewport and existing 54 keyboard checks. | **Automation implemented; final-head CI passed; owner priority/human acceptance pending** |
| M2-E — Next-phase authorization | Recorded D-015 for a precise non-production review scope. | **Authorized for bounded structural review only** |

There is no claim that a branded customer prototype has been accepted, research participants recruited, product-market fit established, catalogue facts validated or any production feature launched.

## M2-A — Brand identity (owner-controlled)

The D-014 kit is a structural source, not a brand system. These inputs remain blank until the owner supplies or explicitly approves them:

- Primary, secondary/supporting, surface, text/contrast and accent colours (exact HEX values and intended roles).
- Display/heading, body and UI typefaces, exact families/weights and licensing/availability.
- Typography hierarchy, type scale and responsive behaviour.
- Original logo/wordmark artwork and approved descriptor.
- Photography art direction, image roles and crop/composition rules.

**No default is selected.** Do not reuse P-015's rejected territories, P-016's historical proposals, the system-token QA fallback or palette/type remembered from another/legacy project. The active field sheet is OWNER-TOKEN-INPUT.md.

**Disposition:** M2-A is blocked on the owner providing exact values/assets and recording approval in DECISIONS.md. No final branded styling is authorized until then.

## M2-B — Customer segment and Japan-first research

### Recommendation

Start with a small qualitative cohort centred on **home/interior shoppers in Japan who have recently considered textiles, handmade objects or material-led décor**. Include **craft/material enthusiasts** as a second, closely related context. Include one or two contrast perspectives from a **trade/design professional** and a **gift/considered-purchase shopper**.

A proposed first round of seven participants, within the existing five-to-eight range in 22-CUSTOMER-VALIDATION-PLAYBOOK.md, is:

| Research context | Proposed count | Why include it |
|---|---:|---|
| Home/interior purchase context with textile/decor interest | 3 | Closest exploratory match to the current broad product/curation hypothesis; tests room/use context, scale, material and styling information needs. |
| Craft/material enthusiast | 2 | Tests whether material, making, condition and provenance evidence changes discovery and confidence. |
| Trade/styling/design professional | 1 | Contrast case for specification, sourcing, repeatability and professional enquiry needs. |
| Gift/considered-purchase shopper | 1 | Tests gifting motivation and what service information would be needed without assuming packaging or gift services exist. |

These are **research contexts, not validated personas**; one participant may overlap categories. Do not infer market size, willingness to pay, conversion or segment profitability from this sample. Ask about recent actual shopping behaviour, not hypothetical "would you buy?" intent.

### Market evidence and limitations

- Japan's Ministry of Economy, Trade and Industry reported that the 2024 domestic B2C e-commerce market reached **¥26.1 trillion**, up **5.1%** year over year; B2B e-commerce reached **¥514.4 trillion**, up **10.6%**. This establishes a substantial and growing online commerce context, not demand for DAG or for any specific textile/craft segment. Source: METI, *Results of FY2024 E-Commerce Market Survey Compiled*, 26 August 2025 — https://www.meti.go.jp/english/press/2025/0826_003.html
- Japan's National Consumer Affairs Center reported **9,127 cross-border consumer consultations in FY2025**, versus 6,005 in FY2024; 98.6% related to online transactions. Its report is a count of consultations/complaints, not a measure of all cross-border purchases or the risk rate for craft products. The largest issue categories include cancellations and service-related cases, so the prudent DAG implication is to make seller identity, cancellation/returns, delivery and customer-support commitments clear once the owner approves them—not to claim that Japanese consumers avoid overseas shops. Source: NCAC, 5 August 2026 — https://www.kokusen.go.jp/news/data/n-20260805_2.html
- Japan's Statistics Bureau's 2025 Household Consumption Status Survey summary identifies record-high online-shopping household participation and expenditure. The published page links the detailed PDF; no additional percentages are asserted here. Source: Statistics Bureau of Japan, *2025 Annual Report — Overview*, https://www.stat.go.jp/data/joukyou/2025ar/gaikyou/index.html

No public source located in this review validates DAG's four proposed customer contexts. The recommended cohort is a product-fit hypothesis grounded in DAG's intended Jaisalmer-rooted textile/object range, to be tested through first-party interviews.

### Research execution boundary

- Proposed discovery method: 5–8 moderated interviews, 30–45 minutes each, using the existing neutral guide.
- No recruitment, incentives, participant spending, recording, personal-data collection or outreach is authorized by this recommendation.
- Owner must confirm cohort, recruitment route/provider, moderator, consent/recording process, private storage/retention and any incentive/spending before fieldwork.
- Stage B prototype usability sessions remain dependent on M2-A, M2-C and explicit prototype scope acceptance.

**Disposition:** M2-B research recommendation is prepared. U-007 remains open until the owner adopts or changes the proposed cohort. No fieldwork is claimed.

## M2-C — Product and photography evidence

The repository/library inputs available for this review contain the owner-supplied structural kit archive and generated browser-review evidence, but no original 10–20 product/photo sample or current Etsy listing export. Browser screenshots and unrelated image files are not catalogue evidence and must not be repurposed.

The private sample remains 10–20 distinct real DAG products, with:

1. Stable owner-reviewed product identity mapped to a source-export row with reconciliation_status=owner_reconciled.
2. Only factual fields supported by an evidence reference; unknown values left blank.
3. Original photos mapped to the correct products and roles, with image identity checked by visual review.
4. A completed private photo-audit report; unreadable and byte-identical duplicates cannot pass as approved sample images.
5. Rights clearance evidence for each image.
6. Separate explicit permission to use each product, fact and image in the named private prototype/review.
7. Product/publication status remains draft/in-review; prototype-use approval does not grant public publication permission.

The updated CSV templates add prototype_use_approval and prototype_use_evidence_reference for product/fact/image records, plus rights_evidence_reference for both local product images and Etsy source-image references marked rights-cleared. The sample validator also requires an owner-reconciled product-source-records.csv mapping for each sample product. The command scripts/validate_catalogue_intake.py --m2-sample enforces a complete 10–20-product evidence set when paired with the same complete photo-audit CSV/JSON output. Its regression tests include valid/invalid sample size, missing approval, missing rights evidence, dirty/duplicate photo-audit records and attempted public publication.

All sample records, raw exports, photo audits and actual photo binaries must remain outside Git and outside public/shared workspaces. This validation is structural: it cannot prove a rights claim or product fact is true.

**Disposition:** M2-C workflow is ready; the actual source evidence is missing. Keep the gate open.

## M2-D — Journey order and responsive acceptance

### Recommended journey order

1. **Discover:** Home → Shop → Collection. Does the shopper understand the route from the initial entry point into a category?
2. **Browse:** Shop → Collection → Product. Can the shopper move from category to a product detail page using the kit's supplied links?
3. **Evaluate:** Product. Can the shopper inspect the four supplied information accordions and understand which facts remain pending? Confirm option and purchase controls remain disabled.
4. **Contextualise:** About → Makers → Journal → Article. Can a shopper move through brand/maker/editorial context without inventing a maker or product claim?
5. **Seek support:** Product → Enquire → Contact. Confirm the enquiry destination exists while contact fields/submission remain disabled and no unapproved service promise is shown.

This order follows increasing information depth: entry/discovery, item finding, decision support, context/trust and service contact. It is a delivery/review order, not a claim about validated customer behaviour.

### Responsive matrix

Every selected journey must be exercised at **390, 430, 768, 1280 and 1440 CSS pixels**. Mobile is cross-cutting, not a standalone journey (D-012).

The final-head Chromium workflow [run #15](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483140888) passed and uploaded 18 full-page screenshots plus JSON/Markdown summaries; the artifact is available [here](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483140888/artifacts/13617964823). The accompanying Project Quality [run #88](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483140897) passed all repository audits and **101/101 Python tests**.

The automated matrix is:
- Nine supplied routes × five widths = **45/45** route/viewport checks.
- Five journeys × five widths = **25/25** journey/viewport checks.
- Existing nine-page Enter/Space mobile-navigation and focus-retention checks = **54** sequences.
- Reduced-motion, document overflow, asset loading, page errors and disabled-control checks all passed.

The automation runs against the local static kit in CI. It does not recruit participants, conduct usability interviews, approve copy or replace human visual/accessibility review.

**Disposition:** The recommended journey sequence and automation are implemented and automated CI acceptance passed. Owner priority confirmation and real-user acceptance remain pending.

## M2-E — Bounded authorization and acceptance

The 8 November 2026 owner instruction to "achieve all the M2 (A-E) in one go" is recorded in D-015 as authorization for this exact, bounded repository-side review:

- Use only the current D-014 nine-page structure and existing routes/links/controls.
- Add non-production review automation and private-sample validation tooling.
- Exercise five defined journeys at the five existing review widths.
- Preserve disabled controls and all source-kit UI assets.
- Report machine results and failures; do not represent automated QA as owner/user approval.

It does **not** authorize:
- Final branded identity, token selection or branded styling.
- New pages, sections, components, navigation or feature behaviour.
- Live search/filter/sort, variants, purchase, cart, checkout, payments, orders, stock, shipping, returns or enquiry submission.
- Public or customer-facing publication of product data/photos.
- External user recruitment, incentives, spending, research recording or personal-data collection.
- Production technology selection, hosting, application development or public deployment.

**Disposition:** M2-E is authorized for the bounded structural review. Final branded prototype approval and any production phase remain separate owner decisions.

## Remaining owner handoff

To close the remaining owner-dependent M2 gates, supply or explicitly decide:

1. **M2-A:** Exact brand-token values and artwork/direction, or state explicitly that branded prototype review should remain deferred.
2. **M2-B:** Accept/change the proposed first cohort; then separately authorize the recruitment/consent/recording/cost plan before fieldwork.
3. **M2-C:** Supply 10–20 product records and original mapped photos privately, together with rights and prototype-use evidence.
4. **M2-D:** Accept/change the proposed five-journey priority order; then decide whether/when human usability sessions should occur.
5. **M2-E:** D-015 already authorizes the bounded structural review only. Any broader prototype or production scope needs a new explicit decision.

Until M2-A and M2-C are satisfied, do not claim a complete branded, genuine-product customer prototype. Do not make production or commercial commitments from this review.

