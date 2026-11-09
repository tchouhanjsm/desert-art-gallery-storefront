# M2 — Private Prototype Entry Gate and Local Review Pipeline

**Status:** D-017 M2-A approval recorded; initial Revision 2 private prototype implemented and statically validated. Owner walkthrough and rendered browser acceptance remain outstanding.  
**Authority:** D-014, D-016 and the unchanged page/component inventories.  
**Scope:** Local/private validation and review only. D-017 approves Revision 2 for the bounded private prototype; production theme, public deployment and commerce remain outside scope.

## 1. Why this phase exists

D-016 authorizes six local/private, non-transactional prototype areas after explicit M2-A approval. D-017 records that approval for Revision 2 and binds it to the proposal SHA-256. The six areas are review groupings across the unchanged nine-page D-014 kit:

| D-016 review area | Exact D-014 pages |
|---|---|
| Homepage | `index.html` |
| Shop and Collections | `pages/shop.html`, `pages/collection.html` |
| Product Detail | `pages/product.html` |
| About and Makers | `pages/about.html`, `pages/makers.html` |
| Journal and Stories | `pages/journal.html`, `pages/article.html` |
| Contact and Support | `pages/contact.html` |

This phase builds the technical entry gate and local review pipeline in the public engineering repository. It does **not** put the private prototype, owner photographs, product data, or review screenshots in the public repository.

## 2. Mandatory entry conditions

The built prototype must continue to satisfy these entry and retention conditions:

1. The owner explicitly approves the M2-A proposal or records exact revisions in `docs/DECISIONS.md`.
2. The approval decision has a numbered decision reference and names the M2-A visual proposal.
3. The approved proposal revision is fixed by SHA-256. If the proposal changes later, the approval hash no longer matches and must be renewed.
4. The private prototype is created outside the Git repository.
5. All nine routes and the exact six-area grouping are preserved; no new HTML page is permitted.
6. Every image is accounted for in the private asset ledger as either an illustrative frame, a layout placeholder, or a genuine DAG photograph with rights, product mapping and separate private prototype-use evidence.
7. No external network resources, API calls, persistence, transaction endpoints or active form submission are included.

The validator does not create or imply owner approval. A manifest set to `pending` must fail. The repository's reusable manifest template remains deliberately pending; the private prototype's own manifest records D-017 and its proposal SHA-256.

## 3. Local prototype manifest

Copy `templates/private-prototype-manifest.template.json` into the private prototype directory as `prototype-manifest.json`. The schema is `schemas/private-prototype-manifest.schema.json`.

The manifest records:
- D-016 as the base authorization.
- The exact nine route paths and six area mappings.
- M2-A approval status, owner decision reference, approved proposal SHA-256 and date.
- An asset ledger for every referenced image.

Allowed image ledger entries:

| Asset kind | Required evidence |
|---|---|
| `illustrative_frame` | Exact visible label: “ILLUSTRATIVE IMAGE FRAME — DAG PHOTOGRAPH PENDING” |
| `layout_placeholder` | Exact visible label: “LAYOUT PLACEHOLDER — NOT A DAG PRODUCT” |
| `genuine_dag_photo` | Rights status and evidence; product-record reference; separate private prototype-use status and evidence |

A prototype-use approval is not public publication approval. The tool checks that evidence references exist as non-empty identifiers; it cannot prove that a rights claim or product fact is true. Keep actual evidence, source files and photographs private.

## 4. Static validation command

Run this from the repository after the private prototype directory exists:

```bash
python3 scripts/validate_private_prototype.py \
  --prototype-root "$HOME/Documents/DAG-private-prototype"
```

The root must be a real directory outside the public repository. The validator checks:
- M2-A approval and decision-register reference.
- Exact current proposal SHA-256.
- Exact D-014 route inventory and D-016 six-area grouping.
- English document language, one title, one main landmark and one H1 per page.
- Local-only links, stylesheets, scripts and image assets; no remote embeds, base URL overrides or meta-refresh navigation.
- Every referenced image has a matching asset-ledger record; placeholders use the exact visible label.
- Genuine DAG photos have cleared rights, product mapping and separate private prototype-use evidence.
- No network APIs, browser persistence, form-submit APIs, dynamic code execution, external endpoints, transaction destinations, POST forms or active form controls.
- Manifest values are type-checked and kept in parity with the JSON schema; asset-ledger paths must be normalized relative POSIX paths and each asset kind accepts only its declared fields.
- Inline event handlers, link `ping`, form-associated submission overrides and background/cross-context worker APIs are rejected. Owner approval dates must be real calendar dates.
- No symlinks or paths escaping the private prototype directory.
- No inline event-handler attributes, `ping` beacons, form override attributes, service-worker/worker registration or cross-context messaging APIs.
- Inline SVG image/symbol references are checked for local-only paths; image-type submit controls are rejected.

The repository's reusable validator template must remain pending and fail closed. The private prototype's own manifest records D-017, the approved proposal SHA-256 and the complete six-area/nine-route map. The validator does not create test products, images or example customer content.

## 5. Local Chromium review command

Install the isolated browser QA dependency on the local machine:

```bash
python3 -m pip install -r requirements-browser.txt
python3 -m playwright install chromium
```

After the static validator passes, run:

```bash
python3 scripts/private_prototype_browser_review.py \
  --prototype-root "$HOME/Documents/DAG-private-prototype" \
  --output-dir "$HOME/Documents/DAG-private-prototype-review"
```

The runner serves the prototype only on loopback (`127.0.0.1`) and blocks all browser requests to other hosts. It checks the nine pages at 390, 430, 768, 1280 and 1440 CSS-pixel widths, producing 45 page/viewport checks. It checks overflow, primary landmarks, image loading/alternatives, link/button names, duplicate IDs, disabled forms, native keyboard focus and the reduced-motion preference. It captures desktop/mobile screenshots for every page (18 images), plus JSON and Markdown summaries.

The runner also requires a viewport meta tag and records browser console errors, failed requests and HTTP resource responses at or above 400. A missing local stylesheet, script or image therefore fails review even when the page document itself returns HTTP 200. A symlinked prototype root is rejected before path resolution.

The output directory must be outside both the public repository and the prototype source directory. It is not uploaded to GitHub Actions, committed or shared by this tooling. Do not attach private screenshots, photos or source data to a public PR.

## 6. What this does not certify

The source-level JavaScript checks are conservative pattern checks, not a formal proof that arbitrary scripts are harmless. Browser network isolation provides a second boundary for local review, but neither tool makes untrusted prototype code safe to execute.

A passing result is static and automated engineering evidence only. It does not certify:
- Owner visual acceptance of the private prototype.
- Customer usability or market demand.
- Screen-reader behaviour, full WCAG conformance or legal compliance.
- The accuracy of the product facts, source records, image rights or consent evidence supplied in the ledger.
- Production readiness, transaction/security readiness or approval to deploy publicly.

The owner walkthrough in `docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md` remains the visual acceptance path. Participant research requires its own separate fieldwork authorization as recorded in D-016 and `docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md`.

## 7. Current gate status

- M2-A: approved under D-017 for the private prototype only; logo artwork, descriptor and production theme remain pending.
- M2-B: seven-person cohort approved as a plan; fieldwork/recruitment/privacy/cost authorization pending.
- M2-C: placeholder approach approved; genuine 10–20 product/photo sample and verified facts pending.
- M2-D: journey priority approved; automation passed; owner walkthrough and human usability acceptance pending.
- M2-E: initial six-area/nine-route local/private prototype implemented; owner walkthrough and rendered browser acceptance remain outstanding.

The private prototype is outside the public repository. D-014 source assets, page inventory, component inventory and QA-only token file remain unchanged. No production styling, deployment, transactions, real imagery, product facts or fieldwork is authorized by D-017.

## 8. PR #14 assurance-hardening validation

The expanded continuation hardening, including inline SVG resource and image-submit control checks, passed [DAG Project Quality run #143](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42511940719) at head `ac0d7474401c77c1eb8a805f65f8fac1e344624f`: repository foundation/source integrity, M2 owner-gate consistency, kit accessibility, documentation consistency, active Markdown links and **136/136 Python tests** passed. The private prototype's static review passed locally. Chromium navigation was attempted, but all navigation was blocked by the current execution environment (`net::ERR_BLOCKED_BY_ADMINISTRATOR`), including loopback and file URLs. No screenshot or browser-pass claim is made. Run the repository's local Chromium runner on the owner's machine after copying the private prototype folder.


## 9. Revision 2 private prototype implementation record

- Owner M2-A approval: D-017, 9 November 2026.
- Approved proposal SHA-256: `3608510164d5b56e46483f54f661737f7da37c41a7db8b0f665aa9d43ff8acaf`.
- Private prototype location at delivery: `/mnt/data/dag-private-prototype` (outside the public repository); distributable archive supplied separately to the owner.
- Nine HTML routes and six D-016 review groupings are implemented. Existing page/section counts are preserved: Home 5 sections; Shop 2; Collection 2; Product 1; About 3; Makers 2; Journal 2; Article 1; Contact 2.
- Static checks passed: exact route count, section/slot counts, internal links, local styles/scripts, English language, title/H1/main landmarks, disabled form controls, placeholder labels, no remote resources, no external navigation, no persistence/transaction/network APIs, CSS parse and JavaScript syntax.
- No photograph binary is included; the asset ledger is empty and all visual image areas are explicit placeholders. The owner-provided 10–20 product/photo sample remains pending.
- Rendered browser checks at 390, 430, 768, 1280 and 1440 pixels remain outstanding because Chromium navigation was blocked by the execution environment. This is not recorded as a passing browser test.


## 9. Revision 2 private prototype implementation record

- Owner M2-A approval: D-017, 9 November 2026.
- Approved proposal SHA-256: `3608510164d5b56e46483f54f661737f7da37c41a7db8b0f665aa9d43ff8acaf`.
- Private prototype location at delivery: `/mnt/data/dag-private-prototype` (outside the public repository); distributable archive supplied separately.
- Nine HTML routes and six D-016 review groupings are implemented. Existing page/section counts are preserved: Home 5 sections; Shop 2; Collection 2; Product 1; About 3; Makers 2; Journal 2; Article 1; Contact 2.
- Static checks passed: exact route count, section/slot counts, internal links, local styles/scripts, English language, title/H1/main semantics, disabled form controls, placeholder labels, no remote resources, no external navigation, no persistence/transaction/network APIs, CSS parsing and JavaScript syntax.
- No photograph binary is included; the asset ledger is empty and all visual image areas are explicit placeholders. The owner-provided 10–20 product/photo sample remains pending.
- Rendered browser checks at 390, 430, 768, 1280 and 1440 pixels remain outstanding because Chromium navigation was blocked by the execution environment. This is not recorded as a passing browser test.
