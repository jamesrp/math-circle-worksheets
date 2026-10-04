# Correctness review: Week 1 tiling packets (B4-A-r1 base draft)

## Method

I rendered all 20 pages (K–1: 6, grades 2–3: 7, grades 4–5: 7) and looked at each one. I rebuilt every board from the printed TikZ figure files (`src/figs/*.tex`). I parsed the drawn segments, holes and filled tiles back into triangular-lattice coordinates, so every check below is on what actually prints and not on `gen.py`'s region definitions. I then re-checked everything with my own solvers (scripts in `scratch/geo.py`, `k1.py`, `g23.py`, `chev.py`, `p7.py`, `g45.py`, `p4.py`, `rib.py`):

- exhaustive blue-rhombus tiling enumeration
- bipartite up/down matching
- exact minimum-cover search, with pieces classified from geometry: chevron = 4 edge-connected triangles sharing a vertex, hexagon = 6 around a vertex, trapezoid = any 3-triangle chain
- memoized normal-play game search
- flip graphs with BFS distances
- enumeration of closed flip walks
- ribbon reading

Every board that children put physical blocks on prints at 1 inch per triangle edge (80 px per edge at 80 dpi, on a Letter page at 612×792 pt with no scaling).

---

## Located problems

### 1. Grades 4–5, page 4, Problem 4: the task cannot be done from two of the six pictured coverings, including the one left on the board after Problem 3

**Text:** "Start with any covering of the hexagon board from Problem 3. Make flips, one at a time, until you are back at the covering you started with. Find a way to do this with 4 flips that never flips the same hexagon twice in a row."

**Evidence:** I built the flip graph of the side-2 hexagon. It has 20 coverings and is bipartite. Then I listed every closed walk of length 4 from each covering, keeping only walks where two flips in a row never use the same hexagon.

- 18 coverings have such a walk.
- Coverings **E** (ribbons RRLL, RRLL) and **F** (ribbons LLRR, LLRR) have **none**.

Each of E and F has exactly one flippable hexagon, the central one. So the first and last flips must both use it, and flips 2 and 3 are forced to be the same hexagon done and undone (a hexagon flipped twice in a row).

The shortest allowed round trip from E or F takes 6 flips. A child who goes on from Problem 3 has covering F on the board, which is a natural reading of "any covering … from Problem 3". That child gets a task that cannot be done, and the page does not say so. Covering A has 3 flippable hexagons and 6 valid 4-flip round trips.

**Smallest fix:** change the first sentence to "Start with covering A from Problem 3." Another option is "Start with covering A, B, C or D from Problem 3." Coverings B, C and D also have valid 4-flip round trips (8, 2 and 2 of them).

### 2. K–1, page 3, Problem 3, and page 6, Problem 6 (minor): there are more blank shapes than ways, and the count depends on whether turned pictures count as new

**Text:** "Find all the ways to cover each shape with blue blocks. Put each way on a shape of its own." The page prints 3 hexagons and 4 long hexagons. Problem 6 ("Find all the ways … Draw each way on a small shape.") prints 8 small shapes.

**Evidence:**
- Exhaustive enumeration gives exactly **2** coverings of the hexagon, **3** of the long hexagon (top and bottom sides 2, slanted sides 1), and **6** of the Problem 6 shape.
- Children who cannot read take the number of blank shapes as the target. On the hexagon they will look for a third way that does not exist, or draw a repeat to fill the last shape.
- The two hexagon coverings are the same picture turned 60°. Two of the three long-hexagon coverings are mirror images. A child who counts "the same, just turned" as one way gets 1 and 2, and the page does not say which count is meant.

The mathematics is right, but the page suggests a different count than the true one.

**Smallest fix (pick one):**
- Add one sentence to each problem: "Some shapes may stay empty."
- Print exactly 2 hexagons and 3 long hexagons in Problem 3.

The adult at the table should know that turned copies count as different ways on the printed shape.

### 3. Grades 4–5, page 5, Problem 6 (minor wording): the second sentence assumes the child's Problem 3 answer is the true minimum

**Text:** "Then explain why nobody can change covering E into covering F in Problem 3 with fewer flips than your answer."

**Evidence:** The true minimum from E to F is 8 flips. This is the BFS distance, and it is also the ribbon lower bound: each ribbon must go from RRLL to LLRR, which takes 4 adjacent swaps, and each flip makes exactly one adjacent swap in one ribbon. A child who wrote 10 in the Problem 3 box is asked to explain something false.

**Smallest fix:** "Then find the fewest flips that change covering E into covering F, and explain why nobody can do it with fewer." This keeps the answer hidden and makes the claim true for every child.

The same presupposition is in grades 2–3 Problem 3: "explain why nobody can cover the biggest triangle with fewer green triangles than you used". It is harmless there, because a child who used more than 5 finds out when the explanation fails. You can leave it.

---

## Band-by-band verification (everything not listed above checks out)

### K–1: correct apart from note 2

| Problem | Intended answer | Verified |
|---|---|---|
| P1: cover with blues or X | hexagon yes; triangle of side 2 no (3 up, 1 down); side-2 rhombus yes (1 way); trapezoid no (3 triangles); chevron yes (1 way); 8-triangle trapezoid no (5 up, 3 down, so even area but impossible) | yes |
| P2: fewest greens on triangles of side 2, 3, 4 | 2, 3, 4 | yes (minimum cover) |
| P3: all ways | hexagon 2, long hexagon 3 | yes |
| P4: fewest blocks (G, B, R, Y, P) | side-3 triangle 3 (three trapezoids; hexagon + 3 greens = 4; no 2-piece cover); side-2 rhombus 3 (two chevrons cannot fit, since only the centre vertex has 4 triangles around it); double trapezoid 4 (7 up, 5 down rules out three chevrons; hexagon leaves an isolated corner) | yes |
| P5: blue-block game, last move wins | strip 4: first (cover the middle pair); strip 5: second; strip 6: first (cover the middle pair); strip 7: first; hexagon: second | yes (full game search; matches Dawson's Kayles values 2, 0, 3, 1 and the 6-cycle) |
| P6: all ways on the (1,2,2) hexagon | 6 | yes |

### Grades 2–3: checks out completely

| Problem | Intended answer | Verified |
|---|---|---|
| P1 | A star: yes (12 triangles, 6/6, exactly 1 covering); B side-3 triangle: no (6 up, 3 down); C double trapezoid: no (7 up, 5 down); D long hexagon: yes (3 coverings) | yes |
| P2 | E (holes are two up-triangles): no (10 up, 12 down); F hourglass: no (balanced 4/4, but its halves touch only at a point and each is a side-2 triangle with an imbalance of 2); G (one up hole, one down hole): yes (4 coverings) | yes; hole orientations in the drawings match |
| P3 | sides 2, 3, 4, 5 need 2, 3, 4, 5 greens; lower bound is the number of up-triangles minus down-triangles | yes (matching and exact search) |
| P4 | 10 and 100 (leave one up-triangle per row) | yes |
| P5 table | blues: 2, 3, 4, 5; chevrons: 4, 5, 4, 5 (most chevrons that fit: 0, 1, 3, 5); chevrons never do better, because each splits into two blues | yes (brute force over all chevron placements) |
| P6 | possible, e.g. a 13-triangle row strip with 6 up-triangles above it and 1 more triangle: 20 triangles, 13 up, 7 down, edge-connected, fits on the 7-inch actual-size grid | yes |
| P7 | rule: works exactly when one green points up and one points down | yes, all 144 up/down pairs give a coverable board and none of the 132 same-direction pairs do |

### Grades 4–5: correct apart from notes 1 and 3

| Problem | Intended answer | Verified |
|---|---|---|
| P1 | 6 coverings of the (1,2,2) hexagon | yes |
| P2 | flip graph has 6 coverings, 6 edges, degrees 1, 1, 2, 2, 3, 3; the unique farthest pair is 4 flips apart (ribbons LLRR and RRLL) | yes |
| P3 | the A–F pictures are valid coverings of the side-2 hexagon; fewest flips A→B = 3, C→D = 4, E→F = 8 (E→F is the largest distance in the graph) | yes (BFS) |
| P4 | 4-flip round trip exists from 18 of 20 coverings (see note 1); 5 and 7 are impossible because the flip graph is bipartite | yes |
| P5 | L and R pictures match the definition; the example on the (1,3,2) board is a valid covering whose followed chain reads LRRLR, with every label on the correct rhombus; the 6 coverings from Problem 1 have the 6 distinct ribbons with two L and two R; on the side-2 hexagon the 20 coverings have 20 distinct ribbon pairs, and every flip swaps one adjacent LR pair in exactly one ribbon | yes |
| P6 | round trips are even (each flip changes the total count of R-before-L pairs by exactly 1); E→F needs 8 | yes |
| P7 | 20 coverings (25 small hexagons given) | yes |
| P8 | (1,3,3) hexagon: 30 triangles, 20 coverings (one ribbon with three L and three R, so C(6,3) = 20) | yes |
