# M2-B — Private Fieldwork Authorization Preflight

**Status:** Preflight tooling implemented in PR #16. **Fieldwork remains unauthorized.**
**Authority:** D-016 and the existing seven-person research plan in docs/28-M2-B-RESEARCH-OPERATIONS-PLAN.md.

## Purpose and boundary

D-016 accepts the seven-person Japan-based cohort as a research plan. It does not authorize recruitment, external contact, participant-data collection, recording, incentives or spending. The research plan requires eight separate written approvals before fieldwork.

This helper prepares and validates a private owner-authored authorization record. It does not contact anyone, recruit, screen, schedule, interview, collect or process participant data, begin recording, engage a vendor, or make a payment. No fieldwork has been started by this implementation.

## The eight required approvals

1. Chosen recruitment route/provider and screening approach.
2. Final invitation text and screener.
3. Moderator and session language.
4. Participant information sheet and consent/recording wording.
5. Private data storage, access, retention and deletion arrangements.
6. Exact participant incentive and recruitment/moderator spend ceiling.
7. Vendor terms, processing/subcontracting and transfer arrangements.
8. Date range and scheduling plan.

The fixed D-016 cohort is preserved by the template: 3 home/interior, 2 craft/material, 1 trade/design and 1 gift/considered-purchase participant. The validator rejects changed cohort counts.

## Create a private authorization record

From the repository root, copy the deliberately pending template to private storage outside the checkout:

    mkdir -p "$HOME/Documents/DAG-fieldwork-authorization"
    cp templates/m2b-fieldwork-authorization.template.json \
      "$HOME/Documents/DAG-fieldwork-authorization/authorization.json"

Complete the private copy only after the owner has reviewed the actual evidence and made each separate decision. For every approval, set status to approved, add its actual approval date and a stable private evidence reference. Do not use placeholder references to simulate approval.

The remaining fieldwork_details fields require explicit values: moderator reference and supported languages; participant-information and consent references; recording mode; storage/access/retention/deletion; vendor and transfer decisions; research-only currency and total spend ceiling; and the schedule/timezone. The research budget currency is only for the approved research-spend cap. It does not decide the storefront's base or display currency.

Recording must remain not_authorized until the owner explicitly selects no_recording or optional_separate_participant_consent. Optional recording also requires a separate recording-consent wording reference. Even then, every participant must separately consent before their own session is recorded.

## Run the private preflight

Use a different private output directory, outside both the record's folder and the public repository:

    python3 scripts/validate_m2b_fieldwork_authorization.py \
      --record "$HOME/Documents/DAG-fieldwork-authorization/authorization.json" \
      --output-dir "$HOME/Documents/DAG-fieldwork-authorization-report"

The helper writes m2b-fieldwork-authorization.json and .md. It refuses symlinked paths, repository-contained inputs/outputs, report paths overlapping the record directory, malformed or unsupported fields, and overwrites. Report files are owner-only (0600) where supported.

Exit results:
- 0 — OWNER_AUTHORIZATION_RECORDED: the record states that all eight approvals and required details are complete and owner confirmation is recorded.
- 1 — FIELDWORK_NOT_AUTHORIZED: the record is structurally valid but has pending/rejected approvals or missing details. A blocker report is written.
- 2 — INVALID_INPUT or WRITE_ERROR: the record is malformed, contradictory, unsafe or could not be written. No valid readiness result is produced.

## Privacy and acceptance limits

The template has no participant names, contact details, screening answers, interview notes or recordings. Use only references to private approval artifacts; do not put participant information into the record. The generated report deliberately excludes evidence references, moderator references and other private setup details.

The validator checks record structure and the presence of references. It does not open or verify those referenced artifacts, authenticate the author, verify that an approval was genuinely granted, assess vendor contracts, or establish legal/privacy/security/ethics compliance. OWNER_AUTHORIZATION_RECORDED is a record status, not an automated start signal or a guarantee that fieldwork is lawful or safe.

Actual recruitment/contact, consent, data handling, recording, incentives and spending remain prohibited until the owner has genuinely approved the complete scope and any separate participant-level consent is obtained. This helper itself does not execute any of those activities.
