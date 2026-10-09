# Week 84 fresh revision stage

Read the complete writer and revision stage instructions, the independent adversarial report and mathematical report. Revised only this run's final student/material sources. The separate facilitator guide is unchanged here and belongs to root's guide revision.

## Changes

- Page 2 now states that the doll's matching cards are a temporary private view, leaves the shared set unchanged while all replies are chosen, and permits public deletion only after simultaneous reveal. The worked visual labels its middle panel “Private matches for doll 1.” This closes the durable-private-filter information leak identified by both reviewers.
- Page 8 replaces the two too-small configuration bins with two cuttable tabletop headers: “Shared possibilities” and “Publicly ruled out.” They label open table areas rather than confining the surviving cards. The three reply slots still exactly match the large reply cards.
- The source README identifies every task/material page and the open tabletop arrangement. Eight supplied configuration cards require about 14.55 × 3.95 inches in a nonoverlapping four-by-two arrangement with quarter-inch gaps. Facilitation must preserve the complete public set while each doll's private view is inspected.
- Footer version is `W84-PK-draft-v2` throughout. Problems 1–4, the café transcript cases, all headband deals, all configuration cards and response cards retain their mathematical content.

## Checks

The packet has eight pages. Two fresh temporary pdfLaTeX builds give byte-identical PDFs (SHA-256 `9613f50b585e91c4f593d33a68012068314856f44b53f911c3ba6f906efe08c9`). The portable builder rejects overfull layout warnings. The author checker and the independently authored information-partition checker both pass, including all eight café cases, all announced/no-announcement headband cases and the no-announcement exact fixed point. The independent checker also confirms the guide's optional bounded grid; this revision adds no grid to the student pages.

Rendered every final page with PyMuPDF, opening the document afresh for each page, and Ghostscript. Inspected pages 1–8, the combined header/footer crops and Ghostscript's changed pages 2 and 8. A page-5 crop corroborates all actual repeated configuration-card borders and position labels; the tool preview sometimes suppresses regions identical to a prior image. No document defect, clipping or overlap was found. `digital-QA.json` records dimensions and evidence.

## Limits

Unpiloted draft. Physical table arrangement, cut cards, headband privacy and simultaneous-reply handling are untested in rehearsal and with children. The guide still needs root's separate fixes: exact prompt solution keys, temporary private filtering, print map, source-link clipping and readiness-dependent routes.
