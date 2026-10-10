# Week 77 (persistent holes): math check

Scope:
- `lowell-math-circle-year-2/week-77/week-77-students.pdf`: one shared Grades 4–5 packet, 5 pages, Problems 1–6. SHA-256 e27735de…4d4787, the same as in `source/week-77/QA.md`.
- `week-77-facilitator.pdf`: 4 pages. SHA-256 86d65e91…6775fc, the same as in QA.md.

Sources read: `source/week-77/student/students.tex` (for the board coordinates), `guide/facilitator.tex`, `MATHEMATICS.md` and the READMEs. I did not run or import the packet's own `check_math.py`, `independent_check.py` or `baseline_check.py`. I rendered the pages to `tmp/review-runs/week-77/render/` and looked at each one. My scripts and their outputs are in `plans/review/checks/week-77/`. Checked October 10, 2026.

**Result: every answer, count, table, construction and proof in the packet and the guide is correct, and every board matches its text. I found 2 problems, both minor. One is a sentence in the guide's overview that leaves out a hypothesis. The other is an optional fix to how the joined board on student p. 3 is drawn.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`: 61 checks, 0 failures)
  - **Model.** It rebuilds the square, joined and fan boards from the coordinates in `students.tex`. Loops are mod-2 edge sets. A saved loop counts as "gone" when some subset of the available filled faces has exactly that edge set as its boundary. The script finds this by brute force over subsets, which is the same test as the student token rule.
  - **Loops.** It finds loops two ways, by a DFS over closed trails that repeat no edge and by listing connected even-degree edge sets. The two lists agree on every board.
  - **Holes.** It counts holes two ways, by the formula E−V+C−F and by a raster flood fill of the drawing that counts enclosed regions not covered by a tile. The two counts agree on every subcomplex of all three boards: 41, 81 and 433 subcomplexes.
  - **Problems.** It checks the following:
    - every schedule in Problems 2, 3 and 4, including legality, hole counts, the first loop and the stage at which it is gone;
    - a search over 8,400 random growing histories for a loop that comes back (Problem 5);
    - Problem 6: all 15 fan loops, the request with two tiles filled, all 6 pairs over all 24 fresh-board orders, and the private outside edge of each fan tile.
  - **Barcode intervals.** It computes them with its own Z/2 column reduction and checks the guide's adult-section intervals.
  - **Guide tables.** It reads the Problem 2, 3, 4 and 6 tables from the delivered guide with `pdftotext` and compares every row with the enumeration.
  - **Preparation arithmetic.** It checks the guide's figures: 11 token labels, 33 and 44 tokens, a maximum of 3 copies of one token needed at once, 16 sheets, 8 and 17 tiles, a diagonal of 8.77 cm and strips of 5.8 cm.
- **`check_diagrams.py`** (output `check_diagrams.py.out`: 32 checks, 0 failures)
  - It reads the delivered student PDF with PyMuPDF. It finds the vertex dots and names each dot after the nearest label. It then records which pairs of dots are joined by a solid or a dashed stroke, counting a solid stroke drawn over a dashed edge place as solid.
  - **Square boards.** The p. 1 square is all dashed. On pp. 2 and 4, AB, BC and CD are solid and DA and AC are dashed. There is no BD. The squares measure 6.2 × 6.2 cm with a 8.77 cm diagonal.
  - **Joined board, p. 3.** AC, BC, CD and CE are solid. AB and DE are dashed and measure 5.8 cm. The board is 11.6 cm wide.
  - **Fan, p. 5.** All 8 edges are solid. The square is 8 cm with O at its centre.
  - **Launch example, p. 1.** The XYZ example has a shaded triangle and the token row XY YZ → XY YZ XY YZ XZ → XZ.

## Problem by problem (all verified)

- **P1 (p. 1).**
  - The square has exactly three loops, P = ABC, Q = ACD and R = ABCD, with R = P + Q.
  - A single filling can kill P or Q. Only R survives either single filling, and both fillings kill it.
  - The guide's answer and its "only three loops" claim are correct.
- **P2 (p. 2).**
  - There are 4 schedules. All are legal, and all have holes 0, 1, 2, 1, 0 by both counts.
  - The first loop survives to stage 8 in exactly 3 of them: DA first with either tile order, and AC first with ACD at stage 5. The guide's table matches in every cell.
- **P3 (p. 3).** All 4 schedules give holes 0, 1, 2, 1, 0. The first loop is gone at 5, 8, 8, 5, in the order of the guide's table. So the answer is no, the counts alone do not tell when the first loop disappears.
- **P4 (p. 4).**
  - The printed schedule gives 0, 1, 1, 0 at stages 0, 2, 4, 8, so it never has 2 holes.
  - Moving AC to stage 3 or ABC to stage 5 is legal and produces 2 holes. Moving AC to stage 5 or ABC to stage 3 is illegal. R is gone at stage 8 in every case.
  - The intervals are as the guide states: the original has only [2, 8), and the two legal changes add [3, 4) or [4, 5).
- **P5 (p. 4).** The answer is no. The guide's argument (reuse the same cancelling selection of tiles) is a complete proof that does not depend on planarity. The random search found no counterexample.
- **P6 (p. 5).**
  - With ABO and BCO filled, exactly four loops meet the first request: L0–L3, with the edge lists and unique required tiles shown in the guide. They differ by boundaries of the filled tiles.
  - On the fresh board, L1 and L2 are the only pair in which each loop can disappear first. Each strict order occurs 6 times out of 24, and the loops tie 12 times. Both of the guide's orders and both orders in MATHEMATICS.md are correct.
- **Guide adult section.**
  - Fillings are unique because face boundaries are independent on all three boards.
  - The formulas E−V+C and E−V+C−F are correct.
  - The square intervals [b, max(u, v)) and [s, min(u, v)) for b < s ≤ min(u, v) are correct. I checked 5 parameter sets.
  - The joined-board intervals [2, 5), [4, 8) and [2, 8), [4, 5) are correct.

## Problems found

1. **Guide p. 1, "Counts versus history" (minor; the overview leaves out a hypothesis).**
   - **Text:** "Either one-tile filling leaves R nonzero; both kill it. Two triangles meeting at a single vertex can *instead* lose their older loop first. Problems 2 and 3 make this distinction explicit."
   - **What it implies:** that the divided square, unlike the joined board, never loses its older loop first.
   - **Evidence:** the guide's own Problem 2 table, row 3 (AC, DA, ABC, ACD), shows the square losing its older loop first. The older loop P is born at 2 and gone at 5, while a class born at 4 lasts to 8. The barcode is [2, 5), [4, 8), the same as the joined board's AB, DE, ABC, CDE schedule (`check_math.py.out`, Problem 2 and Problem 3 lines). The contrast holds only when R is the older loop (DA before AC). The adult section states that assumption (b < s), and MATHEMATICS.md states it ("If the triangular rim closes first … can kill the older class instead"), but the overview leaves it out.
   - **Fix:** "When R closes first (DA before AC), either one-tile filling leaves R nonzero; both kill it. When a triangle rim closes first, whether on the square or on two triangles meeting at a vertex, filling that triangle first kills the older loop. Problem 2 contains both histories; Problem 3 shows the second with identical counts."

2. **Student p. 3, Problem 3 board (minor; the diagram could be misread, though the mathematics is correct).**
   - **Text:** "Start with the four solid edges."
   - **Diagram:** A(0, 0), B(0, 5.8), C(5.8, 2.9), D(11.6, 0), E(11.6, 5.8) cm. A, C and E are collinear (cross product 0), and so are B, C and D. So the four solid edges print as two straight lines crossing at C. `check_diagrams.py` reads these back as solid "AE" and "BD" lines.
   - **Why it matters:** the dot and label at C make the board correct. But a child who names what they see ("line AE, line BD") counts two solid lines, not four edges, and has to split BC out of a straight line when saving AB, BC, AC.
   - **Fix:** put a visible bend at C while keeping DE = 5.8 cm, for example D = (11.6, 1.2) and E = (11.6, 7.0). Shift the board up about 1.2 cm, or move the answer lines down to make room. The guide's strip lengths stay valid.

The student pages are otherwise correct. Every other statement, solution, hint and extension in the guide checks out.
