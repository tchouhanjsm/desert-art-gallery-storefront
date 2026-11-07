# Desert Art Gallery

Desert Art Gallery (DAG) is a premium, product-led ecommerce and gallery experience rooted in Jaisalmer, Rajasthan, with a Japan-first customer focus and an English-only customer-facing storefront.

## Current stage
**M1 — Reference hierarchy and page specification delivered; visual identity and customer-validation gates remain open.**

The owner confirmed a BLEND reference hierarchy: POJ Studio leads the ecommerce structure and page experience; Macaroni Shoten informs curation and select-retail character (D-010). A complete page-by-page implementation specification and updated live reference research are available. The four DAG-specific visual proposals remain unselected. No final palette, typography, art direction or production theme has been approved.

## Start here
1. [Permanent agent instructions](AGENTS.md).
2. [Project Charter](docs/00-PROJECT-CHARTER.md).
3. [Reference-to-DAG implementation specification](docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md).
4. [Dated reference research log](docs/REFERENCE-RESEARCH-LOG.md).
5. [Reference-led design brief](docs/17-REFERENCE-LED-DESIGN-BRIEF.md).
6. [Fresh visual territory specifications](docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md).
7. [Rendered desktop/mobile comparison board](design/explorations/reference-led-directions.html).
8. [Creative Direction](docs/03-CREATIVE-DIRECTION.md).
9. [Visual Design System](docs/04-VISUAL-DESIGN-SYSTEM.md).
10. [Owner-Controlled Visual Direction](docs/14-OWNER-CONTROLLED-VISUAL-DIRECTION.md).
11. [Decision Register](docs/DECISIONS.md).

## New owner-review package

These are four new, non-ranked proposals. None is recommended, preselected or approved.

| Proposal | Visual character |
|---|---|
| Porcelain Index | Material-first gallery catalogue |
| Bordeaux Editions | Atmospheric, chapter-led collector's journal |
| Blue Current | Contemporary studio catalogue |
| Citron Signal | High-contrast graphic object index |

- [Compare all four desktop/mobile previews](design/explorations/reference-led-directions.html)
- [Read exact HEX palettes, typography, layouts, photography, contrast and trade-offs](docs/18-REFERENCE-LED-DIRECTION-SPECIFICATIONS.md)

All object visuals and product names shown on the board are abstract placeholders, not real DAG catalogue content or photographs.

## Rejected historical visual proposals

Graphic Atelier, Future Relics, Living Garden and Modern Folk Pop were explicitly rejected by the owner on 6 November 2026 (D-008). Their comparison board and specifications remain as historical audit evidence only:
- [Archived comparison board](design/explorations/visual-directions.html)
- [Rejected specifications](docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md)

Do not treat any rejected palette, font pairing or preview as an active preference or approved direction.

## Photo library preparation

A read-only photo audit utility is available for the future 10–20 image sample or, later, the full original photo folder. It reports dimensions, formats, file sizes and byte-identical duplicates without modifying source media. Existing report files are never overwritten, and incomplete directory scans are explicitly flagged. See [19 — Non-Destructive Photo Library Audit](docs/19-PHOTO-LIBRARY-AUDIT.md). It does not migrate, optimize or publish images.

## Owner-confirmed reference hierarchy (D-010)

**Reference fidelity: BLEND.**

- **POJ Studio — primary:** overall ecommerce structure, navigation, homepage, Shop/collection, product cards, product detail, maker/story and supporting retail experience.
- **Macaroni Shoten — secondary:** select-shop curation, category grouping, lifestyle-oriented product selection and concise editorial retail character.

The full page-by-page implementation specification is in [15 — Reference-to-DAG Implementation Specification](docs/15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md). This is not permission to clone either reference and does not approve DAG's final palette, typography or visual identity.

## Principal design references

- [POJ Studio](https://pojstudio.com/)
- [Macaroni Shoten](https://shop.macaro-ni.jp/)

DAG adapts retail and customer-experience principles without cloning either brand, layout, copy, products, photography or proprietary assets. The storefront must express its own Jaisalmer identity.

## Permanent principle

**DO NOT ABANDON MINIMALISM. ABANDON EMPTINESS.**

## Market and operational note

Japan-first is the intended customer focus. English-only is the customer-facing language requirement. Exact sales territories, seller jurisdiction, currency, tax, duties, shipping, payment, returns and legal disclosures must be confirmed before implementation.

## Visual decision authority

**THE AI PROPOSES. THE OWNER CHOOSES. THE AI IMPLEMENTS.** No final palette, fonts, visual personality, photography art direction or production theme may be implemented before the owner's explicit selection is recorded in docs/DECISIONS.md.


## Catalogue intake preparation

A source-neutral draft intake standard and local CSV validator are available for future product-data preparation. The templates are blank and are not a production schema or approved taxonomy.

- [Catalogue intake and fact-verification standard](docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md)
- Blank templates: `templates/catalogue/`
- Validate a private working folder with `python scripts/validate_catalogue_intake.py /path/to/private/catalogue-intake`

Do not commit populated product data or private source paths.

- [Etsy source export mapping and reconciliation plan](docs/21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md)
- Read-only source preflight: `python scripts/preview_etsy_export.py /private/path/EtsyListingsDownload.csv`
- Preserve raw export records and IMAGE1–IMAGE10 references in the separate private intake tables; never treat remote Etsy image URLs as local or rights-cleared DAG imagery.
