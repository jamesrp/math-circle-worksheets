# Week 8: Rook moves, Nim, and changing the losing set

Revised September 20, 2026. The original middle activity now requires both halves of a universal winning-position argument. The upper king-variant task is replaced by three-pile Nim, a counterexample to naive matching and to even-total conjectures, then a constructive binary proof. The extra changes the move set again, leading to Wythoff pairs and the golden ratio.

## Print packets

- [Race to the star / Can you copy my move?](../../week-08/week-08-k-1.pdf) — 2 pages, F08-K-v2. Play on a 3-by-3 board; investigate center and top-left; translate matching to two piles of 2.
- [Map the traps / The board is two piles](../../week-08/week-08-grades-2-3.pdf) — 2 pages, F08-M-v2. Classify a 4-by-4 board, prove the equal-pile rule for arbitrary rectangles, then break a naive generalization with three piles.
- [Three piles break the mirror / Binary balance](../../week-08/week-08-grades-4-5.pdf) — 3 pages, F08-U-v2. Play (1,2,3) and (1,2,4); test (1,1,2) against even-total reasoning; find zero-XOR positions and prove how to reach them.
- [One new move, a new world](../../week-08/week-08-extra-grades-6-7.pdf) — 1 page, F08-X-v2. Classify Wythoff positions through 7, generate greedy pairs, distinguish no-edges-between from completeness, test the golden-ratio theorem.
- [Facilitator guide and checked solutions](../../week-08/week-08-facilitator.pdf) — 4 pages: prerequisites, realistic materials, 60-minute flow, prompts/hints, proofs, source links, and reuse guidance.

Print US Letter, single-sided, 100% / Actual Size. No physical fitting requires an exact scale. Give pages one at a time. For the current K,K,1 / 3,3,3 / 5 roster, three K1 packets + three middle packets + one upper packet = **15 student sheets**, plus the optional one-page extra. Grade labels are entry points, not placement rules.

**Kit:** About 60 counters, five paper plates or marked pile areas, pencils, and scraps labeled 1, 2, 4, 8. Reuse the counters between trials; no chess pieces are necessary.

Read the [redesign plan](../../../plans/week-08-redesign.md) for the mathematical trajectory and primary research references. These are prepared activities, not teaching records. Record exact use in the [session use log](../../../plans/fall-k-5-year-a-use-log.md).

## Rebuild and check

Run `sh lowell-math-circle-year-2/source/week-08/build.sh` from the repository root. It runs `verify.py`, compiles all five editable LaTeX sources twice, and places PDFs in `lowell-math-circle-year-2/week-08/`. Requires Python3, pdfLaTeX, TikZ, Source Sans Pro, microtype, geometry, fancyhdr, hyperref, amsmath/amssymb, tabularx, and extarticle. No network access is needed to rebuild.

Backward recursion, independent of XOR, checks 2,197 three-pile positions (each heap 0–12), 169 two-pile positions, and 961 Wythoff positions (0–30); sample moves are checked. Finite checks do not replace the general proofs.

After edits, render and visually inspect all pages. See [REVIEW.md](REVIEW.md) for the completed checks.
