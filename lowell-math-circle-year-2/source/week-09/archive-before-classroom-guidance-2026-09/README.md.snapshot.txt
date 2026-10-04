# Week 9: Unfolding billiards: corners, gcd, and dynamics

Revised September 20, 2026. Unfolding becomes the main representation instead of a brief optional preview. Middle children coordinate two lists of wall locations and design corners; upper children prove the gcd/parity classification, derive an exact bounce formula, and solve inverse existence/impossibility problems. The extra changes slope and distinguishes avoiding corners from being dense, with the density theorem stated for the origin-start √2 path. The [shared divisibility scaffold](../../../plans/coprime-divisibility-scaffold.md) supports the optional arithmetic proof.

## Print packets

- [Bounce to a corner / See a straight path](../../week-09/week-09-k-1.pdf) — 2 pages, F09-K-v2. Compare 2×2,2×4,4×2, then fold mirrored rooms around a straight line.
- [Unbounce the ball / When do walls meet?](../../week-09/week-09-grades-2-3.pdf) — 2 pages, F09-M-v2. Trace 2×3, unfold to (6,6), classify 2×3,3×6,3×9,4×6 and make target tables.
- [A straight line in many rooms / Every corner / Bounce design](../../week-09/week-09-grades-4-5.pdf) — 3 pages, F09-U-v2. Use whole-room counts to rule out bottom-left and count bounces; optionally prove the reduced-side formula with an adult and classify inverse designs.
- [Change the slope](../../week-09/week-09-extra-grades-6-7.pdf) — 1 page, F09-X-v2. In a unit square, derive the first lattice point for p/q, prove √2 never reaches a corner, and find a periodic no-corner diamond from a different start.
- [Facilitator guide and checked solutions](../../week-09/week-09-facilitator.pdf) — 4 pages: prerequisites, realistic materials, 60-minute flow, prompts/hints, proofs, source links, and reuse guidance.

Print US Letter, single-sided, 100% / Actual Size. No physical fitting requires an exact scale. Give pages one at a time. For the current K,K,1 / 3,3,3 / 5 roster, three K1 packets + three middle packets + one upper packet = **15 student sheets**, plus the optional one-page extra. Grade labels are entry points, not placement rules.

**Kit:** Seven counters, rulers, pencils, scrap square-grid paper, and two spare copies of the K1 folding page. An adult may trace while a child chooses bounces. No real ball or precision construction is required.

Read the [redesign plan](../../../plans/week-09-redesign.md) for the mathematical trajectory and primary research references. These are prepared activities, not teaching records. Record exact use in the [session use log](../../../plans/fall-k-5-year-a-use-log.md).

## Rebuild and check

Run `sh lowell-math-circle-year-2/source/week-09/build.sh` from the repository root. It runs `verify.py`, compiles all five editable LaTeX sources twice, and places PDFs in `lowell-math-circle-year-2/week-09/`. Requires Python3, pdfLaTeX, TikZ, Source Sans Pro, microtype, geometry, fancyhdr, hyperref, amsmath/amssymb, tabularx, and extarticle. No network access is needed to rebuild.

An independent unit-step reflection tracer verifies all 900 rectangles of side lengths 1–30 against the formulas, plus the complete four-bounce top-right reduced-pair list and several rational-slope event counts.

After edits, render and visually inspect all pages. See [REVIEW.md](REVIEW.md) for the completed checks.
