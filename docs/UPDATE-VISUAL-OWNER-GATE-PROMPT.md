# Owner-Controlled Brand Identity — Current Instruction

Repository: https://github.com/tchouhanjsm/desert-art-gallery-storefront

D-014 adopts an owner-supplied structural HTML/CSS kit. This does not approve final DAG brand identity.

## Required behaviour
1. Preserve the source kit's original HTML, CSS, responsive styles, script, route/section order and component inventory.
2. Do not redesign the kit, add sections/components, add functionality or invent content.
3. Do not select or recommend brand colours, typography, logo/wordmark/descriptor, photography direction or cropping.
4. Treat `styles/tokens-layout-only.css` as system/browser QA fallback only, not a brand theme.
5. Keep customer-facing UI English-only.
6. P-015 is rejected; P-016 and Material Archive / Collected Colour are historical only. Do not revive or blend those proposals.
7. Keep all existing disabled controls disabled.
8. Record exact owner-supplied brand inputs in `docs/OWNER-TOKEN-INPUT.md` and approved decisions in `docs/DECISIONS.md`.

## Scope boundary
No new pages, sections, shell elements, badges, promotions, reviews, ratings, widgets, popups, sticky/floating features, animation, chat, newsletter/social or extra navigation. No cart, checkout, accounts, wishlist, live search/filter/sort, payments, order flow, shipping calculations, returns or enquiry backend.

## Authorization boundary
D-014 does not authorize production application development, framework/backend selection, public deployment, paid services or commercial/legal decisions. Any new visible or functional scope requires a written proposal and explicit owner approval followed by inventory amendment.

## Reconciliation
Update all conflicting active prompts, docs, validators, tests and workflows. Preserve useful historical evidence with a clear **HISTORICAL — NOT ACTIVE — DO NOT IMPLEMENT** label. Report exact files changed and checks actually run.
