# Week 57 (Area from dots / Pick's theorem): math check

Scope:
- `lowell-math-circle-year-2/week-57/week-57-students.pdf`: one combined packet, 10 pages, Problems 1–10. Pages 1–6 are headed Grades 3–5 and pp. 7–10 Grades 4–5.
- `week-57-facilitator.pdf`: 10 pages (`W57-FAC-v1`).

Sources read: `source/week-57/student/` (`students.tex`, `assets/polygons.json`, `generate_figures.py`, README) and `source/week-57/guide/facilitator.tex`. I did not run or import `verify_math.py`, `verify_pdf.py` or the guide's `verify.py`. My scripts and their outputs are in [checks/week-57/](checks/week-57/). Checked October 10, 2026.

**Result: every figure, record, witness, count and proof step in the student packet and the guide is correct, and every diagram is drawn at the coordinates the guide states. I found 1 problem, a minor one: the guide's overview (p. 1) lists "several shared sides" among the joins for which the joining claim fails. A seam made of consecutive sides still works, and the guide's own key for the P8 pentagon is a two-side seam of this kind.**

## How it was checked

- **`lattice57.py`** holds exact lattice tools written for this review. It classifies dots as inside, boundary or outside with integer arithmetic and finds I and B by visiting every dot. It computes area twice: by shoelace, and separately by clipping the polygon to every unit cell. It also tests whether a polygon is simple and whether two polygons meet exactly along a given segment.
- **`pdfgeom57.py`** is a standard-library reader for the delivered PDFs' content streams. It reads dots, outlines (by their stroke colour), dashed seams, the counting panel's circles and boxes, and shaded and white fills.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`, 177 checks, 0 failures) rebuilds every student diagram from the PDF:
  - It checks that all 20 dot boards are full rectangles with 20.000 mm spacing in both axes. The sizes are 40×20, 40×40, 80×80, 80×60, 120×120 and 120×60 mm, and the 80 mm, 120 mm and 120×60 mm boards are the sizes the guide's p. 2 states.
  - It converts every outline vertex and seam endpoint to dots, compares the result with the guide's coordinates, and recomputes (I, B, A) from the read-back shape.
  - On p. 2 it checks that the circles mark exactly the 8 boundary dots and the box marks exactly the inside dot.
  - On p. 9 it checks that the white fill is exactly the hole.
  - It also checks the guide's p. 8 compact figure: the outline is A(0,0) B(2,1) C(6,6) D(2,6), and the dashed lines are AC and BD.
- **`check_math.py`** (output `out_check_math.txt`, 107 checks, 0 failures):
  - It recomputes every record and dot list in the guide's keys and checks the P1 wedge dissection on a fine grid of sample points.
  - It enumerates every triangle and quadrilateral with (I, B) = (2, 6) on P3's 5×5-dot board, and every area-6 triangle and quadrilateral on P5's 7×7-dot board.
  - It tests the joining formulas on 1,224 random one-segment joins, 4,455 joins on part of a side, and 3,107 bent two-side joins.
  - It tests proof Steps 1–5 directly:
    - every horizontal-base triangle and its attachment order (Step 3);
    - all 2,148 triangles on a 5×5-dot board and all 6,768 on a 6×6-dot board through the guide's Step 4 routing;
    - ears of 1,395 random simple polygons (Step 5).
  - It tests the h-hole rule on 400 random regions.
  - It reads the delivered guide with `pdftotext` and compares its printed numbers.

## Grades 3–5 (pp. 1–6): checks out

- **p. 1 panel:** the triangle (0,0),(2,0),(0,1) and its copy meet exactly along the dashed diagonal. The rectangle's area is 2 and each copy's is 1, as printed.
- **P1:** both areas are 6. The rectangle is 3×2. The parallelogram (0,0),(2,0),(3,3),(1,3) has base 2 and height 3. The guide's wedge (0,0),(1,0),(1,3), moved 2 to the right, turns it into [1,3]×[0,3].
- **p. 2 panel:** the 2×2 square gives I = 1, B = 8, area 4. The marks are on exactly the right dots.
- **P2:** the L-shape is (0,12,5), with all 12 dots on its outline. The triangle (0,0),(3,0),(1,3) is (3,5,9/2), with inside dots (1,1),(1,2),(2,1). Two copies joined on either sloping side make a base-3, height-3 parallelogram of area 9.
- **P3:** on the 5×5-dot board, 28 triangles and 780 four-sided shapes have I = 2, B = 6, and all have area 4. Both guide witnesses are right, including their inside and boundary dots. The guide's hint 3 starts are possible: with a horizontal base of four intervals the apex is (1,2) or (3,2), and a base of two intervals allows a parallelogram.
- **P4:** the records children hold by this point are (1,8,4), (0,12,5), (3,5,9/2) and (2,6,4). Any three of them already force area = I + B/2 − 1 among linear rules, so "use all your records" can succeed. "Area is half of B" fails on the unit square and on the L, as the guide says.
- **P5:** the area-6 records found on the 7×7-dot board are exactly (0,14), (1,12), (2,10), (3,8), (4,6), (5,4). That matches the guide's complete list and its argument (B = 14 − 2I is even and at least 4). All six witnesses are simple, fit 0..6 and have the stated records. The (5,4) parallelogram's strip widths really are 6y/5, then 6/5, then 6(6 − y)/5.
- **P6:** the rectangle pieces are (1,8,4) and (1,8,4), with whole (3,12,8) and k = 3. The slanted pieces are (1,6,3) and (1,6,3), with whole (4,6,6) and k = 4. Each pair meets exactly along its dashed seam.

## Grades 4–5 (pp. 7–10): checks out

- **P7:** I = I₁ + I₂ + k − 2 and B = B₁ + B₂ − 2k + 2 held in every random legal join, and both seam endpoints always stay on the boundary. They also hold when the shared side is a whole side of only one piece (a triangle on part of a rectangle side), so either reading of "one whole side" works. The guide's k = 2 example is (0,4,1) + (0,4,1) → (0,6,2).
- **P8:** the triangle (0,0),(4,1),(1,3) is (5,3,11/2), with exactly the five inside dots listed. Its complements in the 4×3 box are 2, 3 and 3/2. The pentagon is (5,12,10), with (2,2) on the boundary and a notch of area 2.
- **P9:** the ring is (0,24,12). The old expression gives 11, and the one-hole rule is A = I + B/2.
- **P10:** a two-hole shape fits the 7×7-dot board. The rule A = I + B/2 − 1 + h held in all 400 random regions, together with the guide's subtraction identities. Holes that touch break it (holes meeting at one corner give 29/2 against an area of 14), so the page's rule that loops "stay separate" is needed and enough.

## Adult guide: all keys, witnesses and proof steps check out; one overview limit is wrong (Problem 1)

- **Overview (p. 1):** the theorem, the definitions of I and B, the area convention, the joining formulas and the h-hole formula are all correct, with the right hypotheses. The exception is the list of failing cases (Problem 1 below).
- **Preparation (p. 2):** the totals are right: 51 and 25 sheets, 120 raw squares giving 60 squares and 120 halves, kit totals 6/12/6/12, and board sizes as printed.
- **Keys:** every key on pp. 4–9 matches my enumeration, including the P9 second test (6,22,17) and the P10 witness (7,28,22).
- **Proof of Pick's theorem (pp. 7–8):** it is complete and correct.
  - Step 1 holds for all rectangles with sides up to 8.
  - In Step 2, the half-turn swaps the two halves and they meet exactly on the diagonal.
  - In Step 3, every horizontal-base triangle has at most two axis-right complement pieces, and each attachment meets the growing shape in exactly one full side. The stated order (small wedge first) is legal, but so is the reverse.
  - In Step 4, D is always a lattice point on the opposite side of AC from B, ABCD is convex, and ABD, BCD and ACD each have an axis side. Both joins are legal, and Q equals area, for every bridged triangle. The example table (0,8,3), (7,12,12), (2,8,5), (6,10,10), (12,8,15) is right.
  - In Step 5, every random polygon had an ear whose diagonal is a legal join.

### 1. Guide p. 1, "The joining invariant" (minor): "several shared sides" are listed as a case where Q-additivity fails, but a seam of consecutive sides obeys the same formulas

- **Quoted text:** guide p. 1: "Point contacts, several shared sides, overlaps, pinches and closed seams do not satisfy this claim."
  - Guide p. 8 adds, of its own proof: "no bent seam is passed off as one side".
- **Evidence:** suppose two simple polygons with disjoint interiors meet in one connected path of consecutive sides. Every seam dot except the two ends becomes inside, and the two ends stay on the boundary, for the same reason as with one side. So I = I₁ + I₂ + k − 2, B = B₁ + B₂ − 2k + 2 and Q = Q₁ + Q₂, with k counting every dot on the whole path.
  - The guide's own P8 key, "A 4×3 rectangle minus its top notch", is such a join. The notch (0,3),(4,3),(2,2) is (0,6,2) and meets the pentagon (5,12,10) along the two sides (0,3)–(2,2)–(4,3), so k = 3.
  - Then I = 5 + 0 + 1 = 6, B = 12 + 6 − 6 + 2 = 14 and Q = 10 + 2 = 12, which is the rectangle's (6,14,12).
  - `check_math.py` confirms the formulas on 3,107 random two-side seams.
  - Only contact in separate places breaks them. The guide's other examples do: a point contact gives Q = 5/2 for area 2, and two separate shared pieces enclose a hole.
  - As printed, an adult could tell a child that the natural rectangle-minus-notch explanation of the P8 pentagon, or a seam that bends, "does not satisfy" the joining result. In fact it is correct.
- **Smallest fix:** change the sentence to: "Point contacts, contact in two or more separate places, overlaps, pinches and closed seams do not satisfy this claim. A seam made of several consecutive sides does, with k counting every dot on it; P7 needs only one side." Optionally drop "and no bent seam is passed off as one side" on p. 8, or change it to "and every join used is along one side". The student README's "Mathematical facts" paragraph has the same "several shared sides ... need different bookkeeping" wording and should be changed to match.

## Not problems (checked so they need not be re-raised)

- The student README says the 2,148 triangles on a 5×5-dot board split into 1,600 with an axis side and 548 without. That is true. The guide's Step 4 tests only for a vertical side or A_y = C_y, so it sends 948 triangles through the bridge, including some that have a horizontal side AB or BC. The bridge is valid for all of them (0 failures). The guide prints only "2,148", which is correct.
- The (5,4) record in P5 also comes from simple triangles such as (0,0),(2,0),(1,6) or (0,0),(0,2),(6,1), whose base-and-height area children can check. The guide's slender parallelogram is correct, just harder to check.
