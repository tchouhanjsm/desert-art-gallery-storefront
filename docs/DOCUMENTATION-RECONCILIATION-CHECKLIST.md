# Documentation Reconciliation Checklist — DAG v2

## Authority and scope
- [x] Root agent guidance updated to define authority hierarchy.
- [x] Design authority and documentation source-of-truth documents updated.
- [x] Nine-page inventory transcribed from the owner-supplied kit.
- [x] Closed component and disabled-control inventory transcribed.
- [x] D-014 recorded; former D-013 six-page scope marked superseded.
- [x] Japan-first / English-only distinction retained.
- [x] Owner-only brand decisions retained; layout-only tokens are not production tokens.
- [x] POJ primary / Macaroni secondary reference hierarchy retained.
- [x] No-fabrication and no-production-development boundaries retained.

## Repository-wide reconciliation
- [ ] All old visual direction boards and their SVGs moved to a historical, non-operative archive.
- [ ] Old P-015/P-016 specs replaced with historical stubs or archived without active instructions.
- [ ] Former six-route M2 spec and worksheet archived or rewritten to nine-page contract.
- [ ] AI bootstrap, working protocol, visual gate prompts and nested README files updated.
- [ ] All technical, catalogue, research, merchant and content docs checked for contradictions.
- [ ] CI validators and tests no longer require rejected options or the former six-page scope.
- [ ] Complete path-level matrix updated to observed final dispositions (current matrix includes proposed actions, not proof of completion).

## Source-kit installation
- [ ] All 25 original kit files extracted under `design/owner-controlled-kit-v2/`.
- [ ] Nine HTML page paths present and internal CSS/JS references resolve.
- [ ] Original HTML/CSS/JS bytes compare exactly to the supplied archive.
- [ ] Both inventories and governance documents are present in the kit directory.
- [ ] No unsupplied UI, content, sections, components or interactions have been added.
- [ ] `tokens-layout-only.css` remains QA-only; no production brand palette/fonts selected.

## Final quality gate
- [ ] Run `python3 scripts/validate_project.py`.
- [ ] Run `python3 scripts/audit_m2_readiness.py`.
- [ ] Run `python3 -m unittest discover -s tests -v`.
- [ ] Run stale instruction searches distinguishing active docs from historical archives.
- [ ] Validate every Markdown link and every kit file reference.
- [ ] Inspect Git diff for product code, privacy, fabricated data and accidental asset migration.
- [ ] Confirm PR CI is green before merge.

A checked box means the evidence is visible on the branch or in a recorded run. Do not mark a check complete based only on intention or a local result that is no longer available.
