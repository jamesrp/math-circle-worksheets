# Week 26: fixes from the review card, October 23, 2026

This record has two parts from the same day. The guide corrections came first and changed only the adult guide. Later that day the student pages were stored as problem files, unchanged, and then the card's student-page items were made there; that part is at the end.

## Part 1: guide corrections

Only the adult guide changed: the unnumbered overview and printed pages 3, 4, 14 and 18 of `facilitator-guide.pdf` (PDF pages 1, 4, 5, 15 and 19). The student packets, their sources and their reference copies are unchanged. The review card is `plans/review/week-26.md` in the project, with its math check `plans/review/week-26-math.md`.

### What changed

- **Must (card fix 1), Grades 4–5 Problem 2, "Can it have a hole?"** The page does not say whether two tiles touching at a corner close a gap, and the guide answered "yes" and called "no" false. Both answers are right under their conventions. If a corner gap lets the inside out, a hole needs a closed ring of side-joined tiles, which is a cycle, so no maximum (tree) shape has one. If a corner contact closes a gap, the guide's third drawing is a tree with a hole. The overview, p. 3, p. 14 (heading "A hole: it depends on corners", with how to accept a "no" and let the table decide about the corner-closed example) and p. 18 now say this.
- **Should (fix 2), p. 4, K–1 Problem 1 extension.** A fifth tile keeps the boundary at 10 for the L, T and zigzag, never for the square or the straight; the guide named only the L.

Deferred: the student-page half of fix 1 (state the convention in 4–5 P2) and fix 3 (4–5 P3's third shape, with guide p. 15) change student pages and wait for a problem-file conversion. The coulds (4–10) are not done.

### Verification

- `python3 review/verify_card_fixes_2026_10_23.py` enumerates all 691,277 fixed polyominoes with up to 12 tiles (Redelmeier's method; counts match the known sequence) and checks: P = 4n − 2e on every one; no tree up to 12 tiles has a hole if a corner gap leaks; 22,656 twelve-tile trees have one if a corner contact closes a gap; every non-tree has P ≤ 2n; the guide's drawing has a hole under one reading and not the other; the 2-by-2 block has no hole and is not a tree; and which tetrominoes take a fifth tile with no change in boundary.
- The rebuilt guide differs from the October 4 guide only on PDF pages 1, 4, 5, 15 and 19; the other 15 pages are pixel-identical at 100 dpi. All three student PDFs rebuild with exact reference pixels. `facilitator-src/check_pdf.py` passes. Each changed page was rendered and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` with exact 100-dpi pixels on all 38 pages.
- The previous guide and ZIP are archived in the project in `week-26/archive-before-card-fixes-2026-10-23/` and `source/week-26/archive-before-card-fixes-2026-10-23/`.

## Part 2: student-page fixes, after the problem-file conversion

The student pages are now `problems/*.md` and `figures.py` beside `week.toml` (in the ZIP, `problem-files/`). The conversion itself changed nothing: the rebuilt packets matched the print PDFs in pages, text and 100-dpi pixels. Then:

- **Must (card fix 1, student part), Grades 4–5 Problem 2.** The page now states the convention: "Can it have a hole? Two tiles that touch at a corner leave no gap between them." The guide answers under it: p. 14's heading is "A 2-by-2 block: no. A hole: yes, sealed at a corner."; its last paragraph explains that a child who says no is thinking of a hole closed by full sides, for which the argument is right, and how to point back to the page. The overview, p. 3 and p. 18 say the page's convention instead of "the page leaves this open". The same problem now says "none of them a straight row" (card could 9).
- **Should (fix 3), Grades 4–5 Problem 3.** The third printed shape is now the guide's second construction (rows 5; 3 plus a separate tile; 2; 1; boundary 20), so one shape breaks "boundary = 2 × (rows + columns)" and children find the 18 themselves. Guide p. 15's triple and caption read (4, 5, 20), and the guide notes that a child may copy that shape as one of the two the next question asks for.
- **Coulds 7–10.** Grades 2–3 Problem 2 has three recording boxes per start instead of two, so the boxes no longer show how many changes exist (guide p. 9 updated). Grades 2–3 Problem 1 no longer ends "Draw all four shapes and record their boundary lengths", nor Problem 3 "Record each boundary length"; the labelled grids ask for both. Grades 2–3 Problem 4 says "no shape with that many tiles". Grades 4–5 Problem 6 says tiles, not squares, in its prompt and labels (guide p. 17's strap and captions match).

Not done: the guide-only coulds 4–6 (group size on p. 1, materials wording, the formula assumption on p. 14). The K–1 packet did not change.

### Verification

- `python3 review/verify_student_fixes_2026_10_23.py` reads the printed shapes from `figures.py` and checks: the page's corner sentence and the guide's point-sealed example (a hole under the page's rule, none under the other); the three Problem 3 shapes give (2, 6, 16), (3, 4, 14), (4, 5, 20), and only the third exceeds 2 × (rows + columns); over all 2^20 subsets of the 4-by-5 box, the least boundary of a connected shape spanning it is 18, and twelve-tile ones reach 18, 20, 22, 24 and 26; every Grades 2–3 Problem 2 start allows at most two changes, and the three boxes do not overlap; the Problem 6 answers 26, 30, 36. `src/check_shapes.py` and `facilitator-src/check_math.py` were updated for the new shape and pass; `problem-files/check_guide_copy.py` confirms the key view's copy of the guide.
- Changed pages: Grades 2–3 pages 1–4; Grades 4–5 pages 2, 3 and 6; guide PDF pages 1, 4, 10, 15, 16, 18 and 19 (printed pp. 3, 9, 14, 15, 17, 18 and the overview). All other pages, and the whole K–1 packet, are pixel-identical at 100 dpi to the previous release. Each changed page was rendered and inspected.
- The package build's student pages match `build.py`'s from the problem files in pages, text and 100-dpi pixels. A clean rebuild from the extracted ZIP passes `verify_revision.py` with exact reference pixels on all 38 pages.
- The replaced Grades 2–3, Grades 4–5 and guide PDFs are archived in the project in `week-26/archive-before-card-fixes-2026-10-23/` (the guide as `week-26-facilitator-before-student-fixes.pdf`), and the ZIP from the conversion in `source/week-26/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted.

## Part 3: guide-only coulds 4–6

- **Could 4, p. 1.** The group is four younger, four middle and three older children (`worksheet-workflow/context.md`), not three younger.
- **Could 5, p. 1.** The materials no longer name a matching grid, a tile mat or "short edge markers/counters" that no file supplies. The table is the board; about 20 mm tiles or 1-inch colour tiles serve; an edge marker is any small counter set beside one exposed side (dried beans, buttons, plastic counters). A 12-tile row is 24 cm with 20 mm tiles and about 30 cm with 1-inch tiles, wider than a US Letter sheet.
- **Could 6, pp. 10 and 14.** P. 10 suggests testing the Grades 2–3 Problem 3 rule on Problem 1's eight-tile records (7 shared sides give 32 − 14 = 18; 10 give 32 − 20 = 12), since all five Problem 3 cases have ten tiles. P. 14's prerequisites accept "each added tile adds at most 2" (a tile joining k ≥ 1 old tiles changes the boundary by 4 − 2k) as well as the shared-side formula.

Verification: `facilitator-src/check_math.py` and `check_pdf.py` pass and `problem-files/check_guide_copy.py` still finds every key sentence in the guide source. The rebuilt guide differs from the previous one only on PDF pages 2, 11 and 15 (printed pp. 1, 10, 14), each rendered and inspected; the other 17 pages are pixel-identical at 60 dpi with identical text. The student packets and band views did not change. The replaced guide is archived as `week-26/archive-before-card-fixes-2026-10-23/week-26-facilitator-before-guide-coulds.pdf`; the ZIP it replaced is in Git history (commit aa34b9b). A clean rebuild from the new ZIP passes `verify_revision.py`.


## Part 4: footer ids and the guide date

A critic review of the day's changes found that the changed Grades 2–3 and Grades 4–5 packets still carried W26-23-v2 and W26-45-v2, the ids of the October 3 printings, and that the guide footer still read 2026-10-03. The ids are now W26-23-v3 and W26-45-v3 (`week.toml`; K–1 keeps W26-K-v2 and the key W26-G-v2) and the guide footer reads 2026-10-23. Each rebuilt PDF differs from the previous one only in its footer: the extracted text is identical after the id or date swap, and the differing pixels lie in the footer row.
