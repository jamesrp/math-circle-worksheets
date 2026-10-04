# Week 10: Bridge puzzles, Euler trails, and the shortest delivery route

Revised September 20, 2026. Replace the unconstrained mixed-kit workshop with a coherent route investigation. Puzzle design remains, now controlled by an existence theorem, an invariant, and explicit optimality certificates. K1 reasons about dead ends; middle proves odd-degree obstructions and repairs; upper constructs Euler trails and minimizes repeated unit roads; extra solves a weighted postman instance and tests greedy pairing.

## Print packets

- [Cross every bridge once / Dead ends](../../week-10/week-10-k-1.pdf) — 2 pages, F10-K-v2. Triangle and triangle-with-branch; impossible three-leaf star; add one bridge between leaves and show a repaired route.
- [One-walk maps / Repair an impossible map](../../week-10/week-10-grades-2-3.pdf) — 2 pages, F10-M-v2. Find a house Euler trail, prove its endpoints forced, show K4 impossible, add a duplicate bridge to repair, and design a two-odd-vertex puzzle.
- [When a walk exists / Shortest delivery / Algorithm](../../week-10/week-10-grades-4-5.pdf) — 3 pages, F10-U-v2. Physically splice two triangle loops, optionally prove the Euler criterion including the two-odd case, optimize closed K4 at 8 and open K4 at 7, then design a six-odd-vertex network.
- [Cheapest pair first?](../../week-10/week-10-extra-grades-6-7.pdf) — 1 page, F10-X-v2. Weighted K4: original 20, minimum augmentation 3, optimum 23; compare all pairings and reject an incautious greedy choice.
- [Facilitator guide and checked solutions](../../week-10/week-10-facilitator.pdf) — 4 pages: prerequisites, realistic materials, 60-minute flow, prompts/hints, proofs, source links, and reuse guidance.

Print US Letter, single-sided, 100% / Actual Size. No physical fitting requires an exact scale. Give pages one at a time. For the current K,K,1 / 3,3,3 / 5 roster, three K1 packets + three middle packets + one upper packet = **15 student sheets**, plus the optional one-page extra. Grade labels are entry points, not placement rules.

**Kit:** Seven moving counters, about 35 small used-edge markers, pencils, scrap paper, and two short paper strips for the upper loop splice. Optional strings/paper islands enlarge the models. Dots are junctions; line crossings without dots are not junctions.

Read the [redesign plan](../../../plans/week-10-redesign.md) for the mathematical trajectory and primary research references. These are prepared activities, not teaching records. Record exact use in the [session use log](../../../plans/fall-k-5-year-a-use-log.md).

## Rebuild and check

Run `sh lowell-math-circle-year-2/source/week-10/build.sh` from the repository root. It runs `verify.py`, compiles all five editable LaTeX sources twice, and places PDFs in `lowell-math-circle-year-2/week-10/`. Requires Python3, pdfLaTeX, TikZ, Source Sans Pro, microtype, geometry, fancyhdr, hyperref, amsmath/amssymb, tabularx, and extarticle. No network access is needed to rebuild.

Independent Dijkstra search over (current vertex, visited-edge mask) verifies closed/open unit costs 8 and 7 and weighted cost 23. Route edge coverage is checked independently. The parity and pairing certificates prove the claims beyond the computation.

After edits, render and visually inspect all pages. See [REVIEW.md](REVIEW.md) for the completed checks.
