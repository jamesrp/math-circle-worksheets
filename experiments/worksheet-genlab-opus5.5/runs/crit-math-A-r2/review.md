# Mathematical review: Week 1 Tiling packets (base/)

Method: I parsed every TikZ figure in `src/figs/` back into lattice cells, pieces and shaded holes, using my own code (`scratch/geo.py`, `scratch/solve.py`, `scratch/flip.py`, `scratch/offgrid.py`) rather than the author's `tri.py`. I then enumerated tilings, maximum packings, flip graphs, chains and game positions from those coordinates. Rebuilding the sources reproduces `base/*.pdf` pixel for pixel at 50 dpi, so the parsed figures are the printed ones. Every board meant to carry physical blocks measures at actual size (1 inch per small edge) on the rendered pages.

## Problems found

### 1. K–1, page 6, Problem 6: the hexagon game has the opposite answer under the page's own rule (serious)

Text: "In every problem, blocks must stay inside the shape and must not overlap." / "Take turns with a partner putting one green block or one blue block on the shape; whoever puts down the last block wins. For each shape, would you rather go first or second?" Diagrams: hexagon (6 triangles), parallelogram strip (6), trapezoid strip (5).

Intended answers, with blocks placed on the grid triangles: hexagon **second**, 6-strip **first**, 5-strip **first**. My game search over grid placements confirms this. The hexagon is Kayles on a 6-cycle, so the second player wins.

The K–1 packet never says that blocks go along the lines. The 2–3 packet does say so, and the K–1 packet does not. Under the printed rule, the first player wins the hexagon in one move:
- Lay a blue block across the centre of the hexagon, so its long diagonal runs from the midpoint of the bottom edge (0.5, 0) to the midpoint of the top edge (0.5, 1.732), with its other corners at (0, 0.866) and (1, 0.866).
- That is a genuine 1-inch, 60° rhombus, and it lies inside the hexagon.
- What is left is two thin bent strips, each 0.43 in thick. A search over 1.6 million positions and angles finds no green triangle that fits in either strip, so no further block can be placed.
- Even if a block did fit, the rhombus is centred on the hexagon's centre, so the first player could copy each opponent move by a half-turn and still win.

A kindergartner putting a blue block "standing up in the middle" is a very likely first move. The two strips stay first-player wins in the free-placement game too, by mirror play after a centred first move. So only the hexagon flips, and it is the one contrasting case.

**Fix:** add "along the lines" to the K–1 packet rule: "In every problem, blocks go on the lines of the shape, stay inside it, and must not overlap." This matches the 2–3 packet rule. The covering problems (P1–P5) need no change, because exact coverings of these lattice regions are forced onto the grid.

### 2. Grades 4–5, page 1, Problem 1 (with Problem 2): "find every way" next to eight lettered slots, and "different" is undefined (minor)

Text: "Find every different way to do it, and draw each way in one of the small copies below." Below the text are eight copies, pre-labelled **A–H**. Problem 2 then says "write the letters of your coverings from Problem 1".

The board (hexagon with sides 2, 2, 1) has exactly **6** blue coverings. The eight printed letters suggest 8, and G and H would stay empty. The board also has 4 symmetries (half-turn and two reflections). Counting turned or flipped copies as the same gives **3** coverings. A child who counts that way gets 3 vertices in Problem 2 instead of the intended graph: 6 coverings and 6 moves, a 4-cycle with two pendant coverings.

**Fix:** remove the pre-printed letters, so children letter the coverings they find. Then add one sentence to Problem 1: "Coverings count as different when the blocks sit in different places on this board."

### 3. K–1, page 4, Problem 4: copy counts imply more ways than exist (minor)

Text: "Find every way to cover the hexagon with blue blocks, and every way to cover the long shape. Draw each way in a different copy." The page shows 3 hexagon copies and 4 long-shape copies.

True counts: hexagon **2**, long shape (sides 2, 1, 1) **3**. Pre-readers treat "fill every box" as the task, so the extra copy invites a repeated drawing. The same "turned copy" issue applies here: the hexagon's two coverings are 60° turns of each other, and the long shape has 2 coverings up to symmetry.

**Fix:** keep the copies and add a short sentence such as "Some copies may stay empty." If the organizer prefers fixed counts on the board, use 2 hexagon copies and 3 long-shape copies instead.

### 4. Grades 4–5, page 4, Problem 4: not enough recording copies for a full answer (minor)

Text: "Can this be done in exactly 4 moves? In 5? In 6? In 7? For each number, draw the coverings you pass through, or explain why it cannot be done." The page gives 8 copies.

Answers: 4 **yes**, 5 **no**, 6 **yes**, 7 **no**. The flip graph has 20 coverings and 32 moves, and it is bipartite, because each move changes the cube count by one. There are 120 closed 4-move walks with no immediate undo and 756 such 6-move walks, including simple 6-cycles. Drawing both round trips takes 4 + 6 = 10 coverings, which is more than the 8 copies printed.

**Fix:** add "If you run out of copies, you can draw more on the back." (as in Problem 9), or print 10 copies.

## Problems checked with no error found

**K–1:**
- P1: hexagon yes, small triangle no (3 up / 1 down), chevron yes, boat no (4/2), 2×2 rhombus yes, trapezoid no (7/5). All areas are even, so parity alone never decides a board.
- P2: fewest greens 2, 3, 4.
- P3: fewest greens 5.
- P5: pair 1 takes 2 moves (two shortest routes). Pair 2 takes 4 moves, and its start has exactly one available move. The move picture shows the two fillings of a hexagon.

**Grades 2–3:** this band checks out completely.
- P1: A yes (1 way), B no (5/3), C yes (3 ways), D no (6/4), E no (7/5), F yes (1 way).
- P2: fewest greens 2, 3, 4, 5.
- P3: A yes, B no (two up-holes), C no (two down-holes), D yes. Every one-up/one-down hole pair in this hexagon is coverable, 144 of 144.
- P4: 10 up and 6 down triangles, so at least 4 greens.
- P5: 10 and 100 greens, and both are attainable.
- P6: blue row 2, 3, 4, 5; purple row 4, 5, 4, 5. Answer: no.
- P7: possible. For example, take triangle B (side 3) and add one down triangle and two up triangles along its lower right. That gives 12 connected triangles, 8 up and 4 down, so at least 4 greens. There are 3 such shapes inside triangle C.

**Grades 4–5:**
- P2: graph has 6 vertices and 6 edges.
- P3: pair 1 takes 8 moves, and fewer is impossible because each move swaps one adjacent pair in one chain, and each chain LLRR→RRLL needs 4 swaps. Pair 2 takes 4 moves.
- P5: the shaded example is the left chain and reads RLLR, matching the L/R pictures. The answers are A (LLRR, RRLL), B (LRLR, RLRL), C (LRRL, LRRL) and D (RRLL, RRLL).
- P6: LRLR/RRLL is possible, RRLL/LLRR is impossible, RLRL/RLRL is possible, and LRRL/LRLR is impossible because the chains would cross.
- P7: every move changes exactly one chain, by swapping one adjacent LR or RL pair. I checked every move on all three boards.
- P8: 20 coverings, one chain of 3 L and 3 R, C(6,3).
- P9: 20 coverings.
