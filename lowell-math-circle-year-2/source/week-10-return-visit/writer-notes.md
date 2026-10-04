# Week 10 return-visit writer stage

Prepared seven-page student draft, three distinct investigations. Page 1 has the K–5 concrete arrow entry; pages 2–5 are approximately grades 2–5; pages 6–7 are approximately grades 4–5. These are prerequisite bands. Arrow entry needs following a displayed direction and one counter removed per street; safe-choice comparisons need retaining an unchanged initial state between trials; passwords need recognizing three-symbol words and overlapping neighbors. No physical rehearsal or classroom piloting is claimed.

## Actual drawn cases and answers

Problem 1, pages 1–3, arrows must be obeyed:

| Town | Directed streets | Legal starts and a witness |
|---|---|---|
| 1 | A→B, B→C, C→A | Any of A/B/C; A-B-C-A |
| 2 | A→B, A→C, B→C | Impossible |
| 3 | A→B, B→C, C→D | A only; A-B-C-D |
| 4 | A→B, C→B, C→D | Impossible |
| 5 | A→B, B→C, C→D, D→A, A→C | A only, ending C; A-B-C-D-A-C or A-C-D-A-B-C |
| 6 | A→B, B→C, D→C, D→A, A→C | Impossible |
| 7 | A→B, B→C, C→A; D→E, E→F, F→D | Impossible; two disconnected cycles |
| 8 | A→B, B→C, C→A, A→D, D→E, E→A | Any A/B/C/D/E; A-B-C-A-D-E-A |

The compact convention example is X→Y→Z. Its three states are walker X with both counters, walker Y with only YZ unused, walker Z with none unused. Used streets appear gray/dashed only in this convention picture. Children put back all counters before another attempt.

Problem 2, pages 4–5, streets can be crossed either way:

| Town | Streets and start | Safe first streets | Unsafe first streets |
|---|---|---|---|
| 1 | AB, BC, CA, AD; start A | AB, AC | AD |
| 2 | AB, BC, CA, AD; start D | AD | None |
| 3 | AB, BC, CD, DA, AC; start A | AB, AC, AD | None |
| 4 | AB, BC, CA, AD, DE, EF, FD; start A | AB, AC | AD |

The two copies of the triangle-and-tail differ only in marked start, purposely contrasting a forbidden early bridge with a forced bridge. This is one route-choice investigation, not two claimed activities. The shared rules explicitly restore every counter and the walker to the star before another try. The safe test includes the new walker location: after AD from A in Town 1, the isolated walker at D cannot reach the unused triangle even though all remaining edge-bearing vertices form one component.

Complete route witnesses and all first-street witnesses, legal-start enumeration counts, exact graph coordinates and geometry checks are in `draft/build/math-check.json` and `draft/src/towns.json`.

Problem 3, pages 6–7: all eight binary triples are printed. The linear two-button convention uses 0110, producing 01, 11, 10 through adjacent window positions. The circular two-button convention uses clockwise 011, producing 01, 11, 10; the final 10 crosses the displayed join. Neither convention gives a target triple construction.

For adults/reviewers, the linear minimum is 10 (L−2 windows must cover 8), witnessed by 0001011100. The circular minimum is 8 (one window per position), witnessed by 00010111. There are 16 marked minimum circles and two rotation classes, 00010111 and 00011101. These target constructions are absent from student pages.

## Verification and source behavior

`check_math.py` does exhaustive edge-consumption DFS independently of the TeX generator. It checks every starting vertex in all eight directed towns, every first street at the four marked undirected starts, directed degree/connectivity predictions, and the destination-sensitive reachability criterion. It enumerates shorter binary rows/circles, all 256 eight-symbol circles, examples, and target windows.

Every map has equal x/y inch scaling and no unmarked crossing. Counter centers are at least 0.75 inch apart. The minimum spacing is 0.925 inch in the small zigzag chains. Active arrows are at 86% of each street with nominal 3-mm length/2.4-mm width; independent source geometry verifies their whole conservative triangular footprints clear every 0.75-inch counter and island circle. The optional PyMuPDF checker also independently inspects the actual PDF circles, midpoint positions, equal scale, every active arrow direction and physical footprints. Actual PDF minimum arrow-counter clearance is 3.10 points, with arrow stroke included; island clearance is 4.85 points. These are digital checks, not claims that real material placement has been rehearsed.

The standard portable builder uses Python 3.9+ standard library and pdfLaTeX only. Optional PyMuPDF QA is invoked separately with explicit PDF and render-directory paths. `generate.py` plus `towns.json` are authoritative; update the generator when revising wording or footer so rebuilding does not undo edits to generated `return-visit.tex`.

All seven pages were rendered and visually read after corrections. Inspection caught and fixed two missing two-button example outputs caused by an unterminated TeX integer conditional, crowded map labels, a star on a street, and initially counter-obscured arrowheads. Final PDFs have one numbered Problem 1/2/3 label each, with ordinary continuation text. Bounds, page-level bands, all represented examples and vectors pass the optional checker. There are no LaTeX overfull/underfull warnings. Extracted-source build compares all seven page texts and pixel renders; evidence is `draft/clean-rebuild.json`.

All artifacts remain inside this run. No base packets, facilitator files, AGENTS or indexes were edited. The outline records the prior-year two-digit password antecedent; this companion adds directed route balance, safe first decisions, and binary-triple/circular overlap continuations to the existing Week 10 theme.
