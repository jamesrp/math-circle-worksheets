# Adversarial review: Week 68, How many ways out

## Verdict

**Pass mathematically and visually; retain the finite/infinite distinction and specify appropriately small blockers for the grid.** The single four-page Grades 3–5 packet follows the authorized outline. No mathematical or PDF-rendering blocker remains after close inspection. Do not replace the infinite patterns by finite-board exit counts.

## Scope and evidence

Read the actual repository `AGENTS.md`, `README.md`, complete run `PROMPT.md`/`CRITIC.md`, and the draft's LaTeX, README, and checker. Rendered and inspected every page at 120 dpi (`critic-render/page-1.png` through `page-4.png`). Also inspected the introductory deletion example at high resolution and checked its actual PDF vector edges. PDF SHA-256: `0e8c78d13b3134a3da80c30e6efff2679fd8f2ff46d646d864058d83bc7e01e5`.

The writer's checker passes the line, all up-to-four-blocker placements in its ladder core, the grid pocket/wall, and the 3,6,12,24 tree counts. The separate independent kernel and exact-instance audits agree; this PDF and source match their recorded fingerprints. Independently reasoned through the actual printed deletions and the exterior/tail arguments below. No draft edit, physical rehearsal, or classroom pilot was performed.

## Mathematical and page-by-page audit

- **Page 1, shared visual convention:** Deleting the upper-right vertex of the four-cycle leaves the left vertical and bottom horizontal edges, a connected two-edge path. Both edges are present in the PDF, confirmed with high-resolution rendering and vector-path inspection. The example correctly deletes only the chosen vertex and its incident roads.
- **Page 1, Problem 1:** The maximum number of forever pieces is **2** for one, two, or four blockers. With any nonempty finite blocked set, the left and right tails remain, while any intervening components are finite. The task explicitly excludes those finite pockets from the forever-piece count.
- **Page 1, Problem 2:** A four-blocker solution exists on the nine printed vertices. Labeling them −4 through 4 for this audit, blockers at −3,−1,0,2 isolate the two finite singleton pieces −2 and 1. The adjacent blockers −1,0 create no intervening open piece. The same two infinite tails remain. This is an appropriate contrast with simply counting all components.
- **Page 2, Problem 3:** One deleted ladder vertex leaves the infinite ladder connected. Deleting both endpoints of one rung separates the two infinite tails. Two adjacent deleted vertices on one rail do not separate the infinite part, since the other rail provides a detour. The two boards support a retained comparison while partner attempts can be repeated.
- **Page 2, Problem 4:** Four blockers cannot create three forever pieces. Outside the leftmost and rightmost blocked columns there are only two connected tails, and every infinite component must meet one of them. Finite pockets in between do not count. This is a genuine explanation task, not something established by testing all visible placements alone.
- **Page 3, Problem 5:** Four orthogonal neighbors of an open grid vertex trap that vertex. The remaining grid has one forever component. The five closed vertices on the right are (0,−2) through (0,2), with P=(−2,0), Q=(2,0); a detour through row 3 or −3 joins P to Q in **10 steps**. Minimum distance is not asked, so this is an audit check rather than an extra student demand. The wall does not disconnect the infinite grid.
- **Page 3, Problem 6:** The answer is no. Every finite blocked set lies in some square; outside a larger square the grid is connected, and every forever component must reach that exterior. The student task explicitly asks for an argument that extends beyond the page. Do not add a printed enclosing-box method: that is an adult hint/solution.
- **Page 4, Problem 7:** The pictured graph has three branches from the center and two forward branches at every later vertex. The nested deletions of the center, radius 1, and radius 2 leave **3, 6, 12** forever components. The word “too” correctly makes the deletions cumulative.
- **Page 4, Problem 8:** Radius 3 leaves **24** components; each further radius doubles the number. “Branches never join again” and the explicit repeated splitting rule justify this beyond the finite drawing. The printed questions do not incorrectly identify 3, 6, or 12 with the graph's fixed number of ends. Unboundedly many complementary forever pieces is the intended route toward infinitely many ends.

## Operational refinement

**Medium priority for material preparation, page 3:** Its vertex spacing is **10 mm**, appreciably smaller than the line/ladder boards. Ordinary large counters are a poor fit: four around one center overlap and can obscure the open vertex and nearby roads. Specify small opaque squares/counters, about **6–8 mm across**, in the source preparation note and eventual guide, or enlarge the grid if standard larger counters are intended. The existing outline already permits paper squares, so this is inexpensive and does not need a new student instruction block. Have at least **10 blockers per pair** for the radius-2 tree deletion; radius 3 can be reasoned about rather than physically covered. A physical fit test is still needed before claiming classroom readiness.

## Format, independence, and age-fit review

- All four US Letter pages have correct week/topic/Grades 3–5 headers, consistent packet footers, and consecutive Problems 1–8. No text clipping, figure collisions, missing glyphs, off-page labels, or extra blank pages were found. All continuation edges are arrowed; the square grid states that routes may leave the printed window.
- The road-deletion example is a useful input/action/output demonstration before first use. An X records the deleted vertex after a counter is lifted, so state does not depend on memory. The partner's route tracing provides a concrete legality check.
- Line, ladder, grid, and branching tree supply four genuinely contrasting geometries. The progression establishes finite pockets before introducing a grid that goes around every finite obstacle. The later tree never-rejoin rule carries the infinite conclusion, rather than the number of arrowheads alone.
- “Forever piece” is adequately defined as going beyond every distance. The term is informal but more accessible than an unmotivated formal ends definition. Adult discussion must still distinguish “arbitrarily many components after larger finite deletions” from “many visible arrows.”
- The first line tasks and the last doubling prediction may be shorter than five minutes individually for quick children. The whole packet nevertheless has repeated partner attempts and two substantial impossibility explanations. Do not pad every numbered task with more recording just to satisfy a time quota. A later guide can offer more blocker arrangements if a group moves quickly.
- The grade band is a prerequisite gate: route following and small counts provide the entry; claims about any finite obstruction and arbitrary growth are readiness-dependent later work. Adult reading is compatible with children making the actual placements and route choices. This remains an unpiloted pedagogical assessment.

## Revision priority

Preserve all mathematical instances and the four-page progression. Confirm small-blocker preparation, and re-render if any dimensions or text change. No repair to the introductory deletion diagram is required.
