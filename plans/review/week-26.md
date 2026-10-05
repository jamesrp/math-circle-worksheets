# Week 26: Same area, different boundaries (polyomino perimeter)

**Verdict: revise.** The mathematics, problems and pages are at the bar of the approved catalogs, and every student answer checks. One must, in the guide only: Grades 4–5 Problem 2 asks "Can it have a hole?" without saying whether a corner contact closes a hole, and the key answers "yes" and calls "no holes" false, so an adult would correct a child who argued rightly. The verdict rests on this one finding, a must for the same reason as in Weeks 4, 25, 31 and 39.

Reviewed October 5, 2026 by Claude, reconciled from two independent card runs, with the math check in [week-26-math.md](week-26-math.md). Both runs gave revise on the same must and agreed with both math-check findings; they differed on whether fix 3 is a should or a could, and the second run noted that the guide's "yes" matches how physical tiles behave. Packets: week-26-k-1.pdf (W26-K-v2, 6 pp.), week-26-grades-2-3.pdf (W26-23-v2, 6 pp.), week-26-grades-4-5.pdf (W26-45-v2, 6 pp.), each P1–6. Adult guide: week-26-facilitator.pdf (unnumbered overview, printed pp. 1–18, route note numbered 20; cited by printed number). Companions noticed but not reviewed: week-26-bonus.pdf (W26-BON-v1, 4 pp.) and its 5-page guide. Status: unpiloted (source README: "The theme remains **unpiloted**"). Student packets date from October 3; the October 4 revision changed only the guide.

## The mathematics

A shape is n unit squares joined along whole sides; its boundary counts exposed unit edges, hole edges included. Each shared side hides two edges, so P = 4n − 2e: boundaries are even, and a new tile touching k old ones changes P by 4 − 2k. A connected shape has at least n − 1 shared sides, so P ≤ 2n + 2, with equality exactly for trees. From below, a shape spanning r rows and c columns has P ≥ 2(r + c) and n ≤ rc, with equality exactly when every row and column is one run; balancing the dimensions gives the greatest area ⌊s/2⌋⌈s/2⌉ for P = 2s and the least boundary 2⌈2√n⌉ (Harary and Harborth). A mathematician would enjoy it: a discrete isoperimetric problem with certificates on both sides, reached by building. K–1 P2–5 and 2–3 P1–5 carry cancellation and the maximum, 2–3 P2 and P6 carry 4 − 2k, and 4–5 P1 and P3–6 carry the lower bound.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Parity, the tree maximum and the row/column bound are reached through tasks, never stated. |
| Problems | strong | Contrasts under one question: K–1 P4's single 10 against two 12s and 14s; K–1 P6's starts ending at 14, 10, 12, one unshortenable; 2–3 P2's four starts ({+2}, {0, +2}, {−2, +2}, {−4, +2}); 2–3 P6's 1, 3, 5, 7 tiles; 4–5 P4's answers certifying P5. Fix 3. |
| Student pages | strong | Correct header and footer, rules once, one problem per page, square grids that fit the longest answers, spare boxes that hold real "can't" findings. Fixes 3, 7–10. |
| Concreteness | strong | Tiles show overlaps, whole-side joins and turns; a marker on each exposed edge makes every count checkable by a partner. The guide's p. 2 three-tile launch (a join, counting, copying onto a grid) comes before the bands split. Unrehearsed. |
| Correctness | adequate | Every student answer, figure and caption checks. The guide's hole answer holds under one reading only (fix 1); an extension answer is incomplete (fix 2). |
| Adult guide | adequate | Theorem-first overview with limits and band map, materials, launch, routes, held hints, keys with proofs, sourced pages. Fixes 1, 2, 4–6. |
| Age fit, K–1 | strong | One or two sentences per problem; build, mark and count to 18. Prediction: copying every shape onto small grids will be slow for kindergartners; the guide lets the adult record (p. 2). The second run rated this adequate on that ground. |
| Age fit, grades 2–3 | strong | Counting to 26 and small differences; the P3 rule can be said in words; P6's lower bounds are for the quickest. |
| Age fit, grades 4–5 | strong | Multiplication and fixed-sum products; P3–P5 build a real lower-bound argument; the hole question and P6 are for the quickest. |

## Keep

- Each band's rule paragraph that counts sides around holes, the p. 2 launch, one edge marker per exposed side.
- K–1: P1's six grids for five shapes; P4's second "10 sides" box, which nothing fills; P5's impossible 8 and odd lengths; P6's three starts, including the straight one that can't be shortened.
- 2–3: P1's second shortest shape (only the 2×4 and the 3×3 minus a corner exist); P2's four starts, including the frame whose hole gives −4; P3's 9 to 13 shared sides; P5's branch and ring against the row and rectangle; P6.
- 4–5: P1's pairs for 7, 10, 13; P2's 2-by-2 question; P3's fixed 4-by-5 grids, which enforce the span; the P4 → P5 → P6 chain, where 17 and 20 share 18.
- Guide: the overview, p. 3's three arguments, the paired held hints, the K–1 P6 and 2–3 P6 optimality arguments, the honest status.

## Fix

1. **must**, Grades 4–5 p. 2, Problem 2, and guide p. 14 (also the overview, p. 3, p. 18). The page asks "Can it have a hole?"; its rules say only that tiles join "along whole sides". Guide p. 14 heads the answer "A 2-by-2 block: no. A hole: yes.", says "'tree adjacency implies no holes' is false under these worksheet rules" and "Do not silently impose a different hole convention." Its hole is closed only where two tiles meet at a corner. If a corner gap lets the inside out, no twelve-tile shape with boundary 26 has a hole (math check census): a hole closed by full sides needs a ring of side-joined tiles, a loop, so e ≥ n. A child who argues this is right and would be corrected; the bonus p. 2 even forbids that corner pattern for its own theorem. Fix (guide only): head p. 14 "A hole: it depends on corners." After "Do not silently impose…" add "If a child says no because a corner gap lets the inside out, accept it: a hole closed by full sides needs a ring of side-joined tiles, which adds a shared side. Then show the corner-closed example and let the table decide whether its centre counts." Change "under these worksheet rules" to "if two tiles meeting at a corner close a gap", and qualify the overview ("corner contacts can seal a hole"), p. 3 ("a false 'no holes' rule") and p. 18 the same way.
2. **should**, guide p. 4, K–1 P1 extension: "the square cannot, while L can fill its missing corner." The T and zigzag can too; the straight cannot (math check). Fix: "the square and the straight cannot; the L, T and zigzag can, by filling a notch where the new tile touches two old ones." A should, unlike Week 31's extension: it omits cases without denying them, and tiles settle it at the table.
3. **should**, Grades 4–5 p. 3, P3: "Count the occupied rows, occupied columns, and boundary sides of each shape" prints the lower bound's method; all three shapes have boundary exactly 2 × (rows + columns), and the third (rows 5, 3, 2, 2) already answers the next paragraph's "least possible" with boundary 18. Fix: print the guide's second construction instead (rows 5; 3 plus a separate tile; 2; 1; boundary 20), so one shape breaks the pattern and children find the 18 themselves; change guide p. 15's third triple to (4, 5, 20). The second run rated this a could ("keep it if it is the intended bridge").
4. **could**, guide p. 1: "plan for 3 younger children"; context.md has four at the K–1 table.
5. **could**, guide p. 1: "a reusable matching grid", "Never scale a tile mat" and "40 short edge markers" name materials no file supplies or describes; say the table is the board, 1-inch colour tiles serve, and what a volunteer can use as markers.
6. **could**, guide p. 14: 4–5 P2 assumes "the shared-side formula", which only 2–3 P3 builds; also accept "each added tile adds at most 2". Guide p. 10: all five 2–3 P3 cases use ten tiles; suggest testing the rule on P1's eight-tile records.
7. **could**, 2–3 p. 2 P2: two After/Change boxes per start equal the answer count for three starts, so they signal completeness; add a third.
8. **could**, 2–3 P1 "Draw all four shapes and record their boundary lengths" and P3 "Record each boundary length" restate the labelled grids; delete.
9. **could**, 2–3 P4: "no shape using each number of tiles" → "no shape with that many tiles"; 4–5 P2: "with none in a straight row" → "none of them a straight row".
10. **could**, 4–5 P6 says "squares" where every other page says "tiles".

## Overlaps

Week 25 also counts rows and columns, for Ryser's switches rather than boundary; Week 50 (staircases) totals horizontal and vertical pieces, the idea behind P ≥ 2(r + c). Weeks 52 and 53 reach spanning trees, which are this week's longest shapes; cross-reference them. Week 1 fills a given region, where here children choose it; Weeks 48 and 57 relate area and boundary with other objects and theorems; the bonus's corner rule touches Week 56 (Euler). No merge.

## App fit

Fit B, size S, confirmed by both runs. A child taps cells of a square grid to add, remove or move squares; side-joins are enforced and exposed edges light up. Checkable solves: exact targets with every shape found, declared done with no slot per answer (K–1 P1, P4; 2–3 P1); one or more moves to the shortest boundary, with "can't shorten" a claim the app checks (K–1 P6); fewest starting squares for −4 (2–3 P6); least boundary in a 4-by-5 span (4–5 P3); most squares within a boundary (4–5 P4). Certificates: for "can't be shorter", each occupied row's and column's two end edges and the r × c box; for "can't be longer", the n − 1 seams; for odd targets, each seam hides two edges. Pitfalls: with a live count, plain shortest and longest goals are trivial (a blob, a row), so put the difficulty in exact targets, moves, spans, fixed boxes and blocked cells; no "what is this perimeter?" screens; fix the hole convention before a puzzle depends on it. Ported as Garden fences ([app docs](https://github.com/jamesrp/small-math-adventure/blob/main/docs/fences/README.md)), which takes the corner-closed reading for its one pond puzzle and draws the fence to show it.

## Classroom evidence

None reported. The theme is unpiloted, and no after-use notes have been recorded.
