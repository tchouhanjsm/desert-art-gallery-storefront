# 04 — Structural Visual System

## Status

D-014 adopts the owner-supplied HTML/CSS kit as a structural baseline only. It does not approve a DAG brand identity, final visual system or production theme.

## Source files

The intended source directory is `design/owner-controlled-kit-v2/`. Its original `styles/layout.css`, `styles/components.css`, `styles/responsive.css` and `styles/tokens-layout-only.css` must be preserved unchanged unless the owner authorizes an exact defect fix.

## Layout-only tokens

`tokens-layout-only.css` uses browser/system canvas colours and system fonts for structural and responsive QA. It is not a DAG palette, neutral brand identity or production token set. Do not select, rename, promote or extend these values into brand tokens.

## Owner-only identity inputs

Final colours and roles, typefaces/weights/hierarchy/type scale, logo/wordmark/descriptor and photography art direction/cropping remain pending owner input. Record exact owner-approved values in `docs/OWNER-TOKEN-INPUT.md` and `docs/DECISIONS.md` before any branded styling work.

## No-additions boundary

Do not add unlisted sections, components, pages, visual effects, icons, banners, testimonials, badges, reviews, animations, popups, sticky/floating UI, chat/newsletter/social modules or functionality. Do not enable controls supplied as disabled.

## Quality

Maintain semantic markup, accessible labels, keyboard focus and responsive behaviour without changing the approved visual contract. Validate actual supplied pages at 390, 430, 768, 1280 and 1440 CSS-pixel review widths. These are review widths, not breakpoints to impose.
