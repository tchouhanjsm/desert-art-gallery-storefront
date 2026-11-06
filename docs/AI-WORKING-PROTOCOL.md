# AI Working Protocol

## Purpose
A repeatable protocol for every new AI chat, coding agent and autonomous session. The repository, not conversational memory, is the source of truth.

## Session start
1. Read root `AGENTS.md`.
2. Read `README.md`.
3. Read `docs/DECISIONS.md`.
4. Read `docs/10-ROADMAP.md`.
5. Read the project charter and task-relevant design/architecture docs.
6. Inspect branch, working tree, repository state and open PRs if tools allow.
7. Identify current milestone and acceptance criteria.
8. Separate verified facts, assumptions, proposals and blockers.

## Before proposing work
- Identify the customer/business problem.
- Inspect existing work and dependencies.
- Check whether a decision already exists.
- Distinguish proposal from approved direction.
- Define measurable acceptance criteria.
- Avoid creating work that belongs to another active PR.

## During work
- Use a focused branch and reviewable commits.
- Preserve unrelated changes.
- Do not silently change commercial/legal assumptions.
- Do not fabricate product or business content.
- Add tests for meaningful behaviour.
- Update documents when an owner decision changes.
- Never bypass failing checks or misreport results.

## Design-specific protocol
- Do not use the old storefront as the visual starting point.
- Study POJ Studio and Macaroni Shoten; record dated observations and source URLs.
- Develop at least four materially different creative territories.
- Specify exact HEX values, font family/weights/licensing, layout and photography direction.
- Use actual rendered desktop/mobile examples, not descriptions or swatches alone.
- Present neutral trade-offs; do not recommend, rank, score, badge, preselect or select a winner.
- Ask the owner to choose, combine, request revisions or reject all options.
- Stop before final tokens, production theme or global visual styling until an explicit owner choice is recorded.

## Autonomous execution
Proceed independently on reversible in-scope documentation, research, option exploration, code and tests. Do not ask routine questions about ordinary implementation details.

Stop for owner decisions involving foundational visual identity, seller jurisdiction, sales territory, currency, tax, shipping commitments, returns, legal identity, payment commitments, spending, subscriptions, production data, irreversible actions or sensitive credentials.

When one owner decision blocks a feature, isolate it and continue unrelated safe work.

## Completion review
- Review the entire diff.
- Run relevant format, lint, type, unit, integration and build checks available in the chosen stack.
- Inspect rendered routes for UI changes.
- Verify English-only customer-facing content.
- Confirm no fabricated claims or test fixtures leaked into production content.
- Record screenshots only if actually captured and reviewed.
- Report limitations accurately.

## Current visual owner gate

**THE AI PROPOSES. THE OWNER CHOOSES. THE AI IMPLEMENTS.**

Four proposals are documented in `docs/15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md` and rendered in `design/explorations/visual-directions.html`; separate desktop/mobile captures are in `design/explorations/rendered/`. The previous Material Archive / Collected Colour synthesis is historical only, not a default or recommendation. Do not rank or recommend the four options. Ask the owner to select, combine, request revisions or reject all four, then stop. No final design tokens or production theme may be implemented before that explicit choice.

## New-chat continuity
At each major milestone, update `10-ROADMAP.md` and `DECISIONS.md`. Produce a short handover referencing files, commits and PRs. Never rely on the chat alone for durable project knowledge.
