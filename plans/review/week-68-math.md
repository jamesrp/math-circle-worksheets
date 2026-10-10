# Week 68 (How many ways out): math check

Scope:
- `lowell-math-circle-year-2/week-68/week-68-students.pdf`: one shared Grades 3–5 packet, 4 pages, Problems 1–8.
- `week-68-facilitator.pdf`: 2 pages.

Sources read: `source/week-68/student/students.tex` and `source/week-68/guide/facilitator.tex`, plus the package's README, MATHEMATICS.md and the student README. I did not run or import the package's own checkers. My scripts and their saved outputs are in `plans/review/checks/week-68/`. Checked October 10, 2026.

**Result: every student problem is correct, possible where the page assumes it is, and impossible where the intended answer is "no". Every diagram encodes the graph its text describes. The overview's theorems and their hypotheses are right. I found 3 problems, all in the adult guide and all minor: one incomplete answer (P3), one missing edge-case note (P5), and one wording clash with the defined term "end" (P5 hint).**

## How it was checked

- **`check_math.py`** (output `check_math.out`) models each map as an infinite graph cut off far beyond the printed window. Blockers are allowed only on printed dots. A component counts as a forever piece when it reaches the cut-off boundary.
  - **Line:** all placements of 1, 2 and 4 blockers on the 9 dots (P1), and all 126 placements of 4 blockers (P2).
  - **Ladder:** all 18 one-blocker, 153 two-blocker and 3,060 four-blocker placements on the 18 dots (P3, P4).
  - **Grid:** all 194,580 four-blocker placements on the 7×7 window (P5 left). BFS from P to Q around the X wall, both inside the window and on a large board (P5 right). The annulus-connectivity lemma behind the P6 proof.
  - **Tree:** a 3-regular tree to depth 10, with balls of radius 0–4 removed (P7, P8).
- **`check_diagrams.py`** (output `check_diagrams.out`) reads the vector drawings and text positions in the delivered student PDF and rebuilds each map:
  - **p. 1:** the convention example, and the four 9-dot lines with two-way arrows.
  - **p. 2:** the three ladders, with rungs at every column and arrows on all four rail ends.
  - **p. 3:** both 7×7 grids, with spacing, all 28 boundary arrows, and the X, P and Q positions.
  - **p. 4:** the tree's degrees, levels, acyclicity, arrow count and crossings.

## Student packet (pp. 1–4): checks out

- **Convention example (p. 1):** the X counter covers the upper-right dot of the square. The "roads left" frame is exactly the square minus that dot and its two roads: 3 dots and 2 roads forming an L.
- **P1:** every placement of 1, 2 or 4 blockers leaves exactly 2 forever pieces. The possible trapped-piece counts are 0 with 1 blocker, 0–1 with 2 blockers and 0–3 with 4 blockers. All four lines have 9 dots spaced 17.5 mm, with an arrowhead at each end pointing outward.
- **P2:** 60 of the 126 four-blocker placements trap exactly two pieces, so the task is possible. The guide's choice, dots 2, 4, 5 and 7, traps {3} and {6}.
- **P3:** one blocker never disconnects the ladder. Two blockers separate it in 25 of 153 placements and never create a trapped pocket. Both outcomes the task asks for can therefore be kept. Each ladder has 9 rungs, one at every dot column, and 4 rail arrows.
- **P4:** the intended answer is "no". Across all 3,060 placements of four blockers, at most 2 forever pieces remain. The maximum total number of components is 4: two forever pieces and two isolated dots, from a zigzag placement.
- **P5 left:** exactly 25 four-blocker placements trap a dot. Each one is the set of four neighbours of an interior window dot. On both grids the spacing is 10.0 mm in each direction, so the squares are true squares.
- **P5 right:** X is at (0, −2..2), P at (−2, 0) and Q at (2, 0). The shortest open route has 10 steps, both inside the window and on a large board. Every open dot belongs to the one forever piece.
- **P6:** the intended answer is "no", by the one-end argument. The lemma that the box exterior is connected checks for N ≤ 5 and M ≤ N+4.
- **P7 and P8:** the drawing has 22 dots in levels of 1, 3, 6 and 12 and 21 dot-to-dot roads, so it is connected and has no cycles. Each outer dot has 2 arrow roads, so every dot has degree 3. Nothing crosses, and the levels are concentric circles. Removing radius 0–3 gives 3, 6, 12 and 24 forever pieces using 1, 4, 10 and 22 blockers, matching 3·2^r.

## Adult guide

The overview is correct. The line and ladder have two ends, the grid one end and the tree infinitely many ends, with counts of 3·2^r. The tail, enclosing-box and no-rejoin arguments are valid as stated. The answers to P1, P2, P4 (including the three-component example), P5 (including the 10-step optimality argument), P6, P7 and P8 are correct. The preparation numbers are also right: 10 mm grid spacing, and 10 blockers covering the tree through radius 2. Three findings follow.

### 1. Guide p. 2, Problem 3: the separating two-blocker placements are incomplete (minor)

Quoted text: "With two blockers, cover both dots of one rung. This makes **two forever pieces**, since no road crosses that blocked column." The hint adds: "make an actual detour before deciding that a gap in one rail is a separation."

Evidence (`check_math.out`, P3): 25 two-blocker placements separate the ladder. Only 9 of them are same-rung pairs. The other 16 are **diagonal pairs**: one dot on each rail, in neighbouring columns, such as top at column k and bottom at column k+1. Each rail then has only one gap, yet no road joins column k or below to column k+1 or above. The top road between those columns is closed by the blocked dot at its k end, and the bottom road by the blocked dot at its k+1 end.

A child is more likely to find this placement than the rung. The guide describes only the rung, and its hint frames single gaps in a rail as things to detour around. Together these could lead an adult to reject a correct separation.

Fix: after the rung sentence, add: "A diagonal pair also separates: block one rail at a column and the other rail at the next column; no road crosses between those two columns."

### 2. Guide p. 2, Problem 5 (left grid): the trapped dot must be an interior window dot (minor)

Quoted text: "On the left, leave a dot open and block its four immediate neighbors: above, below, left, right."

Evidence (`check_math.out`, P5 left): four blockers trap a dot only when they are its four neighbours. Within the printed 7×7 window, that works only for the 25 interior dots. For any of the 24 dots on the window's edge, one neighbour lies past the arrow and has no printed dot to cover. A child who starts at an edge dot cannot carry out the task.

Fix: add "(choose a dot not on the window's edge)" to that sentence. Optionally, tell adults to steer a child who starts at an edge dot.

### 3. Guide p. 2, Problem 5 hint: "ends" used in a second sense (minor, wording)

Quoted text: "*Hint:* a finite wall has ends; trace around one instead of treating the edge of the page as a wall."

In this guide, "end" is the technical term the whole week builds toward. Here it means the endpoints of the five-X wall, which are not ends in that sense. An adult could misread the hint.

Fix: "*Hint:* a finite wall stops somewhere; trace around its top or bottom instead of treating the edge of the page as a wall."
