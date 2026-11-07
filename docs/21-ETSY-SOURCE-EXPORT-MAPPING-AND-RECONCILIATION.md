# 21 — Etsy Source Export Mapping and Reconciliation

**Status:** Draft compatibility plan. No Etsy CSV has been imported into the new storefront repository and no production import has been authorized.

## Reference source and evidence boundary

The earlier `tchouhanjsm/desert-art-gallery` repository contains [Etsy Listings Import documentation](https://github.com/tchouhanjsm/desert-art-gallery/blob/main/docs/ETSY-LISTINGS-IMPORT.md), a [generic product import template](https://github.com/tchouhanjsm/desert-art-gallery/blob/main/data/product-import-template.csv) and a tested Etsy parser. The new storefront treats that repository as a selective reference under D-001; this document reuses only source-data observations and mapping lessons. It does not inherit that application's schema, database, UI, code or design.

The previous repository's 4 November 2026 import audit records a supplied Etsy Listings Download snapshot with 527 listing rows and 27 columns. It reports TITLE and DESCRIPTION populated for every row, USD as the only currency, quantity 1 on every row, 60 blank SKU values, 13 duplicate-SKU groups affecting 26 rows, 316 distinct title strings, no explicit category/listing ID/status columns, and no populated variation values. It also records 5,216 non-empty IMAGE1–IMAGE10 URL references. **These are historical findings from that earlier audit, not a fresh re-audit of the original CSV.** The original export is not tracked in either Git repository; it must be supplied privately before a new import preview can be run.

## Source field mapping

| Etsy Listings Download field | New DAG intake destination | Handling |
|---|---|---|
| `TITLE` | `products.csv.title_en` and `product-source-records.csv.source_title_raw` | Keep as a draft. Do not use title alone as product identity; repeated titles are documented. |
| `DESCRIPTION` | `products.csv.description_en` and a private source/evidence workflow | Preserve raw source text privately; do not publish before fact and copy review. |
| `PRICE` + `CURRENCY_CODE` | `products.csv.price_amount`, `price_currency`, `price_evidence_reference` plus raw source fields | Copy only with traceable source evidence and explicit owner validation. Do not convert USD to JPY or add taxes/markups. |
| `QUANTITY` | `product-source-records.csv.source_quantity_raw` | Preserve as source data. It is not an approved inventory count or availability promise. |
| `MATERIALS` | `product-source-records.csv.source_materials_raw` and reviewed fact rows | Keep source wording separate from owner-verified product facts. |
| `TAGS` | `product-source-records.csv.source_tags_raw` | Preserve only. Do not automatically convert tags to categories, collections, style claims or SEO keywords. |
| `SKU` | `product-source-records.csv.source_sku_raw`; optionally `products.csv.sku` after reconciliation | Raw blanks and duplicates must be retained. Only independently reconciled identifiers may be assigned as normalized SKU. |
| `IMAGE1`–`IMAGE10` | `etsy-image-sources.csv` | Preserve remote references separately from local image assets. Validate HTTPS and exact host before any future download. |
| `VARIATION 1`–`VARIATION 3` | `product-source-records.csv.source_variations_raw` | Preserve raw values; do not infer sellable options, sizes or colours. The historical snapshot reported no populated values. |
| Category/section | No source field available | Leave `category_candidate` blank until the actual catalogue and owner-approved taxonomy are reviewed. |
| Listing ID/status | No source field available in the documented snapshot | Do not invent a listing ID or assume listing status. |

## Stable source-row identity

The documented Etsy export has no listing ID and repeated titles are common. The proposed row reference is therefore tied to an immutable source-file snapshot:

`etsy:<lowercase-source-file-sha256>:row:<logical-data-row-number>`

The logical data-row number starts at 1 for the first listing after the header. It counts parsed CSV records, not physical text lines; quoted multiline descriptions do not create extra records. The file hash prevents row number 17 in a later re-export from being mistaken for row 17 in an earlier snapshot.

The `product-source-records.csv` table stores the file digest, logical row number and raw source columns. The corresponding `products.csv.source_record_ref` must match the generated source reference. Blank or duplicate raw SKUs are preserved in `source_sku_raw`; they are not silently assigned to `products.csv.sku`.

## Remote image-reference boundary

Etsy `IMAGE1`–`IMAGE10` values are remote source URLs, not local image files and not rights approval. They belong in the private `etsy-image-sources.csv` file. The validator accepts only HTTPS URLs on the exact `i.etsystatic.com` host, without URL credentials or a custom port. This is a source-reference safety check, not a download.

The local `product-images.csv` remains the record for an owner-reviewed local image with a source-relative path, asset ID, role/order, rights state and publication state. When a source image is explicitly downloaded, link it to a local `asset_id`; only after local inspection and rights review may it be marked accepted. The source URLs must never be hotlinked as published DAG product images by default.

The two CSV files and private photo-audit CSV/JSON reports must stay outside Git. The existing photo audit can verify downloaded local paths; it does not verify external image rights, product identity or owner approval.

## Reconciliation controls

- Repeated title strings are not unique product identifiers.
- A duplicate or blank SKU remains in raw source metadata and requires manual reconciliation.
- A unique source SKU is supporting evidence, not automatic proof of product identity.
- Quantity 1 in an export is preserved but does not prove current stock.
- Materials and tags remain raw source values until facts/category decisions are separately reviewed.
- Empty variations do not authorize the creation of sizes, colours or variants.
- No categories, prices, inventory, provenance, maker, condition, measurements, shipping terms, duties, taxes or Japanese-market claims are inferred.
- All imported records, if a future import is explicitly authorized, start as drafts and remain unpublished until the owner reviews identity, facts, commercial state and media rights.

## Read-only source export preflight

Before creating any source-row manifest, run the read-only export preflight against the owner's private original CSV:

```bash
python scripts/preview_etsy_export.py "/private/path/EtsyListingsDownload.csv" \\
  --json "/private/reports/etsy-source-summary.json" \\
  --rows-csv "/private/reports/etsy-source-rows.csv"
```

The preflight computes the source-file SHA-256 and logical data-row references; checks required headers, blank/duplicate SKUs, repeated titles, price/currency and quantity pairing, IMAGE1–IMAGE10 counts and URL hosts, variation population, and the presence of category/listing-ID columns. It handles quoted multiline descriptions. Reports are private and existing report paths are never overwritten. It does not create products, source manifest rows, downloaded images or an import result.

## Local validation

Once the owner supplies the original export privately and a future import-preparation step creates the source manifest, validate it with:

```bash
python scripts/validate_catalogue_intake.py "/path/to/private/catalogue-intake"
```

After the photo inventory and image source references exist, validate local image links separately using the optional photo-audit cross-check described in document 20. No original Etsy export, image file or populated catalogue row belongs in this repository.

## Scope

This plan does not execute an Etsy import, download images, choose an owner-facing category taxonomy, approve price or inventory, define legal seller arrangements, choose a database, or authorize the production storefront. The owner must review the mapping and supply the original data before any real source-row reconciliation is performed.
