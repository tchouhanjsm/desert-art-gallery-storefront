# 04 — Structural Visual System

## Status

D-014 adopts the owner-supplied HTML/CSS kit as a structural baseline only. It does not approve a DAG brand identity, final visual system or production theme.

## Source files

The intended source directory is `design/owner-controlled-kit-v2/`. Its original `styles/layout.css`, `styles/components.css`, `styles/responsive.css` and `styles/tokens-layout-only.css` must be preserved unchanged unless the owner authorizes an exact defect fix.

## Layout-only tokens

`tokens-layout-only.css` uses browser/system canvas colours and system fonts for structural and responsive QA. It is not a DAG palette, neutral brand identity or production token set. Do not select, rename, promote or extend these values into brand tokens.

## One proposal prepared — owner approval pending

D-016 authorizes one reference-led DAG visual proposal, documented in [27 — M2-A Reference-Led Visual Proposal](27-M2-A-REFERENCE-LED-VISUAL-PROPOSAL.md). All proposed HEX values, font recommendations, hierarchy, component rules and photography direction remain unapproved. They are not active design tokens. Do not copy them into the D-014 kit or a private prototype until the owner explicitly approves the proposal.

## Owner-only identity inputs

Final colours and roles, typefaces/weights/hierarchy/type scale, logo/wordmark/descriptor and photography art direction/cropping remain pending explicit owner approval of the M2-A proposal or a subsequent owner decision. Record exact owner-approved values in `docs/OWNER-TOKEN-INPUT.md` and `docs/DECISIONS.md` before any branded styling work.

## No-additions boundary

Do not add unlisted sections, components, pages, visual effects, icons, banners, testimonials, badges, reviews, animations, popups, sticky/floating UI, chat/newsletter/social modules or functionality. Do not enable controls supplied as disabled.

## Quality

Maintain semantic markup, accessible labels, keyboard focus and responsive behaviour without changing the approved visual contract. Validate actual supplied pages at 390, 430, 768, 1280 and 1440 CSS-pixel review widths. These are review widths, not breakpoints to impose.
