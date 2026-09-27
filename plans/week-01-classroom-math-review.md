# Independent review of the revised Week 1 middle boards

September 27, 2026. Reviewed the final board specification in [the packing data](week-01-classroom-middle-checks.json), its [author checker](week-01-classroom-middle-checks.py), and the generated [TikZ geometry](../lowell-math-circle-year-2/source/week-01/middle-geometry.tex). **No mathematical discrepancy found.** This is an independent mathematics and geometry audit; final printed-page layout is reviewed separately.

The [independent checker](week-01-classroom-independent-check.py) imports no author code. It reconstructs cells from polygon boundaries using integer winding numbers, derives blues from shared cell edges, derives chevrons from a separate four-triangle template, enumerates all reachable unions of disjoint placements, and verifies every supplied packing witness. It also reads TikZ coordinates back to the triangular lattice and checks every grid, outline, and solution polygon against the verified data. Including reflected chevrons creates no additional placements: rotations already realize those shapes.

Run `python3 plans/week-01-classroom-independent-check.py` from the repository root. All 14 board records pass, including the final truncated-triangle comparison board F.

## Problem 1

| Board | Triangle cells | Up / down | Maximum blues | Minimum gaps |
|---|---:|---:|---:|---:|
| A: side-3 triangle | 9 | 6 / 3 | 3 | 3 |
| B: three rows of the former two-rhombus parallelogram | 12 | 6 / 6 | 6 | 0 |
| C: B with its top-right down cell removed | 11 | 6 / 5 | 5 | 1 |
| D: long hexagon | 10 | 5 / 5 | 5 | 0 |

Board B is a 2-by-3 array of unit blue rhombi, so it adds two complete four-triangle rows to the old 2-by-1 board. The data's lattice coordinates draw the extension upward; translating the original row to the top gives the same outline as extending downward twice. Board C needs one gap by odd area, and the packing attains it. Its 6/5 orientation imbalance is exactly the unavoidable imbalance of one odd cell, not an additional obstruction that forces more gaps. Board A needs three gaps because only three down triangles are available.

These counts are necessary tests, not a claim that arbitrary balanced boards tile. The checked constructions establish that B and D actually tile. Problem 2 supplies even-area triangles that still fail to tile, making the orientation obstruction distinct from parity.

## Problem 2

| Triangle side | Up / down | Maximum blues | Minimum gaps |
|---|---:|---:|---:|
| 2 | 3 / 1 | 1 | 2 |
| 3 | 6 / 3 | 3 | 3 |
| 4 | 10 / 6 | 6 | 4 |
| 5 | 15 / 10 | 10 | 5 |

Every blue consumes one up and one down cell. The surplus of up cells is the side length. Pair every down cell with the up cell immediately to its lower left; the remaining row-edge up cells give an explicit packing attaining that lower bound. Thus these are proved optima rather than only successful trials.

## Problem 3

“Gaps” always means uncovered **unit triangle spaces**, not the number of tiles missing and not a mixture of blues and purples in one attempt.

| Board | Cells; up/down | Best blues / gaps | Best chevrons / gaps | Requested role |
|---|---|---|---|---|
| A: three-chevron strip | 12; 6/6 | 6 / 0 | 3 / 0 | Both tile |
| B: side-2 diamond | 8; 4/4 | 4 / 0 | 1 / 4 | Only blues tile |
| C: two-chevron arrow | 8; 4/4 | 4 / 0 | 2 / 0 | Both tile |
| D: long hexagon | 10; 5/5 | 5 / 0 | 2 / 2 | Only blues tile |
| E: arrow plus one triangle | 9; 5/4 | 4 / 1 | 2 / 1 | Neither tiles; equal optimal gaps |
| F: side-3 triangle minus its top unit triangle | 8; 5/3 | 3 / 2 | 1 / 4 | Neither tiles; fewer gaps with blues |

The final F polygon is `(0,0), (3,0), (1,2), (0,2)` in the stated axial coordinates. It retains the intended distinction with a shorter physical board than the full side-3 triangle.

The displayed constructions prove the claimed maxima can be reached. Area proves that D needs at least two chevron gaps and E at least one gap with either piece. For F, at most three blues can consume the three available down triangles. Each chevron consumes two down triangles, so at most one chevron fits. These bounds match the witnesses.

### Why the diamond cannot hold two chevrons

There is a short explanation using the exact intended two-blue replacement insight:

1. In a blue tiling of the diamond, the unit triangle at the bottom-left acute corner has only one possible partner. Place that forced blue.
2. Removing it forces the two neighboring blues along the two sides; the final blue is then forced. Therefore the only all-blue tiling consists of four parallel rhombi.
3. Each purple chevron splits into two blues with **different orientations**. If two chevrons tiled the diamond, replace each by those two blues. This would produce a blue tiling with nonparallel rhombi, contradicting the forced tiling.
4. One chevron does fit. It covers four of the eight cells, so four gaps is the exact optimum.

For a more direct physical check, neither acute corner cell can be covered by a chevron without crossing a side. A child can test the possible turns at a sharp corner. The independent enumeration confirms all six legal whole-chevron placements omit both acute corner cells, and every pair of placements overlaps. The forced-blue argument above gives a human explanation without relying on the enumeration.

### Scope of the comparison

Replacing every chevron in **any packing** by two blues preserves exactly the same covered cells. Therefore the best blue-only packing can never leave more gaps than the best chevron-only packing. It may leave the same number or fewer. A chevron tiling always yields a blue tiling; B and D show why the converse fails. No claim about mixed-tile optimization is needed for these tasks.
