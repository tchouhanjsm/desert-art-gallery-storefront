# M2 — Private Prototype Entry Gate and Local Review Pipeline

**Status:** Revision 4 private prototype built outside the public repository; D-017, responsive, journey, content-evidence and semantic checks passed. Owner visual acceptance remains pending.  
**Authority:** D-014, D-016 and the unchanged page/component inventories.  
**Scope:** Local/private prototype validation and owner-review preparation only. D-017 approves the Revision 2 visual values for this private prototype; production styling and public deployment remain unauthorized.

## 1. Why this phase exists

D-016 conditionally authorizes six local/private, non-transactional prototype areas only after the owner explicitly approves the single M2-A visual proposal. The six areas are review groupings across the unchanged nine-page D-014 kit:

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

Before accepting the private prototype for owner review:

1. The owner explicitly approves the M2-A proposal or records exact revisions in `docs/DECISIONS.md`.
2. The approval decision has a numbered decision reference and names the M2-A visual proposal.
3. The approved proposal revision is fixed by SHA-256. If the proposal changes later, the approval hash no longer matches and must be renewed.
4. The private prototype is created outside the Git repository.
5. All nine routes and the exact six-area grouping are preserved; no new HTML page is permitted.
6. Every image is accounted for in the private asset ledger as either an illustrative frame, a layout placeholder, or a genuine DAG photograph with rights, product mapping and separate private prototype-use evidence.
7. No external network resources, API calls, persistence, transaction endpoints or active form submission are included.

The validator does not create or imply owner approval. A manifest set to `pending` must fail. The current manifest template is deliberately pending.

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

The private prototype manifest binds to D-017 and the approved proposal SHA-256. The validator must pass before responsive or journey browser reviews. It does not create test products, images or example customer content.

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

## 6. Five-journey browser review

Run the five owner-approved journeys after the static manifest validator passes:

```bash
python3 scripts/private_prototype_journey_review.py \\
  --prototype-root "$HOME/Documents/DAG-private-prototype" \\
  --output-dir "$HOME/Documents/DAG-private-prototype-journey-review"
```

The runner checks these five journeys at 390, 430, 768, 1280 and 1440 CSS-pixel widths (25 journey/viewport combinations):

1. Discover DAG: Homepage → Shop → Product Detail. Checks the Jaisalmer identity cue, three existing category slots and four curated product slots.
2. Browse: Shop → Collection → Product Detail. Checks that Filter and Sort remain disabled on both catalogue routes.
3. Evaluate: Product Detail. Checks the three existing thumbnail frames, four native information accordions, and disabled Options/Purchase controls.
4. Makers and stories: About → Makers → Journal → Article. Checks the two About editorial splits, maker profile layout, six Journal story slots and article body.
5. Contact: Product Detail → Contact. Checks the gallery information panel, four still-pending contact facts and disabled enquiry fields/submit control with no write endpoint.

The runner uses Playwright and in-memory rendering of the exact local HTML/CSS/JS. It intercepts anchor clicks, resolves relative destinations with the browser URL algorithm, and renders the selected route from the private root. This avoids browser policies that block local HTTP/file navigation; it does not claim to test a hosted server. External assets are not loaded; the static validator rejects external resources before the journey run. JSON and Markdown summaries are written outside both the public repository and the prototype source directory.

The 9-page responsive review and the five-journey review are separate: the first produces 45 route/viewport checks and 18 screenshots; the second produces 25 journey/viewport checks. Both are local/private. Do not upload private prototype files, screenshots or review outputs to GitHub.

## 7. What this does not certify

The source-level JavaScript checks are conservative pattern checks, not a formal proof that arbitrary scripts are harmless. Browser network isolation provides a second boundary for local review, but neither tool makes untrusted prototype code safe to execute.

A passing result is static and automated engineering evidence only. It does not certify:
- Owner visual acceptance of the private prototype.
- Customer usability or market demand.
- Screen-reader behaviour, full WCAG conformance or legal compliance.
- The accuracy of the product facts, source records, image rights or consent evidence supplied in the ledger.
- Production readiness, transaction/security readiness or approval to deploy publicly.

The owner walkthrough in `docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md` remains the visual acceptance path. Participant research requires its own separate fieldwork authorization as recorded in D-016 and `docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md`.

## 8. Current gate status

- M2-A: Revision 2 visual direction approved under D-017; private prototype implementation authorized.
- M2-B: seven-person cohort approved as a plan; fieldwork/recruitment/privacy/cost authorization pending.
- M2-C: placeholder approach approved; genuine 10–20 product/photo sample and verified facts pending.
- M2-D: five journeys automated at five widths; 25/25 checks passed; owner walkthrough and human usability acceptance pending.
- M2-E: six-area local/private prototype built; 45/45 responsive checks and 25/25 journey checks passed; owner visual acceptance pending.

The validator and browser runners are mandatory acceptance gates for the private prototype; the owner walkthrough remains the visual acceptance step. The D-014 kit, page inventory, component inventory and QA-only token file remain unchanged.

## 9. PR #14 assurance-hardening validation

The expanded continuation hardening, including inline SVG resource and image-submit control checks, passed [DAG Project Quality run #143](https://github.com/tchouhanjsm/desert-art-gallery-storefront/actions/runs/42511940719) at head `ac0d7474401c77c1eb8a805f65f8fac1e344624f`: repository foundation/source integrity, M2 owner-gate consistency, kit accessibility, documentation consistency, active Markdown links and **136/136 Python tests** passed. At the time of PR #14, the private Chromium review was not executed because no M2-A-approved private prototype existed. That historical gate is now satisfied under D-017; the subsequent private review evidence is recorded in docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md.


## 10. Private prototype refinements — Revisions 3 and 4

### Revision 3 — D-017 visual system and navigation

The private prototype was aligned to the approved D-017 baseline without changing the D-014 routes, sections or components:
- Applied the six approved colour roles, Source Serif 4 / Inter stacks, approved type hierarchy, spacing scale, 1440px content width, desktop/mobile gutters, square-edged cards and 16:9 / 4:5 / 1:1 image frames. Removed off-palette treatments, gradients and shadows.
- Added current-page/current-section semantics to the six existing navigation destinations across all nine routes.
- Improved the existing mobile disclosure: Escape closes and restores focus to the toggle, selecting a link closes it, and resizing to desktop clears the expanded state.
- Balanced the third existing homepage category card within the existing two-column mobile grid.

### Revision 4 — Content evidence and semantics

The local private prototype has been refined without adding/removing any D-014 route or component:
- Every existing image frame has a visible label and matching accessible name describing the evidence role expected in that slot; each remains explicitly illustrative and pending.
- Exact image slot counts are checked for all nine pages (11, 6, 3, 4, 2, 1, 6, 1, 0).
- The four Product Detail facts use semantic dl/dt/dd markup and retain pending owner-verification values.
- The existing breadcrumbs on Collection, Product Detail and Article use a named navigation landmark and one current-page item.
- Article introduction, publication date, authorship and source credits remain explicitly pending.
- Mobile product-fact label/value rows are checked at all five review widths.

The journey runner validates these conditions at every rendered start/destination page in addition to the D-017 visual and navigation gates. The browser review also confirms zero horizontal overflow across 45 route/viewport combinations. Revision 4's actual private HTML/CSS/JS, screenshots and reports remain outside GitHub.

