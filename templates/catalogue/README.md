# Private Catalogue Intake Templates

These header-only CSV files are proposed preparation templates, not a production schema.

- products.csv — one row per product.
- product-facts.csv — one row per factual claim about a product.
- product-images.csv — one row per product/image mapping.

Copy these files to a private working folder before adding product data. Do not commit populated catalogue files or internal source paths to Git. Run `python scripts/validate_catalogue_intake.py /path/to/private/folder` to check structure and cross-file references.

Review docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md before use. Category values, operational states and fields remain proposals until the owner approves the intake contract.
