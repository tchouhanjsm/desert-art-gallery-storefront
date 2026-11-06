# 14 — Japan-First Customer and Market Research

**Research date:** 6 November 2026  
**Status:** Evidence review completed; customer segments remain hypotheses, not validated personas.

## Executive readout

Japan is a substantial, digitally mature ecommerce market. That makes it a credible primary audience to investigate, not a guarantee that DAG's specific products will sell there. The research points to four design requirements: clear product evidence, transparent cross-border purchase information, mobile-first discovery, and a checkout that does not assume a single payment habit. The current evidence does **not** validate a particular price point, product category, audience segment, sales territory or conversion rate for DAG.

## What the evidence says

### 1. The addressable ecommerce context is large, but category fit is still unproven

A Japan Economic Reports summary of METI's FY2025 survey, published 21 October 2026, reports Japan's domestic B2C ecommerce market at **¥27.6 trillion in 2025**, up **5.5%** year over year. The summary says the survey is METI's 28th annual study. It is an AI-generated digest of the METI original, so the original report should be consulted before using detailed category figures in a business case. METI's directly accessible FY2024 release reported **¥26.1 trillion**, up 5.1% in 2024. Neither statistic demonstrates demand for DAG's specific catalogue or for India-to-Japan craft imports.

Sources: [FY2025 survey summary, attributed to METI (21 Oct 2026)](https://jp-reports.com/en/articles/01M5G4812VGTVGTB6XA9YTV78C/); [METI FY2024 release (26 Aug 2025)](https://www.meti.go.jp/english/press/2025/0826_003.html).

### 2. Payment choice and payment authentication affect purchase completion

GMO Payment Gateway's FY2025 payment-intention survey covered 6,556 online-research respondents, including 3,279 recent physical-goods ecommerce buyers. In the physical-goods sample, reported payment-method use included credit cards (67.3%), PayPay (30.4%), Amazon Pay/Amazon gift balance (14.9%) and convenience-store payment (11.7%). Respondents cited points, ease of use and security as leading selection factors. Among respondents aware of 3-D Secure, 32.2% of physical-goods buyers reported an authentication failure; 16.6% of those reporting failure said they abandoned the purchase.

A separate SB Payment Services survey (2,455 retail-site purchasers; May–June 2025) found credit card, PayPay and Rakuten Pay were the most frequently used methods; over 56.5% said they would leave without purchasing when their preferred payment method was unavailable. These are provider-sponsored surveys, not an independent census, but they reinforce an actionable principle: payment support and a recoverable authentication journey should be validated before checkout design is frozen.

**DAG implication:** do not hard-code a payment-provider decision or promise local wallets now. During M3, verify which providers can onboard the actual seller entity, accept the relevant settlement currency, support Japan-issued payment instruments, handle authentication and provide clear refund/dispute operations.

Sources: [GMO Payment Gateway — FY2025 survey (25 Nov 2025)](https://group.gmo/news/article/9798/); [SB Payment Services — 6th ecommerce payment-method survey (3 Jul 2025)](https://www.sbpayment.jp/en/news/press/2025/20250703_001470/).

### 3. Product information and transparent terms reduce avoidable uncertainty

The U.S. International Trade Administration's Japan ecommerce guide reports that detailed product listings are characteristic of major Japanese marketplaces and cites survey data connecting detailed product information with customer expectations and lower return rates. The same guide summarizes Japan's Specified Commercial Transactions Act disclosure requirements for ecommerce, including product price, shipping costs, payment methods and other customer-borne charges, as well as seller identity and contact details. This is useful risk-screening context, **not legal advice** and not a determination of how Japanese law applies to DAG's still-unconfirmed legal seller and sales model.

**DAG implication:** the product page should be designed around verified information, not atmospheric copy alone. Candidate facts include dimensions, material, condition, construction, colour nuance, care, included items, stock/one-of-a-kind status, origin and maker only where documented. Unknown facts should be explicitly omitted or marked unavailable internally, not guessed. Shipping, duties, returns and seller disclosures need a legal/operational workstream before being published.

Source: [U.S. International Trade Administration — Japan ecommerce guide](https://www.trade.gov/country-commercial-guides/japan-ecommerce-0), accessed 6 Nov 2026. The guide includes older survey references, so its numeric payment data is not used here as current evidence.

### 4. Cross-border trust and after-sales handling deserve visible attention

Japan's National Consumer Affairs Center reported **9,127 cross-border consumer consultations in FY2025**, compared with 6,005 in FY2024. The agency says 98.6% concerned online transactions, 72.1% involved credit-card payments and cancellation issues represented 53.0% of the reported trouble types. Importantly, 55% of the product/service grouping was services, and the agency highlights subscription cancellations and travel-authorisation intermediaries. This data must not be misrepresented as a complaint rate for imported physical goods or as evidence of DAG-specific risk. It is a reason to make seller identity, customer support, cancellation/refund rules and order status easy to find.

Source: [National Consumer Affairs Center of Japan — FY2025 cross-border consumer consultations (5 Aug 2026)](https://www.kokusen.go.jp/news/data/n-20260805_2.html).

### 5. Mobile is a first-class design context

The U.S. ITA guide reports, citing Japan's FY2023 communications usage survey and METI ecommerce data, that 90.6% of households had smartphones and 58.7% of online goods sales were completed by smartphone. These figures are older than the 2026 research date, but they support a conservative design principle: the catalogue, image gallery, filters, product facts and support path must work exceptionally well on mobile. They are not a substitute for DAG-specific analytics after launch.

Source: [U.S. International Trade Administration — Japan ecommerce guide](https://www.trade.gov/country-commercial-guides/japan-ecommerce-0).

## Customer needs to design for

The needs below are design hypotheses derived from the market evidence and the nature of cross-border product evaluation. They are not claims that all Japanese customers behave alike.

| Need hypothesis | Experience implication | How to validate |
|---|---|---|
| Confidence in what is physically being purchased | Multiple useful image views, scale references and specific condition notes | Moderated product-page tests with Japanese shoppers |
| Clear total cost before commitment | Explain what is known about shipping, duties and taxes; do not invent estimates | Test comprehension after actual fulfilment and legal rules are known |
| Easy category discovery | Plain category language, search, usable filters and meaningful product grouping | Tree test and mobile browse task |
| Confidence in a seller outside Japan | Clear seller identity, support channel, delivery/returns information and order updates | Interview and checkout usability test |
| Payment confidence | Familiar, supported payment methods and retry/recovery on authentication failure | Provider capability assessment and payment usability testing |
| Understanding of materials and variations | Close-up photography, dimensions, material and care facts with controlled terminology | Test against a representative 10–20 image/product sample |

## English-only requirement: an explicit market-access risk

The owner has confirmed that customer-facing storefront content must be English-only. This remains the requirement; this research does not recommend silently introducing Japanese translations. It does, however, identify a risk to validate: the inspected POJ Studio site exposes English/Japanese language controls, while the inspected Macaroni Shoten shop is Japanese-language. These reference observations are not proof of customer preference, but they show that language/localization is an intentional part of the reference experiences.

DAG should therefore use plain, precise English; avoid idiom-heavy copy; show dimensions and units clearly; keep policies and product information easy to scan; and test comprehension with Japan-based participants. If English-only comprehension proves to be a material barrier, bring evidence back to the owner rather than changing the confirmed language decision without approval. Do not claim Japanese-language support or service unless it is actually available.

## Audience hypotheses for M1

These are research segments to test, not personas to encode as fact:

1. **Home and interior buyers:** shoppers considering textiles or objects for a lived-in space. Likely questions: scale, palette, texture, care, pairing and delivery.
2. **Craft and material enthusiasts:** customers attracted by construction, technique, provenance or regional context. Likely questions: what is known about how and where a piece was made, what is documented, and what is not.
3. **Gift and considered-purchase buyers:** customers who need a clear product story, presentation, availability, delivery timing and a confident return/support answer.
4. **Trade or design professionals:** stylists, hospitality and interior practitioners who may need dimensions, repeatability, quantity, lead time and a direct enquiry route.

Do not create named fictional personas, demographic claims or market-size estimates from these hypotheses.

## Validation plan before M2 is treated as final

- Conduct 5–8 discovery interviews with Japan-based target customers or people who regularly purchase home/textile/craft goods online. Recruit across the hypotheses above; do not treat this small sample as statistically representative.
- Run 5 moderated mobile browse/product comprehension sessions on the chosen territory once a prototype exists.
- Show 10–20 real, owner-supplied product-photo sets and ask customers what they need to know before buying. Do not use placeholders as if they were real products.
- Record language comprehension, trust questions, missing facts, decision blockers and willingness to enquire. Customer-facing prototype copy stays English-only by owner decision; research discussion can use a facilitator/translator if needed, without introducing Japanese customer-facing copy.
- Ask the owner to identify the first five to ten products that are operationally ready for international sale, with verified price, stock, dimensions, material, origin and available images. If this cannot yet be done, keep the early prototype catalogue clearly labelled as illustrative.

## Important research limits

- There is no validated interview data from Japan-based DAG customers in this research pass.
- The cited national ecommerce totals are broad market context, not a measure of DAG's serviceable market.
- METI's published cross-border figures cover Japan, the United States and China; they do not establish Japan–India product demand.
- Payment studies are sponsored by payment providers and their samples/methodologies differ.
- No price elasticity, target average order value, customer acquisition cost or conversion forecast is established.
- No claim is made that all DAG items are made in Jaisalmer or use any particular Rajasthan craft technique. Product-specific provenance must be documented.
