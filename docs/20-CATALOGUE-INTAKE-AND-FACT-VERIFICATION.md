# 20 — Catalogue Intake and Fact Verification Standard

**Status:** Draft preparation contract for owner review. It is not an approved production data model, catalogue taxonomy or commerce policy.

## Purpose

Prepare accurate source information for the eventual DAG catalogue before selecting a database, CMS, checkout implementation or hosting platform. The owner has approximately 300 products and a substantial original image library. This intake contract provides a consistent way to capture product identity, facts and image references without inventing information.

The CSV templates are blank. They contain no DAG product records, prices, maker claims, source paths or image URLs.

## Non-negotiable content rules

- Customer-facing fields ending in `_en` are intended for English-only publication.
- A field being present in a source export does not automatically make its claim publishable.
- Unknown information stays blank or is captured as an unverified internal fact. Do not infer materials, dimensions, condition, maker, technique, origin, care, availability or sustainability claims.
- Evidence status and public approval are separate. A source may document a fact without the owner approving its public wording.
- No maker, provenance, heritage, certification or environmental claim is published without owner verification and an evidence reference.
- A price requires an amount, an explicit currency code and an evidence reference. Leave all three blank if unresolved. No base currency or conversion rule is selected here.
- A product image requires an asset reference and a source-relative path. Rights clearance and owner publication approval are separate checks.
- Do not place the full catalogue, internal notes, source filenames or photo-library reports in Git.

## Intake package

Create a private working folder by copying the header-only files in `templates/catalogue/`:

| File | One row represents | Purpose |
|---|---|---|
| `products.csv` | One product record | Stable identity, English title/copy, candidate category, internal publication/availability state and evidenced price |
| `product-facts.csv` | One fact about one product | Material, dimensions, condition, care, maker, origin, technique and any other factual attribute with evidence and publication approval |
| `product-images.csv` | One local image mapped to one product | Local source path, asset ID, image role/order, rights state, publication state and English alt text |
| `product-source-records.csv` | One immutable source-export row mapped to one product | Source system, source-file SHA-256, logical data-row number, raw source values and reconciliation state |
| `etsy-image-sources.csv` | One Etsy IMAGE1–IMAGE10 URL reference | Original remote URL, source record link, rights evidence, download/review state and eventual local asset ID |

Do not add real product rows to the repository. Work on private copies outside Git and outside the original photo folder.

## Draft field conventions

### Product record

- `product_id`: stable internal identifier chosen by the owner. It is not assumed to be the SKU.
- `source_record_ref`: optional trace back to an Etsy/export/source record.
- `sku`: optional owner-provided SKU; if used, it must be unique in the intake set.
- `title_en`, `short_description_en`, `description_en`: English customer-facing drafts. Only the title is structurally required for an intake row; the owner controls publication readiness.
- `category_candidate`: provisional classification only. It does not create or approve the final product taxonomy.
- `publication_status`: proposed internal editorial state: `draft`, `in_review`, `approved_for_publication`, `published`, or `archived`.
- `availability_status`: proposed internal state: `not_verified`, `available`, `unavailable`, or `made_to_order`. These do not by themselves authorize a customer-facing purchase/enquiry model.
- `price_amount`, `price_currency`, `price_evidence_reference`: supplied together or all left blank. Currency format is three uppercase letters; the base/display currency remains unresolved.
- `internal_notes`: private workflow notes only. Never put credentials, payment data or unnecessary personal information here.

### Product facts

- `fact_key` and `fact_value` hold one fact per row; `unit` makes measurements explicit.
- `verification_status`: `unverified`, `source_documented`, or `owner_verified`.
- `evidence_reference`: required for documented/verified facts. Use a private source reference or record locator, not a public URL unless it is intended for publication.
- `public_approval`: `not_reviewed`, `approved`, or `do_not_publish`. An approved public fact must be owner-verified and have evidence.

### Product images

- `asset_id`: stable ID for the image asset; it is separate from product ID.
- `source_relative_path`: path relative to the owner's private photo-library root. Use forward slashes and no absolute paths or parent-directory traversal.
- `image_role`: proposed intake labels are `primary`, `detail`, `scale`, `context`, `packaging`, and `other`.
- `sort_order`: positive integer, unique within each product.
- `rights_status`: `unknown`, `cleared`, or `restricted`.
- `publication_status`: `pending`, `approved`, or `blocked`. Approval requires cleared rights and English alt text.

These are intake conventions to support review. They do not select the production media model, public image layout or final storefront presentation.

## Local validation

From the repository root:

```bash
python scripts/validate_catalogue_intake.py "/path/to/private/catalogue-intake"
```

The validator expects the five documented CSV files. It checks headers, IDs, normalized SKU uniqueness, allowed internal states, evidenced price pairs, fact verification/public approval, local image paths/rights/alt text, image ordering, source-file/row identities, remote Etsy image-host restrictions and cross-file product references. Duplicate raw source SKUs remain preserved for reconciliation and are not treated as unique catalogue SKUs. It never edits the CSV files or imports records into an application.

An optional cross-check can verify every product image path against the read-only photo-audit CSV and its JSON summary. Both files must come from the same run, the summary must be marked `read_only=true` and `scan_complete=true`, and its candidate count must match the CSV rows. This also prevents an image with audit status `review` or a byte-identical duplicate from being marked approved.

```bash
python scripts/validate_catalogue_intake.py "/path/to/private/catalogue-intake" \\
  --photo-audit-csv "/path/to/private-reports/dag-photo-audit.csv" \\
  --photo-audit-summary "/path/to/private-reports/dag-photo-audit-summary.json"
```

Keep both report files private and outside Git. This optional check compares references only; it does not copy, transform or publish images.

The checker validates structure and inventory references, not the truth of product claims or the legal right to publish an image. A structurally valid row can still contain inaccurate information; human source review, rights verification and owner publication approval remain mandatory.

An Etsy Listings Download export also has a separate private source-record and remote-image mapping convention. A source image marked rights-cleared must carry its own rights_evidence_reference, even before it has a local asset mapping. See [21 — Etsy Source Export Mapping and Reconciliation](21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md) for the historical source audit and field mapping.

## Private prototype-use approval (M2 sample)

The private M2 sample uses three separate approval/evidence boundaries:

- Product record: prototype-use approval and evidence for the product record.
- Product fact: owner-verified fact evidence plus separate prototype-use approval/evidence.
- Product image: rights-clearance evidence plus separate prototype-use approval/evidence and the completed photo-audit record.

A rights-cleared image is not automatically approved for a private prototype. A prototype-approved fact or image is not approved for public publication. Keep product records in draft/in-review, fact public approval at not_reviewed and image publication status pending throughout private M2 review.

The intake CSV templates include these separate fields. A private 10–20 product M2 sample can be checked with the validator's --m2-sample option and both reports from one complete photo audit:

    python scripts/validate_catalogue_intake.py "/path/to/private/catalogue-intake" --photo-audit-csv "/path/to/private-reports/dag-photo-audit.csv" --photo-audit-summary "/path/to/private-reports/dag-photo-audit-summary.json" --m2-sample

This stricter mode requires 10–20 distinct products, an owner-reconciled source-export row per product, explicit product/fact/image prototype-use approval, at least one owner-verified fact per product, a rights-cleared primary image with evidence, and a completed audit with readable, non-duplicate images. It rejects public publication approval states in the private-sample validation mode. This is a structural validator; it cannot prove the underlying real-world fact or right is valid. Keep the filled CSVs, source export, photos and reports private and outside Git.

## What this does not decide

- Final category taxonomy or collection names.
- Seller identity, sales territory, currency policy, tax, duties, shipping, returns or payments.
- Direct ecommerce, enquiry-led or hybrid commercial model.
- Database, CMS, hosting, storage or image-delivery vendor.
- Product price, inventory quantity, discounts, customer-facing availability promises.
- Final product photography, crop rules, gallery design or visual identity.

## Review sequence

1. Populate a private sample of 10–20 products only when the owner is ready to share source records.
2. Map a small approved image sample with human visual inspection and the photo audit when that utility is available in the active branch.
3. Resolve product IDs and source-record mapping; do not infer SKU relationships.
4. Record factual evidence and keep unknowns visible.
5. Confirm category candidates against the actual catalogue before creating a final taxonomy.
6. Review the proposed intake conventions with the owner before treating them as the production data contract.

Do not convert this draft intake convention into an approved production schema, taxonomy or backend. The owner must review and explicitly approve any production data contract. The active D-014 page and component inventories remain the current scope.


## M2-C — Placeholder and image-frame display rules (D-016)

The owner has approved a clearly labelled placeholder approach for private prototypes:
- Use image frames to demonstrate the proposed aspect ratio, image count and gallery sequence.
- Label an empty product-photo frame exactly: “ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING”.
- Label a non-product layout tile: “LAYOUT PLACEHOLDER — NOT A DAG PRODUCT”.
- Label each absent angle/view; do not silently duplicate an image and imply multiple real photographs.
- Never invent products, maker names, verified attributes, prices or reviews.
- Never use generated artwork, unrelated stock or remote Etsy imagery as a real DAG catalogue image.

The owner expects to provide approximately 10–20 genuine product photographs with associated verified product information when available. Until the sample is supplied and reconciled, product-image validation is PENDING. Keep all photos, raw export rows and completed intake/audit reports in the owner's private storage. The 3,000-photo library must not be bulk migrated or committed.

These display rules do not waive the existing fact, rights, source-row or separate prototype-use approval checks. The D-016 private prototype must remain local/private and outside the public repository.
