# Week 1: undergraduate mathematics behind the pattern-block questions

Research and independently checked adaptations, 2026-09-19. The source statements below are distinguished from our new child-facing problems. This is a source/reasoning note, not an extra worksheet to assign in full.

## 1. Feasibility: invariants, then counterexamples to the invariant's converse

The undergraduate starting point is the mutilated checkerboard: every domino covers one black and one white square, so deleting two same-colored corner squares prevents a tiling. Brian Kell's [CMU 21-110 polyominoes activity](https://www.math.cmu.edu/~bkell/21110-2010s/polyominoes.html), section “Tiling a checkerboard,” explicitly assigns this problem and the deficient-board tromino problem.

**Our triangular-lattice adaptation.** Use the blue 60-degree rhombi. Each one covers exactly one up-pointing and one down-pointing unit triangle, in every permitted orientation. Covering a region with rhombi therefore preserves the difference between the counts of the two kinds of triangle. This is the same invariant method as the checkerboard problem, on a different lattice and with a different tile.

Useful contrast: a parallelogram made from two rhombi has four unit triangles and tiles; the equilateral triangle with side length two also has four unit triangles but does not. Area divisibility alone is insufficient: the latter has three up triangles and only one down triangle.

**K–1 entry.** Build one blue rhombus from two green triangles. Turn it and compare its two little triangles with the marks on a mat. Try the side-two triangle with blue pieces, then fill remaining spaces with green triangles. The mathematical question is whether every space can have a partner. No numerical proof or reading is needed.

**Grades 2–3 core.** After trying the side-two triangle, mark the two triangle orientations differently. Ask, “What two kinds does every blue piece cover?” Let the invariant emerge from the pieces. Ask children to explain why trying more positions cannot fix the unequal numbers. Do not reveal the invariant before they have tried the puzzle.

## 2. Optimization: a construction and a reason no improvement is possible

**Core question.** Tile an equilateral side-three triangle using blue rhombi and green unit triangles. What is the fewest green pieces possible? Blue pieces may turn; they must cover pairs of whole printed cells, without overlap or protrusion.

**Checked answer: three greens and three blues.** There are six up triangles and three down triangles. Each blue uses one of each, so no more than three blues fit. At least three up triangles remain. The following explicit construction attains the lower bound.

Use axial coordinates, with basis vectors `(1,0)` and `(1/2,sqrt(3)/2)` in Cartesian coordinates. Define:

- `U(i,j)` with vertices `(i,j),(i+1,j),(i,j+1)`;
- `D(i,j)` with vertices `(i+1,j+1),(i+1,j),(i,j+1)`.

The side-three triangle has outer vertices `(0,0),(3,0),(0,3)` and these cells:

```
Up:   U(0,0), U(1,0), U(2,0), U(0,1), U(1,1), U(0,2)
Down: D(0,0), D(1,0), D(0,1)
```

Place rhombi on the pairs `U(0,0)+D(0,0)`, `U(1,0)+D(1,0)`, and `U(0,1)+D(0,1)`. Fill `U(2,0), U(1,1), U(0,2)` with greens. Each indicated union is a blue rhombus and the six covered cells are disjoint.

For side two, use `U(0,0)+D(0,0)` and put greens in `U(1,0),U(0,1)`: one blue and two greens. A side-four triangle can use six blues and four greens.

**Teacher extension: exact theorem for every side length.** A side-`n` equilateral triangle contains `n(n+1)/2` up and `n(n-1)/2` down unit triangles. The difference is `n`, so at least `n` greens are needed. For every pair of nonnegative integers `i,j` with `i+j<=n-2`, place the rhombus `U(i,j)+D(i,j)`. Leave the `n` up cells with `i+j=n-1` for greens. This construction proves the lower bound is attained for every positive integer `n`.

Children can discover the counts by rows, without formulas: rows have one more up than down triangle, so each new row creates one additional unmatched up triangle. The general statement is a genuine extremal theorem; making a good packing and proving optimality are different tasks.

**The purple chevron is mathematically useful.** The manufacturer geometry, checked separately against its booklet, shows that each purple piece is the union of two blue rhombi. Hence any blue/purple/green tiling can be converted into a blue/green tiling by replacing each purple piece with its two blues. Adding purple cannot lower the minimum number of greens: the answer remains `n`. More generally, a region is tileable using blues and purples if and only if it is tileable with blues alone, assuming sufficient blue inventory. One direction replaces purples; the other simply uses the all-blue tiling. “Can a new piece rescue an impossible puzzle?” is a concrete introduction to reductions and equivalence of decision problems.

Keep the objective explicit: we minimize **green fillers**, not total blocks. A purple can reduce the total block count while leaving the minimum number of greens unchanged.

## 3. Matching: why equal counts do not guarantee a tiling

Oscar Levin's author-hosted [Discrete Mathematics: An Open Introduction, fourth edition, §2.7](https://discrete.openmathbooks.org/dmoi4/sec_matchings.html), Theorem 2.7.1 and Exercises 1–3, treats Hall's theorem, partial matchings, and augmenting paths. A lozenge tiling is a perfect matching of the bipartite graph whose vertices are the up and down triangles, with an edge for shared sides. The total-count test is only the weakest matching obstruction.

**Our checked six-cell counterexample.** This connected, hole-free region contains three up and three down triangles but has no blue tiling:

```
A = U(0,0)       D = D(0,0)
B = U(1,0)       E = D(-1,1)
C = U(0,1)       F = D(0,1)
```

Its outer boundary, in the same axial coordinates, is:

```
(-1,2), (0,2), (1,2), (1,1), (2,0), (1,0), (0,0), (0,1)
```

Consecutive collinear vertices can be omitted from the outside outline; preserve the internal triangular-cell lines. The first and last vertices are joined.

The only side-adjacencies are `A-D`, `B-D`, `C-D`, `C-E`, `C-F`. Both A and B can pair only with D. Thus at least one must remain uncovered; both cannot use the same neighbor. This is Hall's obstruction with `S={A,B}` and `N(S)={D}`.

**Strong grades 2–3 reserve / grades 4–5 warm-up.** “There are three of each kind. Does that guarantee a tiling?” Let children test, then ask them to circle two spaces competing for the same partner. They do not need graph terminology or Hall's theorem.

**Optimization version.** The minimum green fillers is two, despite the global up/down difference being zero. Use blues `A+D` and `C+E`, then greens at B and F. The competing A/B pair proves at least one up remains; balanced starting counts then force a down to remain too. Adding purple cannot repair tileability, by the replacement argument above.

This counterexample matters pedagogically: do not let the lesson accidentally teach the false theorem “equal up/down counts implies tileable.” A necessary condition is a useful test, not a complete decision procedure.

## 4. Counting and moving among solutions

Kell's CMU activity also asks for counts of domino tilings of `2 by n` boards. Levin's [§4.1, Exercise 16](https://discrete.openmathbooks.org/dmoi4/sec_seq_intro.html) asks students to find and justify the recurrence. Separating cases by the first tile gives `T(n)=T(n-1)+T(n-2)`, with `T(0)=T(1)=1`. The key lesson is explaining an exhaustive count, not merely spotting Fibonacci numbers.

For these physical blocks, the more natural main problem is lozenge tilings of a small hexagon and its graph of local flips. Alexander Postnikov's [MIT 18.312 advanced undergraduate course](https://math.mit.edu/~apost/courses/18.312-2005/) places domino tilings in Lecture 20, Hall's theorem in Lecture 21, Pfaffians/matchings in Lecture 22, and plane partitions/rhombus tilings in Lecture 23. This is a direct undergraduate source trail for using tilings to reach graph theory, counting, and algebra.

**K–1 entry.** A unit regular hexagon has two blue-rhombus tilings. Finding the second and replacing the three rhombi introduces a genuine local move.

**Grades 4–5 main direction.** A hexagon with consecutive side lengths `1,2,2,1,2,2` has eight blue rhombi in every tiling and exactly six tilings. One legal move exchanges the two fillings of a unit hexagon using three rhombi. The six states form a diamond with a tail at each end: edges `0-1, 1-2, 1-3, 2-4, 3-4, 4-5`. This finite case supports exhaustive enumeration, connectivity, shortest transformation sequences, and random-walk extensions. Coordinates, tiling diagrams, and research-level interpretations are developed in the companion research work. The six-state count and adjacency list were also independently verified here by enumerating all perfect matchings of the region's cell-adjacency graph.

Do not transfer the square-grid Fibonacci recurrence to this triangular-grid region. They illustrate related methods, not identical counting sequences.

## 5. Recursive construction: the classic tromino problem as a later paper activity

Eric Lehman, F. Tom Leighton, and Albert R. Meyer, [Mathematics for Computer Science (MIT, 2015)](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/mit6_042js15_textbook.pdf), §5.1.5, printed pp. 119–122, develops the deficient `2^n by 2^n` courtyard. The successful proof strengthens the induction hypothesis from a central missing square to **any** missing square. Divide into four quadrants; place one central L-tromino in the three quadrants without the real missing square; each quadrant now has exactly one missing cell, so recurse.

This is both an existence proof and a constructive algorithm. [Francis Su's HMC “Inductive Tiling”](https://math.hmc.edu/funfacts/inductive-tiling/) gives the same geometric construction and suggests trying the boards before revealing the proof.

For a future grades 4–5 session, paper square-grid L-trominoes and a `4 by 4` board give the concrete entry, with `8 by 8` as the generalization. Keep this as a separate square-grid activity. A purple chevron consists of four triangles, not three squares; the square-board theorem does not automatically become a theorem about the pattern blocks.

## Suggested one-hour emphasis

For grades 2–3: 8 minutes learning the physical pieces; 12 minutes on the four-cell possible/impossible contrast; 20 minutes optimizing the side-three triangle and explaining the lower bound; 10 minutes asking whether purple changes the answer; 10 minutes sharing, or the balanced six-cell counterexample for a group ready to go further. These timings are our planning suggestions, not claims from the undergraduate sources.

Reading can be adult-supported. Counting to nine and comparing two small counts is sufficient for the main problem; no multiplication, algebra, or formal proof notation is required. Offer a larger triangle or the bottleneck only once children have a reason for their original answer.
