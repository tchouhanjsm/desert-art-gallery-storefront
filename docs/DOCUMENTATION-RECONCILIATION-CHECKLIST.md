# Repository-Wide Documentation Reset — Completion Checklist

**Audit baseline:** main at `a4b665f81433e98cd78469e0a1bc1bb81a3528df`  
**Owner archive SHA-256:** `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`  
**Baseline tracked paths audited:** 140

## Authority and owner decisions

- [x] Exact eight-level hierarchy documented in `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`.
- [x] Root `AGENTS.md` separated owner-approved specs (level 5) and inventories (level 6).
- [x] Root README and handoff follow the same order.
- [x] Design authority explicitly governs every nested prompt, README, code comment, source file, workflow and issue template.
- [x] D-014 remains structural-only; no owner identity values or new owner decisions invented.
- [x] D-010 remains only the POJ-primary/Macaroni-secondary reference hierarchy; it does not import reference-site functionality.
- [x] D-007's old four-option AI selection procedure remains superseded.
- [x] P-015 remains rejected; P-016 remains superseded/historical.
- [x] D-013 six-route model remains superseded by D-014.
- [x] M2-A to M2-E and U-001 to U-010 retain their recorded open/pending statuses.

## Owner archive and implementation

- [x] Supplied ZIP read successfully.
- [x] Archive SHA-256 recorded and matches D-014 adoption archive.
- [x] Archive contains exactly 25 files: nine HTML, four CSS, one JS, eleven kit governance/readme/handoff files.
- [x] All 25 files are present in the agreed repository path (verified by existing D-014 inventory/validator).
- [x] All 14 original HTML/CSS/JS assets were verified at PR #8 adoption.
- [x] PR #9's two documented CSS accessibility maintenance amendments remain hash-pinned.
- [x] No structural kit source was redesigned or re-extracted in this reset.

## Documentation repository audit

- [x] 140 tracked baseline paths enumerated from Git.
- [x] All root/nested AGENTS, READMEs, handoffs and prompts included in the audit.
- [x] All Markdown design, creative direction, visual system, implementation, business, research, quality, roadmap and decision documents classified.
- [x] HTML/CSS/JS source, theme tokens, source comments, workflows and issue templates included in path inventory.
- [x] Scripts and tests classified.
- [x] Catalogue, prototype and research templates (including CSV files) classified.
- [x] Full per-path matrix generated in `docs/DOCUMENTATION-RECONCILIATION-MATRIX.md`.
- [x] Unchanged technical/business knowledge retained where valid.
- [x] Active visual-option paths remain non-operative stubs; full old material remains archived.
- [x] Nine superseded historical Markdown files receive a mandatory non-operative banner.
- [x] No files removed; no useful legacy technical/business knowledge discarded.

## Stale instruction prevention

- [x] New tracked-file-aware `scripts/audit_documentation_consistency.py` added.
- [x] New automated consistency tests added.
- [x] Source validator checks the eight-level order and known stale kit-materialization instructions.
- [x] Workflow executes the repository-wide consistency audit.
- [x] Historical mentions in decisions/audit reports are not treated as active instructions.
- [ ] Final consistency audit passes on the committed PR head (pending CI).
- [ ] Final Markdown internal-link audit passes on the committed PR head (pending CI).

## Remaining owner/visual constraints preserved

- [x] Final colours remain owner-controlled and pending.
- [x] Typography/type hierarchy remains owner-controlled and pending.
- [x] Logo/wordmark/descriptor remains owner-controlled and pending.
- [x] Photography direction/cropping remains owner-controlled and pending.
- [x] Layout-only system tokens remain QA-only.
- [x] English-only customer-facing UI remains active.
- [x] No fabricated product, maker, provenance, pricing, policy or business content added.
- [x] No extra pages, sections, controls, banners, testimonials, widgets, animations or functions added.
- [x] No production app, stack, commerce flow, deployment, research recruitment or paid services started.

## Final validation and review

- [ ] `python3 scripts/validate_project.py` — pending final CI.
- [ ] `python3 scripts/audit_m2_readiness.py` — pending final CI.
- [ ] `python3 scripts/audit_kit_accessibility.py` — pending final CI.
- [ ] `python3 scripts/audit_documentation_consistency.py` — pending final CI.
- [ ] `python3 scripts/audit_documentation_links.py` — pending final CI.
- [ ] `python3 -m unittest discover -s tests -v` — pending final CI.
- [ ] Complete PR diff reviewed and no unrelated implementation changes found.
- [ ] PR merged.

A checked item records a source/repository fact already verified in this reset. Items under final validation remain unchecked until the final PR head's actual GitHub Actions results are available.
