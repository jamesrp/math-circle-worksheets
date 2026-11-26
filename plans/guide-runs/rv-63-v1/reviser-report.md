# Reviser report: rv-63-v1

Final output: [8-page facilitator guide](final/facilitator.pdf), identifier **W63-RV-FAC-v2**; [portable source](final/src/), [verification record](final/verification.json). This is the reviser stage only. Original writer sources, PDFs, reports, critic review and critic scripts remain unchanged. Student pages and the existing Week 63 guide/materials are unchanged. Packaging and integration wait for the catalog task.

## Finding dispositions

All **1 must-fix and 7 should-fix findings are addressed**; none is declined.

| Finding | Disposition and location |
|---|---|
| Must 1, both leaks | Guide p. 2 gives each young pair its own A–C set and a cup of 12–20 counters at most 12 mm across, never six pre-counted counters. Each middle pair gets its own unmarked, uncut materials p. 3. Upper trio shares a separate sheet. Extras are now four sheets: one materials p. 2 and three p. 3. Parent's page repeats its kit. |
| Should 1 | P. 1 now names discoveries and evidence levels for each band, rather than listing actions. It distinguishes new any-two-card swaps and exact piles from the first visit's overlapping groups, and identifies the arrows as upper-only prior work. |
| Should 2 | P. 5 works through WUVXY → VUWXY (WV splits a loop) and WUVXY → WUVYX (XY joins loops), then explains exchanged arrow ends and the lower bound. Both examples are checked in the revised checker. |
| Should 3 | P. 4 gives a middle-table completeness argument using the nine first-visit home-free rows and excluding the three two-swapped-pair rows, without requiring arrows. |
| Should 4 | P. 8 replaces the enumeration certificate table with the compatible-triple case proof of maximum nine and impossible five. The checker verifies every case over all 1,820 four-spot boards. P. 4 points adults to that proof. |
| Should 5 | P. 3 is a self-contained parent page with materials-page references, per-pair counter supply/size, starting route, plain-language minimality explanations and a first crossed-out-board demonstration. |
| Should 6 | P. 2 states who reads/scribes, splits the 24-outcome checks between middle partners, pools upper first-home branches, names the grid overlap workload, and gives explicit second/third visit order. Reversible reasoning is removed as a first-route demand. |
| Should 7 | P. 2 launches with real U–X scrap-paper cards and a physical non-neighbor VX swap. The printed input/step/output bridge remains. |
| Minor 1 | P. 3 asks which outcomes give A a counter, without disclosing “two.” |
| Minor 2 | Deleted the final-page/same-number revision-history sentence. |
| Minor 3 | P. 3 completes the forced-home argument for CDAB without redundant wording. |
| Minor 4 | P. 5 asks whether the swap can put a card home before loop vocabulary. |
| Minor 5 | P. 5 states the child-facing rule: a k-card loop needs k−1 swaps; add them, including singletons. |
| Minor 6 | Removed checker/process commentary and superseded-numbering history from facilitator prose. Middle paired-home reasoning is written locally. |
| Minor 7 | P. 2 adds erasers and a precise minimum cut set if the base kit was not retained. Two materials-page-2 copies are needed for two young pairs, rather than one; using one would contradict the accepted per-pair fix. The retained-kit forecast is clearly untested. |
| Minor 8 | P. 4 explicitly bridges four free cards with the complete A–D deck's 24 outcomes. |
| Minor 9 | Accepted concision edits: shortened repeated setup/prose, removed process notes and the certificate table, compacted source leads. Required explanations add similar space: extracted text is 4,966 words versus 4,972 in the draft, still 8 pages. A model-length reduction to about 3,000 words was not imposed: it would discard the complete catalogs, keys, or newly required explanations. No mathematical route was removed merely to hit a word target. |

The source trail now explicitly treats Frieze D14/D16 as references cited in the base notes; originals were not reopened during revision. Retained writer consultation history is labelled as such rather than presented as new reviser source access.

## Final student pages and materials checked

All 21 actual final student pages were rendered and inspected, alongside all 11 base-guide and 3 material pages and the 8-page writer draft. SHA-256 pins remain unchanged in `final/src/student-manifest.json`.

| Packet | Page → problem mapping |
|---|---|
| K–1, 5 pp. | 1 → 1; 2 → 2–3; 3 → 4; 4 → 5–6; 5 → 7–8 |
| Grades 2–3, 6 pp. | 1 → 1; 2 → 2–3; 3 → 4–5; 4 → 6–7; 5 → 8; 6 → 9 |
| Grades 4–5, 10 pp. | 1 → 1; 2 → 2; 3 → 3; 4 → 4–5; 5 → 6–7; 6 → 8–9; 7 → 10; 8 → 11; 9 → 12; 10 → 13 |

Material counts were checked on W63-M-v3: page 1 has two A–E decks and two strips; page 2 has six A–C outcomes, five group labels and twelve blank records; page 3 has all 24 distinct A–D outcomes. Five page-1 kits supply the table arrangement. Minimum new cutting: page 1 ×5, A–C outcomes from page 2 ×2, page 3 ×2, plus the four uncut extras. Unneeded labels/blank records stay uncut.

The review's measurement script was rerun against the actual PDFs. K–1 pp. 4–5 and upper pp. 7–8 have 35 × 45 mm homes. Middle p. 5 uses 32 × 13 mm cells and p. 6 uses 36 × 13 mm cells; they remain reference boards rather than placement mats. Card/outcome dimensions and home-label visibility were checked against the actual material pages.

## Student-page issues and workarounds

No student-page mathematical error was found. Tiny outcome cells/crossed pictures remain handling and visibility risks; the guide allows pointing and a shared pencil alternative, warns that spare record boxes do not encode answer counts, and keeps cards off the middle reference boards. Material sharing had been a guide-preparation error, now fixed without changing pages. The upper grids are correctly treated as separate Problems 12–13 on pages 9–10.

## Mathematics, build and visual QA

- `final/src/build.sh` compiles twice with real pdfLaTeX, rejects errors/overfull boxes, writes `../facilitator.pdf`, and finishes with the checker. Final run passed: **8 pages, no LaTeX errors or overfull boxes**.
- Revised `check_guide.py` passes student hashes and all 21 page/problem mappings; breadth-first distances for all 152 states on 2–5 cards; exact path lengths 0–7; every printed swap, loop, tally, pile, hardest-row/strip/ring catalog and rook sum; and all 1,820 four-spot boards. New assertions verify both split/join examples and each case of the adult proof, rather than only repeating its final answer.
- Every final guide page was rerendered after the final edits and visually inspected at readable size. All eight retain the original 11-point main type, consistent headers/footers, intact tables and complete parent/middle/upper pages, with no clipping, overlapping text, or spill pages. All problem/page citations and material quantities were checked against the final PDFs.
- A clean copy outside the repository containing only `src/` and the three student PDFs rebuilt successfully, with its checker passing there. Both the PDF bytes and `pdftotext -layout` output are identical to the in-repository final. PDF SHA-256: `0ed76922f18d4c879004548e6c42d5dba1724c799aa89feb1a85efbbfa86824b`.

All guides remain **untested with children and physically unrehearsed**. Digital dimensions, mathematical checks and clean builds do not establish card/counter fit in use, preparation time, staffing load, or age fit. No packaging, catalog modification, deployment, approval or integration was performed by this reviser.
