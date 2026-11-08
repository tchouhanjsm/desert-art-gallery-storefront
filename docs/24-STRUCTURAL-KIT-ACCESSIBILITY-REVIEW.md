# 24 — Structural Kit Accessibility Review

**Review date:** 2026-11-08
**Baseline:** D-014; design/owner-controlled-kit-v2/
**Scope:** Static source review and narrowly scoped accessibility maintenance. This is not a visual redesign, brand approval or production acceptance.

## Source baseline and change boundary

PR #8 installed the 25-file owner kit and verified all 14 original HTML/CSS/JS implementation assets byte-for-byte against the supplied archive. This follow-up changes only two existing CSS files:

- **styles/components.css** — adds an authored :focus-visible outline (2px solid currentColor, 3px offset). It inherits the existing text colour and introduces no palette, colour token or typography value.
- **styles/layout.css** — adds a prefers-reduced-motion: reduce rule that changes the existing smooth-scroll behaviour to scroll-behavior: auto.

The nine HTML pages, page structure, JavaScript prototype, token fallback, responsive breakpoints, controls, form labels, placeholders and disabled states remain unchanged. Twelve of the original 14 implementation assets remain byte-identical to the owner archive; the two amended CSS files are now checked against their current reviewed Git blob hashes by scripts/validate_project.py.

## Static findings and treatment

| Review area | Static observation | Treatment |
|---|---|---|
| Document language | All 9 pages declare English (lang=en). | Retained. |
| Main landmark | All 9 pages contain exactly one main landmark with id=main-content. | Retained for landmark navigation. |
| Page heading | All 9 pages contain exactly one h1. | Retained. |
| Mobile navigation | All 9 pages have a named toggle, aria-expanded, aria-controls and a matching labelled navigation landmark. The supplied script updates the expanded state. | Retained; no menu behaviour added. |
| Form/control labels | Shop and Collection sort selects are wrapped by Sort labels; Product variant has its existing for/id label; Contact input and textarea are nested within existing labels. | Retained; disabled states unchanged. |
| Keyboard focus | Original CSS had no authored :focus-visible treatment. | Added an outline using currentColor; no brand colour selected. |
| Reduced motion | Original layout CSS enabled smooth scrolling without a reduced-motion override. | Added an override for prefers-reduced-motion: reduce. |
| Skip link | No explicit skip link is supplied. Each page has a main landmark. | No new component added because the component inventory is closed. |
| Brand contrast | Production colour tokens are not approved; the fallback uses system/browser values. | Not assessed or claimed. |

## Static checks

The read-only audit script scripts/audit_kit_accessibility.py checks all nine source pages for:
- English document language.
- Exactly one main landmark with the expected target ID.
- Exactly one page-level heading.
- A mobile-navigation toggle with an accessible name, expanded state and valid navigation target.
- An authored :focus-visible treatment that uses currentColor.
- A reduced-motion rule that disables the existing smooth scrolling.

tests/test_kit_accessibility.py checks these rules and verifies that the existing disabled controls and their labels remain present.

## Not yet verified

This report does not claim:
- Browser-rendered layout acceptance at 390, 430, 768, 1280 or 1440 CSS-pixel widths.
- Real keyboard traversal or visible-focus quality in each browser.
- Screen-reader behaviour with VoiceOver, NVDA or another assistive technology.
- Touch-target adequacy or zoom/reflow behaviour.
- WCAG conformance or final colour-contrast ratios.
- Production visual identity, photography, copy or content approval.

Those checks require actual browser and assistive-technology review. Final colour-contrast acceptance remains blocked until the owner supplies exact brand tokens; do not substitute the system fallback or a historic proposal.

## Scope and decision boundary

No pages, sections, components, navigation items, features, product claims, images, external dependencies, brand tokens or production behaviours were added. Search, filter/sort, variant, purchase and enquiry controls remain disabled. D-014 and M2-A through M2-E owner gates remain unchanged.

The next technical acceptance step is browser/keyboard review of all nine pages at the specified viewport widths. Any proposed visible or structural addition, including a skip-link component, must be handled through the owner change-control process.
