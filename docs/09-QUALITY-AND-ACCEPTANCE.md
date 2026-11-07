# 09 — Quality and Acceptance

## Governing design scope

Use D-014 and the active inventories only. The nine-page source kit defines structure and disabled states. This is not approval of brand identity, production copy, commerce behaviour or an application stack.

## Structural acceptance

- Preserve the supplied nine page files and their page/section order.
- Preserve original HTML, CSS, responsive rules, JavaScript and component inventory.
- Preserve all explicit placeholders and disabled controls.
- Do not add or remove pages, shell items, components, sections or functionality.
- Keep customer-facing language English-only.
- Do not fabricate product, maker, material, dimension, provenance, price, inventory, review, contact, policy or delivery claims.
- Do not copy proprietary content, assets, CSS or branded layouts from reference sites.

## Responsive and accessibility review

Review all supplied pages at 390, 430, 768, 1280 and 1440 CSS-pixel widths. Record actual observations for overflow, clipping, reading order, navigation, touch target access, focus visibility, image behaviour and content hierarchy. These are review widths, not fixed breakpoints. Preserve the kit's design unless the owner approves a scoped correction.

Test semantic HTML, heading hierarchy, accessible names, keyboard operation, visible focus, reduced motion and colour contrast once an owner-approved brand identity exists. System fallback tokens are not evidence of final brand contrast.

## Brand identity gate

Final colour roles/HEX values, typefaces/weights/hierarchy/type scale, logo/wordmark/descriptor and photography art direction/crop rules remain owner-controlled and pending. Do not create an AI-selected option set, recommend a direction, select a winner or use P-015/P-016 values as defaults. Record the owner's exact choices in `docs/DECISIONS.md` and `docs/OWNER-TOKEN-INPUT.md` before branded styling.

## Functional boundary

Disabled Search, filter/sort, option/purchase and enquiry-form concepts stay disabled. No cart, checkout, account, wishlist, live search/filter/sort, payment, order, shipping calculation or returns functionality is in scope.

## Delivery evidence

A task is complete only when actual checks have been run and recorded. Run the repository validators and unit tests after the kit is materialized and validators have been reconciled. Do not report unrun checks as passing. Review the full diff and disclose remaining limitations.
