# Week 1: tiling, impossibility, and flips

Revised September 27, 2026, for the organizer's **21st Century Pattern Blocks** and **Upscale Pattern Blocks**. These LaTeX/TikZ worksheets replace the first draft with investigations of tileability, invariants, optimal packing, and local moves. Grade bands are entry points, not placement rules.

## Print packets

Revised September 27, 2026 after the organizer's classroom feedback. The new versions are prepared, not yet taught. [Classroom review and adopted guidance](../../../plans/week-01-classroom-review.md) records the observations and organizer-approved guidance, now adopted in AGENTS.md.

- [K–1](../../week-01/week-01-k-1.pdf) — 4 pages, F01-K-v4. Same eight full-size filling shapes; direct numbered problems and no Name/Date fields or competing page titles.
- [Grades 2–3](../../week-01/week-01-grades-2-3.pdf) — 4 pages, F01-M-v3. Four larger blue-only boards; explicit side-2, 3, 4 and 5 triangles; six blue-only versus purple-only comparisons. The pink-triangle task is removed. Problem 2 spans two pages to keep every triangle at actual block size.
- [Grades 4–5](../../week-01/week-01-grades-4-5.pdf) — 5 pages, F01-U-v3. One full-size board and eight recording copies on page 1; flip demonstration and map drawn on six cards; routes and odd returns; a sequence of ribbon tracing, reconstruction, counting and flip problems.
- [Facilitator guide and solutions](../../week-01/week-01-facilitator.pdf) — 6 pages. Whole-group warmup, preparation, prerequisites, solutions, packing bounds, ribbon arguments, and reserves.
- [Optional paper rhombi](../../week-01/week-01-extra-rhombi.pdf) — 1 page, 12 small rhombi.

Print **US Letter, single-sided, 100% / Actual Size**. Use **1× pieces**. Check a printed edge against a real block; the calibration line is in the adult guide and cutout sheet. After free handling, bring everyone together to place blues on middle Problem 1 before distributing separate starting tasks. Give later pages when children are ready. Keep the upper reference cards back until they have built and recorded tilings themselves. Finishing every page is not the goal.

For the current 3 / 3 / 1 roster: 3 K–1 packets, 3 middle packets and 1 upper packet = **29 student sheets**. Each K–1 child needs 6 blues, 12 greens, 3 purples and a few reds/yellows; each middle child needs 10 blues, 5 greens and 3 purples; the upper child needs 8 blues. Gather **56 small blues, 51 greens and 18 purples** across the kits, reusing them between boards. The side-5 triangle drives the increased blue count. No pink pieces are needed.

The [classroom snapshot PDFs](../../week-01/archive-classroom-2026-09/) and [sources](archive-classroom-2026-09/README.md) preserve the materials brought to the previous meeting. The exact meeting date and each child's completed problems are unknown; optional extensions were reported unused. The older `archive-v1/` remains a separate first draft.

## Does the size match?

The default small edge is **1 inch (25.4 mm)**. The user measured a green triangle at approximately one inch. Christopher Danielson's [mosaic account](https://talkingmathwithkids.com/blog/minnesotas-largest-pattern-block-mosaic/) identifies one-inch shortest sides for 21st Century blocks, and his [production account](https://talkingmathwithkids.com/blog/21st-century-pattern-blocks-scaling-up/) describes compatibility with traditional blocks. This supports nominal compatibility, not an exact measurement of this particular batch.

Check the printed calibration line against a 1× green edge. A 25 mm block is about 1.6% smaller than 25.4 mm. If the mismatch is visible, trace the actual pieces or set `\blockside` in `common.tex` to the measured value and rebuild. The user's physical **2× and 3× green triangles are exact boundary templates** for the corresponding middle boards. The larger side-4 and side-5 triangles use the same one-inch unit edge. Avoid “Fit to page,” which changes the scale unpredictably.

The purple chevron is the concave six-sided piece, not the gray dart. No square is required. The [manufacturer booklet](https://mathforlove.com/wp-content/uploads/2024/10/21st-Century-Pattern-Block-Booklet-to-share.pdf), p. 2, identifies the shapes and counts.

## Back-pocket extensions

For children ready to go further, a separate packet offers four investigations at roughly a **grades 6–7 reasoning level**. Give one challenge at a time; the facilitator guide starts with a selection table, prerequisites, materials, and flexible timing.

- [Student challenges and full-size mat](../../week-01/week-01-extensions.pdf) — 5 pages. A balanced board with four unavoidable gaps; distances among twenty tilings; forty-two shortest routes; two random-walk rules with different visit frequencies.
- [Extension facilitator guide and solutions](../../week-01/week-01-extensions-facilitator.pdf) — 5 pages. Gradual hints, constructions, proofs, generalizations, and optional expected-return calculations.

X1 uses seven small blues and four greens. X2 uses fifteen small blues, or three R slips and three L slips. X3 uses the letter slips; X4 uses a counter, die, scrap paper, and four numbered slips. Student page 5 is the large X2 mat. Print only the chosen pages at Actual Size. The [extension plan and source notes](../../../plans/week-01-extensions.md) and [independent review](EXTENSIONS-REVIEW.md) document the mathematics and verification.

Rebuild with `sh lowell-math-circle-year-2/source/week-01/build-extensions.sh`. Editable sources are `week-01-extensions.tex` and `week-01-extensions-facilitator.tex`; generated geometry comes from `generate-extensions.py` and the checked JSON files in `plans/`. Core packet sources remain separate. Extension problem content is unchanged in the classroom revision; only Name/Date fields were removed.

## Mathematical direction and sources

Start with [the redesign rationale](../../../plans/week-01-tiling-redesign.md). The [undergraduate notes](../../../plans/week-01-undergraduate-notes.md) document coloring invariants, matching, recursive construction, and the exact middle-level solutions. The [research notes](../../../plans/week-01-research-level-notes.md) document Thurston, lozenge flip graphs, height functions, enumeration, and random dynamics, with primary links and assumptions.

The [revised activity guide](../../../plans/fall-k-5-year-a-activities.md#week-1-tiling-impossibility-and-flips) gives the full hour. The old P1/P2 minimum-piece [PDFs](../../week-01/archive-v1/) and [sources](archive-v1/README.md) are preserved as optional, untaught reserves; they are no longer the default middle and upper activities. Preparation is not evidence of teaching: record actual instances in [the use log](../../../plans/fall-k-5-year-a-use-log.md).

## Build and verify

Run `sh lowell-math-circle-year-2/source/week-01/build.sh` from the repository root. Requires Python 3 and pdfLaTeX with TikZ, Source Sans Pro, microtype, fancyhdr, geometry, tabularx, hyperref, amsmath, and extarticle (available in TeX Live/MacTeX). The build regenerates `tilings.tex`, `k1-geometry.tex`, and `middle-geometry.tex` from checked geometry, compiles the five sources, and writes final PDFs to `lowell-math-circle-year-2/week-01/`.

`python3 plans/week-01-lozenge-research.py` exhaustively enumerates the six eight-rhombus tilings and their legal flips, checks heights and shortest paths, and verifies the 20-tiling scaled-hexagon count. Its JSON is the geometry source for the drawings. Mathematical proofs in the facilitator guide explain the results independently of enumeration. `python3 plans/week-01-classroom-middle-checks.py` checks every new middle board and packing; `python3 plans/week-01-classroom-independent-check.py` independently reconstructs cells, enumerates packings and reads back the generated drawing coordinates. After changing dimensions or text, render and inspect all pages again.

`python3 plans/week-01-k1-shape-checks.py` checks every new outline and saves exact tiling witnesses in its adjacent JSON. The K–1 generator reads that data to draw the mats and facilitator examples at the same one-inch scale.

The [review record](REVIEW.md) documents the fresh subagent's independent mathematical and visual checks, the feedback incorporated, and final print verification.
