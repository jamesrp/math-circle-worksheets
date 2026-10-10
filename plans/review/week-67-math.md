# Week 67 (Meeting on shortest roads): math check

Scope:
- `lowell-math-circle-year-2/week-67/week-67-students.pdf`: one shared packet, 4 pages, headed Grades 3–5, with Problems 1–5 and footer ID GGT67-S-v1.
- `week-67-facilitator.pdf`: 2 pages, footer ID GGT67-FAC-v1.

Sources read: `source/week-67/student/students.tex` and `source/week-67/guide/facilitator.tex`, plus the package READMEs and `MATHEMATICS.md`. I did not run or import the package's `checks/`, `student/check_math.py` or `guide/check_math.py`. My scripts and their output are in `plans/review/checks/week-67/`. Checked October 10, 2026.

**Result: every answer, count, diagram and theorem in the packet and guide is correct. I found 1 problem, and it is minor: Problem 5 has no unmarked cube map for its new homes.**

## How it was checked

- **`pdfgraph67.py`** rebuilds each printed road map as a graph from the delivered student PDF's vector drawings, not from the TeX. Filled discs become dots. White circles become labelled dots, with labels taken from the PDF text. Each stroked segment or rectangle becomes roads between the consecutive dots it passes through.
- **`check_math67.py`** (output `check_math67.out`, 40 checks, 0 failures) runs three groups of checks.
  - **Part A, the printed maps.** It runs a breadth-first search on every map and applies all three pair tests to every dot. It also checks:
    - grid size and equal x/y spacing;
    - the p. 1 example's labels, its thick route and its four printed step counts;
    - the tree's shape;
    - that the four-cycle is drawn as a square;
    - that every cube road changes exactly one digit, that both maps are Q3, that each has 2 crossings away from labelled dots, and that each front face is square.
  - **Part B, enumeration.**
    - All 2,300 distinct and 2,925 repeated triples on the 5×5 grid.
    - Every full w×h grid with 1 ≤ w, h ≤ 6: 36,701 triples, each with a unique meeting dot equal to the coordinate median, which is also the sum minimiser.
    - A grid with missing roads that has no meeting dot, which confirms the guide's "full grid" hypothesis is needed.
    - All 120 cube triples (majority rule) and the guide's P5 lemma.
    - All 18,247 labelled trees on 3–7 vertices: 1,489,089 triples, each with a unique meeting vertex equal to the common point of the three paths.
    - The triangle, which has no meeting vertex even though every vertex minimises total travel.
  - **Part C, the guide.** It compares the delivered guide's printed answers, P1 table rows, P4 routes and stated counts with those computations, using `pdftotext`.

## Shared packet (pp. 1–4): checks out except Problem 1 below

- **p. 1 rules and example:** P = (0,0), Q = (2,1) and M = (1,1) on a 3×2 grid. The thick route is P→(1,0)→M→Q. The printed counts are correct: "P to M: 2, M to Q: 1, Through M: 3, Shortest P to Q: 3".
- **P1:** the answers are unique.
  - Left board: A(0,0), B(4,1), C(1,4) meet only at (1,1). The pair sums 2+3 = 5, 2+3 = 5 and 3+3 = 6 equal the pair distances.
  - Right board: A(0,3), B(4,0), C(4,4) meet only at (4,3). The pair sums 4+3 = 7, 4+1 = 5 and 3+1 = 4 also equal the pair distances.
  - Both boards are full 5×5 grids with equal spacing (45.3–45.4 pt).
- **P2:** the four boards are full 5×5 grids. Every one of the 2,300 placements on three different dots has exactly one meeting dot. So both "no meeting dot works" and "more than one" are impossible, as the guide says.
- **P3:**
  - Tree: 10 dots and 9 roads. The only meeting dot is the degree-3 junction directly below C. Each home is 2 roads away and every pair distance is 4.
  - Triangle: no meeting dot. It is drawn isosceles (103.3, 103.3 and 106.3 pt) and is not called regular.
  - Four-cycle: drawn square (102.0 × 102.0 pt). Only B works.
  - "Even when drawn longer" correctly covers the two diagonal tree roads.
- **p. 4 rule example:** 001→101 changes the first digit and 101→100 the last, as labelled.
- **P4:** both maps are correct cubes, and the crossings are away from labelled dots. With homes 000/110/101 the only meeting label is 100. With 001/010/111 it is 011. Both are majority labels, and every home pair is 2 roads apart.
- **P5:** the majority rule holds for all 120 triples, repeats included.

### 1. Page 4, Problem 5 (minor): no unmarked cube map for the "new homes"

- **Quoted text:** "Choose three new homes on a cube map. Can you predict the meeting label from the home labels? …" Below it are only three answer rules.
- **Evidence:** p. 4 has exactly two cube drawings, and Problem 4 uses both. Children mark three homes on each and draw three coloured routes on each. To place three new homes "on a cube map", they must reuse a map that already carries 3 homes and 3 coloured routes, or draw their own cube. The mathematics is right. The issue is that the requested action has no clean workspace.
- **Smallest fix:** add one blank `\cube` to Problem 5. The page has room at the bottom, for example in place of one answer rule. Alternatively, reword the task to "Choose three new home labels".

## Adult guide (pp. 1–2): checks out

These are all true with the stated hypotheses:
- the overview's three interval equations;
- the "some, not every, shortest route" caveat;
- the grid median rule, its proof that it holds coordinate by coordinate, and its "full grid, no missing roads or diagonals" limit;
- the tree tripod centre;
- the cube majority rule;
- that the triangle has no meeting vertex;
- the warning against replacing the tests by minimising total travel.

The launch claim is also correct: the upper-left dot (0,1) also lies on a shortest P–Q route; in fact all 6 dots do. Every numbered answer, table entry, route and hint matches the computations. The P5 existence-and-uniqueness argument is complete.

I did not check the Druţu–Kapovich page and definition references, because no local copy of the book is available.
