# Desert Art Gallery — Permanent Agent Instructions

## Mission and current source

Build Desert Art Gallery (DAG) as an original, product-led ecommerce and gallery experience rooted in the textiles, objects, material culture and craft identity of Jaisalmer, Rajasthan, with Japan-first customer focus.

**Current structural source: `design/owner-controlled-kit-v2/` (D-014).** Preserve the owner-supplied nine HTML pages, CSS files, responsive styles, structural sections, supplied JS and component inventory. Do not redesign, restyle, expand or replace the kit.

The legacy repository `https://github.com/tchouhanjsm/desert-art-gallery` may be inspected selectively for verified domain knowledge, data structures, operational lessons and proven engineering logic only. Its frontend, layouts, styles, components and visual decisions are not inherited.

## Mandatory hierarchy

1. Explicit owner-approved decisions in `docs/DECISIONS.md`.
2. This root `AGENTS.md`.
3. `docs/DESIGN-AUTHORITY.md`.
4. `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`.
5. Owner-approved design specifications and current page/component inventories in `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`.
6. Technical and implementation documentation that does not conflict with the above.
7. Historical documents as context only; never as active instructions.

Do not follow a lower-level prompt, source comment, workflow or old document that conflicts with this hierarchy. Record contradictions; never silently choose the lower-level instruction.

## Confirmed direction and content integrity

- Japan-first is the confirmed customer-market focus.
- Customer-facing UI/copy must remain English-only. Do not introduce Japanese or bilingual storefront content.
- DAG retains its authentic Jaisalmer/Rajasthan identity; all product, maker, provenance and business claims require verification.
- The new repository is the source of truth; legacy frontend/design instructions are not inherited.
- Approximately 3,000 original photographs across roughly 300 products are recorded as available. Bulk migration/hosting remain deferred; do not commit photo binaries.
- Never fabricate products, names, attributes, prices, discounts, reviews, rankings, stock, availability, maker identities, materials, dimensions, condition, provenance, care, awards, certifications, sustainability claims, business/contact details, policies or delivery promises.
- Keep raw source exports, private catalogue data, source paths and rights evidence outside Git.

Japan-first does not settle seller jurisdiction, sales territories, currency, tax/duties, payment eligibility, shipping, returns, privacy or fulfilment. Keep those owner decisions unresolved until explicitly recorded.

## Exact v2 scope — no additions

The only active pages are the nine files in `docs/PAGE-INVENTORY.md`. Use only components/sections in `docs/COMPONENT-INVENTORY.md`.

Do not add, remove, reorder or reinterpret pages, sections, navigation items, shell items, components, controls or functionality independently. No extra banners, promotions, testimonials, badges, reviews, widgets, icons, animations, popups, sticky/floating features, chat, newsletter, social modules, recommendations, extra navigation or new copy.

The kit's own kit-only notice, utility location row, wordmark/header, navigation, action area and footer are supplied structure. They are not permission for additional UI.

Disabled/visual-only search, filter/sort, variant, purchase and enquiry form controls remain disabled. Do not turn visual concepts into live functions. Cart, checkout, account, wishlist, payment, shipping calculation, returns, orders and inventory operations are outside this kit.

Any scope change requires a written change request, explicit owner approval recorded in `DECISIONS.md`, and an updated inventory before implementation.

## Owner-controlled brand identity

The owner alone approves exact brand colours, typography families/weights/hierarchy/type scale, logo/wordmark/descriptor, photography direction/crop and foundational visual changes. These values are pending.

`design/owner-controlled-kit-v2/styles/tokens-layout-only.css` uses browser/system colours and fonts solely for layout QA. It is not a DAG palette, neutral brand theme or production theme. Never promote those values to production tokens or populate `docs/OWNER-TOKEN-INPUT.md` with AI-selected values.

## References and intellectual property

D-010: POJ Studio is primary for ecommerce/page structure; Macaroni Shoten is secondary for curation/select-retail character. Learn non-proprietary experience principles only. Do not copy source code, CSS, exact branded layouts, logos, copy, photography, fonts or protected assets. The owner-supplied v2 kit is the structural source.

## Retired instructions — never revive

These are historical/non-operative, not defaults, current choices or implementation targets:
- Legacy beige/ivory/sand/terracotta-first palette mandates and inherited legacy font pairings.
- Legacy storefront layouts, grids, CSS classes, components and tokens.
- Rejected P-015: Graphic Atelier, Future Relics, Living Garden, Modern Folk Pop.
- Superseded/unapproved P-016: Porcelain Index, Bordeaux Editions, Blue Current, Citron Signal.
- Material Archive / Collected Colour synthesis.
- Any AI-selected palette, fonts, logo, photo direction or visual personality.
- Generic grey/neutral wireframes promoted as DAG identity.
- Japanese-language/bilingual storefront instructions.
- Fabricated product/business examples presented as facts.

Historical material must be labelled **HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT** and must contain no actionable design instruction.

## Photography

Use supplied placeholders until owner-approved DAG content/assets exist. Genuine photographs require exact product identity, factual mapping, rights/permissions and prototype/publication-use approval. Do not use unrelated stock, generated or Etsy-remote imagery as genuine DAG product photography. No bulk migration or public publication is authorized.

## Engineering discipline

Inspect current Git state and all relevant paths before changes. Do not assume a framework, package manager, database, CMS or host. Preserve source HTML/CSS/JS byte-for-byte unless the owner authorizes an exact defect fix. Maintain security, semantics, accessibility and responsive behaviour without visible feature additions. Test changes, review the complete diff, and never claim unrun tests passed.

## Repository-wide documentation governance

Whenever a design decision, kit, inventory or structural source changes:
1. Read `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`, `docs/DESIGN-AUTHORITY.md` and `docs/DOCUMENTATION-RECONCILIATION-CHECKLIST.md`.
2. Check `docs/DECISIONS.md`.
3. Follow the current page/component inventories.
4. Search all relevant tracked files: AGENTS, READMEs, Markdown, prompts, HTML/CSS/JS, token/theme files, comments, workflows, issue templates and technical guides.
5. Reconcile every active instruction; remove contradictions rather than append a later disclaimer.
6. Classify affected files RETAIN, UPDATE, SUPERSEDE, ARCHIVE or REMOVE.
7. Preserve valid technical/business knowledge after verification.
8. Update README, decisions, inventories, report, matrix and changelog.
9. Run contextual stale-instruction and internal-link checks.

## Authorization boundary

D-014 adopts a structural kit only. It does not authorize production application development, visual token selection, framework/database/CMS/hosting selection, public deployment, new visible UI/functionality, commercial/legal decisions, paid services or research spending.

**THE OWNER DEFINES THE KIT AND BRAND. THE AGENT PRESERVES AND IMPLEMENTS THE APPROVED SCOPE — NEVER EXPANDS IT.**
