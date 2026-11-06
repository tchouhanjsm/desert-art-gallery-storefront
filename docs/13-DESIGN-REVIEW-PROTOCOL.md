# 13 — Design Review Protocol

## Principal design references

Our principal references are:

- **POJ Studio:** https://pojstudio.com/
- **Macaroni Shoten:** https://shop.macaro-ni.jp/

These are DAG's primary references for creative and retail study. Study their actual editorial presentation, merchandising, product discovery, navigation, typography, photography and responsive customer experience. Learn from their principles, but do not copy their assets, exact layouts, content or brand identity. DAG must express its own Jaisalmer textile, object and craft identity.

## Purpose
Prevent superficial redesigns and ensure visual direction is reviewed as an actual customer experience.

## Design status
Every major design asset or decision must be marked:
- Exploration.
- Proposed.
- Owner-approved.
- Implemented.
- Visually verified.
- Retired.

An AI agent cannot approve its own proposal.

## Required evidence for a major design proposal
- Rationale and intended customer benefit.
- Reference observations with source URLs and access dates.
- Palette and typography specimens.
- Page composition and component samples.
- Responsive layouts.
- Actual rendered HTML/CSS prototypes.
- Explanation of alternatives considered.
- Known limitations and content dependencies.

## Required page review
Review complete rendered pages, not only hero mockups:
- Homepage.
- Shop/category.
- Product detail.
- About/Makers.
- Journal.
- Contact.
- Cart/checkout concept.

## Viewports
At minimum: 390px, 430px, 768px, 1280px and 1440px.

## Review questions
- Does this look and behave like a premium curated retail experience?
- Is it unmistakably DAG rather than a generic template?
- Are products central?
- Is merchandising substantial without becoming cluttered?
- Is whitespace purposeful?
- Is hierarchy clear?
- Are product details readable?
- Do mobile layouts feel designed rather than merely stacked?
- Are stories and claims authentic?
- Is the customer journey obvious?
- Does the design learn from POJ Studio and Macaroni Shoten without cloning them?

## Anti-superficial-change test
A redesign is not accepted if it only changes colour values, spacing, font sizes, border radii or decorative effects while retaining the same weak composition and merchandising.

Compare old and proposed experiences at equivalent routes and viewports when an old design exists. For this new repository, compare the proposal against the approved creative brief and reference analysis.

## Review record
For each major review, record:
- Date.
- Routes and viewports.
- Screenshots and prototype path.
- What works.
- What fails.
- Required corrections.
- Owner decision.

## Owner-controlled visual selection

**THE AI PROPOSES. THE OWNER CHOOSES. THE AI IMPLEMENTS.**

A visual review package must present at least four materially distinct options, each with exact palette roles/HEX values, font families/weights/licensing, layout/component examples, image art direction, contrast checks and actual desktop/mobile renders. Include neutral strengths, trade-offs and risks. The AI must not recommend, rank, score or identify a winner. The owner may choose, combine, request changes or reject all. Stop until the owner decision is explicit and recorded in `DECISIONS.md`. Do not create production tokens or theme styling before that gate.

Current proposal package: [four-direction specifications](15-FOUR-VISUAL-DIRECTION-SPECIFICATIONS.md) and [rendered board](../design/explorations/visual-directions.html). The historic Material Archive / Collected Colour synthesis is not an approved default.
