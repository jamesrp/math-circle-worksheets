# Week 1, grades 2–3: checked classroom revisions

These are the exact boards and solutions for the four-page **F01-M-v3** packet. This revision follows the organizer's classroom feedback: expand hands-on examples before asking for the structural explanation; state the activity directly; compare separate blue-only and purple-only attempts; remove pink triangles.

All student mats use nominal one-inch unit edges. Problem 2 occupies two pages so all four triangles remain usable with actual small blocks. Problem 3 uses six boards of height two triangle rows, so all six fit at full size on one page.

## Problem 1: four boards

| Board | Total cells | Up | Down | Most blues | Fewest empty cells |
|---|---:|---:|---:|---:|---:|
| A: side-3 triangle | 9 | 6 | 3 | 3 | 3 |
| B: original two-rhombus parallelogram, extended by two rows | 12 | 6 | 6 | 6 | 0 |
| C: B with the upper-right down-pointing cell removed | 11 | 6 | 5 | 5 | 1 |
| D: long hexagon | 10 | 5 | 5 | 5 | 0 |

Each blue covers two cells, so an odd total prevents a full covering. Each blue also uses exactly one up and one down cell, so it cannot remove an excess of either orientation. A requires at least three empty cells; five blues cover all but one of C. B and D have explicit full coverings.

**Parity nuance:** an odd-cell board cannot have equal up and down counts. The intended “parity is the only gate” for C means that the odd-area argument already gives its sharp one-gap bound: there is no additional geometric obstruction. It does not mean orientation counts are equal, or that parity and orientation are independent on C. Problem 2 supplies the even-area counterexamples (side 2 and side 4) needed to show that even area alone is insufficient. Equal orientation counts are necessary but not sufficient for arbitrary regions; no worksheet asks children to assert sufficiency.

## Problem 2: triangles of four sizes

| Side length | Total cells | Up | Down | Most blues | Fewest empty cells |
|---|---:|---:|---:|---:|---:|
| 2 | 4 | 3 | 1 | 1 | 2 |
| 3 | 9 | 6 | 3 | 3 | 3 |
| 4 | 16 | 10 | 6 | 6 | 4 |
| 5 | 25 | 15 | 10 | 10 | 5 |

In each horizontal row there is one more up than down triangle. Every blue uses one of each, so the total up/down imbalance is n and at least n cells stay empty. The gaps need not be distributed one per row. Pair each down cell with the up cell immediately below-left of it. The unpaired cells lie along one sloping boundary, attaining exactly the side length in gaps. This gives a child-accessible argument using rows and actual pieces, without formulas. For adults, the counts are n(n+1)/2 up and n(n−1)/2 down; the optimum is n(n−1)/2 blues and n gaps.

## Problem 3: six separate comparisons

Clear the board between trials. The first trial permits only small blue rhombi; the second permits only purple chevrons. Mixing colors would hide the strict restriction the comparison is designed to reveal.

| Board | Cells | Up/down | Most blues | Blue gaps | Most purples | Purple gaps | Requested category |
|---|---:|---:|---:|---:|---:|---:|---|
| A: wide arrow | 12 | 6/6 | 6 | 0 | 3 | 0 | Both tile |
| B: side-2 diamond | 8 | 4/4 | 4 | 0 | 1 | 4 | Blue only |
| C: arrow | 8 | 4/4 | 4 | 0 | 2 | 0 | Both tile |
| D: long hexagon | 10 | 5/5 | 5 | 0 | 2 | 2 | Blue only |
| E: expanded arrow | 9 | 5/4 | 4 | 1 | 2 | 1 | Neither; equal optimum gaps |
| F: flat-topped triangle | 8 | 5/3 | 3 | 2 | 1 | 4 | Neither; blues leave fewer gaps |

A and C have displayed full coverings in both colors. D's ten cells require at least two gaps with purples because each purple covers four; two purples attain this. E needs at least one gap by odd area; four blues or two purples attain it. F has three down cells, so at most three blues fit. Every purple covers two up and two down cells, so at most one purple fits; the witnesses attain both bounds.

B is the geometric example: it has a multiple of four cells and balanced orientation counts but still cannot fit two purples. Its blue tiling is forced: the acute lower-left corner cell has only one possible blue partner; removing that blue forces the next two, then the last. All four blues are parallel. Each purple splits into two nonparallel blues. If two purples tiled the diamond, replacing them would produce a blue tiling with nonparallel pieces, contradicting the forced tiling. One purple fits, so four gaps is the exact optimum. The exhaustive placement search and separate independent review agree with this geometric proof.

Finally, ask children to cover one purple with blues. Every purple can be replaced by two blues on exactly its footprint. Consequently every purple-only packing produces a blue-only packing with the same empty cells, and the best blue packing can never leave more gaps than the best purple packing. A/C/E show equality is possible; B/D/F show the restriction can matter. Do not infer that each pair of blues can be combined into a purple.

## Verification and editable geometry

`week-01-classroom-middle-checks.py` defines the polygons, enumerates all legal blue and purple placements, computes maximum covered area with a bitmask dynamic program, validates each witness, checks simple edge-connected board boundaries and whole-cell areas, and independently verifies every blue optimum using bipartite augmenting paths. It also checks that all six rotated orientations of the physical purple are exactly coverable by two blues. Saved data and witnesses are in `week-01-classroom-middle-checks.json`.

`generate-middle-geometry.py` builds `middle-geometry.tex` from those checked data. In LaTeX:

- `\MiddleBoard{OneA}{1}` prints a full-size blank board.
- `\MiddleSolution{ThreeB}{purple}{.6}` prints a purple optimum at 60% scale.
- Names: `OneA`–`OneD`, `Triangle2`–`Triangle5`, `ThreeA`–`ThreeF`.

The blue/purple cell definitions and physical chevron match the existing `common.tex` and `plans/week-01-k1-shape-checks.py`. Triangle-row reasoning continues the checked Week 1 facilitator mathematics; the six comparison-board selection and progression are new adaptations of the organizer's classroom feedback, not a claimed quotation from a source.

Supplies per middle child: ten small blues, three purples, optionally five greens to mark empty cells; reuse the same pieces for each board. Counting now reaches 25 cells. Reading the short instructions can be supported aloud; no arithmetic beyond counting, pairing, and comparing is needed for the intended explanations.
