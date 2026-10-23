# Week 89 (Growing shapes and totals): math check

Scope:
- `lowell-math-circle-year-2/week-89/week-89-students.pdf`: one shared Grades K–5 packet, 11 pages, Problems 1–20. There is no separate band packet. The band-views table lists this packet as "whole packet" for all three bands.
  - pp. 1–3: square, stair and rectangle layers (P1–P6).
  - pp. 4–5: one tray (P7–P10). pp. 6–7: two trays (P11–P13).
  - p. 8: two building rules (P14–P15). p. 9: cube shells (P16–P17). pp. 10–11: three trays and corner piles (P18–P20).
- `week-89-materials.pdf`: 2 pages, with a 120 × 120 mm board, a 140 × 120 mm board, input cards and total cards.
- `week-89-facilitator.pdf`: 8 pages.
- The three PDFs are byte-identical to `source/week-89/reference-pdfs/`.

Sources read: `source/week-89/student/students.tex`, `student/materials.tex`, `guide/facilitator.tex`, `build.py`, `README.md`, `QA.md` and `SOURCES.md`. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-89/`. Checked October 23, 2026.

**Result: 2 problems, both minor. Every answer, count and formula on the student pages and in the guide is correct.**
1. The Problem 19 cube pictures are drawn in the wrong depth order.
2. The guide calls Problem 18's worked turn a "non-task example", but it is the task's own turn 3.

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures):
  - **Shapes.** Builds each figure as a cell set from the same rules the TikZ macros use, keeps the old shape in the corner and measures each layer (row plus column). Gives the P6 table and its second differences.
  - **P2.** Lists the corner squares inside a side-5 square.
  - **P4.** For n = 2–6, an exact-cover search tries every rectangle of area n(n+1), with the stairs in all 8 orientations.
  - **One tray.** All 120 orders for P7. P8 by subtraction. P9 by brute force over every integer start from −20 to 39 and every input 0–5.
  - **Two trays.** P10 over all small input lists. P11: all 30 distinct orders. P12: all 6 placements. P13: optimal orders checked by brute force for every multiset from 0–5 and for 300 random signed rational lists. Also the adjacent-exchange identity and the formula B_N = N·u₁ + … + u_N.
  - **P14–P15.** The two rules and the guide's third rule as cell sets.
  - **Cubes.** P16 shells. P17: every partition of the shell into three boxes for old sides 1–4, plus the guide's split by which coordinate equals n.
  - **Three trays and piles.** P18 three-tray simulation. P19 piles built by the page's stacking rule. The guide's triple bijection checked up to n = 12.
  - **Guide background.** The difference facts for polynomials and binomial coefficients.
  - **Materials.** The input cards against each task, and board fit.
- **`check_diagrams.py`** (output `check_diagrams.py.out`) reads the delivered PDFs with PyMuPDF:
  - **Pages.** Headers, footers, consecutive numbering 1–20, page counts and US Letter.
  - **Tile figures on pp. 1–3 and 8.** Read from the drawn squares, so the result does not depend on the source code. Each figure is matched to its caption, cell size 5 mm, and the opening example's shading is checked.
  - **Slips and tables.** Slip digits on pp. 4, 6 and 7, and the P8/P9 tables.
  - **Materials.** Board sizes and 20 mm grid spacing, and the card digits.
  - **P19 pictures.** The cube boxes are parsed from the TikZ source in drawing order. A ray test in the picture's own oblique projection then compares the painted image with the true nearest cube. **2 failures, which are item 1.**
  - **Guide.** Its page references.

## Student packet, Grades K–5 (pp. 1–11): correct except items 1–2

- **Opening (p. 1).** A 1 × 2 shape plus 4 shaded tiles makes a 2 × 3. The white cells are exactly the old shape, and white plus grey is the new shape.
- **P1.** The layer from side n to n + 1 is a row of n + 1 plus a column of n. For sides 1→2 up to 4→5 that is 3, 5, 7, 9. Figures are 1 × 1 to 4 × 4 with equal 5 mm cells.
- **P2.** The corner squares have sides 1, 2, 3 and 4, removing 24, 21, 16 and 9 tiles.
- **P3.** Stair totals 1, 3, 6, 10, 15, 21, with each new bottom row one longer. The figures are left-aligned 1- to 4-row stairs, as the text says.
- **P4.** For every n from 2 to 6, two copies tile the n × (n + 1) rectangle (2 tilings, mirror images) and no other rectangle. The stairs' n × n bounding box rules out the rest. The figures are two 3-row stairs.
- **P5.** The n × (n + 1) rectangle grows by a row of n + 2 plus a column of n, so 2n + 2. Totals 2, 6, 12, 20, 30, 42. The figures are 1 × 2 to 4 × 5.
- **P6.** Rows read 3, 5, 7, 9, 11 / 2, 3, 4, 5, 6 / 4, 6, 8, 10, 12, and they grow by 2, 1 and 2 forever.
- **P7.** Every one of the 120 orders ends at 10 from start 0 and at 13 from start 3. The worked turn 2 + 3 → 5 is right.
- **P8.** The inputs are 3, 0, 4, 3, and they are unique.
- **P9.** Inputs 2–4 are forced to 3, 0, 5. The starts are 0–4, with first input 4 − start, which gives 5 cases.
  - The only other integer solution is start −1 (inputs 5, 3, 0, 5). It is excluded because a start is a pile of counters, and the guide says so.
- **P10.** The rows are 1, 3, 3, 6, 7 and 4, 6, 6, 9, 10, so the gap stays 3. The gap always equals the difference of the starts.
- **P11.** The worked turn (1, 1) with input 2 → (3, 4) is right. Of the 30 orders, the maximum 21 comes only from 2, 2, 1, 0, 0 and the minimum 9 only from 0, 0, 1, 2, 2. Every value from 9 to 21 occurs.
- **P12.** With 1 before 3, the six rows give 13, 10, 7, 9, 6, 5. Zeros last gives the largest, 13; zeros first gives the smallest, 5.
- **P13.** Descending order is best and ascending worst, for every 5-input multiset from 0–5. Swapping adjacent a, b to b, a changes the result by exactly b − a.
- **P14.** Both rules give the pictured squares at steps 1–4. Rule A gives 25 and 36; Rule B gives 26 and 38. The pictures do not decide step 5.
- **P15.** Possible. The guide's rule, a tail of 2(n − 4), gives 27 and 40.
- **P16.** The shells are 7, 19, 37 and the cubes 1, 8, 27, 64. The pictured cubes have 1 × 1, 2 × 2 and 3 × 3 grids on all three visible faces, with equal front scaling.
- **P17.** Possible for every old side. Every box inside the shell is automatically one cube thick. For old sides 1–4 there are exactly 6 three-slab splits, all of sizes (n + 1)², n(n + 1) and n².
- **P18.** The totals after six turns are 6, 21, 56. The rules are n, n(n + 1)/2 and n(n + 1)(n + 2)/6. The worked turn (2, 3, 4) → (3, 6, 10) follows the page's rule. See item 2.
- **P19.** The stacking rule produces exactly the corner pile {i + j + k < n}. The piles hold 1, 4, 10, 20, 35, equal to the third tray. The step-2 picture holds the right 4 cubes. See item 1 for how they are drawn.
- **P20.** 220 = 10·11·12/6 = 1 + 3 + 6 + … + 55.
- **Materials.**
  - The boards measure 120.00 × 120.00 and 140.00 × 120.00 mm, with 20 mm cells, so 6 × 6 and 7 × 6.
  - The side-5 square, the 6-row stairs and Rule A step 6 fit board 1. The 6 × 7 rectangles of P4 and P5 fit board 2. Rule B step 6 is 8 wide and needs the table, as the guide says.
  - The cards 0, 0, 1, 2, 2, 3, 4 cover the inputs of P7, P10, P11 and P12.

### 1. p. 11, Problem 19 (minor): the two cube pictures put the corner cube in front of a cube that is nearer the viewer

- **Diagram.** There are two pictures, "put it on the square corner of a 2-row bottom layer" and "step-2 pile". In `students.tex` each picture draws its cubes in this order:
  - first the back stair cube (0,1,0);
  - then the front-right stair cube (1,0,0);
  - last the corner cube (0,0,0), which in "step-2 pile" is the two-cube column (0,0,0)–(0,0,2).
- **Evidence.**
  - The projection sends x to 7 mm across and z to 7 mm up. The visible faces are front (−y), right (+x) and top (+z), so the viewer is on the +x side.
  - The corner cube's right face is the plane x = 1, shared with cube (1,0,0). That face is hidden behind cube (1,0,0).
  - The corner cube is drawn last, so its grey right face is painted over the left part of cube (1,0,0)'s front face. That patch is 3.5 × 7 mm, 24.1 mm² by `check_diagrams.py`.
  - In the printed picture (`p11-problem19-picture.png`), the front-right stair cube looks tucked behind the corner cube even though its bottom edge lies in the same front plane. No real arrangement of cubes looks like this.
  - The stair layer is what children are asked to recognise and build, so this makes it harder to read. The cube set itself is right: {i + j + k < 2}, 4 cubes, as the guide says.
- **Smallest fix.** In both scopes, move the three `\filldraw` lines of the cube at (1,0,0) to just after the corner cube (middle picture) or the column (step-2 pile).
  - The draw order becomes back cube, corner cube or column, then (1,0,0). In the middle picture, move the cube before the falling cube's `\begin{scope}[shift={(0,0,1.8)}]`.
  - `check_diagrams.py` confirms that this order paints both pictures correctly, with zero misdrawn area. A full back-to-front, left-to-right, bottom-up order also works.

### 2. Guide p. 7, Problem 18 (minor): the "non-task example" is the task's own turn 3

- **Quoted text.**
  - Guide: "The non-task example begins at the valid state $(2,3,4)$ and ends at $(3,6,10)$ after one input 1."
  - The student page (p. 10) shows "One turn with input 1: before 2 3 4 … add new second total 3 6 10".
  - Problem 18 asks for "Start three trays at 0 and use input 1 for six turns".
- **Evidence.** From (0,0,0) with input 1 each turn, the states are (1,1,1), (2,3,4), (3,6,10), (4,10,20), and so on (`check_math.py`). So (2,3,4) → (3,6,10) is exactly turn 2 → turn 3 of the task. The page therefore prints the first three rows of the six-turn table, not a separate instance. The guide's description is false, and the example does not meet the project's rule of demonstrating on a non-task instance.
- **Smallest fix.** Start the example from a valid state that is off the all-ones path. For example, (3,3,3) is one input-3 turn from zero:
  - "before 3 3 3 / add input 1: 4 3 3 / add new first total: 4 7 3 / add new second total: 4 7 10".
  - Change the guide sentence to "(3,3,3) … (4,7,10)".
  - Copying old totals instead would give (4,6,6), so the example still tells the two readings apart (`check_math.py`).
  - If the organizer prefers to keep the printed example, change only the guide sentence instead: "The worked turn is the task's own turn 2 → 3 …".

## Adult guide (8 pp.): correct except item 2

The overview's facts hold under the hypotheses it states:
- **Layers.** 2n + 1, n + 1 and 2n + 2, with second differences 2, 1, 2.
- **Accumulation and its inverse.** A_n − A_{n−1} = u_n. A missing start leaves only a constant shift, and the gap equals the difference of the starts.
- **Cascade.** B_N = N·u₁ + (N − 1)·u₂ + … + u_N. Exchanging adjacent a < b gains b − a. The bounds for {2, 2, 1, 0, 0} are 21 and 9, and order does not matter for a single tray.
- **Three stages, input 1.** The totals are n, n(n + 1)/2 and n(n + 1)(n + 2)/6.
- **Polynomials.** A degree-d polynomial has constant d-th differences equal to d! times the leading coefficient, and zero (d + 1)-st differences.
- **Binomials.** Δ C(n, k) = C(n, k − 1) for k ≥ 1.
- **Prediction.** Four squares do not force the fifth. The n − 4 tail is a valid counter-rule.

Every solution, table, hint and extension in the guide checks:
- P1–P6, with the tables of P6, P9, P10, P11, P12 and P18.
- The P9 completeness argument and the P13 exchange proof. It also holds for signed real inputs, as the guide claims.
- P14 and P15 (27, 40).
- P16, and P17's slabs (4, 2, 1), (9, 6, 4) and (16, 12, 9) with its priority split.
- The shell differences 12 and 18 and the cubic third difference 6.
- The P19 recurrence matching, P20's 220, and the triple bijection (i + 1, i + j + 2, i + j + k + 3).
- The kit arithmetic: 360 tiles, 120 counters, 6 trays, 64 cubes and a 42-tile largest pairing.
- All seven student-page references.

**Not counted (outside the math scope, or handled as printed):**
- **Opening example (p. 1).** The worked growth 1 × 2 → 2 × 3 (add 4) is the first growth of Problem 5 and the first rectangle entry of Problem 6's table. It is correct and the guide makes no non-task claim for it. Still, the project's launch rule asks for a non-task instance, and a 1 × 3 → 2 × 4 or an L-shape would avoid the overlap.
- **Problem 9 start −1.** The page bounds the inputs but not the start. Start −1 with inputs 5, 3, 0, 5 fits the numbers. The counters model and the guide ("A negative start cannot be a collection of counters") exclude it.
- **Problem 20 "listing all ten running totals".** The ten stair-layer sizes are the second tray's running totals, so the condition can be read as forbidding the method the guide accepts. The guide states its reading explicitly, so this is wording only.
- **Problem 11 picture (p. 6).** The label "same input / already added" touches the bottom edge of its input box (0.5 pt bounding-box overlap) and the line "Copy the new first total…". This is layout, not mathematics.
- **Guide board size.** It writes "120 × 140 mm" where the material page writes "140 mm × 120 mm" (width × height). This is the same board.
