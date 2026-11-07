# 05 — Art Direction and Photography

## Asset position
The owner has approximately 3,000 original photographs for roughly 300 products, around 2 GB in total. Bulk migration and hosting are deferred until the frontend direction is ready.

## Current rules
- Do not commit the photo library to Git.
- Do not bulk-download Etsy image URLs.
- Do not assume Etsy CDN URLs are permanent media hosting.
- Do not invent product images or use unrelated stock as product representations.
- Use attractive, clearly labelled design placeholders.
- Never publish a placeholder as genuine catalogue media.

## What happens now
Photography art direction must be developed now, separately from bulk migration. When the owner can provide a representative sample of 10–20 images, use it to test the design's ability to present actual textile colours, texture, scale and detail. Do not require the full photo library for this study.

## Art-direction brief
Define:
- Product backgrounds and surfaces.
- Natural and studio lighting.
- Textile texture and macro details.
- Object scale and context.
- Flat-lay, portrait and lifestyle compositions.
- Colour fidelity and post-processing.
- Crop and aspect-ratio rules.
- Gallery sequence: primary, detail, scale/context, maker/process only where verified.
- Alt text based on the actual image and product.
- Rights, consent and publication workflow.

## Future image integration
When explicitly authorized, map stable product IDs/SKUs to source photographs, preserve originals and independent backups, generate responsive optimized formats, produce a migration report and validate image-to-product associations before publication.


## Non-destructive source inventory

The repository includes a stdlib-only inventory command: `scripts/audit_photo_library.py`. It can inspect a selected image sample or, when explicitly requested, the wider folder. It reports format, dimensions where supported, size, SHA-256 and exact byte-duplicate groups. It never edits source media. See [19 — Non-Destructive Photo Library Audit](19-PHOTO-LIBRARY-AUDIT.md) for supported formats, limitations, safe output handling and usage. This is preparation only, not image migration or hosting.
