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
- [x] All 14 original HTML/CSS/JS assets byte-verified against the owner ZIP using Git blob SHA-1.
- [x] Validator enforces exact 25-file inventory and all 14 source-asset hashes.
- [ ] CI run confirms source integrity validator passes.

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
- [ ] Complete tracked-path stale-instruction pass recorded.
- [ ] Final path-level matrix spot-check against the complete Git tree.

## Quality gate
- [ ] Run `python3 scripts/validate_project.py`.
- [ ] Run `python3 scripts/audit_m2_readiness.py`.
- [ ] Run `python3 -m unittest discover -s tests -v`.
- [ ] Validate internal Markdown links.
- [ ] Complete contextual stale-term search and distinguish active vs historical matches.
- [ ] Review complete PR diff for fabricated data, accidental product changes, scope additions or private data.
- [ ] Confirm GitHub Actions is green before merge.

A checked box indicates evidence exists on the branch or in a recorded run. Do not mark CI or local checks complete until the actual results are known.
