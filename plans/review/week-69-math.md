# Week 69 math check: Thin and fat road triangles

Packet checked: `lowell-math-circle-year-2/week-69/week-69-students.pdf` (one shared Grades 4–5 packet, 4 pages, GGT69-S-v1) and `week-69-facilitator.pdf` (2 pages, GGT69-FAC-v1). Sources: `lowell-math-circle-year-2/source/week-69/student/students.tex`, `guide/facilitator.tex`. Pages were rendered and read; the diagram data came from the TeX source and the PDF vector content.

Scripts and their outputs (in `plans/review/checks/week-69/`; each finds the repository four folders up):
- `check_week69.py` / `.out`: uses BFS on explicit graphs, with no Manhattan-distance shortcut, to check every numbered claim.
- `check_pdf_diagrams.py` / `.out`: checks the dot lattices and tree dot counts in the delivered PDF.

## What was verified

- **Launch examples (p.1, p.2).** The P→Q route (0,0)–(1,0)–(1,1)–(2,1) has 3 roads. That is the shortest length, and 3 shortest routes exist. In the gap example, P=(0,1) is exactly 3 steps from the dark side x=3 of the 3×2 grid.
- **Problem 1 (p.1).** The trees parsed from the source are connected and acyclic: 12 dots/11 roads and 11 dots/10 roads. No road passes through another dot and no two roads cross. The PDF draws 23 tree dots. Across all 220+165 = 385 home triples, every road lies on 0 or 2 of the three routes, never 1 or 3, so the intended answer "No" is correct. 400 random trees agree.
- **Problem 5 (p.4).** Every gap is 0 for all 385 printed triples and for the random trees. The guide's two proofs (tripod; edge separation) are correct for any tree.
- **Problems 2–3 (pp.2–3).** The printed boards are 4,4 (P2) and 2,4,6 (P3). Each has A=(0,0), B=(n,0), C=(n,n) and equal x/y spacing in the PDF. AB and BC have unique shortest routes. The number of shortest AC routes is C(2n,n), giving 6/70/924 for n=2/4/6. For every AC route with n=1..7, gaps were computed on the full grid:
  - The maximum gap is exactly n, reached only by AC = left-then-top, at the dot (0,n).
  - The only route with every gap 0 is AC = bottom-then-right.
  - On the 4×4 board, 53 of 70 routes give a gap of at least 2.
  - The guide's bound (gap at most min(y, n−x) on AC, at most n on AB/BC) holds for every dot.
  - The answers do not change when the board is embedded in a larger grid.
  - Splitting each road into half-steps (the continuous-edge version) still gives thinness exactly n.
- **Problem 4 (p.4).** For k = 0..11, n = k+1 gives a marked gap of k+1 > k. The guide's general argument is correct.
- **Guide overview and solutions.** Every stated fact is true under its stated hypotheses:
  - the tripod with at most one zero arm for distinct homes
  - the corner construction with lengths n, n, 2n and gap n
  - "no uniform bound" stated as a property of the family, not of every grid triangle
  - the continuous-edge remark
  - the 385/6/70/924 check counts
  - the P3 table
  - the P2 hint ("why three cannot work")

  The P3 hint about colored roads is borne out: on the 4×4 board, measuring along colored roads alone overstates the maximum gap for 53 of 70 routes, and 19 of those falsely appear to reach 4.

**Student packet: checks out completely.**

## Finding (guide, minor; not a mathematical error)

1. **Guide p.2, Problem 2:** "For a **positive gap**, leave AB and BC unchanged and take AC up the left and across the top. Circle the top-left dot. Its gap is **4**…".
   - **Issue:** Problem 3 prints the same 4×4 board with the same homes (student p.3, middle) and asks for the largest gap. The computation shows left-then-top is the *unique* optimum there. The guide's suggested Problem 2 answer therefore gives away Problem 3's middle board. An adult who steers a child to it in Problem 2 removes that discovery.
   - **Smallest fix:** in the Problem 2 answer, give a modest example instead. For instance, AC goes up 2, right 4, up 2: (0,0)→(0,2)→(4,2)→(4,4). That example has maximum gap 2, for example at (0,2), which is 2 steps down to A and 4 steps from the right side (checked in `check_week69.py`). Then add one clause: "Save the left/top choice for Problem 3."
