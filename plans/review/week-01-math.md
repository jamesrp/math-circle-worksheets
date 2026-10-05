# Week 1 tiling lab: math check

Packet checked: `lowell-math-circle-year-2/week-01/week-01-k-1.pdf` (F01-K-v4), `week-01-grades-2-3.pdf` (F01-M-v3), `week-01-grades-4-5.pdf` (F01-U-v3) and `week-01-facilitator.pdf` (FACILITATOR v3). Sources: `lowell-math-circle-year-2/source/week-01/`, including the generated `k1-geometry.tex`, `middle-geometry.tex` and `tilings.tex`. I did not use the author's checker or JSON files.

## Method

Math check for the Week 1 review card, October 5, 2026. My scripts and their outputs (`out_*.txt`) are in [checks/week-01/](checks/week-01/); each runs from the repository with `python3 plans/review/checks/week-01/<script>`.

- `lattice.py`: shared triangular-lattice code. It converts coordinates to lattice points, finds the cells inside a polygon, places pieces in all 12 symmetries, and runs exact exhaustive search for maximum packings and tilings. Pieces: green, blue, red, yellow, and the purple chevron `\ChevronPath` (two blues joined along a horizontal edge).
- `check_k1.py` and `check_k1_witness.py`: the eight K–1 outlines (area, lattice alignment, up/down counts, tilings with each piece type, mixed tilings) and every K–1 solution drawing in the guide.
- `check_middle.py`: all 14 grades 2–3 boards. For each: whether the drawn grid equals the outline, the up/down counts, the exact maximum blue and purple packings, and every witness drawing in the guide. It also lists all purple placements on Problem 3 Board B.
- `check_upper.py`: all blue tilings of the H122 board. It checks that cards A–F are exactly those tilings, computes each ribbon and compares it with the drawn path, and finds flips geometrically from the four interior lattice points. It then checks the map edges, the shortest routes, bipartiteness and closed-walk counts, the highlighted flip patch, both random-walk claims (exact fractions), the side-2 hexagon count and the "bottleneck" reserve.
- `check_symmetry.py`: the board symmetries acting on cards A–F.
- `check_pdf_geometry.py`: reads the vector drawings in the delivered PDFs, converts them back to lattice data and compares them with the source. Every outline is lattice-exact at one scale in both axes. The grid matches the outline on every board. Each card's drawn tiling is the labelled tiling. The printed ribbons read RRLL on A (Problem 5), RLLR and LLRR (Problem 8). The extracted PDF text matches the `.tex` problem statements.

## Located problems

### 1. Grades 4–5, page 1, Problem 1: the expected count depends on whether mirror images count (low–moderate)

Text: "Fill the large board using only small blue rhombi. Find as many different tilings as you can. **Keep the bold edge at the bottom.** … How many different tilings did you find?"

The intended answer is 6 (guide p. 5: "there are \(\binom42=6\) tilings"). But the left–right mirror of the board keeps the bold edge at the bottom, and it maps the tilings in pairs:

```
left-right mirror (keeps bold edge at bottom): A<->F, B<->E, C<->D   (no tiling is symmetric)
180-degree rotation (moves bold edge to top):   A<->F, B<->E, C, D fixed
```
(`out_check_symmetry.txt`)

A child who counts a flipped copy as "the same tiling" is following the printed rule and gets **3**. The bold edge rules out only the symmetries that move it to the top: the 180° rotation and the top–bottom mirror. Under the full symmetry group of the board the count is also 3. So the edge does not force the answer 6.

Smallest fix: add one sentence to Problem 1: "Mirror images count as different tilings." Alternatively, add a guide note: "An answer of 3 pairs mirror images (A/F, B/E, C/D); the bold edge does not rule that out. Ask which tilings come in mirror pairs." Either keeps the six cards and the map.

### 2. Facilitator guide: no theorem-first mathematical overview (structural; the facts themselves are correct)

Page 1 ("Start together") covers materials, the warm-up, readiness and timing. The mathematical facts first appear inside the per-problem solutions on pp. 2–5. There is no opening statement of the theorems, their hypotheses and limits, or a map to the bands. The project's guide requirements call for one. Every fact the guide does state checks out (see "Checked and correct" below).

Smallest fix: add a short overview at the top of page 1, or as a page-1 box. Every statement below is verified by the scripts:

> **Mathematical destination.** (1) With grid-aligned pieces, a blue covers one up and one down triangle. So a board can be filled only if its area is even and its up and down counts are equal, and at least |up − down| spaces stay empty in any blue packing. In the side-*n* triangle (*n* ups more than downs) the best packing leaves exactly *n* gaps. (2) These counting conditions are necessary, not sufficient: the six-cell "bottleneck" reserve is balanced but cannot be filled (a matching obstruction). (3) A purple is two blues, so the fewest blue gaps are never more than the fewest purple gaps. Blues do strictly better on Problem 3 boards B, D and F and tie on A, C and E. (4) The 1-2-2 hexagon has exactly six blue tilings. Each is fixed by its ribbon, a word with two L's and two R's, and all six words occur. A flip swaps one adjacent RL or LR. The flip map is connected, A to F takes four flips, and every return trip has even length (the R-position sum changes parity at each flip). *Limits:* grid-aligned placements only. The one-ribbon argument uses the fact that this board has a single bottom and a single top horizontal edge; larger hexagons have several ribbons. *Bands:* K–1 experiment with fillings; 2–3 find and explain obstructions and best packings; 4–5 study the space of all tilings. The packing counts and the six tilings are experiments. "Gaps ≥ |up − down|", "the ribbon determines the tiling" and "no odd returns" are the explanations.

### 3. Grades 2–3, pages 2–3: two problems are numbered "Problem 2" (low; label only)

Page 2: "**Problem 2:** Use only small blue rhombi on these triangles and the triangle on the next page…". Page 3: "**Problem 2:** Fit as many small blue rhombi as you can in this triangle…". Page 4 is then "Problem 3", so the packet reads 1, 2, 2, 3. The mathematics is unaffected: the guide's "Middle Problem 3" is the student page labelled Problem 3, and "Compare your four best packings" correctly means the side-2, 3, 4 and 5 triangles. Still, a repeated number makes "Problem 2" ambiguous when adults and children refer to problems.

Smallest fix (page 3 is meant to continue page 2): delete the second "Problem 2:" heading and its restated rule sentence on page 3, keeping the side-5 triangle, the record line and the comparison question. Alternatively, renumber page 3 as Problem 3 and the purple page as Problem 4, and rename the guide's "Middle Problem 3" heading to match.

### 4. Facilitator guide, page 2, Middle Problem 2: "below-left" names the wrong neighbour (low)

Text: "Pair each down space with the up space **just below-left of it**. The remaining ups run along the right edge, attaining exactly *n* gaps."

The construction is correct only if the partner is the up triangle beside it, sharing its left slanted edge, in the **same row**. That triangle's centre is lower and to the left, but it is not in the row below. A down triangle has no edge-adjacent up triangle in the row below; its three neighbours are left, right and above. An adult who reads "below-left" as "in the row below" will try to pair triangles that touch only at a corner. With the same-row reading I checked the construction for n = 2…5: it leaves exactly the n up triangles along the right edge.

Smallest fix: "Pair each down space with the up space just to its left in the same row."

### 5. Grades 4–5, page 5, Problem 8: copying a card can stand in for the rebuild and the uniqueness check (low)

Text: "Rebuild the tiling from each ribbon. … Can either ribbon give you two different tilings?" The two printed ribbons are RLLR and LLRR. These are exactly the ribbons the child drew on cards D and F in Problem 6 (verified from the PDF drawings). The child can copy card D and card F. They can also answer "no" because each code appears on only one card. That argument assumes the six cards are all the tilings, which is what the ribbon argument is meant to prove (the guide itself says, p. 4, "The cards are a supplied list until the child can explain why the ribbon accounts for every tiling"). On this board every ribbon belongs to some card, so the problem cannot avoid this. The mathematics is correct; only the evidence is circular.

Smallest fix (guide only): "Have the child rebuild from the ribbon with the cards turned over. The answer 'no' should come from the forced filling: each remaining triangle has only one possible partner. It should not come from the card list."

## Checked and correct

- **K–1:** checks out completely. Areas: sailboat 11, cat 7, hexagon 6, diamond 8, arrow 8, star 12, long hexagon 10, mountain 9. The arrow has 1 purple tiling, the star 2. The diamond has no purple tiling but has 132 mixed tilings, so "two different ways" works. The hexagon has 52 mixed tilings, the long hexagon 3 blue-only tilings, the mountain 1 green-only tiling. All fit the stated kit (6 blues, 12 greens, 3 purples). Every guide example and drawing is a valid exact tiling.
- **Grades 2–3:** the mathematics checks out; only the label issue in item 3. Problem 1: A 9 cells (6 up/3 down, 3 blues, 3 gaps); B 12 (6/6, tiles); C 11 (6/5, 5 blues, 1 gap); D 10 (5/5, tiles). Problem 2: side 2–5 triangles give at most 1, 3, 6, 10 blues and at least 2, 3, 4, 5 gaps, so "you cannot leave fewer" is true. Problem 3: areas 12/8/8/10/9/8; most blues 6/4/4/5/4/3; most purples 3/1/2/2/2/1. On B, only 6 purple placements exist and none covers either sharp corner. Every witness drawing is valid.
- **Grades 4–5:** apart from item 1, every intended answer is right. The board has exactly 6 tilings, and cards A–F are all of them, distinct and correctly labelled. Ribbons: A RRLL, B RLRL, C LRRL, D RLLR, E LRLR, F LLRR, and each printed path matches. Flip edges: AB, BC, BD, CE, DE, EF. Degrees 1, 3, 2, 2, 3, 1 equal the number of adjacent RL/LR pairs, and each flip swaps exactly one such pair. The A–B highlighted patch is a unit hexagon containing exactly the three changed rhombi. Shortest A→F routes: ABCEF and ABDEF (4 flips). The map is bipartite, {A,C,D,F} | {B,E}. Closed walks from A of lengths 1–8: 0, 1, 0, 3, 0, 13, 0, 63, so there is no odd return.
- **Guide solutions, hints and extensions:** all correct. This covers both middle tables and their bounds arguments, the purple-versus-blue comparison, the edge list and graph, the colour and R-sum parity proofs, the "≥ 4 flips" argument, the one-ribbon and forced-remainder argument, and the adjacent-turn flip rule. Also correct: the materials totals (56 blues, 51 greens, 18 purples for 3/3/1); the bottleneck reserve (A and B neighbour only D, so at most 2 blues and 2 gaps); the side-2 hexagon (24 cells, 12 blues, 20 tilings); the four flip centres; the simple random walk (stationary (1,3,2,2,3,1)/12, mean return to A = 12); and the centre-choice chain (uniform, mean return 6, counting a stay as a return).
