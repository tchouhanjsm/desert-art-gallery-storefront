# Desert Art Gallery — Owner-Controlled Design Kit v2

**Current structural source:** `design/owner-controlled-kit-v2/`  
**Status:** Adopted by D-014. The uploaded 25-file owner archive is materialized in the repository and its SHA-256 (`64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`) matches the adoption archive. PR #8 verified all 14 original HTML/CSS/JS assets. PR #9 amended styles/components.css (keyboard focus visibility) and styles/layout.css (reduced-motion support). PR #11 adds a mobile-only Product Detail thumbnail-grid sizing correction in styles/responsive.css, retaining all three supplied thumbnail slots. The nine HTML pages and supplied script remain unchanged; 11 of the 14 original implementation assets remain byte-identical. CI verifies current implementation hashes and the exact kit inventory. This remains structural-only and is not brand identity approval. D-016 authorizes six local/private, non-transactional prototype areas; D-017 records the owner's Revision 2 M2-A visual approval and permits branded implementation within that private boundary.

## Authority hierarchy

1. `docs/DECISIONS.md` — explicit owner decisions.
2. Root `AGENTS.md` — permanent agent rules.
3. `docs/DESIGN-AUTHORITY.md` — owner control and closed design scope.
4. `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md` — repository-wide hierarchy/reconciliation policy.
5. Owner-approved design specifications.
6. Current page and component inventories: `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`.
7. Technical and implementation documentation, only where it does not conflict with levels 1–6.
8. Historical files — audit context only, never active instructions.

## Preview and implementation source

Open `design/owner-controlled-kit-v2/index.html` and the pages under `design/owner-controlled-kit-v2/pages/`. Preserve the nine original HTML pages, responsive rules, script, page/section order, supplied components and disabled states. Documented maintenance is limited to keyboard focus visibility, reduced-motion support and the mobile Product Detail gallery grid correction; see docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md. A dedicated Chromium workflow reviews all nine routes at 390, 430, 768, 1280 and 1440 CSS-pixel widths and uploads screenshots plus JSON/Markdown results. CI verifies the exact kit file inventory and current implementation asset hashes. The files are a non-production structural kit, not a live store or production app.

## Exact page inventory

1. Homepage — `index.html`
2. Shop / all products — `pages/shop.html`
3. Category / collection — `pages/collection.html`
4. Product detail — `pages/product.html`
5. About DAG — `pages/about.html`
6. Makers — `pages/makers.html`
7. Journal index — `pages/journal.html`
8. Journal article — `pages/article.html`
9. Contact / support — `pages/contact.html`

See `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md` for exact sections, slot counts and components. See `docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md` for browser assurance, `docs/25-M2-DECISION-AND-REVIEW-PACK.md` for owner decisions, `docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md` for prototype review, `docs/27-M2-A-REFERENCE-LED-VISUAL-PROPOSAL.md` for the owner-approved Revision 2 visual direction (D-017), `docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md` for the approved cohort plan, and `docs/20-CATALOGUE-INTAKE-AND-FACT-VERIFICATION.md` for private sample evidence validation. `docs/29-M2-PRIVATE-PROTOTYPE-VALIDATION-AND-REVIEW.md` documents the local/private prototype entry validator and Chromium review runner; M2-A approval is recorded as D-017; private implementation and review may proceed within the local/private boundary.

## Approved visual direction and private prototype boundary

The owner approved Revision 2 (“Material in Focus”) under D-017 on 9 November 2026. Exact colour, typography, hierarchy and layout values are recorded in `docs/OWNER-TOKEN-INPUT.md` and `docs/27-M2-A-REFERENCE-LED-VISUAL-PROPOSAL.md`. This approval authorizes those values for the six-area local/private prototype only; `styles/tokens-layout-only.css` remains system-colour/system-font QA fallback only, not a DAG palette or production theme; the D-014 kit remains unchanged.

The owner has accepted a seven-person research cohort (see `docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md`) and the five-journey priority. No fieldwork is authorized. The six private prototype areas and owner walkthrough sequence are in `docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md`; M2-E implementation may now proceed outside this public repository, subject to the exact scope and non-transactional restrictions.

## Language, content and commerce

Customer-facing content is English-only; Japan-first does not imply Japanese-language UI or settle seller jurisdiction, sales territories, currency, tax/duties, shipping, payments, returns or service commitments.

Never fabricate product, maker, material, dimension, provenance, price, stock, review, contact, policy or delivery information. Existing placeholders stay visibly pending; disabled controls stay disabled. Cart, checkout, account, wishlist, live search/filter/sort, payment, orders, shipping calculation and returns are out of scope.

Do not add pages, sections, navigation, banners, testimonials, badges, reviews, widgets, popups, new sticky elements, animations, newsletter/social, chat, extra nav or functionality without explicit owner approval and inventory amendment.

## References and IP

POJ Studio is primary for ecommerce/page structure; Macaroni Shoten is secondary for curation/select-shop character (D-010). Do not clone proprietary HTML/CSS/JS, branded layouts, logos, text, photography, fonts or assets.

## Documentation governance

- `docs/DOCUMENTATION-RECONCILIATION-MATRIX.md` — path-level dispositions.
- `docs/DOCUMENTATION-RECONCILIATION-REPORT.md` — audit findings and evidence.
- `docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md` — completion status and exceptions.
- `docs/DOCUMENTATION-CHANGELOG.md` — dated changes.
- `docs/OWNER-TOKEN-INPUT.md` — pending owner values.

Whenever a decision or source changes, reconcile all relevant tracked documents, prompts, code comments, HTML/CSS/JS, workflows and issue templates. Do not claim completion until validation evidence exists.
