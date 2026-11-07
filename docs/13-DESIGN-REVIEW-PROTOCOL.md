# 13 — Design Review Protocol

## Current source

D-014 adopts the owner-controlled v2 HTML/CSS kit as the active structural source. Review its nine pages using the exact page and component inventories. Do not treat earlier exploration boards or design specs as current implementation references.

## Reference hierarchy

D-010 remains active: POJ Studio is the primary reference for ecommerce/page structure; Macaroni Shoten is secondary for curation/select-shop character. Study non-proprietary experience principles only. Do not copy code, CSS, exact branded compositions, text, photography, logos, fonts or protected assets.

## Review scope

Review the actual supplied nine pages, shared shell and components at 390, 430, 768, 1280 and 1440 CSS-pixel widths. Record date, route, viewport, observed behaviour, issues and evidence. Check keyboard navigation, semantic structure, visible focus, responsive overflow, placeholder clarity and disabled control states.

## Closed scope

No additional page, section, navigation item, banner, testimonial, badge, rating, review, icon, widget, animation, popup, sticky/floating item, chat, newsletter, social module, search/filter/sort functionality or commerce feature may be introduced without explicit owner approval and inventory amendment.

## Owner-controlled brand identity

Final colours, typography families/weights/hierarchy/type scale, logo/wordmark/descriptor and photography direction/cropping remain pending. The layout-only system tokens are QA fallback only. The AI must not choose, rank or synthesize a brand direction. P-015 is rejected; P-016 is historical only. Use `docs/OWNER-TOKEN-INPUT.md` to record owner-supplied values and `docs/DECISIONS.md` for approvals.

## Evidence and acceptance

A screenshot is not evidence of inspection unless the rendered route and viewport were actually reviewed. Distinguish proposed, owner-approved, implemented and visually verified states. Do not claim page, browser, accessibility or CI checks that were not performed.
