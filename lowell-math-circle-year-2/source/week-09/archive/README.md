> Archived October 3, 2026. This version was replaced by the [concrete revision](../README.md); its PDFs are in `lowell-math-circle-year-2/week-09/archive/`, and `sh lowell-math-circle-year-2/source/week-09/archive/build.sh` rebuilds it there.

# Week 9: Unfolding billiards: corners, gcd, and dynamics

Revised September 27, 2026 from the Week 1 classroom feedback and adopted AGENTS.md guidance. **All v3 pages are unpiloted.** Several contrasting bounce traces now precede mirrored rooms. Original and unfolded paths are paired with numbered crossings; two more concrete room pictures and endpoint-count records support folding before multiples are used to predict. Upper tasks separate scaled copies, first-corner failure, wall-count work and inverse design. The extra now has five rational-slope trials and a visible midpoint diamond before discussing irrational direction and density.

## Current print packets

| Packet | Pages | Activity ID |
| --- | ---: | --- |
| [K–1](../../../week-09/archive/week-09-k-1.pdf) | 3 | F09-K-v3 |
| [Grades 2–3](../../../week-09/archive/week-09-grades-2-3.pdf) | 4 | F09-M-v3 |
| [Grades 4–5](../../../week-09/archive/week-09-grades-4-5.pdf) | 5 | F09-U-v3 |
| [Optional grades 6–7](../../../week-09/archive/week-09-extra-grades-6-7.pdf) | 3 | F09-X-v3 |
| [Facilitator guide and solutions](../../../week-09/archive/week-09-facilitator.pdf) | 6 | F09-F-v3 |

Print page 1 for each child's starting level (3 K–1, 3 middle, 1 upper = **7 sheets**) and keep continuation masters ready. Copy further pages as needed, give one at a time and retain earlier diagrams when referenced. The complete roster core set would be 26 sheets; it is not a completion expectation or the default print instruction. The separate extra is a three-page reserve. Print US Letter, single-sided, actual size; no physical fitting needs calibration.

**Kit:** Counters, rulers, pencils, scrap square-grid paper and adult scissors. Copy K page 3 separately and cut between the two panels before folding; keep traced earlier pages available for comparison. An adult may draw while a child chooses each direction.

The six-page guide gives the short shared launch after handling materials, prerequisites, specific hint ladders, representation gates, useful stopping points, optional proofs and keyed solutions to all added examples. Record actual use in the [session use log](../../../../plans/fall-k-5-year-a-use-log.md), separating observation, conjecture and supplied theorem.

Read the [redesign plan](../../../../plans/week-09-redesign.md) for rationale, source citations and returning-child branches. The prior [source archive](../archive-before-classroom-guidance-2026-09/) and [PDF archive](../../../week-09/archive-before-classroom-guidance-2026-09/) remain separate from current outputs.

## Rebuild and verify

Run `sh lowell-math-circle-year-2/source/week-09/build.sh` from the repository root. It runs `verify.py`, compiles all five TeX sources twice with pdfLaTeX and copies current PDFs to `lowell-math-circle-year-2/week-09/`. Intermediate files go to `tmp/pdfs/week-09-build/`. Requires Python 3, pdfLaTeX, TikZ, Source Sans Pro, microtype, geometry, fancyhdr, hyperref, amsmath/amssymb, tabularx and extarticle. No network access is needed.

An independent unit-step reflection tracer checks all 900 rectangles with sides 1–30. Added assertions cover the height-6, swapped/square, scaled and inverse-design examples, and first vertices for 1/2, 2/4, 2/3, 3/2 and 3/4. Origin-start and normalized-slope qualifications remain in the guide; density is supplied as a separate theorem. See [REVIEW.md](REVIEW.md) for visual and structural verification.
