# Documentation Reconciliation Checklist — DAG v2

## Authority and scope
- [x] Root `AGENTS.md` establishes the authority hierarchy and D-014 baseline.
- [x] Root `README.md` identifies the installed source and nine-page scope.
- [x] `docs/DESIGN-AUTHORITY.md` and `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md` define control boundaries.
- [x] D-014 recorded; D-013 six-page scope marked superseded.
- [x] P-015 explicitly rejected; P-016 and Material Archive / Collected Colour historical only.
- [x] Japan-first / English-only distinction retained.
- [x] Owner-only brand decisions remain pending.
- [x] Layout-only system tokens remain QA fallback, not production brand tokens.
- [x] Closed page and component inventories reflect the supplied kit.
- [x] Disabled controls and no-production/no-additions boundary documented.

## Source kit
- [x] All 25 kit files materialized under `design/owner-controlled-kit-v2/`.
- [x] Nine supplied HTML pages present.
- [x] Four supplied CSS files present.
- [x] Supplied prototype JavaScript present.
- [x] Eleven kit-local README/authority/inventory/governance files present and reconciled to D-014.
- [x] At PR #8 adoption, all 14 original HTML/CSS/JS assets were byte-verified against the owner ZIP using Git blob SHA-1.
- [x] PR #9 amends only styles/components.css and styles/layout.css for focus visibility and reduced motion; the other 12 implementation assets remain byte-identical.
- [x] Validator enforces the exact 25-file inventory and current hashes for all 14 implementation assets.
- [x] CI run confirms source-integrity validator passes (run 62).

## Repository-wide reconciliation
- [x] Root README and AGENTS updated.
- [x] Active design/creative direction, visual system, photography and information architecture docs reconciled.
- [x] Technical, quality, roadmap and design review docs reconciled.
- [x] AI bootstrap, working protocol and owner-gate prompt updated.
- [x] Owner decision and owner-input registers updated.
- [x] Six-route M2 acceptance pack replaced with nine-page D-014 acceptance contract.
- [x] Old visual board/spec files moved to historical archive; active paths retired.
- [x] Old M1 review and six-route M2 worksheet/pack preserved historically.
- [x] Photo, catalogue, Etsy, research and merchant materials retained where still valid.
- [x] CI validator, M2 readiness audit and affected tests updated.
- [x] Contextual stale-instruction search completed across active design, decision, prompt, research and template documents; retained matches are explicitly historical or scoped as reference observations.
- [x] Final path-level matrix spot-check completed against the 101-file PR diff and current tracked tree.

## Accessibility maintenance
- [x] Existing nine-page landmarks, headings, navigation state and labels inspected at source level.
- [x] Shared :focus-visible outline uses currentColor; no brand token added.
- [x] Existing smooth-scroll behaviour respects prefers-reduced-motion.
- [x] No HTML page, component inventory item, control, section or interaction added.
- [x] Static audit and regression tests added; browser/assistive-technology checks remain pending.

## Quality gate
- [x] `python3 scripts/validate_project.py` — PASS in GitHub Actions run 62.
- [x] `python3 scripts/audit_m2_readiness.py` — PASS in GitHub Actions run 62; five owner gates remain open as intended.
- [x] `python3 -m unittest discover -s tests -v` — PASS; 77 tests.
- [x] `python3 scripts/audit_documentation_links.py` — PASS in GitHub Actions run 62.
- [x] Contextual stale-term search completed; P-015/P-016 references are historical/rejected and reference-site feature observations are explicitly scoped as non-requirements.
- [x] Reviewed the complete 101-file PR diff; no production application code, catalogue payloads, photo binaries or unapproved feature additions were introduced.
- [x] PR #8 branch validation run 62 was green; PR #8 subsequently merged after run 63 and main-branch run 64 passed. PR #9 is a separate follow-up.

A checked box indicates evidence exists on the branch or in a recorded run. Do not mark CI or local checks complete until the actual results are known.

- [ ] Rendered browser review at 390, 430, 768, 1280 and 1440 CSS-pixel widths (not completed by this source-only pass).
- [ ] Keyboard and assistive-technology review (not completed by this source-only pass).
