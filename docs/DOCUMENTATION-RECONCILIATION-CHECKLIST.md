# Repository-Wide Documentation Reset — Completion Checklist

**Audit baseline:** main at `a4b665f81433e98cd78469e0a1bc1bb81a3528df`  
**Decision update:** D-017 recorded 9 November 2026; M2-A Revision 2 approved for private prototype.
**Owner archive SHA-256:** `64ad72784abf7fdd24b01f48f6ea832bf40424a518793eb80c7cfa23effaa8cd`  
**Baseline tracked paths audited:** 140

## Authority and owner decisions

- [x] Exact eight-level hierarchy documented in `docs/DOCUMENTATION-SOURCE-OF-TRUTH.md`.
- [x] Root `AGENTS.md` separated owner-approved specs (level 5) and inventories (level 6).
- [x] Root README and handoff follow the same order.
- [x] Design authority explicitly governs every nested prompt, README, code comment, source file, workflow and issue template.
- [x] D-014 remains structural-only; D-017 records the owner's explicit M2-A Revision 2 approval for private-prototype use.
- [x] D-010 remains only the POJ-primary/Macaroni-secondary reference hierarchy; it does not import reference-site functionality.
- [x] D-007's old four-option AI selection procedure remains superseded.
- [x] P-015 remains rejected; P-016 remains superseded/historical.
- [x] D-013 six-route model remains superseded by D-014.
- [x] M2-A Revision 2 approval recorded under D-017; M2-B fieldwork, M2-C genuine sample evidence and U-001 to U-010 retain their separate open/pending statuses.

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
- [x] Final consistency audit passes on the committed PR #10 head (GitHub Actions run #77).
- [x] Final Markdown internal-link audit passes on the committed PR #10 head (GitHub Actions run #77).

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

## Follow-up after merged PR #11

- [x] PR #11 merged into main at `95079bbb5ccf6aaf888d4523a5adfda582ab448c`.
- [x] The three newly tracked browser-QA paths are individually classified in the reconciliation matrix.
- [x] PR #11's responsive Product Detail fix is reflected in the current owner-source history and CSS asset-integrity hash.
- [x] Dedicated Chromium workflow run #5 passed 45/45 page/viewport combinations (nine pages × five widths).
- [x] Reduced-motion, keyboard-focus and mobile-navigation checks passed; no overflow, browser page errors or failed local assets were reported.
- [x] 18 full-page screenshots and JSON/Markdown summaries were published as the PR #11 CI artifact.
- [ ] Re-run the complete project-quality workflow after PR #10 is based on the PR #11 main commit.

## Final validation and review

- [x] `python3 scripts/validate_project.py` — PASS (GitHub Actions run #77).
- [x] `python3 scripts/audit_m2_readiness.py` — PASS (GitHub Actions run #77).
- [x] `python3 scripts/audit_kit_accessibility.py` — PASS (GitHub Actions run #77).
- [x] `python3 scripts/audit_documentation_consistency.py` — PASS (GitHub Actions run #77).
- [x] `python3 scripts/audit_documentation_links.py` — PASS (GitHub Actions run #77).
- [x] `python3 -m unittest discover -s tests -v` — PASS (GitHub Actions run #77).
- [ ] Complete PR diff reviewed and no unrelated implementation changes found.
- [ ] PR merged.

A checked item records a source/repository fact already verified in this reset. Items under final validation remain unchecked until the final PR head's actual GitHub Actions results are available.


## D-016 M2 owner decision and prototype-scope reconciliation

- [x] D-016 recorded the POJ-primary / Macaroni-secondary reference hierarchy and one reference-led visual proposal; approval remains pending.
- [x] Seven-person Japan qualitative cohort approved as a research plan; external recruitment, contact, consent, recording and any spend remain separately unauthorized.
- [x] Placeholder and image-frame approach approved; real product/photo sample and image validation remain pending; no full-library migration.
- [x] Five-journey priority confirmed; responsive automated coverage is retained; human owner/customer usability acceptance remains outstanding.
- [x] Exactly six local/private non-transactional prototype areas authorized after M2-A visual approval; no public repository prototype, production app or public deployment.
- [x] Decision, owner register, reference log, M2 pack, roadmap, visual proposal, research operations, walkthroughs, catalogue guidance, governance and regression audits reconciled.
- [x] D-014 nine-page HTML/CSS/JS structural kit, inventories and QA-only token fallback retained unchanged.
- [ ] Owner approval of the M2-A visual proposal.
- [ ] Owner supplies approximately 10–20 genuine product photographs and verified product information.
- [ ] Separate fieldwork authorization (recruitment route, consent/privacy, data handling and budget).
- [ ] Private six-area prototype build after visual approval.
- [ ] Owner-led walkthrough and any separately authorized human usability research.


## M2 private prototype tooling reconciliation — 8 November 2026

- [x] Added the manifest schema and pending template for the exact D-016 private prototype boundary.
- [x] Added a static validator enforcing private-root, M2-A decision/proposal hash, exact route/area, asset-evidence, network and transaction checks.
- [x] Added a local-only Chromium runner that requires static validation first and writes review artifacts outside the public repository.
- [x] Added regression tests for both the static validation rules and the browser runner's M2-A entry gate.
- [x] Reconciled README, AGENTS, roadmap, M2 acceptance pack, changelog and path-level matrix.
- [x] M2-A visual approval and D-017 decision recorded.
- [ ] Owner supplies 10–20 genuine product photographs and verified facts.
- [ ] Create the six private prototype areas under D-017; keep all assets/reports outside the public repository.
- [ ] Run the local/private validator and browser review against the actual private prototype.
- [ ] Complete owner visual walkthrough; customer usability testing remains separately authorized.


## PR #16 owner walkthrough record-support overlay — 10 November 2026

- [x] Added a deliberately pending template for the six D-016 review areas and five established viewport widths.
- [x] Added a local validator for area decisions, five observation dimensions, viewport coverage and route/component-scoped requests.
- [x] Designed the private readiness summary to exclude free-text observations and requested-change descriptions.
- [x] Added repository-boundary, symlink, no-overwrite and output-permission protections.
- [x] Added regression tests for incomplete, accepted, revision, rejected and invalid record states.
- [ ] Complete the actual owner-led walkthrough and record owner confirmation outside Git.
- [ ] Supply and validate the genuine 10–20 product/photo evidence sample for M2-C.
- [ ] Obtain separate authorization before any M2-B participant recruitment or fieldwork.

The checklist items above distinguish preparation tooling from owner action. They do not mark the owner visual-acceptance gate as complete.


## PR #16 M2-C photo-audit pair-integrity overlay — 10 November 2026

- [x] The photo-audit JSON summary records the SHA-256 digest of its exact CSV inventory.
- [x] Catalogue intake rejects missing, malformed or cross-run photo-audit pairs even when candidate counts match.
- [x] Regression tests cover digest emission, missing digest and same-count report substitution.
- [ ] Owner supplies the genuine 10–20 product/photo sample and corresponding complete photo-audit outputs.
- [ ] Owner-led factual/source/rights review and prototype-use evidence remain pending.

The automated digest proves report-file pairing only. It does not prove image rights, product identity, content truth or owner approval.


## PR #16 M2-B fieldwork authorization preflight overlay — 10 November 2026

- [x] Added the private eight-item D-016 fieldwork authorization schema and pending template.
- [x] Added fail-closed validation of the fixed seven-person cohort and all eight approval states.
- [x] Added required checks for moderator/language, participant information/consent, recording mode, data retention/deletion, vendor/transfer, research spend cap and scheduling.
- [x] Added private blocker reports that omit evidence references and enforce private-path, symlink and no-overwrite controls.
- [x] Added regression tests for pending/complete/rejected states and malformed/unsafe authorization records.
- [ ] Owner genuinely approves all eight fieldwork items in writing and confirms the complete scope.
- [ ] Obtain separate informed consent from each participant; obtain separate consent before any optional recording.
- [ ] Only after those gates, separately determine and authorize actual recruitment, contact, interviews, data handling, recording and spend.

The preflight checks the record only; it does not authenticate the owner, verify evidence artifacts, initiate fieldwork or establish legal/privacy/ethics compliance. M2-B fieldwork remains unauthorized.