# Week 93 (Squaring a rectangle): math check

Scope:
- `lowell-math-circle-year-2/week-93/week-93-students.pdf` (SHA-256 `9478fffa…6158`): one consolidated packet, 5 pages.
  - pp. 1–4, header "Grades 3–5": p. 1 shared rules and Problem 1; p. 2 Problem 2; p. 3 the reshaping move, its worked 1-by-3 example, and Problem 3; p. 4 Problems 4–5.
  - p. 5, header "Grades 4–5, ready for general reasoning": Problems 6–7.
- `week-93-facilitator.pdf` (SHA-256 `4cebc5f3…8d56`): 5 pages.

Sources read: `source/week-93/student/students.tex`, `guide/facilitator.tex`, `build.py`, `README.md`, `QA.md`, `SOURCES.md` and `PROVENANCE.md`. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-93/`. Each finds the repository through `repo_path.py`, four folders up from its committed location. Checked October 23, 2026.

**Result: every answer, diagram, card and guide statement is mathematically correct. I found 3 problems, all minor. Two are student-page wordings with a second reading that changes the answer (Problems 1 and 2). One is a guide notation clash: the letter d means b − a in the overview and (b − a)/2 in the Problem 6–7 solutions.**

## How it was checked

- **`check_math93.py`** (output `check_math93.out`, 0 failures). Exact `Fraction` arithmetic throughout.
  - **P1.** Lists every rectangle that uses all 24 tiles. Compares closeness by side difference, ratio and perimeter. Tests the guide's completeness argument and the fit on the 24-by-20 grid. Counts the rectangles under the other reading of "use 24 tiles".
  - **P2.** Searches every no-cut and one-straight-cut grid dissection of 6×2 into 4×4 and of 4×2 into 3×3, with every placement and rotation. Records which ones leave a single square hole. Replays the guide's two dissections cell by cell.
  - **P3, P4.** Applies the move to each case and card. Over all pairs of the four marked lengths, finds the narrowest pair that brackets √A, decided by squaring. Tests all 24 card orders.
  - **P5.** Squares the decimal endpoints exactly. Lists the hundredth-grid pairs that trap √12, and tests the guide's finer pair.
  - **P6.** Checks the guide's two-piece dissection with exact rectangle coordinates for 2,030 rational pairs a < b: containment, disjoint interiors, areas, and the corner hole of side (b − a)/2.
  - **P7 and the overview.** Runs 1,104 rational starts through 5 exact moves each. Checks area kept, strict nesting a < h < √A < m < b, the gap formula, gap < old gap/2, width < d/2ⁿ, and that sides never become equal. Also checks the 4×9 return-visit example, Newton's form, and the guide's return-visit question: for equal areas, a more square-like rectangle always gives a tighter next bracket.
- **`check_pdf93.py`** (output `check_pdf93.out`, 0 failures) measures the delivered PDF with PyMuPDF. It checks:
  - headers, footers, and Problems 1–7 numbered in order;
  - the p. 1 grid's cells and millimetre size;
  - each p. 2 outline against its letter and side labels, its scale in each direction, and its internal grid lines;
  - the p. 3 example's proportions, segment lengths and halving arrow, and the three number lines' ticks and labels;
  - the p. 4 card sizes, and the fractions read from inside each card;
  - the p. 5 proportions;
  - every guide sentence quoted below.
- **`rebuild_compare.py`** (output `rebuild_compare.out`). Rebuilds both PDFs from source into a temporary folder. The text is identical to the delivered PDFs, so the reviewed `.tex` is what is printed. The bytes differ only through the TeX version.
- All 10 pages were rendered with `pdftoppm -r 80` (`render/`) and inspected.

## Grades 3–5 (pp. 1–4): correct except items 1 and 2

- **P1** asks for every rectangle made from 24 tiles, and which is closest to a square. There are exactly four: 1×24, 2×12, 3×8 and 4×6. 4×6 is closest by difference, ratio and perimeter alike. The 7 mm grid is 24 × 20 cells (168 × 140 mm), and all four rectangles fit with long sides horizontal (stacked heights 1 + 2 + 3 + 4 = 10). See item 1.
- **P2** asks children to cut each rectangle and fit it into the matching square, leaving one square uncovered.
  - The diagrams are correct. All four outlines are 15.000 mm per unit both ways: A 90 × 30 mm with a 60 × 60 square, B 60 × 30 mm with a 45 × 45 square. Grid lines fall one per unit, and letters and side labels match the shapes. Each square's side is the average of its rectangle's sides (4 = (6 + 2)/2, 3 = (4 + 2)/2).
  - The answers are side 2 for A and side 1 for B. Area forces them: 16 − 12 = 4 and 9 − 8 = 1.
  - With one straight grid cut there are 16 placements for each case, all leaving a square hole of the forced side. Neither rectangle fits uncut.
  - See item 2.
- **Worked example (p. 3)** is correct and drawn to one scale. 1 × 3 → average (1 + 3)/2 = 2 → 3 ÷ 2 = 3/2, giving a 2 × 3/2 output of area 3. The joined segments measure 1 and 3 units and the halving arrow spans 2. The line's "20 ÷ 6 = 10/3" is correct; it is also the new short side of P3's third case, a design choice recorded in QA.md and not a correctness issue.
- **P3** asks for one move on each of 2×6, 3×6 and 2×10, then the tightest bracketing pair among the four lengths.
  - The moves give (3, 4), (4, 9/2) and (10/3, 6).
  - Over all pairs, the narrowest pair that brackets √A is the new pair each time: 9 < 12 < 16, 16 < 18 < 81/4, and 100/9 < 20 < 36.
  - The printed areas are right, every length lies on the 0–10 lines, and the ticks are equally spaced (16 mm).
- **P4** asks children to order the cards and pick the tightest.
  - All four cards have area 12, with the shorter side first. The PDF shows A 24/7 by 7/2, B 2 by 6, C 336/97 by 97/28 and D 3 by 4, on 70 × 20 mm cards.
  - The only follow relations are B→D, D→A and A→C, so B, D, A, C is the unique order.
  - The widths are 4, 1, 1/14 and 1/2716, so C is tightest. Its exact check is (336/97)² = 112896/9409 < 12 < 9409/784 = (97/28)².
- **P5** asks for two decimals one hundredth apart around √12.
  - 3.46² = 11.9716 < 12 < 12.0409 = 3.47². This is the only pair on the hundredth grid. Finer pairs such as 3.455 and 3.465 also qualify, and the guide accepts them.
  - "Could either decimal be the exact side?" — no. The strict area checks show it, and no terminating decimal squares to 12 (12·100ᵏ has an odd power of 3). C's range lies inside (3.46, 3.47).

### 1. p. 1 Problem 1 (minor): "use 24 square tiles" has a second reading that changes the answer

- **Quoted text:** "Use 24 square tiles to make every different rectangle you can. Draw your collection. Which rectangle comes closest to being a square?"
- **Evidence.** Nothing says each rectangle must use all 24 tiles.
  - Read as "with 24 tiles available", there are 44 rectangles a ≤ b with ab ≤ 24 (`check_math93.out`). They include the squares 1×1, 2×2, 3×3 and 4×4, so "closest to being a square" becomes trivially a square.
  - The guide's answer (four rectangles, 4×6 closest) and its completeness argument assume the all-24 reading.
  - The final question points toward that reading, and the usual classroom idiom supports it, so the risk is small.
- **Smallest fix:** "Use all 24 square tiles to make each different rectangle you can."

### 2. p. 2 Problem 2 (minor): "exactly one square uncovered" can mean one grid square

- **Quoted text:** "Can you leave exactly one square uncovered in each case? Find the side length of each uncovered square." The shared rule on p. 1 calls the cells "grid-square[s]", and square A is drawn with 16 grid cells.
- **Evidence.** If "one square" means one grid cell, A is impossible: 16 − 12 = 4 cells must stay uncovered, whatever the cut (`check_math93.out`). A child who answers "No for A, four squares are left; yes for B, side 1" is right under that reading. The guide expects "yes, side 2" for A. The follow-up question only partly disambiguates, since under the cell reading every uncovered square has side 1.
- **Smallest fix:** "Can the uncovered part be a single square, of any size, in each case? Find its side length."

## Grades 4–5 (p. 5): correct

- **P6.** Yes: the average-side square has area at least ab, with equality only for a square. The extra area is ((b − a)/2)². The guide's two-piece dissection was checked exactly on 2,030 pairs: an m-by-a piece across the bottom, and the d-by-a strip turned into the top row, leaving a d-square corner. The schematic rectangle is 7:3 and the square 5 × 5, so the pair is in fact in proportion. The "Diagrams not to scale" label is harmless.
- **P7.** Yes, the bracket can become as narrow as wanted: the new gap is (b − a)²/(2(a + b)), less than half the old one. No move produces the exact square, because the gap stays positive. This held exactly on every start tested, including area 36 from 4×9 (6 is strictly inside every bracket for 6 moves). From 2×6, the width is below 10⁻¹² after 5 moves. A 10-digit display shows equal sides after 5 moves, which illustrates the guide's warning about rounded displays.

## Facilitator guide: correct except item 3

- **Overview (p. 1).** Every stated fact is true, with the stated hypothesis of positive sides:
  - s = √A between a and b; hm = ab; a ≤ h ≤ s ≤ m ≤ b, strict for unequal sides;
  - m² − ab = ((b − a)/2)²;
  - d_new = (b − a)²/(2(a + b)) < d/2;
  - widths below d/2ⁿ after n moves, and no finite move gives a square, even for A = 36;
  - near equality, the new gap is roughly proportional to the square of the old gap.
- **Pp. 2–5.** The preparation numbers match the PDF: 7 mm cells; 90 × 30, 60 × 60, 60 × 30 and 45 × 45 mm at 15 mm/unit. Also correct:
  - the launch example;
  - the P1–P7 solutions, including P1's completeness argument and the P2 dissections;
  - the P3 table and checks, and the P4 means, widths and order;
  - the P5 uniqueness statement (unique only on the hundredth grid), the P6 dissection, and the P7 identity and argument;
  - every hint;
  - the return visits: 4×9 → 72/13, 13/2, and "the more square-like one always gives the tighter next bracket" is true for equal areas;
  - the Newton form x_next = (x + A/x)/2.

### 3. Guide p. 1 vs p. 4 (minor): the letter d means two different things

- **Quoted text.**
  - Overview, p. 1: "If d = b − a, then d_new = m − h = (b − a)²/(2(a + b)) < d/2 (a < b)" and "widths smaller than d/2ⁿ after n moves".
  - Problem 6, p. 4: "Put m = (a + b)/2 and d = (b − a)/2".
  - Problem 7, p. 4: "Using Problem 6, m − h = (m² − A)/m = d²/m = (b − a)²/(2(a + b)). Since b − a < a + b for positive sides, the new gap is less than half the old gap."
- **Evidence.** In the Problem 7 identity, d²/m is correct only with Problem 6's d = (b − a)/2. An adult carrying the overview's d = b − a into it gets a gap 4 times too large, and "less than half the old gap" then no longer follows from the displayed line. The end expressions are right, so this is a reading hazard, not a false claim (`check_pdf93.out` confirms both definitions in the source).
- **Smallest fix:** in Problem 7, write "Using Problem 6's d = (b − a)/2, half the old gap, m − h = …". Alternatively, rename the overview's gap g = b − a, with g_new and g/2ⁿ.
