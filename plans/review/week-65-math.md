# Week 65 (Hyperbolic octagon streets): math check

Scope:
- `lowell-math-circle-year-2/week-65/week-65-students.pdf`: one shared Grades 3–5 packet. It has 6 pages: Problems 1–5 on pp. 1–5, and p. 6 is the route sheet for Problem 5.
- `week-65-facilitator.pdf`: 7 pages.

Sources read: `source/week-65/student/build.py` (it generates `students.tex`) and `source/week-65/guide/facilitator.tex`. I did not run or import the author's `verify_geometry.py`, `verify_routes.py`, `independent_check.py` or the builder's `verify()`. Checked October 10, 2026.

**Result: every answer, count, construction and theorem in the packet and the guide is correct. Every diagram is a true, equally scaled picture of the {8,4} geometry it claims to show. I found 1 problem, a minor label placement on student p. 4.**

## How it was checked

My scripts and their outputs are in `plans/review/checks/week-65/`. Each script finds the repository four folders up from its own location.

- **`check_math.py`** (output `check_math.out`: 51 checks, 0 failures).
  - It builds {8,4} in the Lorentz (hyperboloid) model. It starts from cosh R = cot(π/8)·cot(π/4) and reflects rooms across their sides with Minkowski reflections. It does not use the author's circle formulas.
  - It derives every turn from tangent vectors in the Lorentz tangent plane, oriented by sign det[v, a, d].
  - It checks:
    - the side lengths and right angles;
    - layers 1, 8, 48 (the next layer is 280);
    - the 56 / 40 + 8 two-step multiplicities;
    - the P2 walks;
    - the P3 boundary walk, done on the actual two-room cluster;
    - all crossing relations among the 8 drawn complete streets, using |⟨n_i, n_j⟩| < 1 for crossing lines;
    - the P5 routes on the actual room adjacency at a vertex;
    - an enumeration of P1 on the printed 6 × 6 board;
    - every number in the guide's adult proof.
- **`check_pdf.py`** (output `check_pdf.out`: 59 checks, 1 failure, which is Problem 1 below).
  - It reads the delivered PDF's vector drawing with PyMuPDF: dot centres, Bézier strokes, arrow shafts and label positions.
  - It compares each diagram with the independent model using hyperbolic invariants: geodesic membership, the full matrix of hyperbolic distances, and tangent directions.
  - It also checks that the delivered guide text contains the stated keys.

## Grades 3–5 student packet (pp. 1–6): mathematics checks out; see Problem 1 for the p. 4 label

**Problem 1 (p. 1).**
- The task is to return to A facing east after 4, 6 and 8 moves, with no U-turns, where the final turn counts.
- On the printed board there are 2, 6 and 54 such routes, so every requested length exists.
- No route of 2 moves or of odd length exists.
- The guide's ENWS, EENWWS, EENNWWSS and ENWS·ENWS are all legal and fit the board.
- The board is 6 × 6 squares at 0.76 in in both directions, with A at the centre and the arrow pointing east. The three procedure panels show E, E, N, as their labels say.

**Problem 2 (p. 2).**
- The left-turn walk from A toward B visits A, B, C, D, E, F, G, H, A. After 4 moves it is at E, and its first full-state return comes after 8 moves.
- The right-turn walk from A toward H visits A, H, G, …, B, A. It also returns after 8 moves, and its fourth stop is E.
- The diagram matches the model:
  - The 8 dots lie at the model's vertices to within 4 × 10⁻⁵ disk units, and the labels A–H run counterclockwise.
  - The 8 edges are true geodesics, and the 16 stubs continue their sides.
  - The board arrow follows the true tangent toward B to within 0.00°.
  - The start, arrive and turn-left panels match the true tangents, and the turn is exactly +90°.

**Problem 3 (p. 3).**
- The octagon board is an isometric image of the true two-room cluster: all 14 × 14 hyperbolic distances match to 4 × 10⁻⁴.
- Measured from the drawn coordinates, the turns are 12 × +90° and 2 × 0°. The two straight dots are A and the lower end of the shared wall. No dot sits at the wall's midpoint, and every dot shows 4 branches at right angles.
- The start arrow keeps both rooms on the left.
- The squares board has 4 left turns and 2 straight junctions on 1.1 in squares.

**Problem 4 (p. 4).**
- The 8 drawn streets are the complete geodesics of the 8 central sides, and each ends on the dotted circle.
- They cross only at the 8 octagon vertices. Exactly two of them pass through P = v₀.
- Both of those are ultraparallel to the dashed street R, which is the geodesic of v₃v₄. So the answer is 2.
- The Euclidean question has the answer no (Playfair). That answer holds whether or not the third line passes through the point.

**Problem 5 (pp. 5–6).**
- The 28 drawn sides are exactly the sides of the four rooms at one vertex.
- Home and ⋆ are opposite rooms, and A and B are the two side-neighbours of Home. The room graph is a 4-cycle.
- There are exactly 2 two-door routes and 8 four-door routes.
  - Read as "stop at the first arrival", the count would be 4. The page's "You may visit a room … more than once" rules that reading out, so this is not a problem.
- The C → D → E example shows three equal adjacent boxes with the arrow crossing two walls.
- The route sheet has 3 lines for 2 answers and 10 lines for 8.

### 1. Page 4, Problem 4 (minor diagram label): the "R" label sits closer to a different street than to the dashed street it names

- **Quoted diagram:**
  - The label "R" is at disk coordinates (−0.77, 0.08) (`build.py`: `at (-0.77,0.08) {R}`).
  - That puts it in the outer room beyond the dashed arc, just below the thin street that continues the central octagon's upper-left side (v₂v₃) to the left map edge.
- **Evidence** (`check_pdf.out`, measured on the printed page):
  - The label centre is 9.5 mm from the v₂v₃ street and 16.2 mm from the heavy dashed street R.
  - It is 20.6 mm from the v₄v₅ street.
  - The text identifies R as "the heavy dashed street R", so the style still tells a reader which street is meant. The answer (2) is unaffected.
  - However, a child matching the letter to the nearest line, or reading it as the name of the room it sits in, is pointed at the wrong object.
- **Smallest fix:** move the label to (−0.66, 0) on R's mirror axis, in the same room.
  - There it is 8.7 mm from the dashed street and 16.1 mm from each neighbouring street (checked in `check_pdf.out`).
  - Alternatively, place it on the dashed arc itself with its existing white fill.

## Adult guide (pp. 1–7): mathematically correct throughout

- **Overview (p. 1):**
  - These facts are all true with the stated scope:
    - The tiling is {8,4}, with equal sides, right angles and four rooms per vertex. The map is conformal.
    - The one-octagon walk returns after 8 moves and is at the opposite vertex after 4.
    - The cluster walk has 12 quarter-turns and 2 straight junctions, against 4 for two squares.
    - The two streets through P miss the complete street R.
    - Problem 5 has 2 and 8 routes.
  - It correctly limits the walk claim to the supplied equal-edge walk. It also correctly says that other lines through P exist.
- **Keys:**
  - The P1 examples and the "final southward arrival, then left turn" remark are correct.
  - The P2 vertex sequences and the headings after the final turn are correct.
  - The P3 table (6/4/2 and 14/12/2) is correct. So are 16 − 4 = 12, 8 − 4 = 4, 8 + 8 − 2 = 14 and 4 + 4 − 2 = 6, and the description of the counterclockwise start.
  - The P4 description of the two streets (upper right, and down the right side) is correct.
  - The P5 eight-route table and its three-binary-choice completeness argument are correct.
- **Adult proof (p. 6):**
  - These are all correct:
    - the orthogonal-circle centre equations and ρ² = |c|² − 1;
    - the centres C e^{iπ/4}, C and −C, with C = 2^{1/4};
    - the common radius r = √(√2 − 1);
    - the bounds −C + r = −0.546, C/√2 − r = 0.197 and C − r = 0.546;
    - the identity (C/√2)² − r² = 1 − √2/2.
  - So the separation by x = 0 is a valid whole-line proof.
- **Extension and preparation:**
  - These are all correct:
    - 8 × 7 = 56, with 8 doubly reached rooms, giving 48 = 40 + 8;
    - the square-grid layers 1, 4, 8;
    - 17.9 mm minimum junction spacing (measured 17.85 mm);
    - five packets × 6 = 30 sheets;
    - six working counters.
