# Week 26: guide corrections from the review card, October 23, 2026

Only the adult guide changed: the unnumbered overview and printed pages 3, 4, 14 and 18 of `facilitator-guide.pdf` (PDF pages 1, 4, 5, 15 and 19). The student packets, their sources and their reference copies are unchanged. The review card is `plans/review/week-26.md` in the project, with its math check `plans/review/week-26-math.md`.

## What changed

- **Must (card fix 1), Grades 4–5 Problem 2, "Can it have a hole?"** The page does not say whether two tiles touching at a corner close a gap, and the guide answered "yes" and called "no" false. Both answers are right under their conventions. If a corner gap lets the inside out, a hole needs a closed ring of side-joined tiles, which is a cycle, so no maximum (tree) shape has one. If a corner contact closes a gap, the guide's third drawing is a tree with a hole. The overview, p. 3, p. 14 (heading "A hole: it depends on corners", with how to accept a "no" and let the table decide about the corner-closed example) and p. 18 now say this.
- **Should (fix 2), p. 4, K–1 Problem 1 extension.** A fifth tile keeps the boundary at 10 for the L, T and zigzag, never for the square or the straight; the guide named only the L.

Deferred: the student-page half of fix 1 (state the convention in 4–5 P2) and fix 3 (4–5 P3's third shape, with guide p. 15) change student pages and wait for a problem-file conversion. The coulds (4–10) are not done.

## Verification

- `python3 review/verify_card_fixes_2026_10_23.py` enumerates all 691,277 fixed polyominoes with up to 12 tiles (Redelmeier's method; counts match the known sequence) and checks: P = 4n − 2e on every one; no tree up to 12 tiles has a hole if a corner gap leaks; 22,656 twelve-tile trees have one if a corner contact closes a gap; every non-tree has P ≤ 2n; the guide's drawing has a hole under one reading and not the other; the 2-by-2 block has no hole and is not a tree; and which tetrominoes take a fifth tile with no change in boundary.
- The rebuilt guide differs from the October 4 guide only on PDF pages 1, 4, 5, 15 and 19; the other 15 pages are pixel-identical at 100 dpi. All three student PDFs rebuild with exact reference pixels. `facilitator-src/check_pdf.py` passes. Each changed page was rendered and inspected.
- A clean rebuild from the extracted portable ZIP passes `verify_revision.py` with exact 100-dpi pixels on all 38 pages.
- The previous guide and ZIP are archived in the project in `week-26/archive-before-card-fixes-2026-10-23/` and `source/week-26/archive-before-card-fixes-2026-10-23/`.

The theme remains unpiloted.
