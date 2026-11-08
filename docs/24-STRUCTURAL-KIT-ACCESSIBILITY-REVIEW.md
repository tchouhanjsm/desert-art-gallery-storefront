# 24 — Structural Kit Accessibility and Browser Review

**Review date:** 2026-11-08  
**Baseline:** D-014; `design/owner-controlled-kit-v2/`  
**Scope:** Static source review, narrowly scoped accessibility maintenance, and automated Chromium responsive/interaction review. This is not a brand redesign, production acceptance or WCAG certification.

## Source baseline and change boundary

PR #8 installed the 25-file owner kit and verified all 14 original HTML/CSS/JS implementation assets byte-for-byte against the supplied archive.

PR #9 amended two existing CSS files:
- **styles/components.css** — adds a `:focus-visible` outline (2px solid `currentColor`, 3px offset).
- **styles/layout.css** — respects `prefers-reduced-motion: reduce` for the existing smooth-scroll rule.

The first Chromium browser review then exposed a real mobile defect in the supplied Product Detail gallery: the three-column thumbnail grid retained 220px automatic minimum tracks, forcing the gallery and its information column to 684px wide at 390px and 430px viewport widths.

PR #11 corrects that defect in **styles/responsive.css** at the existing 640px mobile breakpoint:
- Constrains the Product Detail grid to a shrinkable single track.
- Allows the existing gallery and information grid items to shrink.
- Uses three `minmax(0, 1fr)` thumbnail tracks.
- Removes the thumbnail placeholders' conflicting 220px minimum height so their existing square aspect ratio can size to the available mobile width.

The three supplied thumbnail slots remain in the same order. No HTML, route, page section, control, label, component, supplied JavaScript or desktop/tablet breakpoint is changed. Three of the original 14 implementation assets now contain narrowly scoped, documented CSS maintenance; the other 11 remain byte-identical to the owner archive. The current asset hashes are enforced by `scripts/validate_project.py`.

## Static findings and treatment

| Review area | Static observation | Treatment |
|---|---|---|
| Document language | All 9 pages declare English (`lang=en`). | Retained. |
| Main landmark | All 9 pages contain exactly one main landmark with `id=main-content`. | Retained. |
| Page heading | All 9 pages contain exactly one h1. | Retained. |
| Mobile navigation | All 9 pages have a named toggle, `aria-expanded`, `aria-controls` and a matching labelled navigation landmark. | Supplied JavaScript is retained and exercised in Chromium. |
| Form/control labels | Shop and Collection sort selects are labelled; Product variant has its existing `for/id` label; Contact input and textarea remain nested within labels. | Retained; disabled states unchanged. |
| Keyboard focus | Shared `:focus-visible` rule uses `currentColor`. | Retained; no brand token introduced. |
| Reduced motion | Existing smooth scrolling is disabled under `prefers-reduced-motion: reduce`. | Retained and browser-checked. |
| Product Detail mobile gallery | Original thumbnail grid expanded to 684px at narrow widths because of automatic minimum grid tracks. | Corrected at the existing mobile breakpoint without changing slot count or markup. |
| Brand contrast | Production colour tokens are not approved; fallback uses system/browser values. | Not assessed or claimed. |

## Automated browser review

The dedicated workflow `.github/workflows/kit-browser-review.yml` runs Playwright with Chromium for all nine supplied routes at **390, 430, 768, 1280 and 1440 CSS-pixel widths** (45 route/viewport combinations).

Checks include:
- HTTP document response and four local stylesheet loads.
- Exactly one h1 and one `main#main-content`.
- Horizontal document overflow.
- Desktop versus mobile navigation visibility.
- Mobile navigation open/close and `aria-expanded` state.
- Keyboard focus-visible outline.
- Browser page errors and failed local document/style/script requests.
- Reduced-motion computed style.
- Full-page screenshots for each route at 390px and 1440px, plus JSON and Markdown summaries.

The first real run completed **43/45** route/viewport checks and correctly failed only Product Detail at 390px and 430px. It reported a document width of 700px and identified the three 220px thumbnail tracks as the cause. The responsive correction above is now included; the post-fix workflow result must be checked before this review can be marked green.

The workflow artifact is diagnostic evidence, not owner visual sign-off. It does not claim screen-reader coverage, WCAG conformance, final colour contrast, or review in every browser engine.

## Not yet verified

- Screen-reader behaviour with VoiceOver, NVDA or another assistive technology.
- Touch-target adequacy and zoom/reflow behaviour.
- WCAG conformance or final colour-contrast ratios.
- Brand identity, photography, copy or factual catalogue approval.
- Owner's final rendered visual acceptance.

Final colour-contrast acceptance remains blocked until the owner supplies exact brand tokens; do not substitute system fallback values or historic proposals.

## Scope and decision boundary

No pages, sections, components, navigation items, features, product claims, images, brand tokens or production behaviours were added. Search, filter/sort, variant, purchase and enquiry controls remain disabled. D-014 and M2-A through M2-E owner gates remain unchanged.
