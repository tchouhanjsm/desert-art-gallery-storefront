# Update the DAG repository: enforce owner-controlled creative direction

Repository: https://github.com/tchouhanjsm/desert-art-gallery-storefront

The owner does not want the AI agent to choose the brand palette or typography by itself.

## Assignment
Update authoritative repository instructions so the owner, not the AI agent, controls foundational visual identity decisions.

Read `AGENTS.md`, `docs/03-CREATIVE-DIRECTION.md`, `docs/04-VISUAL-DESIGN-SYSTEM.md`, `docs/09-QUALITY-AND-ACCEPTANCE.md`, `docs/DECISIONS.md` and `docs/AI-WORKING-PROTOCOL.md`.

## Mandatory behaviour
1. The agent must never independently finalize DAG's palette, typography, visual personality or art direction.
2. It must prepare at least four materially distinct visual territories.
3. Options must not all be beige, grey, ivory, greige or muted earth tones.
4. Each option must have exact HEX colours, font families/weights, layout examples, component examples and photography direction.
5. Render desktop and mobile examples. Swatches or text-only proposals are insufficient.
6. Present neutral trade-offs. Do not label a winner.
7. Ask the owner to choose, combine, request revisions or reject all options.
8. Stop before final design tokens or production visual styling are implemented.
9. After selection, record exact values and the decision ID; follow them.
10. Routine implementation within the approved design system may proceed without asking.

Remove contradictory instructions that give the AI unilateral authority to choose the final palette or style. Preserve historical research but withdraw its former recommendation as a default.

This is documentation governance and visual exploration only. Do not build the production application, select a framework or implement a final theme.

Report exact files changed and checks actually run.
