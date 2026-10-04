> Archived October 3, 2026. This version was replaced by the [concrete revision](../README.md); its PDFs are in `lowell-math-circle-year-2/week-08/archive/`, and `sh lowell-math-circle-year-2/source/week-08/archive/build.sh` rebuilds it there.

# Week 8: Rook moves, Nim, and changing the losing set

Revised September 27, 2026 from the Week 1 classroom feedback and adopted AGENTS.md guidance. **All v3 pages are unpiloted.** Rook and pile games now get repeated equal/unequal trials before a trap map. The board-to-piles correspondence is acted out before use. Three-pile play and the complete six-reply experiment precede grouping counters into binary bundles; several separate bundle records precede the repair algorithm. Wythoff now has concrete play, a full classification grid, and a later greedy-pair record on separate pages.

## Current print packets

| Packet | Pages | Activity ID |
| --- | ---: | --- |
| [K–1](../../../week-08/archive/week-08-k-1.pdf) | 3 | F08-K-v3 |
| [Grades 2–3](../../../week-08/archive/week-08-grades-2-3.pdf) | 4 | F08-M-v3 |
| [Grades 4–5](../../../week-08/archive/week-08-grades-4-5.pdf) | 5 | F08-U-v3 |
| [Optional grades 6–7](../../../week-08/archive/week-08-extra-grades-6-7.pdf) | 3 | F08-X-v3 |
| [Facilitator guide and solutions](../../../week-08/archive/week-08-facilitator.pdf) | 6 | F08-F-v3 |

Print page 1 for each child's starting level (3 K–1, 3 middle, 1 upper = **7 sheets**) and keep continuation masters ready. Copy further pages as needed, give one at a time and retain earlier diagrams when referenced. The complete roster core set would be 26 sheets; it is not a completion expectation or the default print instruction. The separate extra is a three-page reserve. Print US Letter, single-sided, actual size; no physical fitting needs calibration.

**Kit:** About 60 counters, five plates or pile areas, pencils, and scraps labeled 1, 2, 4, 8. Reset and reuse the printed counter-sized mats. Middle page 3 reuses its earlier rook board.

The six-page guide gives the short shared launch after handling materials, prerequisites, specific hint ladders, representation gates, useful stopping points, optional proofs and keyed solutions to all added examples. Record actual use in the [session use log](../../../../plans/fall-k-5-year-a-use-log.md), separating observation, conjecture and supplied theorem.

Read the [redesign plan](../../../../plans/week-08-redesign.md) for rationale, source citations and returning-child branches. The prior [source archive](../archive-before-classroom-guidance-2026-09/) and [PDF archive](../../../week-08/archive-before-classroom-guidance-2026-09/) remain separate from current outputs.

## Rebuild and verify

Run `sh lowell-math-circle-year-2/source/week-08/build.sh` from the repository root. It runs `verify.py`, compiles all five TeX sources twice with pdfLaTeX and copies current PDFs to `lowell-math-circle-year-2/week-08/`. Intermediate files go to `tmp/pdfs/week-08-build/`. Requires Python 3, pdfLaTeX, TikZ, Source Sans Pro, microtype, geometry, fancyhdr, hyperref, amsmath/amssymb, tabularx and extarticle. No network access is needed.

Backward recursion checks 2,197 three-pile positions, 169 two-pile positions and 961 Wythoff positions. Added v3 assertions check the six replies to (1,2,3), three repairs of (4,6,7), balancing third piles and new Wythoff moves. See [REVIEW.md](REVIEW.md) for visual and structural verification.
