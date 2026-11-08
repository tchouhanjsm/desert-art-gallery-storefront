# M2 — Private Prototype Entry Gate and Local Review Pipeline

**Status:** Readiness tooling implemented; actual prototype build is still gated by explicit M2-A visual approval.  
**Authority:** D-014, D-016 and the unchanged page/component inventories.  
**Scope:** Local/private validation and review only. This document does not approve a visual identity or start prototype styling.

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

Before a branded private prototype can be built:

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
- No symlinks or paths escaping the private prototype directory.

The command is intentionally expected to fail until M2-A is explicitly approved and a complete prototype/manifest is supplied. It does not create test products, images or example customer content.

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

The output directory must be outside both the public repository and the prototype source directory. It is not uploaded to GitHub Actions, committed or shared by this tooling. Do not attach private screenshots, photos or source data to a public PR.

## 6. What this does not certify

A passing result is static and automated engineering evidence only. It does not certify:
- Owner visual acceptance of the private prototype.
- Customer usability or market demand.
- Screen-reader behaviour, full WCAG conformance or legal compliance.
- The accuracy of the product facts, source records, image rights or consent evidence supplied in the ledger.
- Production readiness, transaction/security readiness or approval to deploy publicly.

The owner walkthrough in `docs/26-M2-OWNER-REVIEW-WALKTHROUGHS.md` remains the visual acceptance path. Participant research requires its own separate fieldwork authorization as recorded in D-016 and `docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md`.

## 7. Current gate status

- M2-A: proposal prepared; explicit owner visual approval pending.
- M2-B: seven-person cohort approved as a plan; fieldwork/recruitment/privacy/cost authorization pending.
- M2-C: placeholder approach approved; genuine 10–20 product/photo sample and verified facts pending.
- M2-D: journey priority approved; automation passed; owner walkthrough and human usability acceptance pending.
- M2-E: six-area local/private prototype scope conditionally authorized; branded implementation must wait for M2-A approval.

Until these gates are satisfied, the validator and browser runner are readiness tooling only. The D-014 kit, page inventory, component inventory and QA-only token file remain unchanged.
