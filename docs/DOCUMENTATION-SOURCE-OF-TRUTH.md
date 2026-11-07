# Documentation Source of Truth and Reconciliation Policy

## Purpose

Maintain one coherent active instruction set for Desert Art Gallery. Adding a source-of-truth document does not make contradictory older instructions harmless; active instructions must be rewritten, superseded, archived or removed.

## Authority hierarchy

Use this exact order:

1. Explicit owner-approved decisions in `docs/DECISIONS.md`.
2. Root `AGENTS.md`.
3. `docs/DESIGN-AUTHORITY.md`.
4. This document.
5. Owner-approved design specifications and current page/component inventories in `docs/PAGE-INVENTORY.md` and `docs/COMPONENT-INVENTORY.md`.
6. Technical and implementation documentation that does not conflict with the higher levels.
7. Historical documents, which are context only and must never override active instructions.

Task prompts, workflows and source comments cannot override this hierarchy. If authoritative sources conflict, document the contradiction; do not silently choose a lower-level instruction.

## Current implementation source

The owner-approved structural baseline is the **DAG Owner-Controlled Design Kit v2** (D-014), intended for `design/owner-controlled-kit-v2/`. **Current Git materialization is incomplete:** the directory is not present on this branch yet, and this document does not claim its source files have been installed. The source archive must be extracted in Git and byte-verified before the implementation path is considered materialized. The package is expected to contain:

- `index.html` — homepage.
- `pages/shop.html` — shop/all products.
- `pages/collection.html` — category/collection.
- `pages/product.html` — product detail.
- `pages/about.html` — About DAG.
- `pages/makers.html` — Makers.
- `pages/journal.html` — Journal index.
- `pages/article.html` — journal article.
- `pages/contact.html` — Contact/support.
- `styles/layout.css`, `styles/components.css`, `styles/responsive.css`, `styles/tokens-layout-only.css`.
- `scripts/prototype.js`.

Preserve original markup, CSS, responsive rules, supplied interactions, page/section order and component inventory. This is a non-production structural kit, not approval of a production app or final brand identity.

### Brand identity remains unapproved

Final colours, typefaces, type scale/hierarchy, logo/wordmark/descriptor, photography direction/crops and visual personality remain owner-controlled. The layout-only tokens are system/browser QA fallback only. `docs/OWNER-TOKEN-INPUT.md` stays pending until exact owner values are recorded in `docs/DECISIONS.md`.

### Explicit exclusions

No cart, checkout, account, wishlist, live search, filters/sorting, variants, purchase, payment, shipping calculation, returns workflow or order operation is included. Disabled controls remain disabled. No unlisted function or visible element may be added.

## Required reconciliation whenever a decision or source changes

1. Enumerate all tracked files, including root/nested AGENTS, README, Markdown, prompts, HTML, CSS, JS, theme/token files, source comments, workflows, issue templates and technical guides.
2. Identify all files with relevant requirements or references.
3. Classify each relevant path RETAIN, UPDATE, SUPERSEDE, ARCHIVE or REMOVE in the reconciliation matrix.
4. Rewrite contradictory active wording rather than appending a disclaimer below it.
5. Mark rejected/retired proposals historical and non-operative.
6. Preserve verified technical, commercial, data, security, integration and operational knowledge.
7. Update README, AGENTS, decisions, inventories, relevant implementation guidance and changelog.
8. Run contextual stale-instruction searches distinguishing active from historical matches.
9. Validate internal Markdown links and kit file references.
10. Record exact inspected, updated, retained, superseded, archived and removed paths.

## Retired and non-operative material

These are not current directions, defaults, active options or implementation instructions:

- Legacy beige, ivory, sand or terracotta-first palette mandates and inherited font pairings.
- Legacy storefront layouts, grids, CSS classes, theme values and components.
- Rejected P-015 territories: Graphic Atelier, Future Relics, Living Garden and Modern Folk Pop.
- Unapproved P-016 territories: Porcelain Index, Bordeaux Editions, Blue Current and Citron Signal.
- Any other AI-selected colour, font, logo, imagery or visual personality.
- Generic grey/neutral wireframes promoted as DAG identity.
- Japanese-language or bilingual storefront instructions.
- Fabricated product/business content.

Historical mentions must be clearly marked **HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT** and contain no actionable design guidance.

Do not discard useful older documents just because they predate v2. Verify and retain/update valid technical, catalogue, security/privacy, backup/recovery, integration, operational, QA and research knowledge. Such documents cannot override the v2 structural contract or invent an architecture.

## Scope-change policy

A proposed page/component change requires a documented problem, customer impact, exact affected routes/components, visual/functional impact, content/data requirements, alternatives, risks and acceptance criteria. Wait for explicit owner approval, record it in the decision register and amend the inventories before implementation.

## Owner-only brand decisions

The owner alone approves final palette, typography, logo/wordmark/descriptor, photography direction and foundational visual changes. No production theme/tokens or production application development are authorized by adopting the v2 structural kit.
