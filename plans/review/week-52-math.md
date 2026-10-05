# Week 52 (hinged frames and braces): math check

Scope: `lowell-math-circle-year-2/week-52/week-52-students.pdf` (one combined packet, F52-S-v2, 12 pages, Problems 1–14). Pages 1–2 are headed K–1, pp. 3–4 Grades 2–3, pp. 5–9 Grades 3–5 and pp. 10–12 Grades 4–5. Also `week-52-facilitator.pdf` (F52-FAC-v2, 10 pages). I read the sources in `source/week-52/student/students.tex` and `source/week-52/guide/facilitator.tex` for the macros, scales and brace lists. I did not run or import the packet's `verify_math.py`, `audit_pdf_math.py` or `verify_guide.py`. My scripts and their outputs are in this folder. Checked October 5, 2026.

**Result: every answer, count, example and theorem in the student pages and the guide is correct under the packet's model: a complete square grid, fixed bar lengths, free pins, at most one brace per cell, motion in the plane. I found 3 problems on the student pages. One matters: Problem 13's answer depends on the one-brace-per-cell rule, which no page given to the upper group states. The other two are minor: the planar rule is printed only for K–1, and the page 1 triangle and square are drawn with different bar lengths. The guide has no mathematical errors. It has one garbled line of non-mathematical text.**

## How it was checked

- **`geom52.py`** uses PyMuPDF to read the delivered PDFs, not the TeX. It recovers every grid: its side bars, joint circles, braced cells with their orientation, and the R/C labels. It also recovers every link picture: which R/C dots exist and which links join them. It finds the repository by walking up to `AGENTS.md`, so it runs from `tmp/review-runs/week-52/` or from `plans/review/checks/week-52/`.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`) compares all 39 student diagrams (31 grids and 8 link pictures) and the 9 guide diagrams (2 grids and 7 link pictures) with my hand transcription from the renders, and with the designs that the text and answers refer to. Every grid has square cells: x and y spacing agree to under 0.05 pt. Every bar spans its grid, there is one joint per grid point, and all braces run lower-left to upper-right. Labels are centred on their strips, and every link picture has all its dots and exactly the intended links. The one FAIL it reports is Problem 3 below.
- **`check_math.py`** (output `out_check_math.txt`) decides rigidity without using the link-graph theorem. "Holds" is certified by exact rank 2V−3 of the rigidity matrix at the square placement, computed mod two 61/62-bit primes. Full rank mod p implies full rank over Q, so the frame is infinitesimally rigid and therefore rigid. "Flexes" is certified by an explicit finite motion: strip directions are turned in groups by different angles, and every joint is rebuilt. At four angle scales, all side bars and braces keep their lengths to 1e−12 while some cell diagonal changes. Every design is given one certificate or the other. The script enumerates:
  - every subset of the 2-by-2 and 2-by-3 grids;
  - all 84 six-cell sets of the 3-by-3;
  - all 77,520 seven-brace and 125,970 eight-brace designs of the 4-by-5;
  - every covering subset of the 4-by-4.

  On 1×1 through 3×4 grids (4,958 subsets) it checks that rank = 2(m+1)(n+1) − 2 − k for every subset, where k is the number of link groups. It also checks out-of-plane folding in 3-D and the guide's kit and printing arithmetic.

## K–1 (pp. 1–2): the mathematics checks out. See Problems 2 and 3 for the shared rules and the page 1 figure.

- **P1:** the equilateral triangle is rigid in the plane (rigidity rank 3 = 2·3−3). The square flexes through rhombi. The drawn triangle is equilateral (three sides of 113.39 pt), and the square has four equal sides at right angles.
- **P2:** one diagonal is the minimum. Either diagonal gives rank 5 = 2·4−3, and with no diagonal the square flexes. The two 50 mm boards are square.
- **P3:** the only four-bar shapes with opposite corners L√2 apart are the square and the degenerate placement with B=D, a doubled right isosceles triangle. I checked that the unbraced frame can reach the B=D placement: it passes through the flat placement where A, B=D and C lie on one line, keeping all four sides at length L. The guide's 60° rhombus diagonals of 60 and 103.92 mm are correct.

## Grades 2–3 (pp. 3–4): the mathematics checks out. The diagrams are correct.

- **P4:** A {11} flexes, B {11,22} flexes, C {11,12,21} holds and D (all four) holds. Circle C and D.
- **P5:** the minimum is 3. All four 3-cell sets hold, with every orientation choice; no 2-cell set holds. Four boards are printed for the four cell sets.

## Grades 3–5 (pp. 5–9): the mathematics checks out. The diagrams are correct.

- **P6:** the minimum is 4, with exactly 12 minimum cell sets. These are exactly the sets left after omitting any pair of cells except the two cells of one column. The guide's example 11,12,13,21 holds.
- **Page 6 worked example:** the 1-by-3 grid with its middle brace reads R1–C2, and C1 and C3 stay as dots. It is a non-task frame, and it flexes.
- **P7:** A {11,12,21,22} flexes because C3 is free; B {11,12,13,21} holds. Circle B only.
- **P8:** A {11,12,21,22,33} and B {11,12,13,21,31} both have a brace in every row and column. A flexes and B holds, so the answer is No. The guide's extension is true: each of A's four empty cells (13, 23, 31, 32) repairs it.
- **P9:** the design {11,12,13,21,22} holds. The removable single braces are 11, 12, 21 and 22; 13 is essential. The printed link picture is exactly R1–C1, R1–C2, R1–C3, R2–C1, R2–C2. After one permitted removal, every further single removal flexes, as the guide's extension says.
- **P10:** of the 15 pairs removed from the full 2-by-3, exactly 3 make it flex: 11/21, 12/22 and 13/23, the two cells of one column. The other 12 hold.
- **P11:** for A, no single added brace works. For B, exactly 13, 23, 31 and 32 work; 21 does not. A has 8 two-brace repairs, including the guide's 13+31.

## Grades 4–5 (pp. 10–12): the mathematics checks out under the one-brace-per-cell rule. See Problem 1.

- **P12:** the minimum for 4-by-5 is 8. All 77,520 seven-brace designs have an explicit finite flex. The guide's example 11,12,13,14,15,21,31,41 holds. Exactly 32,000 eight-brace designs hold, which equals the number of spanning trees of K₄,₅ (4⁴·5³).
- **P13:** Yes. Of the 84 six-cell sets, 78 cover every row and column, and all 78 hold. This assumes one brace per cell; see Problem 1.
- **P14:** No. The guide's nine-brace set 11,12,13,21,22,23,31,32,44 covers every row and column, and it flexes by an explicit motion. Among covering 4-by-4 designs, the numbers that flex are: 144 of the 9,696 with nine braces, 16 of the 7,480 with ten, and none with eleven or more.

## Problems found

### 1. Page 11, Problem 13: the answer "Yes" needs the one-brace-per-cell rule, which the upper packet never states

- **Quoted text:** "A 3-by-3 grid has six braces, with a brace in every row and column. Must it hold its shape? Explain."
- **Where the rule is printed:** the only printed rule is on p. 3, "In a grid, use at most one diagonal brace in each cell." That page is the Grades 2–3 page. The guide's print plan gives the upper trio pp. 5–9 and then pp. 10–12, never p. 3. No sentence on pp. 5–12 limits a cell to one brace. The guide states the dependency ("One brace per cell matters to this bound"), but the student page does not.
- **Evidence (`out_check_math.txt`, [P13]):** put both diagonals in cells 11, 22 and 33. That is six braces, with a brace in every row and every column. Its rigidity rank is 27 mod both primes, short of the 29 = 2·16−3 that rigidity needs. The explicit motion turns the three groups {R1,C1}, {R2,C2} and {R3,C3} by different angles, keeping all 24 side bars and all 6 braces at their lengths while unbraced cells change shape. A second example also flexes: 11, 12, 21 and 22, plus both diagonals of 33. If doubled braces are allowed, 321 of the 804 covering six-brace placements flex. Read literally, a child who doubles braces has a correct counterexample, and the answer "Yes" is then wrong.
- **Smallest fix:** in P13, write "A 3-by-3 grid has braces in six different cells, with a brace in every row and column." Alternatively, add "Use at most one brace in each cell." to the opening of p. 5, the first page of the upper packet, and to p. 10 if pp. 10–12 are used on their own. That can be combined with the opening suggested in Problem 2.

### 2. Pages 3–12 (minor): the planar, fixed-length rules are printed only on the K–1 page

- **Quoted text:** p. 1 opens "Keep the frames flat. Bars stay straight and keep their length; joints may turn. Sliding or turning the whole frame does not change its shape." No such sentence appears on pp. 3–12. The Grades 2–3 opening is only the one-per-cell rule, and the Grades 3–5 and 4–5 pages have no shared rules.
- **Evidence (`out_check_math.txt`, [planarity]):** every "holds its shape" answer on pp. 3–12 is a planar statement: P4 C/D, P5, P6, P7 B, P8 B, P9, P10, P11 B, P12 and P13. Lifted off the table, every grid with two or more columns folds along an interior grid line with all bar and brace lengths unchanged. My check folds the fully braced 2-by-3 along x = 1 and P8 B along x = 2. A braced square folds along its own brace. Under that reading every "Must it hold?" becomes No, and P12 has no answer. The guide's launch does say "Keep the bars straight and the frame on the table" aloud, so physical work is covered. The paper universal questions (P8, P13, P14) rest on that spoken rule alone.
- **Smallest fix:** repeat the p. 1 opening sentence, or a shorter "Keep the frames flat; moving the whole frame is not a change of shape.", at the top of p. 3 and p. 5. Add it to p. 10 too if pp. 10–12 are handed out separately on a return visit.

### 3. Page 1, Problem 1 (minor diagram): the triangle and square are drawn with different bar lengths

- **Diagram:** the triangle has sides of 113.39 pt (40.0 mm). The square has sides of 98.20 pt (34.6 mm), the triangle's height. That makes the triangle's bars 15.5% longer than the square's.
- **Evidence (`out_check_diagrams.txt`, [page 1]):** the guide's kit uses one side template for every side bar: "Each K–1 kit uses 7 side bars", each 60 mm hole to hole. So the triangle and square that children hold have equal bars, and the picture contradicts the objects. Equal bars matter here, because the comparison is that the same bars make a rigid triangle but a flexible square.
- **Smallest fix:** in `students.tex` p. 1, draw the square with 4 cm sides, replacing `3.4641` with `4` in its `rectangle` and in its corner list. It still fits the 0.46-linewidth column, about 84 mm wide. Alternatively, draw the triangle with 3.4641 cm sides.

## Adult guide: the mathematics checks out completely

- **Overview (p. 1):** each statement is true with the stated hypotheses. Infinitesimal rigidity holds exactly when the link graph is connected. There are k−1 nontrivial first-order motions, confirmed as rank 2V−2−k on all 4,958 subsets of every grid from 1×1 to 3×4, and by exact rational ranks for the printed P4B, P7A, P8A, P8B and handoff designs. The finite-motion argument is valid: near the square each cell stays on its parallelogram branch, so strip directions are shared and a brace forces perpendicularity. The disconnected construction is a real flex, and my certificates are exactly that construction, checked numerically. The minimum is m+n−1. The scope limits are right, and the remark about folding out of the plane is correct.
- **Proof page (p. 9):** u(i,j) = a_i and v(i,j) = b_j for the side bars. Either diagonal gives A_i + B_j = 0, which I also confirmed numerically: both diagonals of a cell span the same residual constraint. The rank formula 2(m+1)(n+1)−2−k is correct. In the finite argument, |H_j ± V_i| = L√2 ⇔ H_j·V_i = 0.
- **Keys:** P1–P14 all agree with my enumeration, including:
  - the 12 minimum 2-by-3 sets and their omit-a-pair rule;
  - the three P10 failing pairs;
  - the P11 group descriptions;
  - the P12 counting argument;
  - the P13 capacity bound (5 and 4 for two groups, 3 for three);
  - the 84/78/78 count;
  - the P14 counterexample, and the extension's 10/8/6/4 bounds: covering 4-by-4 designs flex with at most 10 braces, the ten-brace block plus 44 flexes, and 11 always hold.
- **Diagrams:** the handoff grid and links (11,12,23), the P7, P8 and P11 answer link pictures, and the P14 counterexample grid all match their text exactly.
- **Handoff:** the spare 2-by-3 with 11, 12, 23 covers every strip, has the two groups {R1,C1,C2} and {R2,C3}, and flexes; each empty cell (13, 21, 22) makes it hold. The P4B groups and repairs are also right.
- **Materials and printing:** the per-kit counts are correct (2-by-2: 12 sides, 4 braces, 9 pins; 2-by-3: 17, 6, 12; 3-by-3: 24, 9, 16), and so are the table totals 76/23/60 and 84/27/72. The diagonal spacing 60√2 = 84.853 mm and its total length of 100.853 mm are correct, as are the 16 student sheets and the 15 label tabs.
- **Non-mathematical slip (p. 2, first line):** "parent with KK11; … organizer with 445" should read "parent with K–1; … organizer with 4–5" (`facilitator.tex` line 53).
