# Week 26 revised answers and assumptions

Three distinct investigations: internal room interfaces (P1–P2), boundary corners and holes (P3), exposed cube-building surfaces (P4–P6). One shared Grades K–5 packet; the concrete room/cube route admits routine adult recording, while formulas and optimum explanations require readiness. No material is classroom tested. Physical 20 mm tile fit, face covers, cube inspection and the boundary convention have not been rehearsed. The P1 grids are 20 mm per side in source geometry; counting/building in P3–P6 happens beside the page, and small diagrams are records.

## Problems 1 and 2

Minimum shared fence in a balanced 4×4 partition is four, attained by a straight middle horizontal or vertical cut. Both rooms then have perimeter 12 and the outside square has perimeter 16. For every partition, P_R+P_B=16+2L, where L is the shared fence count. Outside edges appear once and every shared side appears twice. P2 permits other room sizes; the identity does not require balance and survives disconnected rooms, though the printed room condition asks for connected rooms.

Elementary lower bound for P1: if all four rows are mixed, they each contribute a horizontal R/B transition, so L≥4. If both an all-R and an all-B row exist, each column contributes a vertical transition, so L≥4. Otherwise there is an all-R row and no all-B row, or the reverse. Eight B squares then occupy at least three mixed rows (at most three B per mixed row) and at least three columns (at most three B per column, because of the all-R row). Those rows contribute at least three horizontal transitions and columns at least three vertical transitions; L≥6. These cases exhaust all partitions. `src/check.py` checks all 12,870 balanced colorings and independently both-connected subsets; both minimums are four.

## Problem 3

Counts for the actual printed shapes:

| Shape | C | R | Holes |
|---|---:|---:|---:|
| 1, 3×2 rectangle | 4 | 0 | 0 |
| 2, one-tile-thick L with arms length 3 | 5 | 1 | 0 |
| 3, 3×3 ring | 4 | 4 | 1 |
| 4, 5×3 rectangle missing (1,1),(3,1), zero-based | 4 | 8 | 2 |

**The outline's numerical L example (6,2) does not apply to the actual ordinary L drawn here: its polygon has six vertices, five convex and one concave.** The general theorem remains C−R=4(1−h). Count every hole boundary. Restriction: side-connected polyomino; no vertex has exactly two diagonally opposite occupied squares. A side-connected shape can still contain such a pinch elsewhere, so the crossed-out local picture is a separate necessary restriction. Every printed shape obeys it.

A non-task local visual identifies the one-occupied-square convex corner and three-occupied-square concave corner by circling the common grid vertex. No traversal code is required on students' pages. For an explanation, trace each loop with occupied tiles on the left: outer loop has four more left quarter-turns, each hole loop four more right turns. Hence C−R=4−4h. Counts suggest the conjecture; the turning argument establishes it. Pinched shapes are outside the claim.

## Problems 4 and 5

Worked footprint conversion: two adjacent footprint squares with two cubes on each become a 2×1×2 building with four cubes. This illustrates stacking, not the target surface count.

Eight-cube buildings: row of eight has 34 exposed faces; 2×4 single layer has 28; 2×2×2 has 24, the least among those three buildings. P4 does not ask or claim a global optimum among every possible sculpture. Bottom faces count.

For a footprint of m squares, perimeter P including every hole boundary, and h solid layers everywhere, S=2m+hP. Top and bottom supply m each; every footprint-boundary edge supports h exposed side faces. Cube number mh. Side-connected footprint, positive integer height, no gaps or overhangs. P5's request to make a building has no prescribed unique footprint; this general formula answers every legal choice.

## Problem 6

Four positive stacks use ten cubes on the fixed 2×2 footprint. Top and bottom contribute eight faces. Each column has two exterior edges, so outside sides contribute 2(1+2+3+4)=20 regardless of permutation. Internal adjacent columns contribute the absolute height differences around the four-cycle. Thus S=28+cycle variation.

Minimum variation 6 gives S=34, e.g. row heights `1 2 / 3 4`; maximum 8 gives S=36, e.g. `1 3 / 4 2`. Of all 24 labeled permutations, sixteen give 34 and eight give 36 (independently check this count before using it). Every cycle visits min 1 and max 4, so the two paths between them each vary by at least 3, establishing lower bound 6. For the maximum, each edge joins two heights, and exhaustive 24-permutation comparison is an elementary complete explanation. More generally S=2m+sum(exterior-edge heights)+sum(neighbor absolute differences), under the solid vertical-stack assumptions. This is exposed surface work, separate from Week 1 height-map/flip tasks.

## QA and source status

`src/check.py` checks balanced partitions, actual corner counts, explicit exposed cube faces, and all 24 terrain arrangements. `writer-checks.json` records results. It is writer validation, not independent math review. Portable source build accepts an output directory, finds pdflatex or PDFLATEX, and depends only on standard LaTeX packages. Every page rendered/inspected. The outline makes no downloaded-source attribution for these new elementary cancellation/turning arguments.

## Revision convention scope

The shared cube guidance now explicitly counts bottoms for all cube tasks, including the equal-height rule in Problem 5. The local no-pinch restriction expressly applies even when the two diagonal tiles connect elsewhere. No new mathematical task or example was introduced.
