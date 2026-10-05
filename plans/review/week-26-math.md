# Week 26 (same area, different boundaries): math check

Scope: everything current in `lowell-math-circle-year-2/week-26/`, archive folders excluded:

- `week-26-k-1.pdf` (W26-K-v2, 6 pp., P1–P6)
- `week-26-grades-2-3.pdf` (W26-23-v2, 6 pp., P1–P6)
- `week-26-grades-4-5.pdf` (W26-45-v2, 6 pp., P1–P6)
- `week-26-facilitator.pdf` (20 PDF pages: an unnumbered overview, printed pp. 1–18, and an appended route note numbered 20). Guide page numbers below are the printed ones.
- The bonus companion `week-26-bonus.pdf` (W26-BON-v1, 4 pp., P1–P6) and its guide `week-26-bonus-facilitator.pdf` (W26-BON-FAC-v1, 5 pp.).

Sources read: `source/week-26/editable/src/build_packets.py` (tile and grid coordinates), `facilitator-src/build_guide.py` (figure layout only), and `source/week-26-bonus/student-src/bonus.tex`. The delivered PDFs are byte-identical to the reference copies in both source folders. I did not use the packet's answer files (`math-checks.json`, `checks.json`), its checkers or its review notes. Checked October 5, 2026.

**Result: no mathematical errors in any student band, including the bonus. The bonus guide checks out completely. The base guide has two located problems: its "yes" answer to Grades 4–5 Problem 2's "Can it have a hole?" holds only if a corner contact seals a hole, and the student page does not say so; and a K–1 extension answer is incomplete. Every figure, caption, count and worked number in both guides is correct.**

## How it was checked

My scripts and their saved outputs are in [checks/week-26/](checks/week-26/). Each script finds the repository from its own location. Run `extract.py` first; the check scripts run it themselves if `extracted.json` is missing.

- `common.py`: my own polyomino tools. Exposed edges are counted side by side, not from a formula. It also has shared sides, connectivity, row and column runs, free (turn/flip) canonical forms and outward/inward/pinch vertex counts. Holes are counted two ways: empty cells joined only through sides (a diagonal tile contact seals) and empty cells also joined through corners (a corner gap leaks). Fixed polyominoes are enumerated by Redelmeier's method; the counts 1, 2, 6, 19, 63, 216, 760, 2725, 9910, 36446, 135268, 505861 for n = 1–12 match the known sequence.
- `extract.py` → `extracted.json`, `extract.out`: reads every printed tile shape, every working grid (columns, rows, cell width and height) and every problem heading from the vector drawings of the student PDFs. From the guide it reads all 82 answer figures with the caption drawn right after each one, and records the green "+" cells.
- `check_students.py` → `check_students.out`: a census of all 691,277 fixed polyominoes with up to 12 tiles, then every student problem. Larger cases use exhaustive bounding-box searches. These rest on the lemma P ≥ 2(rows + columns), which the census confirms for every shape up to 12 tiles. The 4×5-span question was searched over all 2^20 subsets of the box.
- `check_guide.py` → `check_guide.out`: checks every guide figure against the numbers in its caption: P, e, n, row lengths, rows and columns, before/after values and changes. It also checks the guide's general claims, worked numbers, move counts and cross-references.
- `check_bonus.py` → `check_bonus.out`: P1–P2 over all 65,536 two-colourings of the 4×4 square; P3 from the shapes, circles and crossed pattern read from the PDF; P4–P6 by counting the exposed faces of actual unit cubes.

**Results common to every band.** Every working grid and printed tile in the three bands is square: 9.5, 11, 10, 7.5, 8, 6.5, 6.2, 5.5, 7, 9 and 6 mm. Each grid is large enough for the intended answers. The longest rows fit (6 in 7 columns, 8 in 8, 12 in 14), and so do the 6×6+1, 7×7+1 and 8×9+1 drawings in the 11×10 grids. Problems are numbered 1–6, one per page, in every band. For every n ≤ 12, the possible boundaries are every even number from 2⌈2√n⌉ to 2n + 2. P = 4n − 2e holds on every shape.

## K–1: checks out completely

- **P1:** there are exactly five tetrominoes up to turns and flips. The square has boundary 8 and the other four have 10, so six grids leave one spare.
- **P2–P3:** with 5, 6, 7 and 8 tiles, the shortest boundaries are 10, 10, 12 and 12, and the longest are 12, 14, 16 and 18.
- **P4:** with six tiles, P = 10 has 1 shape (2×3), P = 12 has 7 and P = 14 has 27. So exactly 12 and 14 can be made two different ways.
- **P5:** five tiles give only 10 or 12, so 8, 9, 11 and 13 are impossible.
- **P6:** the three starts read from the page (a row of 6; 4 + two below; 4 + two down) all have P = 14. Over every legal one-tile move, the best results are 14, 10 and 12, so only the middle and bottom starts can be shortened. The result grids (8×5) hold the answers.

## Grades 2–3: checks out completely

- **P1:** with eight tiles the shortest boundary is 12 and the longest is 18. Exactly 2 shapes reach 12 (the 2×4 and the 3×3 minus a corner); 255 reach 18.
- **P2:** the four starts on the page have these complete change sets:
  - row (before 12): {+2};
  - stair (before 12): {0, +2};
  - U (before 12): {−2, +2};
  - frame (before 16): {−4, +2}.
  There are at most two changes per start, and two recording grids are printed for each.
- **P3:** ten tiles allow e = 9 to 13 (P from 22 down to 14). Nothing outside that range is possible, and P = 4n − 2e.
- **P4:** the longest boundaries are 10, 16, 22 and 26.
- **P5:** in reading order the shapes have P = 18, 18, 12 and 16, so the row and the branch are the maximal ones. 64 free 8-tile shapes have P = 18 and no straight run of four, and all fit the 10×5 grids.
- **P6:** exhaustive over every start of up to 7 tiles, the fewest starting tiles are 1, 3, 5 and 7 for +2, 0, −2 and −4. No legal start of 6 or fewer tiles surrounds an empty cell on all four sides.

## Grades 4–5: checks out completely, apart from the hole reading in P2 (problem 1 below)

- **P1:** the shortest boundaries are 12, 14 and 16 for 7, 10 and 13 tiles. 4, 6 and 11 different shapes reach them, so "two different shapes" is always possible, and all fit the 7×5 grids.
- **P2:**
  - The maximum is 26; every 12-tile tree reaches it, and no tree contains a 2×2 block (census).
  - Holes depend on the convention. A maximal shape has a hole only if a diagonal tile contact seals it (see problem 1 below).
- **P3:**
  - The three given shapes have (rows, columns, boundary) = (2, 6, 16), (3, 4, 14) and (4, 5, 18).
  - Over every connected shape spanning exactly 4 rows and 5 columns, the least boundary is 18. Twelve-tile shapes with that span reach 18, 20, 22, 24 and 26.
- **P4:** the greatest areas are 9, 12, 16 and 20 for boundaries 12, 14, 16 and 18. Each is reached by a rectangle with exactly that boundary. One more tile needs at least the next even boundary (box search).
- **P5:** the least boundaries are 14, 16, 18, 18 and 20 for 12, 13, 17, 20 and 21 tiles (box search).
- **P6:** the greatest area for even P ≥ 4 is ⌊s/2⌋·⌈s/2⌉ with s = P/2, which equals ⌊P²/16⌋. This was checked for P ≤ 80. The least boundaries for 37, 50 and 73 squares are 26, 30 and 36.

## Bonus companion: checks out completely

- **P1:** among balanced splits with both rooms side-connected, the least shared fence is 4. Exactly 4 labelled colourings reach it: the horizontal or vertical half cut, with either colour on either side. Each room then has boundary 12. Even without the connectedness rule, a balanced split needs a fence of 4.
- **P2:** P_R + P_B = 16 + 2L holds for every split of the square, whatever the room sizes and whether or not the rooms are connected.
- **P3:**
  - The labelled shapes are: 1 = 3×2 rectangle (C, R, H) = (4, 0, 0); 2 = five-square L (5, 1, 0); 3 = 3×3 ring (4, 4, 1); 4 = 5×3 with two separated holes (4, 8, 2), which uses 13 tiles.
  - The "Outward corner" circle sits on a vertex touching one tile, the "Inward corner" circle on a vertex touching three, and the crossed-out pattern is two diagonal tiles.
  - C − R = 4(1 − H) holds on all 48,416 pinch-free fixed polyominoes with up to 10 tiles. With a pinch it can fail: the 3×3 frame missing a corner, with a tail, has C = 6, R = 4 and H = 1.
- **P4:** the row of eight has 34 exposed faces, the 2×4 one layer 28 and the 2×2 two layers 24; all three use 8 cubes. The drawn footprints read from the PDF are 8×1, 4×2 and 2×2, with square cells. The opening example (two squares, two layers) has 4 cubes.
- **P5:** S = 2m + kP holds for 11,384 equal-height buildings. These are every footprint of up to 8 tiles at k = 1–3, plus the ring and the two-hole footprint at k = 1–4. Hole walls are included.
- **P6:** of the 24 arrangements, 16 give 34 faces and 8 give 36, so the fewest is 34 and the most is 36.

## Base adult guide

The overview's facts are correct, with one hypothesis left implicit: the hole claims, problem 1 below.

- **Shared sides:** P = 4n − 2e, and P is even.
- **Adding a tile:** adding a tile with k neighbours changes P by 4 − 2k.
- **Maximum:** P ≤ 2n + 2, with equality exactly for trees, and no 2×2 block at the maximum.
- **Row and column bound:** P ≥ 2(r + c) with n ≤ rc. Equality holds exactly when every row and column is a single run, which the census confirms on all fixed shapes up to 12 tiles.
- **Area for a given boundary:** the greatest area for P = 2s is ⌊s/2⌋⌈s/2⌉.
- **Least boundary:** 2⌈2√n⌉. This matches the census for n ≤ 12 and the box bound for n ≤ 200.

The p. 3 construction (a k×k square, then a corner-started strip, then k×(k+1), then a strip) attains the bound for every n ≤ 200. The p. 18 interval statement (4k; 4k + 2; 4k + 4) is right.

All 82 figures match their captions. In detail:

- **K–1 P1:** the five tetrominoes are distinct, with shared sides 3, 4, 3, 3 and 3.
- **K–1 P2–3:** the pictured extremes equal the true minima and maxima, and the seven-tile minimum is a 2×4 minus a corner.
- **K–1 P4:** the 12-side pair have 4×2 and 3×3 boxes.
- **K–1 P6:** the starts match the student page. Each pictured result is one legal move away and optimal. The optimal (source, destination) move counts are exactly 22, 1 and 2, as the guide says. Every 2×3 or 3×2 box holds at most 4 of the bottom L's tiles.
- **Grades 2–3 P1:** a 3×3 square minus a corner, an edge cell or the centre has P = 12, 14 or 16.
- **Grades 2–3 P2:**
  - The change sets are as listed.
  - A tile beyond the left end of each top row gives 14, 14, 14 and 18.
  - The U has no two-neighbour position.
- **Grades 2–3 P3:** the row sums 7 + 1 + 2 = 10, 6 + 2 + 3 = 11, 5 + 3 + 4 = 12 and 4 + 4 + 5 = 13 are right.
- **Grades 2–3 P5:** the given shapes match the page in reading order, with e = 7, 7, 10 and 8. The two new shapes have 8 tiles, e = 7, longest runs 2 and 3, and boxes 5×4 and 3×4.
- **Grades 2–3 P6:** the start perimeters are 4, 8, 12 and 16, becoming 6, 8, 10 and 12. The −4 start is the 3×3 frame missing its centre and one corner. The chessboard argument's conclusion is confirmed exhaustively.
- **Grades 4–5 P1:** the pairs are genuinely different. The 13-tile pair have least tile degrees 1 and 2.
- **Grades 4–5 P2:** the three twelve-tile trees reach P = 26. In the third, the centre has four side neighbours and the upper-left corner is empty; the hole has 4 inner edges and the outer boundary 22.
- **Grades 4–5 P3:** the second construction is the first with its bottom-row right tile moved to the far right of row 2, and it has P = 20.
- **Grades 4–5 P4–6:** every row and column in the P5 constructions is a single run. The 6×6+1, 7×7+1 and 9×8+1 drawings each add one tile touching one side.

The cross-references ("page 3", "page 5", "page 6", "page 14") point to the right printed pages.

## Bonus adult guide: checks out completely

- **P1:** the four labelled optima and the lower-bound case split are right. The bound holds even without connectedness, which is what the argument uses.
- **P2:** the identity, including the fixed-region version P_R + P_B = P_region + 2L, is right.
- **P3:** the (C, R, H) list, the turning argument and the stated need for the no-pinch rule are right.
- **P4:** the counts 34, 28 and 24 are right.
- **P5:** S = 2m + kP and the cube count mk are right.
- **P6:**
  - The surface is 28 + the variation around the four-cycle.
  - The minimum variation is 6 and the cycles (1,2,3,4), (1,2,4,3) and (1,3,2,4) vary by 6, 6 and 8.
  - The examples 1 2 / 3 4 = 34 and 1 3 / 4 2 = 36 are right, and so is "sixteen give 34 and eight give 36".
- **Terrain rule:** checked on 400 random positive terrains.
- **Materials:** "thirteen tiles" for the two-hole shape is right.

## Located problems

### 1. Grades 4–5 p. 2, Problem 2, and base guide p. 14 (also overview, p. 3, p. 18): "Can it have a hole?" has two readings, and the guide accepts only one (moderate)

- **Student text:** "What is the longest possible boundary of a twelve-tile shape? … Can such a shape contain a 2-by-2 block? Can it have a hole?" The page's opening rules say only "Count every side with no tile beside it, including sides around holes." They never say whether a gap closed off only by two tiles touching at a corner is a hole.
- **Guide text (p. 14):**
  - The heading is "A 2-by-2 block: no. A hole: yes."
  - The guide then says: "At the point where those two empty cells meet diagonally, two occupied tiles meet at a corner and close the passage. … Hence 'tree adjacency implies no holes' is false under these worksheet rules. … Do not silently impose a different hole convention."
  - The overview repeats "corner contacts can seal a hole without adding a shared side", and p. 3 calls "no holes" a "false … rule". The hint steers toward that one example: "Try leaving a corner out of a ring."
- **Evidence:** in the census, 22,656 of the fixed 12-tile trees enclose a cell if a corner contact seals it. None of the trees up to 12 tiles encloses a cell if a corner gap lets the inside out. The guide's own example is like this: holes = 1 with side-only empty connections, 0 with corner connections.
  - **General argument:** a hole sealed by full sides is surrounded by a closed ring of side-joined tiles. That ring is a cycle, so e ≥ n.
  - **The student rules point the other way:** they say tiles join only "along whole sides". A child who reasons that a corner does not join tiles, so it does not seal a space either, answers "no" with a correct proof. As written, the guide tells the adult that this answer is wrong.
  - **The bonus companion uses the opposite convention:** its p. 2 rule, "forbid the two-diagonal-tile pattern shown crossed out, even if those tiles connect elsewhere", excludes exactly the configuration that makes the base guide's "yes" work.
  - **Hole edges are unaffected:** the sides around the enclosed cell count under either reading, since they have no tile beside them. Only the yes/no answer depends on the convention.
- **Smallest fix (guide only):**
  - On p. 14, replace the heading with "A 2-by-2 block: no. A hole: it depends on corners." After "Do not silently impose a different hole convention", add: "If a child says no because a corner gap lets the inside out, accept it: a hole sealed by full sides needs a closed ring of side-joined tiles, which is a cycle, so it cannot occur when there are exactly n − 1 shared sides. Then show the corner-sealed example and ask whether its centre should count as a hole."
  - Change "under these worksheet rules" to "if two tiles meeting at a corner close a gap".
  - Make the same qualification in the overview ("a hole closed only at a corner contact") and on p. 3 and p. 18.
- **Alternative:** state the convention in the student question ("Count a gap as a hole even if it is closed only where two tiles touch at a corner"). That would mean changing the student page.

### 2. Base guide p. 4, K–1 Problem 1, "A useful stopping point": the extension answer omits two shapes (minor)

- **Quoted text:** "For an extension, ask which shape can gain a fifth tile without increasing its boundary; the square cannot, while L can fill its missing corner."
- **Evidence:** a fifth tile leaves the boundary unchanged exactly when it touches two old tiles. The T can do this (a tile beside its stem gives the P-pentomino), and so can the zigzag (either notch). The straight cannot, and neither can the square. So the answer is L, T and zigzag. `check_guide.py` computes the possible changes for all five pictured tetrominoes. An adult reading only this sentence may doubt a child who offers the T or the zigzag.
- **Smallest fix:** "…the square and the straight cannot; the L, T and zigzag can, by filling a notch where the new tile touches two old tiles."

## Observations that are not errors

- **Page numbering:** the appended route-note page of the base guide is numbered 20, following printed page 18. This is layout only, and nothing refers to it.
- **Two-diagonal contacts:** the base packet's legal shapes may contain two tiles touching only at a corner inside a connected shape, and the bonus forbids that pattern for its corner investigation. Each is stated where it applies. Problem 1 is the one place where the difference changes an answer.
- **Unique minimum shapes:** Grades 4–5 P5 does not ask for two shapes, and for 12 and 20 tiles the minimum is reached only by the rectangle (3×4, 4×5). A child looking for a second shape there will not find one. The page does not ask for one.
