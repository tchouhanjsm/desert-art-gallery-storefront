# M2 — Revision 3 Private Prototype Implementation

**Status:** Implemented in the local/private, non-transactional Revision 2 prototype.  
**Authority:** D-016 and D-017.  
**Public source boundary:** The D-014 owner-controlled HTML/CSS/JS kit remains unchanged. The prototype, photographs, catalogue information, screenshots and review outputs remain outside this repository.

## Implementation delivered

### D-017 visual-system alignment
- Restricted the prototype to the six owner-approved colours: canvas #FFFFFF, ink #132A3A, brand/action #174F6B, accent #E5AD26, cool surface #F3F7F8 and divider #D4E0E5.
- Removed unapproved placeholder colours, gradients and shadows.
- Applied the approved Source Serif 4 / Inter stacks, responsive heading/body hierarchy, 4–64px spacing scale, 1440px content maximum, 56px desktop / 20px mobile gutters, square card edges and 16:9 / 4:5 / 1:1 image frames.
- Added the selected navigation indicator to the six existing destinations. Current states are explicit across the nine routes; product and article detail use aria-current=location for their parent section.

### Existing navigation interaction quality
- Kept the existing six destinations and the supplied mobile-menu toggle; no new navigation item or overlay was introduced.
- Escape closes the mobile disclosure and returns keyboard focus to the toggle.
- Selecting an existing navigation link closes the disclosure.
- Resizing from mobile to desktop while the menu is open clears aria-expanded; returning to mobile leaves the disclosure collapsed.
- The three existing homepage category cards are balanced on mobile by centering the third card in the two-column grid; no content slot was added or removed.

## Automated evidence

| Gate | Result |
|---|---:|
| D-017 CSS palette/layout audit | PASS — 6 approved palette colours, 14 required type/layout markers, no gradient/shadow/remote CSS |
| Responsive route review | 45/45 — 9 routes × 5 widths (390, 430, 768, 1280, 1440 CSS px) |
| Captured screenshots | 18 — mobile (390px) and desktop (1440px) for all nine routes |
| Five-priority journey review | 25/25 — 5 journeys × 5 widths |
| Existing navigation interaction checks | 125 — mobile open, Escape focus restoration, link-close, breakpoint resize and desktop visibility |
| Python regression tests | 9/9 passed |

The browser review renders local files in memory and writes evidence outside both the public repository and private prototype root. These are automated engineering checks, not screen-reader certification, full WCAG compliance, owner visual sign-off or participant usability research.

## Scope and pending gates

- Exactly the nine D-014 routes and six D-016 review areas remain.
- Search, Filter, Sort, product options, Purchase and enquiry fields/submit remain disabled. No cart, checkout, order, payment, shipping/tax or live enquiry processing exists.
- Image frames remain clearly labelled; no genuine 10–20 product sample, product photographs, verified prices/specifications, maker facts, editorial evidence or rights ledger was supplied.
- Wordmark artwork, descriptor wording and final copy remain pending owner input.
- The prototype remains local/private and non-transactional. No production stack, hosting, commercial terms, public deployment, participant fieldwork or spend is authorized.
- Owner visual acceptance and human customer usability acceptance remain outstanding.
