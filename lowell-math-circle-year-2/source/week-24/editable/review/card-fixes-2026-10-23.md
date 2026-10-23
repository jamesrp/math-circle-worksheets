# Week 24: fixes from the review card, October 23, 2026

The review card is `plans/review/week-24.md` in the project, with its math check `plans/review/week-24-math.md`. Its verdict was keep; it listed five shoulds and seven coulds, and all twelve are done. The student pages were first stored as problem files with no wording change (the rebuilt LaTeX was the old builder's byte for byte, apart from a final newline), and that conversion was committed alone. Then:

## Student pages (K–1 now F24-K-v3, Grades 4–5 F24-45-v3; Grades 2–3 unchanged)

- **Should 2, K–1 Problems 1–3.** Each begins "Circle the winner in each pair."; Problem 1's sentence asking children to split the pairs and share one page is gone (dividing the work is the adult's job, in the guide).
- **Should 3, K–1 Problem 4.** "Your partner takes A. Choose a deck that wins more card pairs against it and play six rounds. Do the same for B and C. Must your chosen deck win more rounds?"
- **Should 5, K–1 footer.** F24-K-v3, as the guide had said since October 4.
- **Could 11, Grades 4–5 Problem 1.** The three decks sit 0.25 in lower, so the label A no longer touches "question?" (now about 17 pt clear).
- **Could 12, K–1 Problem 6.** Ends "Start each swap from these decks."

## Adult guide (pages 1–4, 7, 10, 13, the overview and the route page)

- **Should 1, p. 10, Grades 4–5 Problem 4 gate.** "Counting distinct printed number-pairs as equally likely gives the wrong answer for the four-card decks (B over C would look like 5/9 instead of 7/16). It works for the six-card decks only because every card is copied equally."
- **Should 3, p. 4, K–1 Problem 4.** The partner holds A, then B, then C; the eighteen counters record the rounds, one per round in the winner's style (also in the p. 1 materials).
- **Should 4, p. 1, materials and time.** Index cards cut in half, written large in marker with dots for K–1, and small paper lunch bags; the room needs 57 cards (27 originals, 27 spares, 10, 11 and 12). "Once, about 30 minutes" to make them, then 10–15 minutes before each session. The "4 x 6 cm" size is gone.
- **Could 6, pp. 7 and 13.** The older review's 14, 15, 16 examples and the "Final authority … PROMPT.md, review.md" paragraph are cut.
- **Could 7, p. 2.** Grades 2–3 Problem 2: an adult secretly puts two of the decks in two bags, a child draws from each, and the adult announces only which bag won.
- **Could 8, p. 3.** K–1 Problem 1's hints name the pictured pairs: look at the row of pairs that share one A card, then check every pictured pair has a circled winner.
- **Could 9.** One title, "Three random decks", on the overview, every guide page and the route page (it said "Nontransitive dice and fair decks" and "Nontransitive random decks"); the route page is numbered 14, following p. 13 (`route-note.json` sets `unnumbered_pages` for the overview, and this package's `add_route_note.py` subtracts it).
- **Could 10, p. 2.** The 0–60 minute plan is now a launch of about 5 minutes, two 15–20 minute blocks at the tables (35–40 minutes) and a few minutes of sharing. P. 1 names the packets F24-K-v3, F24-23-v2 and F24-45-v3, and the footer and overview dates read October 23.

Nothing on the card is deferred. The index-card kit and the timing are unrehearsed.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py [folder]` reads the built PDFs and checks each fix and its mathematics: footers in all three packets and the guide's packet list; the K–1 Problem 1–3 openings and the cut sentence; the 5-of-9 cycle; Problem 4's wording, the unique deck beating each of A, B, C and 18 = 3 × 6 counters; Problem 6's sentence and its five working swaps; the 4–5 Problem 1 clearance from the rendered words; the gate sentence, with B over C at 5/9 by distinct pairs and 7/16 by physical pairs, the six-card chances unchanged by counting distinct pairs, and the four-card chances 10/16, 7/16, 10/16; 57 = 27 + 27 + 3 cards and the restated time; the cut residue; the bag sentence; the K–1 hint; one title and the route page's number 14; the table plan. `src/check_answers.py` and `facilitator-src/checks.py` still pass in the build.
- Against the previous print PDFs at 100 dpi: K–1 pages 1–4 and 6 changed in content and every page in the footer; pages 5, 7 and 8 differ otherwise only by glyph metrics, because the previous K–1 print copy was made with pdfTeX 1.40.27 and this build with 1.40.25 (vector drawings identical). Grades 4–5 page 1 changed, the rest only in the footer. Grades 2–3 rebuilds pixel-identical to its print copy, which is kept. Guide pages 1–5, 8, 11, 14 and 15 (of 15) changed in content; the others only in the footer date. Each changed page was rendered and inspected.
- `review/reference-manifest.json` has the new K–1, Grades 4–5 and guide hashes; `review/rebuild-pixel-allowances.json` no longer lists Grades 4–5 alternates. A clean rebuild from the extracted ZIP passes `verify_revision.py` and the card-fix verifier.
- The replaced packets and guide are archived in the project in `week-24/archive-before-card-fixes-2026-10-23/`, and the conversion's ZIP in `source/week-24/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted.
