# 10 — Roadmap

## Completed milestone — D-014 structural kit adoption

The owner-approved DAG Owner-Controlled Design Kit v2 is materialized at `design/owner-controlled-kit-v2/`. All 25 files are present. At adoption (PR #8), all 14 original HTML/CSS/JS files were byte-verified against the supplied ZIP by Git blob SHA-1 and exact file size. PR #9 amends only two CSS files for accessibility maintenance; the other 12 implementation assets remain byte-identical. The source-integrity validator enforces the closed file inventory and current reviewed source hashes.

This milestone adopts structure only. It does not approve brand identity, production styling, production app development, commerce functionality, hosting or technology choices.

### Completed evidence
1. All 25 source kit files materialized under the agreed path.
2. All 14 original implementation assets byte-verified.
3. All nine page paths and relative CSS/JS references validated by `scripts/validate_project.py`.
4. Active docs/prompts and old visual proposal paths reconciled to D-014.
5. Page/component inventories corrected against the supplied source.
6. CI validators and relevant tests updated for the new authority.
7. Repository reconciliation report, matrix, changelog and checklist committed.

## Current maintenance delivery — source-level accessibility (PR #9)

The follow-up maintenance patch is limited to the supplied kit's existing CSS and does not alter the nine HTML pages, structure, copy, controls, disabled states, responsive breakpoints or token values:
- styles/components.css adds an explicit :focus-visible outline using currentColor; no brand colour is introduced.
- styles/layout.css respects prefers-reduced-motion by disabling the existing smooth-scroll behaviour.
- A read-only audit script and regression tests check the nine-page landmarks, heading and navigation state, focus treatment and reduced-motion rule.

This is source-level support only. No claim is made about rendered-page, keyboard, assistive-technology or viewport acceptance; those checks remain outstanding and are listed in docs/24-STRUCTURAL-KIT-ACCESSIBILITY-REVIEW.md.

### Validation required for PR #9
- Run python3 scripts/validate_project.py.
- Run python3 scripts/audit_m2_readiness.py.
- Run python3 scripts/audit_kit_accessibility.py.
- Run python3 -m unittest discover -s tests -v.
- Run python3 scripts/audit_documentation_links.py.
- Confirm the PR workflow is green before merge.

## Owner gates retained

- **Brand identity:** exact colours, typography, logo/wordmark/descriptor and photography direction remain pending owner input. The system-token fallback is QA only.
- **Customer validation:** Japan-first segments and journey priority remain to be confirmed; no fieldwork is represented as complete.
- **Product/photo evidence:** only owner-approved genuine sample photographs with verified mapping and rights may be used; label placeholders for missing views (D-011).
- **Responsive journey acceptance:** mobile/tablet/desktop must be tested across every selected journey (D-012).
- **Next-phase authorization:** D-014 alone does not authorize added prototype scope or production development.

## Technical and commercial work

Preserve existing catalogue intake, photo audit, Etsy mapping, research and merchant documentation where valid. Do not select a production framework, database, CMS, hosting provider, payment provider, currency, sales territory, tax treatment, shipping terms, return policy or commercial model by inference.

## Explicit exclusions

No additional routes, sections, components, banners, testimonials, badges, reviews, widgets, icons, animations, popups, sticky/floating UI, chat/newsletter/social modules or new navigation. No cart, checkout, account, wishlist, live search/filter/sort, variants, payment, order operations, shipping calculation or returns workflow.

## Roadmap update rule

Update this roadmap only when an actual owner decision, evidence-backed milestone, implementation or validation result changes. State what is complete, incomplete and blocked without anticipating future results.
