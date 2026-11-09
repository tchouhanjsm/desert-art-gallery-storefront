# M2 — Revision 4 Content-Evidence and Semantic Implementation

**Status:** Implemented in the local/private, non-transactional prototype under D-016/D-017.  
**Public source boundary:** The D-014 structural kit, its nine HTML routes and component inventory remain unchanged. Private prototype files, images and review evidence are not committed.

## Implementation delivered

- Replaced generic repeated image-frame labels with route-specific accessible and visible evidence placeholders for the homepage hero, categories, catalogue products, Product Detail primary/detail/context views, place/material editorial, maker portrait, Journal stories and Article lead image.
- Preserved existing image-frame counts exactly: Homepage 11; Shop 6; Collection 3; Product Detail 4; About 2; Makers 1; Journal 6; Article 1; Contact 0.
- Converted Product Detail's four existing facts into a semantic description list (dl, dt, dd) without inventing attributes or values. All four remain pending owner verification; price and currency remain pending owner confirmation.
- Exposed the existing Collection, Product Detail and Article breadcrumbs as labelled navigation landmarks, with one current-page item.
- Clarified that article introduction, publication date, authorship and source credits require owner-supplied verification.
- Refined mobile product-fact rows so long evidence states wrap without breaking label/value hierarchy.

## Automated evidence

| Gate | Result |
|---|---:|
| Responsive rendering | 45/45 — 9 routes × 5 approved widths |
| Screenshot set | 18 — 9 routes × 390px and 1440px |
| Horizontal overflow | 0 routes at all 5 widths |
| Image slot inventory | 34/34 across the nine routes; all visible/accessibly labelled and pending |
| Breadcrumb semantics | 3/3 approved routes |
| Product fact structure | 4 semantic label/value pairs; all values pending |
| Product accordions | 4/4 existing accordions open correctly |
| Mobile navigation | Escape closes and restores focus across the nine routes at mobile widths |
| Disabled states | Product options/purchase and all enquiry controls remain disabled |
| External resources | 0 external network requests observed |

The local/private runner adds these content-evidence checks to the existing D-017 visual audit and five-journey review. Automated checks do not constitute owner visual acceptance, participant research, screen-reader testing or full WCAG/legal compliance.

## Boundaries and pending inputs

- No genuine catalogue sample, product photographs, verified product details, maker identities, editorial source records or contact details were provided.
- No price, currency, provenance, materials, dimensions, care details, publication date, author credit or rights status is fabricated.
- All image frames are still illustrative placeholders, not DAG photography.
- Search/filter/sort, variants/options, purchase and enquiry submission remain disabled.
- No production stack, public deployment, transaction capability, fieldwork or spend is authorized.
- Owner visual acceptance and human customer usability acceptance remain pending.
