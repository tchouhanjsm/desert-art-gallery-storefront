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
- Study references and record concrete observations with URLs and access dates.
- Explore alternatives before choosing a direction.
- Use actual rendered prototypes, not descriptions alone.
- Review full pages at mobile, tablet and desktop sizes.
- Mark designs as exploration/proposed/approved/implemented/verified.
- Do not self-approve.

## Autonomous execution
Proceed independently on reversible in-scope design, documentation, code and test tasks. Do not ask routine questions about ordinary implementation details.

Stop for owner decisions involving seller jurisdiction, sales territory, currency, tax, shipping commitments, returns, legal identity, payment commitments, spending, subscriptions, production data, irreversible actions or sensitive credentials.

When one decision blocks a feature, isolate it and continue unrelated safe work.

## Completion review
- Review the entire diff.
- Run relevant format, lint, type, unit, integration and build checks available in the chosen stack.
- Inspect rendered routes for UI changes.
- Verify English-only customer-facing content.
- Confirm no fabricated claims or test fixtures leaked into production content.
- Record screenshots only if actually captured and reviewed.
- Report limitations accurately.

## Completion report
Include objective, milestone, files changed, decisions/assumptions, actual tests and results, visual evidence, risks, owner decisions and documentation updates.

## Current M1 handoff

The M1 research and creative proposal package is in `docs/14-JAPAN-FIRST-CUSTOMER-RESEARCH.md`, `docs/15-CREATIVE-DIRECTION-OPTIONS.md`, `docs/16-COMMERCIAL-MODEL-ASSESSMENT.md` and `docs/M1-OWNER-REVIEW.md`. The recommended direction is Material Archive with the product-discovery clarity of Collected Colour. It is a proposal, not an owner-approved decision. Do not start M2 production work or mark the territory approved until the owner responds.

## New-chat continuity
At each major milestone, update `10-ROADMAP.md` and `DECISIONS.md`. Produce a short handover referencing files, commits and PRs. Never rely on the chat alone for durable project knowledge.
