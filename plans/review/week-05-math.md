# Week 5 (Tower cities): math check

Scope: `lowell-math-circle-year-2/week-05/week-05-k-1.pdf` (F05-K-v4, 7 pp., Problems 1–7), `week-05-grades-2-3.pdf` (F05-M-v4, 9 pp., Problems 1–7), `week-05-grades-4-5.pdf` (F05-U-v4, 8 pp., Problems 1–9) and the adult guide `week-05-facilitator.pdf` (F05-FAC-v4, 9 pp.). Sources read for data: `source/week-05/src/` (`k-1.tex`, `grades-2-3.tex`, `grades-4-5.tex`) and `guide-src/facilitator.tex`. I did not use the packet's `towers.py`, `grader.py`, `check.py` or their reports. The return visit (`week-05-return-visit.pdf`, F05-RV-v1, 3 pp., with `week-05-return-visit-facilitator.pdf`, F05-RV-FAC-v1, 4 pp.) is a companion and got a brief check (last section). Archive folders were not checked. pdfLaTeX is not installed here, so I did not test a clean rebuild. Checked October 10, 2026.

**Result: every printed puzzle, card and picture is right, and every answer, count, list and argument in the guide checks out, including its computer counts (156, 1600, 40, 66, 204, 262, 152) and its "passes" note. I found five located problems in the main packet. One matters in use: in 4–5 Problem 5 about a third of the cities a child can build (204 of 576, among them Problem 4's cities A and D) cannot be made into a one-city puzzle at all, and the guide's Problem 5 entry does not say so (item 1). The other four are small guide slips (items 2–5). The companion has one slip in a proof (item 6).**

## How it was checked

All scripts are in the run folder and find the repository from their own location.
- `extract_pdf.py` reads the final PDFs' vector drawings with pdfplumber. It finds every grid frame and measures it (n, square size, equal spacing). It reads every edge number by its position beside a row or column, every card's two numbers, every tower picture from its cube rectangles, and every solved grid in the guide (black heights, grey edge numbers). It writes `pdf_data.json` and the dump `extract_pdf.out`.
- `check_week05.py` (output `check_week05.out`, 124 checks, 0 mismatches) recomputes everything without the packet's code. It works through every row of 1–7 towers, all 12 and 576 Latin squares (and counts the 161 280 of order 5), and every set of one, two and three edge places. It solves each printed puzzle against the numbers read from the PDF and compares the solution with the guide's grid. It recomputes the guide's lists, which I transcribed by hand: card rows, added-number lists, the Problem 7 table and counts. It also runs a line-at-a-time solver for the 4–5 "passes" note.
- `source_vs_pdf.py`: the edge numbers and card numbers in the `.tex` sources are the ones the PDFs print (0 differences).
- `guide_towers.py`: the guide's small tower pictures match their labels.
- `geometry.py`: side-view sight lines for the "eye at the table, a foot away" rule and the guide's evening test.
- `edge_cases.py`: cities no puzzle can single out, the K–1 Problem 4 hint, and the average number seen.
- `check_return_visit.py`: the companion.
- `renders/` holds page images I looked at. They are scratch and not needed for the report.

Rows are written left to right (132 = 1-, 3-, 2-cube towers), (L, R) = numbers seen from the left and right ends, cities by rows top to bottom (123/231/312).

## K–1: checks out completely

- **Page 1 picture and P1:** the eye picture is 1, 3, 2 (2 seen from the eye). P1 rows 132 → (2, 2) and 321 → (1, 3).
- **P2:** 6 rows, 8 frames.
- **P3:** cards 1-3 → 321; 2-1 → 213; 2-2 → 132 or 231; 1-2 → 312; 3-3 and 1-1 impossible.
- **P4:** the dashed hidden row is 231 (2, 2). A hider can say (1, 2), (1, 3), (2, 1), (2, 2), (3, 1).
- **P5:** the 6 rows starting with 4 (8 frames).
- **P6:** 6 rows (1423, 2413, 3412, 2143, 3142, 3241), 8 frames.
- **P7:** 2-3 → 1432/2431/3421; 1-4 → 4321; 3-1 → 1324/2134/2314; 1-2 → 4123/4213; 3-3 and 4-2 impossible (L + R ≤ 5).
- A pair's two 1-2-3 sets make 1, 2, 3, 4 with 10 of their 12 cubes.

## Grades 2–3: checks out completely

- **P1:** six rows; never (1,1), (3,3), (2,3), (3,2). 8 slots.
- **P2:** 12 cities, 18 cubes each; 1-inch squares (72.0 pt) on every large grid, pp. 2–7.
- **P3:** puzzle 1 → 231/312/123, puzzle 2 → 213/321/132, puzzle 3 (2, 2, 2 above) → no city, puzzle 4 → 123/231/312. Each of the others has exactly one city.
- **P4:** the 1 above column 1 and the 2 left of row 3 fit exactly 3 cities (6 small grids). The guide's full list of single added numbers that leave each city is exactly right.
- **P5:** no one-number puzzle has one city; 156 two-number puzzles do. Every one of the 12 cities can be fixed by two of its own numbers.
- **P6:** 12, with 15 grids printed.
- **P7:** every city totals 22. A line's two numbers add to 3 exactly when its middle is 1.

## Grades 4–5: every answer is right; Problem 5 has the gap in item 1

- **P1:** the eight cards: (1,2) 2 rows, (2,3) 3, (3,3) none, (2,2) 6, (1,4) 1, (1,1) none, (3,2) 3, (4,2) none.
- **P2:** 576 cities, 40 cubes each.
- **P3:** A–F carry 12, 8, 6, 6, 5 and 4 numbers. Each has exactly one city, equal to the guide's grid, and the guide's grey numbers equal the page's. The note "A–C two passes, D three, E five, F seven" matches a solver that goes through the rows and columns in turn and uses each line's deductions at once (2, 2, 2, 3, 5, 7).
- **P4:** 4 cities (6 small grids). Only B and C can be singled out, by exactly the guide's eight numbers. A and D have identical sixteen numbers.
- **P5–P6:** no two-number puzzle has one city; 1600 three-number puzzles do; 40 of them use no 4, and 16 of those are all 3s. Both guide examples have exactly one city.
- **P7:** the table is right.
- **P8:** 24 and 50, split 24 + 12 + 8 + 6 by first tower.
- **P9:** yes. 66 shared sets cover 204 cities and 262 pairs, and 152 of those pairs differ by one 2-by-2 switch.
- Grid squares on pp. 3–8 are 1.0–1.7 cm, smaller than a 1.905 cm cube, as the guide says.

## Adult guide

Everything not listed below checks out:
- the launch numbers;
- the materials arithmetic (12/36/48 = 96 towers; 24 + 72 + 120 = 216 cubes, 242 with spares; 10 folders);
- every answer, "Why", "Starts" claim and hint (for example, 2–3 puzzle 4's bottom cell of column 2 must be 1, and C's column-2 4 is in row 2);
- the fallback "two can be enough";
- the overview in section 5: L + R ≤ n + 1, with equality for the 2^(n−1) rise-then-fall rows; the Stirling recurrence and rows; the (a, b) formula C(a+b−2, a−1)·c(n−1, a+b−2), checked for every (a, b) up to n = 7; the Latin-square counts; the 22 total; the twelve distinct 3-by-3 edge sets; and fewest numbers 2 and 3.

The evening test is consistent with geometry (`geometry.py`). With the eye at table level, the 4 in 3, 1, 2, 4 shows over the 3 only beyond 9 inches. At a foot, every row of three and four gives the rule's count for eye heights 0–3.5 inches, on a 1-inch grid or with towers touching. The thinnest strip that must be seen is 0.18 inches (eye on the table, 4 behind 3).

### 1. Many 4-by-4 hidden cities cannot be made into a one-city puzzle (4–5 Problem 5, p. 6; guide p. 7)

- **Quoted text:**
  - Student p. 6: "Write some of its numbers around an empty grid so that your city is the only one that fits, using as few numbers as you can. Your partner solves the puzzle and then tries to find a second city that fits the same numbers."
  - Guide p. 7: "Fewest: 3. … The solver hunts for a second city; the referee settles it by building." Hint (1): "Problem 4 had two numbers and four cities. Add one number."
- **Evidence** (`edge_cases.out`):
  - 204 of the 576 cities share all sixteen edge numbers with another city, so for them no set of numbers fits only that city, however many are written.
  - They include Problem 4's A (1234/2143/3412/4321) and D (1234/2413/3142/4321), which the children have just built. Two of Problem 4's four cities are like this, and 4 of the 24 cities that start with the guide's suggested top row 1234.
  - A pair whose hidden city is one of these keeps finding a second city and cannot finish the task. For A or D, hint (1) leads nowhere.
  - The guide gives the 204 only under Problem 9 and in section 5, not where an adult running Problem 5 would look.
  - In 3-by-3 every city can be fixed (by two numbers), so 2–3 Problem 5 has no such case.
- **Smallest fix:** add to the guide's Problem 5 answer: "About a third of cities (204 of 576, including Problem 4's A and D) share all sixteen numbers with another city, so no puzzle can single them out. If the solver finds a second city even with all sixteen numbers written, the builder has made no mistake: that is Problem 9. Keep both cities and build a new hidden one." In hint (1), add "(this works for B or C, not A or D)". The student page can stay as it is, so Problem 9 keeps its discovery.

### 2. The K–1 Problem 4 hint points to a card that does not exist for "3 and 1" (guide p. 4)

- **Quoted text:** "Hints (1) … (2) 'Find the card in Problem 3 with these numbers.'"
- **Evidence** (`edge_cases.out`): a hider can say (1,2), (1,3), (2,1), (2,2) or (3,1). Problem 3's cards are 1-3, 2-1, 3-3, 2-2, 1-1 and 1-2, with no 3-and-1 card, so the hint fails for the row 123.
- **Smallest fix:** "(2) 'Find these numbers on your Problem 2 page.'" (that page holds all six rows), or add "(for 3 and 1, turn the 1-and-3 card round)".

### 3. "From each end" across a folder can reverse left and right (K–1 Problem 4, p. 4; guide launch step 4, p. 2)

- **Quoted text:** "One partner hides a row of three towers behind a folder and says how many towers you can see from each end. The other builds a row that shows those numbers…"
- **Evidence:** if the partners face each other across the folder, the hider's left end is the builder's right end. A builder who hears "2 and 1" and builds 213 has built the mirror of the hider's 312 (seen from the builder's side). When the folder is lifted, the two rows show the numbers at opposite ends, and a right row looks wrong. This affects every pair except 2 and 2.
- **Smallest fix:** in the guide (Problem 4 and launch step 4): "The hider points to each end as they say its number, and the builder writes that number in the circle at the same end." Or seat partners side by side.

### 4. "≈ ln n" understates the average number seen (guide section 5, p. 8)

- **Quoted text:** "so on average 1 + 1/2 + · · · + 1/n ≈ ln n towers are seen."
- **Evidence:** H_n − ln n decreases toward 0.577 but never reaches it. The averages are H_3 = 1.83, H_4 = 2.08 (= 50/24 from the Problem 7 table) and H_5 = 2.28. The logarithms are ln 3 = 1.10, ln 4 = 1.39 and ln 5 = 1.61. An adult who checks against the packet's own table finds a 50% gap.
- **Smallest fix:** "≈ ln n + 0.58 (25/12 ≈ 2.08 for n = 4)".

### 5. "Fewer numbers each time" (guide p. 1)

- **Quoted text:** "The children climb the ladder of puzzles (fewer numbers each time)."
- **Evidence:** the ladder carries 12, 8, 6, 6, 5 and 4 numbers, so C and D both have 6.
- **Smallest fix:** "(fewer numbers as they go)".

## Return visit (companion, brief check)

Every count and example in the companion guide is right (`check_return_visit.out`):
- **Four-cell trades:** no 3-by-3 city has an alternating rectangle. Of the 4-by-4 cities, 432 have 4 trades and 144 have 12. City A's four are exactly rows 1,3 or 2,4 with columns 1,3 or 2,4; B has 12 and C has 0. Every exactly-four-cell change of a 4-by-4 city is such a trade. Distinct cities differ in at least 6 cells (order 3) or 4 cells (order 4). The before/after example is a city.
- **Diagonals:** no 3-by-3 city has both diagonals; 48 of the 576 4-by-4 cities do. The example's diagonals read 1,4,2,3 and 4,1,3,2.
- **Roof routes:** the peaks of D and E are as listed. The peak histograms are 3:8, 4:4 (order 3) and 4:226, 5:136, 6:172, 7:8, 8:34 (order 4). Both order-4 examples are right.
- **Pages and materials:** 25 mm working boards and 10–11 mm records; 200/112/156 cubes. On the 2-by-2 key, the dashed diagonal reads 2, 2 and the dotted one 1, 1.

### 6. A step in the order-3 diagonal proof is backwards (return-visit guide p. 3)

- **Quoted text:** "The top two corners must differ because they share a row, so they are a, b. The bottom corners are forced to be b, a."
- **Evidence:** with top-left a and top-right b, the main diagonal forces bottom-right = b and the other diagonal forces bottom-left = a. The bottom corners therefore read a, b, left to right, in every filling (enumerated). The conclusion still holds, and sooner than the text says: columns 1 and 3 already repeat a height.
- **Smallest fix:** "The bottom corners are forced to be a, b: each repeats the corner above it, so the first and last columns already repeat a height."
