# 10 — Roadmap

## Completed milestone — D-014 structural kit adoption

The owner-approved DAG Owner-Controlled Design Kit v2 is materialized at `design/owner-controlled-kit-v2/`. All 25 files are present; the 14 original HTML/CSS/JS files are byte-verified against the supplied ZIP by Git blob SHA-1 and exact file size. The source-integrity validator enforces the closed file inventory and original source hashes.

This milestone adopts structure only. It does not approve brand identity, production styling, production app development, commerce functionality, hosting or technology choices.

### Completed evidence
1. All 25 source kit files materialized under the agreed path.
2. All 14 original implementation assets byte-verified.
3. All nine page paths and relative CSS/JS references validated by `scripts/validate_project.py`.
4. Active docs/prompts and old visual proposal paths reconciled to D-014.
5. Page/component inventories corrected against the supplied source.
6. CI validators and relevant tests updated for the new authority.
7. Repository reconciliation report, matrix, changelog and checklist committed.

### Remaining PR quality gates
- Run `python3 scripts/validate_project.py`.
- Run `python3 scripts/audit_m2_readiness.py`.
- Run `python3 -m unittest discover -s tests -v`.
- Complete final contextual stale-instruction and Markdown-link checks.
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
