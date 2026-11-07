# AI Working Protocol

## Session start
1. Read root `AGENTS.md` and `README.md`.
2. Read `docs/DECISIONS.md`, `docs/DESIGN-AUTHORITY.md` and `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`.
3. Read the active page and component inventories.
4. Inspect current Git state, branch, changed paths, existing PRs and test configuration.
5. Distinguish confirmed decisions, proposals, assumptions and unresolved owner inputs.

## Authority and scope
D-014 adopts the owner-controlled nine-page DAG v2 structural kit. Preserve supplied HTML/CSS/responsive styles, page and section order, prototype script, component structure, placeholders and disabled states. Follow only the active inventories. The former six-page scope is superseded by D-014.

Customer-facing content remains English-only. Japan-first does not imply Japanese UI or settle seller jurisdiction, sales territories, currency, tax/duties, shipping, payments or returns. Never invent business or product facts.

## Owner-controlled identity
The owner alone approves exact colours, typography, logo/wordmark/descriptor and photography direction/crops. These remain pending. Do not select or recommend a palette, typeface, visual territory or default. `tokens-layout-only.css` is QA fallback only. P-015 is rejected; P-016 is historical only.

## No additions
Do not add pages, sections, navigation, shell elements, components, banners, testimonials, badges, ratings, reviews, icons, widgets, animations, popups, sticky/floating elements, chat, newsletter/social or any functionality not explicitly listed in the component inventory. Existing disabled controls remain disabled.

No cart, checkout, account, wishlist, live search/filter/sort, payment, orders, shipping calculation, returns workflow or enquiry backend is authorized.

## Engineering discipline
- Make focused, reviewable changes on the correct branch.
- Preserve unrelated work.
- Reconcile instructions rather than appending contradictory notes.
- Do not invent application frameworks, databases or hosting architecture.
- Add or update tests for changed validation logic.
- Run relevant checks and report exact outcomes.
- Inspect the full diff before proposing a merge.
- Never bypass failing checks or claim unrun tests pass.

## Stop conditions
Stop for owner decisions on brand identity, legal seller/jurisdiction, sales territory, currency, tax, shipping commitments, returns, payment commitments, sensitive credentials, spending, irreversible actions or scope expansion. Continue independent safe documentation and quality work.

## Repository-wide reconciliation
When a source or decision changes, inspect all tracked AGENTS, READMEs, Markdown, prompts, HTML/CSS/JS, token/theme files, comments, workflows, issue templates, scripts and tests. Classify affected files RETAIN, UPDATE, SUPERSEDE, ARCHIVE or REMOVE. Update report, matrix, checklist, changelog, README and decisions as applicable. Run contextual stale-instruction and internal-link checks.

## Completion
Record actual routes and viewport sizes inspected, checks run, commit/PR identifiers and unresolved limitations. No implementation is complete solely because a plan or document exists.
