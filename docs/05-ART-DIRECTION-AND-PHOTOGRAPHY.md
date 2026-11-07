# 05 — Art Direction and Photography

## Current authority

D-014 provides page and component structure only. Photography art direction, image crop rules and final visual identity remain owner-controlled and pending.

## Evidence and rights

D-011 confirms a mixed evidence approach for future authorized customer-experience review:
- Genuine DAG sample photographs only where product/image identity, factual mapping, rights/permissions and prototype-use approval are verified.
- Clearly labelled illustrative placeholders for missing product images, additional views or states.
- No unrelated stock, generated image or remote Etsy image may be represented as genuine DAG product photography.

This does not confirm that a real sample has been supplied or cleared. No bulk migration, public publication or photo binary commit is authorized.

## Existing photo library

Approximately 3,000 original photographs across roughly 300 products are recorded as available. Bulk migration and hosting remain deferred. Preserve originals and independent backups. Do not commit the photo library to Git or bulk-download Etsy image URLs.

The stdlib-only inventory utility `scripts/audit_photo_library.py` is non-destructive preparation. See `docs/19-PHOTO-LIBRARY-AUDIT.md` for its usage, limitations and safe output handling.

## Owner-only decisions

The owner must approve lighting, backgrounds/surfaces, object scale/context, flat-lay/portrait/lifestyle approach, crop/aspect ratios, sequence, colour treatment and production art direction. Do not synthesize these decisions from P-015, P-016 or the system-token fallback. Record exact approval in `docs/DECISIONS.md`.

## Publication integrity

Alt text must describe the actual image. Product-image associations require verified product identity and source evidence. Do not publish placeholders as real catalogue media or assert maker/process/provenance claims without evidence.
