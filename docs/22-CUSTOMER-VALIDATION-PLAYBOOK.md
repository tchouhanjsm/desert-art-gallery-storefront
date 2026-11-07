# 22 — Japan-First Customer Validation Playbook

**Status:** Research operations prepared for owner review. No participant recruitment, interviews or usability sessions have been conducted. This playbook is not authorization to recruit or spend money.

## 1. Purpose and evidence boundary

Turn the research hypotheses in [14 — Japan-First Customer and Market Research](14-JAPAN-FIRST-CUSTOMER-RESEARCH.md) into a repeatable, low-bias study. The goal is to understand how people in Japan discover, evaluate and seek confidence in home, textile, craft and considered-purchase products—not to manufacture personas or claim product-market fit.

Known project constraints:
- Japan is the intended primary customer market.
- Customer-facing storefront content remains English-only.
- The four audience groups in document 14 are hypotheses, not validated segments.
- There is no first-party DAG interview data yet.
- Exact seller jurisdiction, sales territories, currency, shipping, duties, payment, returns and legal disclosures remain unresolved.
- The owner controls the visual direction. M2 prototypes remain blocked until a visual territory is explicitly approved and recorded.

This playbook is a proposed method. It does not change any confirmed decision, make a commercial promise, or establish a legal/privacy policy.

## 2. Study stages and approval gates

| Stage | Activity | Can begin when | Output |
|---|---|---|---|
| A — Discovery | Moderated interviews about recent purchases, evaluation and trust | Owner confirms the cohort focus, recruitment route and any participant cost | Anonymized evidence log and research synthesis |
| B — Usability | Moderated mobile-first browse and product-comprehension tests | Stage A findings are reviewed; visual direction is owner-approved; prototype and real product sample are ready | Task observations, usability findings and prioritized open questions |

Stage A does not require a visual prototype. Do not use it to ask participants to choose the DAG visual territories on the owner's behalf. Stage B must use an owner-approved DAG prototype; it must not be built in production style before the visual gate.

## 3. Stage A — exploratory discovery

### Proposed sample

A small first round of **six to eight participants** is proposed as qualitative discovery only. It is not statistically representative and cannot establish market size, conversion, price elasticity or the prevalence of a need.

Recruit across the four hypotheses in document 14 without treating them as fixed personas:

1. Home and interior purchase context.
2. Craft and material interest.
3. Gift and considered-purchase context.
4. Trade, styling or design-professional context.

Participants may fit more than one context. Record the context evidenced in the conversation, not a persona label. Do not rank the four groups or treat one or two interviews as proof that a segment is attractive.

### Proposed eligibility checks

Use only the minimum checks needed for the study:
- The person lives in Japan or regularly shops online for delivery in Japan.
- They have recently researched or purchased home, textile, craft, object or considered-purchase goods online; trade participants may instead specify or source products professionally.
- They can take part in the intended discussion format. The customer-facing prototype remains English-only; the facilitator may explain the research process in a participant's preferred language, but must not translate interface content during an English-comprehension task.

Do not screen by age, gender, income, ethnicity, religion or other irrelevant personal characteristics. Do not collect home addresses, personal email/phone details, payment details or exact birth dates in the research templates. Keep recruitment contact details, if needed, in a separate owner-controlled system outside Git.

### Session format

Proposed duration: 30–45 minutes per participant. Run one session at a time and capture notes in the blank templates under `templates/research/`.

Suggested flow:
1. Explain the purpose, voluntary nature, note-taking and any recording request.
2. Ask about the participant's most recent relevant online shopping experience.
3. Explore how they discovered, compared and evaluated the item.
4. Ask what product evidence and service information they needed before deciding.
5. Explore cross-border concerns only from the participant's own experience; do not assume they have bought from India.
6. Ask what would make them contact a seller rather than proceed independently.
7. Ask what they found confusing, missing or reassuring.
8. Close by inviting corrections and reminding them they may withdraw their contribution.

Avoid asking “Would you buy this?” as a proxy for actual demand. Prefer questions about a specific past behaviour and the information used at the time.

## 4. Stage A — discussion prompts

Use the [discovery interview guide](../templates/research/discovery-interview-guide.md) for the full neutral script. Core prompts:

- Tell me about the last time you searched for or bought a home, textile, craft or decorative object online.
- What started the search, and where did you look first?
- What did you compare before deciding?
- Which facts or images were essential? Which were difficult to find?
- What made the seller or product feel credible—or gave you pause?
- Have you bought from a seller outside Japan? What did you need to know before proceeding?
- What do you normally look for about delivery, taxes/duties, payment, returns and support? Do not offer an answer on DAG's behalf.
- In what circumstances would you contact a seller before buying?
- What would you still need to know after viewing a product page?

Ask follow-up questions such as “What happened next?” and “Can you show or describe how you checked?” Do not lead participants toward the POJ or Macaroni reference patterns.

## 5. Stage B — prototype usability

Begin only after all of the following are true:
- The owner has explicitly selected or combined a visual territory and recorded it in `docs/DECISIONS.md`.
- The relevant M2 prototype is available and clearly labelled as a prototype.
- A representative sample of 10–20 real DAG products and image sets has been supplied privately and its facts/images are verified for the test purpose.
- Any purchase, enquiry, price, availability or service content shown in the prototype is either owner-approved or clearly identified as a research-only scenario. Do not imply that hypothetical checkout or policies are operational.

Use five moderated sessions as an initial usability pass, not a statistical benchmark. Test the real browse and product-evaluation journey on a participant's phone or an equivalent mobile viewport. Review desktop and tablet separately as part of the owner design review.

Suggested tasks:
1. Find a product or category using the participant's own words.
2. Browse a category/collection and explain what the grouping means.
3. Open a product and describe what they believe is being offered.
4. Find dimensions, materials, condition, care and maker/origin details where those facts are actually supplied.
5. Explain which information is missing or unclear before deciding.
6. Find the support/contact route.
7. Explain what they would need to know about delivery, duties, payment and returns—without implying that unresolved DAG policies already exist.

Do not test checkout completion, payment authentication or delivery promises until the commercial rules and provider capabilities are approved. See [prototype usability guide](../templates/research/prototype-usability-guide.md).

## 6. Evidence capture and analysis

Use these blank templates:
- `participant-screener.csv`: eligibility outcome and anonymized participant code only.
- `research-session-notes.csv`: de-identified context and interview notes.
- `task-observations.csv`: task outcome, observed behaviour and friction.
- `finding-synthesis.csv`: evidence-linked themes, counter-evidence and implications.

For every finding, separate:
- **Observed:** what the participant did during the session.
- **Reported:** what the participant said about past behaviour or needs.
- **Inferred:** the team's interpretation, marked as an inference.
- **Proposed:** a possible product or content response, not an approved requirement.

Link findings to session/task evidence references. Record contradictory observations, not only supporting examples. Paraphrase by default; store a verbatim quote only when recording/quote permission is explicit and the wording contains no identifying detail.

A small qualitative sample does not support population percentages or market forecasts. Report counts with the denominator (for example, “3 of 7 sessions”), context and limitations. A repeated theme is a signal for follow-up, not automatic proof. Do not claim that the site is validated, that customers prefer a specific design, or that a commercial model is proven from this study alone.

Suggested friction severity:
- **Critical:** participant cannot complete a core task or forms a materially wrong understanding of the item.
- **High:** a major product/trust question blocks or materially delays the task.
- **Medium:** avoidable hesitation or confusion that the participant can work around.
- **Low:** refinement opportunity with no meaningful task impact.

Assign confidence separately from severity. A severe issue from one unusual session may still have low confidence.

## 7. Participant privacy and session handling

This is a research-workflow safeguard, not a substitute for legal advice or an approved privacy notice.

- Participation is voluntary. A participant may skip a question or stop.
- Ask for consent before taking notes; ask separately for audio/video recording and any use of identifiable quotations.
- Recording is optional and should be avoided unless it materially helps the study. If permission is not given, take notes only.
- Collect only information needed to answer the study question.
- Use participant codes (for example, `R01`) in the templates. Do not place participant names, emails, phone numbers, addresses, social handles, payment information or other direct identifiers in Git.
- Keep contact details, raw recordings and any identifiable source material in a separate owner-controlled private location with access limited to the people conducting the research.
- Do not upload raw recordings, transcripts or identifiable notes to this public repository, a public issue, a pull request or a shared AI workspace.
- Before publishing any insight internally, remove identifying details and check that a quotation cannot reasonably identify the participant.
- Agree a retention/deletion process with the owner before collecting any recordings or identifiable data.

## 8. Reporting format

The research readout should contain:
1. Study dates, method, sample size and recruitment context.
2. Participants described only by relevant shopping context and anonymized codes.
3. Key observed/reported needs with evidence references and counter-evidence.
4. Product-information gaps and trust questions.
5. English-only comprehension observations.
6. Mobile discovery and product-evaluation friction, when Stage B is run.
7. Unresolved commercial questions surfaced by participants—without answering them on behalf of DAG.
8. Implications, confidence, limitations and proposed next tests.
9. Decisions requiring explicit owner approval.

Do not write named personas, market-size claims, purchase forecasts or conversion assumptions from a small qualitative sample.

## 9. Owner decisions required before execution

- **M1-B:** Confirm the initial validation focus. The proposed broad exploratory cohort above is an option, not a selected target segment.
- Confirm the recruitment route and whether any participant cost or incentive is acceptable. No spending is authorized by this playbook.
- Confirm who will moderate and where private research notes will be stored.
- **M1-C:** Supply a representative 10–20 product/photo sample when ready. Keep it private; do not commit it to Git.
- **M1-A:** Separately choose, combine, revise or reject the four visual territories. A customer interview does not replace this owner decision.

Until these inputs are confirmed, this milestone is **research-ready, not research-complete**. No participant recruitment or customer validation has been claimed.

## 10. Related project documents

- [Japan-first research and audience hypotheses](14-JAPAN-FIRST-CUSTOMER-RESEARCH.md)
- [Reference-to-DAG implementation specification](15-REFERENCE-TO-DAG-IMPLEMENTATION-SPEC.md)
- [Owner-controlled visual direction](14-OWNER-CONTROLLED-VISUAL-DIRECTION.md)
- [M1 owner review and exit gate](M1-OWNER-REVIEW.md)
- [Owner input register](OWNER-INPUT-REGISTER.md)
