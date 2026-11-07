# DAG v2 Handoff — Owner-Controlled Structural Kit

Read root `AGENTS.md`, `README.md`, `docs/DECISIONS.md`, `docs/DESIGN-AUTHORITY.md`, `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`, the page/component inventories and the reconciliation report before implementation.

## Current decision
D-014 adopts the owner-supplied DAG v2 kit as the structural source for exactly nine pages. It does not approve brand identity, production copy, product facts, functionality, technology or production application development. D-013's former six-page scope is superseded.

## Non-negotiable boundaries
- Customer-facing content is English-only.
- POJ Studio is primary for ecommerce/page structure; Macaroni Shoten is secondary for curation.
- Preserve the source kit's HTML/CSS/responsive styles, page order, components, placeholders and disabled controls.
- Do not add pages, sections, shell elements, UI, animations, widgets or interactions.
- Do not fabricate products, makers, materials, provenance, dimensions, prices, stock, reviews, policies or business facts.
- Do not select brand colours, fonts, logo/wordmark/descriptor or photography direction. These remain owner-controlled.
- P-015 is rejected; P-016 is historical only.
- No cart, checkout, account, wishlist, live search/filter/sort, payments, order flow, shipping calculation or returns workflow.
- No production application development or technology selection is authorized.

## Required handoff checks
The repository reconciliation report identifies the current blocker: the original 25-file archive has not yet been materialized under `design/owner-controlled-kit-v2/` in GitHub. Do not claim installation. Finish source extraction and exact byte verification before treating D-014 as fully materialized. Then apply all remaining checklist items, update the matrix to observed dispositions, run validators/tests, check links and stale instructions, and open/complete the PR only with truthful CI evidence.
