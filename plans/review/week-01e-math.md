# Week 1 encore (Pattern blocks II): math check

Packet checked: the four delivered PDFs in `lowell-math-circle-year-2/week-01-encore/`: `week-01-encore-k-1.pdf` (F01E-K-v1, 7 pages), `week-01-encore-grades-2-3.pdf` (F01E-M-v1, 7 pages), `week-01-encore-grades-4-5.pdf` (F01E-U-v1, 10 pages) and `week-01-encore-facilitator.pdf` (F01E-FAC-v1, 8 pages). Sources: `lowell-math-circle-year-2/source/week-01-encore/`. Every quoted sentence below is also in the sources (`src/k-1.tex`, `src/grades-4-5.tex`, `guide-src/facilitator.tex`), so the PDFs match them. I took every board, piece and picture from the vector drawings in the delivered PDFs. I did not use the author's checkers or solvers (`guide-src/check.py`, `guide-src/lattice.py`, `src/verify.py`, `src/fewest.py`, `src/tri.py`, `src/cubes.py`).

## Method

Math check for the Week 1 encore review card, October 9, 2026. The scripts and their saved outputs (`<script>.out`) are in the run folder and go to `checks/week-01e/`. Each finds the repository four folders up from its own location (with a fallback for the run folder) and runs with `python3 <script>`. They need only Python 3 and `pdftotext`. I tested a copy at the committed location against the repository and got the same output. An earlier run of this stage wrote the first drafts of these scripts. I reread them, reran them and fixed them: the outputs are now named per script, PDF paths in outputs are relative, a stream/page count check is added, corner-snap distances are reported in inches, a meaningless C-ring line is replaced by a real mirror test, the Problem 9 centre-blue report is added and the 3,3,3 search is bounded. `check_cross.py` is new: it re-derives the main answers with separately written code.

- `pdfpaths.py`: a small standard-library PDF reader. It finds the page content streams, checks that there is one per page, and interprets the path, colour and transformation operators. It returns every painted path in inches, plus words with positions from `pdftotext -bbox`.
- `boards.py` → `boards.out`: snaps each closed outline to a triangular lattice. The unit and angle come from the outline's own grid lines, or from its sides when there is no grid. It lists the cells inside each outline and checks that the drawn grid lines are exactly the interior edges. The census covers every outline on every page.
- `lat.py`: lattice code. It has the pieces (found from cell adjacency), exact-cover counting and enumeration in reading order, a fewest-pieces dynamic program that also records colour mixes and the best result for each number of yellows, maximum packings, half-turn centres, and a Sprague–Grundy game solver. `fastgame.py` is a bitmask version of the game solver, memoised under the board's own symmetries.
- `common.py`: page helpers, reconstruction of drawn tilings from piece polygons, and a 3-D model of cube piles. The model generates every plane partition in an a×b×c box and projects the visible faces isometrically (x to the lower left, y to the lower right, z up). It then matches the projections against drawn or enumerated rhombus tilings.
- `check_k1.py`, `check_middle.py`, `check_upper.py` → `.out`: every problem in each band.
- `check_guide.py` → `check_guide.out`: every answer picture in the guide (pp. 3, 6, 7), the C and D positions, MacMahon numbers, the centre rule over many boards, up/down counts and the fewest-piece bounds.
- `check_extra.py` → `check_extra.out`: the 0, 1, 2 ring numbering behind the guide's 4–5 Problem 7 argument, and the game on the 1,3,3 hexagon.
- `check_cross.py` → `check_cross.out`: this script recomputes the main answers with code written separately from `lat.py` and `fastgame.py`. Pieces come from base shapes under the 12 lattice symmetries, including the purple chevron. Exact cover takes the cell with the fewest choices. The game uses plain win/lose search with no Grundy values and no symmetry. Yellow packings are found by brute force over hexagon centres. The 3,3,3 fewest-piece answer comes from the yellow argument alone. Two-down trapezoids are counted from each trapezoid's middle cell. Shades come from rhombus directions. Every value agrees with the other scripts.
- `big_games.py` → `big_games_4x4.out`, `big_games_hex333.out`: exhaustive game search on the two largest Problem 9 boards. The 4-by-4 board is a second-player win (17 s). On hexagon 3,3,3 (54 cells), the search hit its 600 s bound without finishing. That answer rests on the copying proof, whose one hypothesis (the half-turn centre is a lattice point) is verified.

## Located problems

### 1. K–1, page 1, Problem 1: "of the same colour" has two readings, and the X answers need one of them (low)

Text: "Fill each shape with small pieces **of the same colour**, with no gaps and no piece sticking out. Then do the same on the biggest green, blue, red and yellow pieces on your table. Write how many pieces you used, or draw an X if it can't be done."

The guide (p. 4, P1) reads it as "small pieces **of its own colour**". It expects triangle 4, rhombus 4, trapezoid 4, hexagon X on the printed shapes and 9, 9, 9, X on the 3× pieces. Page 1 of the guide also counts on the X: K–1 children "find a shape that cannot be filled and say why". The printed sentence also reads naturally as "use pieces that are all one colour". Under that reading nothing is impossible, and most shapes have several answers (`check_k1.out`, `check_cross.out` §1):

```
2x hexagon (yellow tint):   yellow none (at most 3 fit); green 24; blue 12; red 8
3x hexagon:                 yellow none (at most 7 fit); green 54; blue 27; red 18
2x rhombus: blue 4 or green 8      2x trapezoid: red 4 or green 12
3x triangle: green 9 or red 3      3x rhombus: blue 9, red 6 or green 18
```

A child who fills the yellow hexagon with eight reds has followed the printed words, gets no X, and may be told the answer is X. The adult reads the problem aloud, and the tints and the guide point to "its own colour", so the risk is small. Still, the page wording does not settle it.

Smallest fix: "Fill each shape with small pieces **of its own colour**, …". These are the guide's own words.

### 2. Grades 4–5, page 7, Problem 7: the count of "every way" depends on whether turned fillings are different (low)

Text: "Fill the hexagon from Problem 4 with small red trapezoids. **Find every way to do it**, draw each one, and explain how you know you have found them all." Guide p. 6: "9 fillings: 3 rings times 3 ways to cut the middle (all below)."

On the fixed board there are exactly 9 fillings; two separate enumerations agree (`check_upper.out`, `check_cross.out`). A sixth of a turn keeps each ring and moves the middle cut to the next one (`check_upper.out`). The two pinwheel rings are mirror images. So up to turning there are **3** fillings, and up to turning and flipping **2** (`check_upper.out`: "fillings up to rotation: 3; up to rotation and reflection: 2"). The page prints 12 blank copies, which says nothing about the convention. Elsewhere the copies do: K–1 Problem 7 prints exactly 3 + 2, and 2–3 Problem 4 exactly 2 triangle copies, matching their fixed-board counts. A child who says "three ways; the rest are these turned" has a correct, complete answer under a natural reading. The guide gives only 9.

Smallest fix (guide, p. 6, P7 answer): "9 counts turned and flipped copies as different. Up to turning there are 3, one per ring; up to turning and flipping, 2. Accept either if the child says which they count, and ask how many each one makes on the fixed board." Alternatively, add "Turned or flipped fillings count as different" to the problem.

### 3. Adult guide, page 8, §5 "Cubes": the general labelling gives the wrong light count for the guide's own 1,3,3 hexagon (low)

Text: "A blue filling of the hexagon *a, b, c* is the picture of a pile of unit cubes in an *a×b×c* box … **The light rhombi are the tops over the *ab* floor squares**, and the other shades are the faces seen against the two walls, *bc* and *ca* of them."

The guide names hexagons by consecutive sides: "the hexagon a, b, c, a, b, c" (§5, Copying), and "the 1,3,3 hexagon" for 4–5 page 6. As printed, that board has sides 1, 3, 3, 1, 3, 3 in order, with the length-1 sides vertical (`boards.out`). With *a, b, c* = 1, 3, 3 the sentence predicts *ab* = 3 light rhombi. The light rhombi of A and B are the ones whose two triangles share a vertical edge (`check_cross.out` §7: shade 0.84, direction 90°). On the 1,3,3 board every one of the 20 fillings has **9** such rhombi, with 3 and 3 of the other two kinds. The two sides meeting at the bottom corner are 3 and 3. The only box whose corner picture has this outline is 3×3×1 (`check_upper.out`: box `[(3, 3, 1)]`, face types `top 9, xwall 3, ywall 3` for all 20). The P6 answer ("9 light, 3 medium and 3 dark … the box is 3 by 3 by 1") and its explanation are right. Only the general sentence is mislabelled. An adult who used it to check P6 would expect 3.

Smallest fix: "The light rhombi are the tops over the floor squares: the product of the two sides that meet at the bottom corner of the picture (4 for 2,2,2; 9 for 1,3,3). The other two shades are the faces against the two walls."

### 4. Adult guide, page 1 overview and page 6 P9: the copying rule is stated without its centre condition (low)

Overview (p. 1): "On a board that looks the same after a half turn, one player can win every game by copying: **answer each move with the same move on the opposite side.**" P9 answer (p. 6): "Hexagon 3,3,3: 2nd. Hexagon 1,2,3: 1st. 4-by-4: 2nd. 5-by-2: 1st. **All by copying; the first player takes the centre blue first.**"

Every half-turn-symmetric board in the packet follows the rule in §5, and exhaustive search confirms every board where it finished:

- **Centre at a lattice point: second player wins by answering moves.** Hexagons 1,1,1, 2,2,2, 1,3,3 and 3,3,3 (3,3,3 by the proof only), and the 2-by-2, 4-by-2 and 4-by-4 boards (`check_k1.out`, `check_middle.out`, `check_upper.out`, `check_extra.out`, `big_games_4x4.out`).
- **Centre at an edge midpoint: first player wins by taking the one blue that is its own image, then copying.** The 3-by-1, 3-by-2, 3-by-3 and 5-by-2 boards and hexagons 1,1,2 and 1,2,3. On the 3-by-1, 3-by-2, 1,1,2 and 1,2,3 boards that blue is the only winning first move (1 of 5, 13, 11 and 27). On the 3-by-3 board it is one of 7 winning first moves, and on the 5-by-2 board one of 5.

The overview describes only the second player's reply. On an edge-centre board, a second player who just answers moves loses once the first player takes the centre blue. So the overview leaves out half of what 4–5 Problem 9 and 2–3 Problem 5 ask children to decide. Read literally, the P9 cell has the first player take a centre blue on all four boards. Two of them are second-player wins with no blue that is its own image. The correct statement is in §5 and in the P9 explanation on p. 7, so this is a wording repair.

Smallest fix: overview: "…one player can win every game by copying. If the centre of the half turn is a grid point, the second player answers each move with the move opposite it. If the centre is the middle of a grid edge, the first player takes the blue across that edge and then copies." P9: "Hexagon 3,3,3 and 4-by-4: 2nd, by copying. Hexagon 1,2,3 and 5-by-2: 1st: take the centre blue, then copy."

### 5. Adult guide, page 6, 4–5 P4: "no overhangs" does not single out the 20 piles (low)

Text: "20 fillings, one for each pile in a 2 by 2 by 2 box **with no overhangs**, listed below (0 to 8 cubes)."

A 2 by 2 by 2 box holds **81** overhang-free piles: each of the four stacks has 0, 1 or 2 cubes. Only **20** are pushed into the corner, with no stack taller than the stack behind it toward either wall (`check_cross.out` §8). These are the plane partitions; my 3-D model matches them one-to-one to the 20 fillings and to the guide's list (`check_upper.out`). For example, the pile 0001, a single cube in the front position, has no overhang but is not in the list. Seen from the front, it hides part of the floor squares beside it, so its picture is not a filling. §5 states the right condition ("pushed into the corner with no overhangs: a plane partition"), and the list on p. 7 is right. So this is a wording repair for the P4 cell, where an adult is most likely to look while a child builds.

Smallest fix: "20 fillings, one for each pile pushed into the corner of a 2 by 2 by 2 box (no stack taller than the one behind it), listed below (0 to 8 cubes)."

## Checked and correct

**Diagrams (all bands).** Every board, picture and recording copy is lattice-exact at one scale in both axes. The largest distance from a drawn corner or grid end to its lattice point is 0.0001 in on the student pages and 0.0014 in on the guide's small pictures (`boards.out`). So the triangles and hexagons are regular, and each board has exactly the side lengths named in the guide. Every gridded board's grid lines are exactly its interior edges. Every board children place blocks on is at actual size (small edge 1.0000 in): K–1 pages 1–7 (page 1's printed shapes are the 2× outlines, sides 2 in), the 2–3 main boards, and the 4–5 boards on pages 1–4, 6 and 10. The 4–5 Problem 9 boards are drawn at 0.3 in, as the problem intends. The 4–5 boards on pages 1, 2 and 10 are identical to 2–3 Problems 1, 5 and 6. Recording copies match their boards in shape and orientation. The 2–3 Problem 4 copies keep horizontal grid lines, so "up" and "down" mean the same as on the board. Mathematical and digital checks only: I did not test the fit of real Upscale pieces, snap cubes or the box.

**K–1** (apart from finding 1):
- P1: the 2× shapes take triangle 4 greens, rhombus 4 blues and trapezoid 4 reds, each in exactly one way. The hexagon has no yellow filling (at most 3 fit). The 3× pieces take 9, 9 and 9 (the 3× trapezoid in 49 ways), and the hexagon is X (at most 7 fit, in 2 placements).
- P2: hexagon 2nd; 2-by-2 2nd; strip 1st, and only by the centre blue (1 of 5).
- P3: triangle fewest 3 (three reds, 2 tilings; a yellow forces 4), most 9. Star fewest 6 (65 tilings), most 12. The guide's "every point of the star needs its own piece" holds: no allowed piece covers two points. A point touches only its own inner triangle, each inner triangle touches one point, and the only yellow that fits is the middle one.
- P4: 3-by-2: 1st, only by the centre (1 of 13). Triangle 3: 1st; every game lasts exactly 3 moves. 4-by-2: 2nd.
- P5: arrow, 4 reds in 3 ways and 6 blues in 1 way. Trapezoid, 5 reds (5 ways); blues X (9 up, 6 down). Hexagon 2,1,2: reds X (16 cells); 8 blues (6 ways).
- P6: boat fewest 5 (one tiling: 1 yellow, 3 reds, 1 green), most 16. 2× hexagon fewest 6 (2 tilings, 3 yellows and 3 blues; with 1 or 2 yellows the best is 7), most 24.
- P7: 3 red ways and 2 blue ways, matching the 3 + 2 recording hexagons.

**Grades 2–3: checks out completely.**
- P1: 2nd, 2nd, 1st (hexagon 1,1,2, centre only, 1 of 11), 1st (3-by-2, centre only, 1 of 13).
- P2: triangle 3, 1st (every first move wins; length always 3); triangle 4, 2nd (all 18 first moves lose; lengths 5 or 6); 4-by-2, 2nd.
- P3: 2× hexagon 6, always 3 yellows and 3 blues (2 tilings). Triangle 4, 5, always 1 yellow, 3 reds and 1 green (3 tilings; at most one yellow fits).
- P4: the triangle has exactly 2 red fillings, mirror images, each 3 two-up and 0 two-down. The hexagon has 9, each 4 and 4. Up and down were measured on the page, and the middle-cell count gives the same.
- P5: hexagon 2,2,2: second player (lattice-point centre). 3-by-3: first player, with the centre blue among its 7 winning first moves.
- P6: fewest 12, exactly 2 tilings (6 yellows and 6 reds), related by a sixth of a turn. Seven yellows fit in exactly 2 placements, leaving six 2-cell holes (13) or twelve single cells (19). With h ≤ 6 yellows at least 18 − h pieces are needed.
- P7: 220 red fillings, every one with exactly 3 two-down trapezoids.

**Grades 4–5** (apart from finding 2):
- P1–P3: as in 2–3.
- P4: 20 blue fillings, each the picture of exactly one pile in the 2×2×2 corner. By cube count: 1, 1, 3, 3, 4, 3, 3, 1, 1. A and B are valid fillings: the piles with 0 and 8 cubes, matching the printed "cubes: 0" and "cubes: 8". The shading follows face direction consistently: tops 0.84, faces parallel to one wall 0.60, to the other 0.34.
- P5: fewest flips A→B is 8. The flip graph (20 fillings, 32 flips) is connected and bipartite, and every flip changes the cube count by exactly 1.
- P6: 20 fillings; the box matching the printed outline is 3×3×1; every filling has 9 light, 3 and 3; empty to full takes 9 flips.
- P8: C and D are valid red fillings with the same middle and different rings; C's ring is a pinwheel and D's is mirror-symmetric (the frame). With moves of at most 2 or at most 5 trapezoids, the 9 fillings fall into three classes of 3, one per ring, so C cannot reach D. With 6, all 9 connect. Re-cutting the middle gives a round trip of 3 two-trapezoid moves.
- P9: hexagon 3,3,3: 2nd (copying; lattice-point centre). Hexagon 1,2,3: 1st, centre blue only (1 of 27). 4-by-4: 2nd (search). 5-by-2: 1st; the centre blue is one of 5 winning first moves.
- P10: as 2–3 P6.

**Adult guide** (apart from findings 3–5):
- Every answer picture on pp. 3, 6 and 7 is a valid filling of the printed student shape, with the labelled count and correct piece colours. Where several are drawn they are all different, and each is optimal where it claims to be. Each winning-move picture shows the centre blue, and it wins.
- The 9-filling grid on p. 7 has one ring per row and one middle per column. Row 2 is the mirror-symmetric frame; rows 1 and 3 are mirror-image pinwheels. Student C is at row 3, column 3 and D at row 2, column 3, as stated. The pile list on p. 7 equals the model's 20 plane partitions in the stated back/left/right/front order.
- The explanations hold:
  - the 2× hexagon bound: every possible yellow covers 2 or 6 of the six middle triangles;
  - the triangle 6 count: 21 up, 15 down, so 9 and 3;
  - copying, including that a move and its image never overlap;
  - the cube and flip arguments;
  - the ring argument: the 18 ring cells form one loop, and the cells touching the middle are every third, so the 0, 1, 2 numbering is consistent. Ring trapezoids cover one of each number, and reaching trapezoids cover ring numbers {2}, {0,2} or {1,2} only;
  - "C to D: no": different rings share no trapezoid.
- §5 facts hold:
  - the centre rule: no counterexample over a-by-b boards with a, b ≤ 5 and hexagons with a, b, c ≤ 4; it also follows from the centre ((a − c)e₁ + (b + c)e₂)/2;
  - U and D for triangles; ab, bc and ca rhombi of the three directions in each hexagon filling;
  - the MacMahon numbers 20, 20 and 6 (and 4 flips for 1,2,2);
  - the bound h + ⌈(N − 6h)/3⌉ and the 3× hexagon argument.
- The 1,3,3 hexagon game ("when attention runs out") is a second-player win: lattice-point centre, and search over 38 first moves.
- "Take the purple … pieces off": purple chevrons do change a fewest answer. The K–1 star drops from 6 to 3 (`check_cross.out` §4).
- Materials note, not a mathematical error: the 4–5 blue count "40 (15 per filling of the Problem 6 hexagon, two fillings side by side, plus a game)" covers two fillings (30) plus a game on any board except a long game on the 2,2,2 or 1,3,3 hexagon, which can last 12 or 15 moves (`check_cross.out` §9).
