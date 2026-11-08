# AI Bootstrap Prompt — Desert Art Gallery

Repository: https://github.com/tchouhanjsm/desert-art-gallery-storefront

You are joining a new DAG repository. The root `AGENTS.md`, `README.md`, owner decisions and design authority are mandatory. The repository, not conversational memory, is the source of truth.

## First action
1. Read root `AGENTS.md` and `README.md`.
2. Read `docs/DECISIONS.md`, `docs/DESIGN-AUTHORITY.md` and `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`.
3. Read owner-approved design specifications (level 5), then `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md` (level 6), and the current reconciliation checklist.
4. Inspect the current branch, complete tracked repository tree, open PRs, relevant sources, workflows and issue templates before changing anything.

## Current confirmed scope
D-014 adopts the owner-supplied DAG v2 structural kit as the sole active HTML/CSS implementation source for exactly nine pages. Preserve original markup, CSS, responsive rules, prototype script, page/section order, components, placeholders and disabled states. The kit is not a production app and does not approve final brand identity.

The active kit is materialized at `design/owner-controlled-kit-v2/`. The current owner archive SHA-256 is `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`; verify the 25-file inventory and current implementation asset hashes with `scripts/validate_project.py`. Do not describe kit materialization as blocked or treat this document as permission to re-extract/alter the supplied kit.

## Owner-controlled identity
The owner alone approves exact colours, typography families/weights/hierarchy/type scale, logo/wordmark/descriptor and photography direction/crops. These values remain pending in `docs/OWNER-TOKEN-INPUT.md`. Do not generate an option set, recommend a visual territory, blend historical ideas or select defaults. `tokens-layout-only.css` is browser/system QA fallback only, not a DAG palette or production theme.

## Content and language integrity
- Japan-first is the confirmed target-market focus; customer-facing UI/copy remains English-only.
- Never fabricate product names, attributes, maker identities, material, dimensions, provenance, price, stock, reviews, availability, policies, contact information or delivery promises.
- Preserve supplied placeholders until owner-approved facts and assets exist.
- Use only owner-cleared DAG photography with verified identity/mapping and rights; label missing evidence as a placeholder.
- Do not commit source exports, private catalogue data or the photo library to Git.

## Closed scope — additions are not allowed
Use only the nine pages and exact components in the active inventories. Do not add banners, testimonials, badges, ratings, reviews, widgets, icons, animation, popups, sticky/floating elements, chat, newsletter/social modules, extra navigation or new page sections. Existing disabled controls remain disabled.

There is no cart, checkout, account, wishlist, live search/filter/sort, functional variants, payment, order workflow, shipping calculation, return workflow or enquiry backend in this kit.

## References and IP
D-010: POJ Studio is primary for ecommerce/page structure; Macaroni Shoten is secondary for curation/select-shop character. Study non-proprietary principles only. Do not copy code, CSS, exact layouts, text, branded graphics, logos, fonts or photography.

## Authorization boundary
D-014 does not authorize production app development, framework/database/CMS/hosting selection, public deployment, paid services, research spending or commercial/legal decisions. Record a written change request and obtain explicit owner approval before changing scope.

## Documentation hierarchy and reset rule
Follow the exact eight levels in `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`. If a lower-level prompt or file conflicts with a higher level, reconcile the lower-level active text; do not merely add a note alongside it. Historical paths are audit-only and cannot be used as current implementation instructions. When a decision changes, update the root decisions and affected specifications/inventories, then run the repository-wide contextual consistency and link audits.

## Reporting
Report exact files changed, checks actually run, test results, remaining blockers and whether the kit has been materialized and hash-verified in Git. Never claim unperformed validation.
