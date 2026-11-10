# Owner Walkthrough Record Validation — Private Review Support

**Status:** Tooling implemented in PR #16; owner visual acceptance remains pending until the owner completes and confirms a private record.  
**Authority:** D-016, D-017 and the unchanged D-014 route/component inventories.  
**Purpose:** Prepare and validate the six-area owner walkthrough described in [26 — M2 Owner Review Walkthroughs](26-M2-OWNER-REVIEW-WALKTHROUGHS.md).

## What the helper does

- Validates one private owner-authored JSON record for the exact six review areas: Homepage; Shop and Collections; Product Detail; About and Makers; Journal and Stories; Contact and Support.
- Requires the five already-approved review widths for every decided area: 390, 430, 768, 1280 and 1440 CSS pixels.
- Captures the five review dimensions already listed in the walkthrough: visual hierarchy/density; image ratio/crop/placeholder clarity; content/factual evidence gaps; navigation/shared shell; keyboard focus/disabled states.
- Requires route- and component-scoped requested changes for request_revision and reject decisions.
- Allows OWNER_VISUAL_ACCEPTED only when all six areas are accepted, all 30 area/viewport reviews are marked reviewed, and the record explicitly carries owner confirmation and dates.
- Writes a private JSON and Markdown readiness summary. The generated summary omits free-text observations and requested-change text.

This is an evidence-format validator, not a review agent or identity/signature service. It cannot establish who completed the record, verify that a visual review genuinely happened, validate factual claims or grant approval. The owner must inspect the actual local/private prototype and author the record. It does not perform usability research.

## Create and complete a private record

From the repository root, copy the deliberately pending template to a private location outside the Git checkout:

    mkdir -p "$HOME/Documents/DAG-owner-walkthrough"
    cp templates/owner-walkthrough-record.template.json \
      "$HOME/Documents/DAG-owner-walkthrough/owner-walkthrough.json"

Edit only that private copy. For each of the six areas:
1. Review all five widths listed in viewport_reviews.
2. Mark each width reviewed and add a short observation, or mark it blocked with the reason.
3. Record all five observation categories. Use a clear statement such as “Reviewed; no outstanding issue” where appropriate; do not leave a category blank for a decided area.
4. Set the area decision to accept, request_revision or reject. A revision/rejection requires an exact D-014 route, component and requested change.
5. Keep decisions pending while review is incomplete. Do not mark owner confirmation until all six areas are accepted.

The template contains only the six area IDs, existing route/width contract and blank fields. It includes no product data, photography, fabricated review notes or private paths.

## Validate and generate the private summary

    python3 scripts/validate_owner_walkthrough.py \
      --record "$HOME/Documents/DAG-owner-walkthrough/owner-walkthrough.json" \
      --output-dir "$HOME/Documents/DAG-owner-walkthrough/report"

The command produces owner-walkthrough-readiness.json and owner-walkthrough-readiness.md in the private report directory. It never edits the source record or prototype, refuses symlinked input/output roots, refuses paths inside the public repository and will not overwrite existing reports. Files are created with owner-only permissions where supported by the host OS.

Exit results:
- 0 — OWNER_VISUAL_ACCEPTED: all six areas accepted, 30/30 viewport reviews recorded and owner confirmation present.
- 1 — review is incomplete, a revision was requested or an area was rejected. A summary is still generated so the remaining work is visible.
- 2 — malformed record, invalid scope, unsafe path or report-write error. No readiness report is written for an invalid record.

## Acceptance boundary

A successful report records the owner's stated visual acceptance of the D-016/D-017 local/private, non-transactional prototype only. It does not authorize:
- Publishing the prototype or product data.
- Customer/participant recruitment, contact, consent, recording or fieldwork.
- Checkout, payment, orders, shipping, tax, returns or live enquiry.
- A production framework, database, CMS, hosting provider or deployment.
- Use of genuine product photography without the separate identity, facts, rights and prototype-use evidence gates.

The genuine 10–20 product/photo sample remains a separate M2-C owner-input dependency. Human customer usability research remains blocked on separate fieldwork authorization. The D-014 nine pages, six navigation destinations, section/component inventory and disabled controls are unchanged.
