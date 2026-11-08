# DAG v2 Handoff — Owner-Controlled Structural Kit

Read root `AGENTS.md` and `README.md`; then follow the exact eight-level authority order in `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`: decisions, root agent rules, design authority, source-of-truth policy, owner-approved specifications, page/component inventories, compatible technical docs, and finally historical audit material. Also inspect the reconciliation matrix/report/checklist before changing repository guidance.

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
The original 25-file owner archive is materialized under `design/owner-controlled-kit-v2/`; PR #8 records byte verification of all 14 original HTML/CSS/JS assets. PR #9 makes only two additive accessibility maintenance changes to the existing CSS: a keyboard focus-visible outline using currentColor and a reduced-motion override for the supplied smooth-scroll rule. See docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md for scope and evidence. Preserve all nine HTML pages and every existing section, control, label, placeholder, responsive breakpoint and supplied script. Do not choose brand tokens or introduce a skip-link component, new features or production application code. Run validators, source audit, tests and Markdown-link checks; report browser/assistive-technology validation as pending until performed.
