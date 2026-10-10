# Week 78 (three-armed lines): math check

Scope:
- `lowell-math-circle-year-2/week-78/week-78-students.pdf`: one shared Grades 4–5 packet, 4 pages, Problems 1–7. It is the only band.
- `week-78-facilitator.pdf`: 4 pages.

Sources read: `source/week-78/student/` (`students.tex`, `data.py`, `build.py`, README) and `source/week-78/guide/facilitator.tex`, plus the package's `MATHEMATICS.md`. I did not run or import `checks/independent_check.py`, `student/check_math.py` or `guide/check_math.py`. My scripts and their outputs are in `plans/review/checks/week-78/`. Checked October 10, 2026.

**Result: every answer, ray, junction set, theorem and proof step in the packet and guide is correct, and every diagram encodes what its text says. I found 1 problem, a minor wording slip in a model child explanation in the guide (p. 3).**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures):
  - Membership test: the least of x−a, y−b, 0 occurs at least twice. My own exact-Fraction intersection of closed rays covers both the line arms (E, N, SW) and the reversed junction fans (W, S, NE).
  - Every exact result is cross-checked both ways against brute-force membership on a ½-step grid over [−6, 16]².
  - Recomputes the opening example, all six P1 menu/fixed cases, all four P2 pairs, both P4 pairs (including which arm each target uses), all three P5 junction sets and P6.
  - Checks that for A = (4,4) every integer B on the 0–8 board puts the meeting point or ray start on the printed board, with all four meeting kinds available.
  - Runs a finite regression of the intersection theorem over 6,480 half-integer pairs and 4,000 random rational pairs, aligned cases included. Every result is one point or exactly the predicted ray.
  - Runs a finite regression of the joining theorem over 2,352 half-integer target pairs: one junction, or the west, south or northeast ray stated in the guide.
  - Also checks the coincident-target case, the half-turn (reflection-through-origin) identity, and the guide's preparation and hour arithmetic.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures):
  - Reads the delivered student PDF with PyMuPDF and finds all 15 boards. Every board is square, with a 9 × 9 line grid at equal unit spacing in x and y, and tick labels 0–8 on matching lines.
  - Maps every filled junction dot and open target circle to board coordinates with its letter. All of them match the problem data (P1 A(4,4) ×2, A(2,2)/B(6,5), A(2,2)/B(5,6); P2–P6 as listed below; P7 blank).
  - Opening diagram: arms leave (2,2) east, north and southwest; P = (4,2) filled; Q = (4,4) open.
  - Confirms with `pdftotext` that the guide prints each answer the math check recomputes.

The general claims are also proved by hand, not just checked on samples: the case split of the minimum tie, the rectangle argument in every NW/SE, SW/NE, square, zero-width and zero-height case, and the reduction of the reversed fan to the intersection theorem by a half-turn.

## Student packet (Grades 4–5, pp. 1–4): checks out

- **Opening (p. 1):**
  - For (4,2) the numbers are 4, 2, 2, so the least is tied and the point is on the line. For (4,4) they are 4, 4, 2, so the least occurs once and the point is off the line. The larger tie correctly does not count.
  - "compare x, y, and 2" is the same set as min(x−2, y−2, 0) at every tested point, and its tie set is exactly the E, N and SW closed rays from (2,2).
- **P1:**
  - The top boards (A = (4,4), with B chosen by the child) admit a single point, an east ray, a north ray, a SW ray, or the whole line when B = A. Every meeting stays on the printed board.
  - The fixed boards give (2,2)&(6,5) → only (3,2), and (2,2)&(5,6) → only (2,3). These are the two unequal SW/NE rectangles.
- **P2:**
  - (2,5)&(6,2) → only (6,5).
  - (3,2)&(3,6) → north ray from (3,6).
  - (2,4)&(6,4) → east ray from (6,4).
  - (2,2)&(6,6) → SW ray from (2,2). The segment from (2,2) to (6,6) is correctly not shared.
- **P3:** no. Distinct junctions always give one point or one ray.
- **P4:**
  - (2,5),(6,2) → unique junction (2,2), with P on the north arm and Q on the east arm.
  - (2,2),(6,5) → unique junction (5,5), with P on the SW arm and Q on the east arm.
  - No second line exists for either pair, so "Can you find a second line" correctly has the answer no.
- **P5:**
  - Every junction answer is a closed ray.
  - (2,4),(6,4) → the west ray from (2,4).
  - (3,2),(3,6) → the south ray from (3,2).
  - (2,2),(5,5) → the NE ray from (5,5).
  - Each ray is visible on its board, so "Mark a whole stretch" is apt.
- **P6:**
  - (2,7)&(10,5) meet only at (10,7). That point is off the 0–8 board, as intended, and inside the guide's 0–12 extra grid.
  - No two lines miss. More than one shared point occurs exactly for a shared row, column or rising diagonal, or for equal junctions.
- **P7:**
  - Exactly one line passes through two different points unless they share a row, column or rising diagonal. Then infinitely many lines pass through them.

## Adult guide: correct except for one wording slip

The overview's intersection table, joining theorem, tropical (min-plus corner-locus) description, all P1–P7 solutions and the p. 4 proofs are correct. Each proof states the right hypotheses: distinct junctions, distinct targets, closed rays and all real coordinates. The guide also says which cases are experiments and which are proofs.

### 1. Guide p. 3, Problem 3 (minor): the model child explanation omits "rising", so read literally it states a false rule

- **Quoted text:** "Child explanation after the rectangle argument: 'If the junctions are on the same row, column or diagonal, the matching arms keep sharing forever. Otherwise the arms meet once at the rectangle crossing.'"
- **Evidence:** junctions on the same falling diagonal meet in exactly one point (`check_math.py.out`, last block):
  - L(2,5) and L(5,2) meet only at (5,5).
  - L(2,6) and L(6,2) meet only at (6,6).

  Every other statement of the rule in the guide qualifies it: p. 1 says "Same rising diagonal: a − b = c − d", p. 3 P6 says "shared column, row or rising diagonal", and P7 says "rising slope-1 diagonal". This model answer is the one an adult is most likely to echo to children, and "diagonal" alone would accept an incorrect child rule.
- **Smallest fix:** change "same row, column or diagonal" to "same row, column or southwest–northeast diagonal".
