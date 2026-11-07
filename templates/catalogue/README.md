# Private Catalogue Intake Templates

These header-only CSV files are proposed preparation templates, not a production schema.

- products.csv — one row per product.
- product-facts.csv — one row per factual claim about a product.
- product-images.csv — one row per local product/image mapping.
- product-source-records.csv — one row per immutable source-export record.
- etsy-image-sources.csv — one row per private Etsy remote image URL reference.

Copy these files to a private working folder before adding product data. Do not commit populated catalogue files or internal source paths to Git. Run `python scripts/validate_catalogue_intake.py /path/to/private/folder` to check structure and cross-file references.

Review docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md and docs/21-ETSY-SOURCE-EXPORT-MAPPING-AND-RECONCILIATION.md before use. Category values, operational states and fields remain proposals until the owner approves the intake contract.
