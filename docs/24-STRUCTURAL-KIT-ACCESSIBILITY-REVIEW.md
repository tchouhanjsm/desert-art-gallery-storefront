# 24 — Structural Kit Accessibility and Browser Review

**Review date:** 2026-11-08  
**Baseline:** D-014; `design/owner-controlled-kit-v2/`  
**Scope:** Static semantic review, narrowly scoped accessibility maintenance, and automated Chromium responsive/keyboard review. This is not a brand redesign, production acceptance, screen-reader sign-off or WCAG certification.

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

The three supplied thumbnail slots remain in the same order. No HTML, route, page section, control, label, component, supplied JavaScript or desktop/tablet breakpoint is changed. Three of the original 14 implementation assets now contain narrowly scoped, documented CSS maintenance; the other 11 remain byte-identical to the owner archive. The current asset hashes are enforced by `scripts/validate_project.py`. PR #12 changes only repository QA scripts and tests: no supplied HTML, CSS or JavaScript asset is modified by that PR.

## Static findings and treatment

| Review area | Static observation | Treatment |
|---|---|---|
| Document language | All 9 pages declare English (`lang=en`). | Retained. |
| Main landmark | All 9 pages contain exactly one main landmark with `id=main-content`. | Retained. |
| Page heading | All 9 pages contain exactly one h1. | Retained. |
| Mobile navigation | All 9 pages have a named toggle, `aria-expanded`, `aria-controls` and a matching labelled navigation landmark. | Supplied JavaScript is retained; Chromium verifies pointer operation and native Enter/Space activation with `aria-expanded` and focus retention. |
| Form/control labels | Shop and Collection sort selects are labelled; Product variant has its existing `for/id` label; Contact input and textarea remain nested within labels. | Retained; disabled states unchanged. |
| Keyboard focus | Shared `:focus-visible` rule uses `currentColor`. | Retained; no brand token introduced. |
| Reduced motion | Existing smooth scrolling is disabled under `prefers-reduced-motion: reduce`. | Retained and browser-checked. |
| Product Detail mobile gallery | Original thumbnail grid expanded to 684px at narrow widths because of automatic minimum grid tracks. | Corrected at the existing mobile breakpoint without changing slot count or markup. |
| Semantic relationships | Unique IDs, named links/buttons/navigation, programmatic control labels, image alternatives and ARIA ID references are checked by a standard-library HTML parser and browser DOM audit. | PR #12 adds source and rendered-DOM regression coverage. |
| Brand contrast | Production colour tokens are not approved; fallback uses system/browser values. | Not assessed or claimed. |

## Automated browser review

The dedicated workflow `.github/workflows/kit-browser-review.yml` runs Playwright with Chromium for all nine supplied routes at **390, 430, 768, 1280 and 1440 CSS-pixel widths** (45 route/viewport combinations).

Checks include:
- HTTP document response and four local stylesheet loads.
- Exactly one h1 and one `main#main-content`.
- Horizontal document overflow.
- Desktop versus mobile navigation visibility.
- Mobile navigation open/close and `aria-expanded` state.
- Native Enter and Space activation on the existing mobile navigation button, with focus retention.
- DOM semantics: accessible names, labelled form controls, image alternatives, unique IDs, valid `aria-controls` / `aria-labelledby` targets and no positive `tabindex`.
- Keyboard focus-visible outline.
- Browser page errors and failed local document/style/script requests.
- Reduced-motion computed style.
- Full-page screenshots for each route at 390px and 1440px, plus JSON and Markdown summaries.

The first real run completed **43/45** route/viewport checks and correctly failed only Product Detail at 390px and 430px. It reported a document width of 700px and identified the three 220px thumbnail tracks as the cause. After the responsive correction, Chromium workflow run **#4** passed **45/45** route/viewport checks across all nine pages and five widths; reduced-motion, keyboard-focus and mobile-navigation checks passed, with no browser errors, failed local assets or overflow. The run produced 18 full-page screenshots and JSON/Markdown summaries in CI artifact `dag-kit-browser-review-4-3aac02d8b2244f4caa5b862fc5fb93ccfd4aebf7`.

The workflow artifact is diagnostic evidence, not owner visual sign-off. It does not claim screen-reader coverage, WCAG conformance, final colour contrast, or review in every browser engine.

PR #12 added semantic and keyboard-operation checks without modifying the supplied HTML, CSS or JavaScript. On PR #12 head `d5ad89d768ef641ed865d1f4e16fae70ef101f10`, GitHub Actions [DAG Structural Kit Browser Review run #7](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42466004123) passed **45/45** route/viewport combinations, **54** native Enter/Space mobile navigation sequences across nine pages at 390px, 430px and 768px, and the reduced-motion check. No horizontal overflow, browser page errors or failed local document/style/script assets were reported. The run uploaded 18 full-page screenshots plus JSON and Markdown summaries in artifact `dag-kit-browser-review-7-c0381a76d2298ab2a1077c4ce754ee19bbb6a9b3`. The companion [DAG Project Quality run #79](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42466004185) passed the foundation, owner-gate, accessibility, documentation and link audits and the complete **89-test** Python suite.

## M2 structural journey coverage added on the active M2 branch

The M2 branch adds five journeys using only links and controls already present in D-014:
1. Home → Shop → Collection (discover).
2. Shop → Collection → Product (browse).
3. Product information accordions and verification that variant/purchase remain disabled (evaluate).
4. About → Makers → Journal → Article (contextualise).
5. Product → Enquire → Contact, with supplied form controls/submission still disabled (support).

Each journey is executed at 390, 430, 768, 1280 and 1440 CSS-pixel widths (25 journey/viewport combinations). On final PR #13 head, [Chromium Browser Review run #15](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483140888) passed 25/25 journey/viewport combinations, the existing nine-page × five-width matrix (45 checks), 54 mobile Enter/Space focus-retention sequences and reduced-motion. It uploaded 18 full-page screenshots plus JSON/Markdown summaries in [artifact 13617964823](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483140888/artifacts/13617964823). Companion [Project Quality run #88](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42483140897) passed all audits and 101/101 Python tests. This evidence is structural automation, not human usability or owner visual acceptance.

## Not yet verified

- Screen-reader behaviour with VoiceOver, NVDA or another assistive technology.
- Touch-target adequacy and zoom/reflow behaviour.
- WCAG conformance or final colour-contrast ratios.
- Brand identity, photography, copy or factual catalogue approval.
- Owner's final rendered visual acceptance.

Final colour-contrast acceptance remains blocked until the owner supplies exact brand tokens; do not substitute system fallback values or historic proposals.

## Scope and decision boundary

No pages, sections, components, navigation items, features, product claims, images, brand tokens or production behaviours were added. Search, filter/sort, variant, purchase and enquiry controls remain disabled. D-014 and M2-A through M2-E owner gates remain unchanged.
