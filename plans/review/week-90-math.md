# Week 90 (Sliding number arrays): math check

Scope:
- `lowell-math-circle-year-2/week-90/week-90-students.pdf`: one shared Grades 2–5 packet, 8 pages, Problems 1–9.
  - p. 1: rules, a three-state worked example and Problem 1.
  - p. 2: Problem 2.
  - p. 3: the rules for several gray squares, a four-state example and Problem 3.
  - pp. 4–6: Problems 4, 5 and 6.
  - p. 7: the undo rules, a four-state example and Problem 7.
  - p. 8: Problems 8 and 9.
- `week-90-materials.pdf`: 11 pages.
  - pp. 1–4: the A, B and D boards and the 2×2 demonstration board.
  - p. 5: pieces.
  - pp. 6–10: the A, D and B cards.
  - p. 11: blank group cards.
- `week-90-facilitator.pdf`: 9 pages.

The delivered PDFs are byte-identical to `source/week-90/reference-pdfs/`.

Sources read: `source/week-90/student/students.tex`, `student/materials.tex`, `guide/facilitator.tex`, `build.py`, `README.md`, `QA.md` and `SOURCES.md`. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-90/`. Checked October 23, 2026.

Notation: rows are separated by a slash, so 13/2 means a top row 1, 3 and a second row 2. Cells are written (row, column), counting from 1 at the top left, as in the guide.

**Result: the student packet and the materials are mathematically correct throughout. Every card, worked example, target diagram, intended answer and count checks out. The guide's overview, tables and proofs are also correct, apart from 2 minor problems:**
1. **A Problem 7 hint describes a situation that cannot happen. Together with the overview, it treats the start marker S as necessary, but the exit E alone determines the undo.**
2. **Problem 3 calls the D labels' diagonal "descending", and never says that its table reads that diagonal from top right to bottom left.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures), standard library only:
  - **Parsing.** Reads every grid on every student and materials page straight from the TikZ coordinates in the sources: labels, white, gray, dark, ring, and the S and E markers. Each grid is named by the card title printed above it.
  - **Cards.** Every copy of a card on the student pages matches its materials card. The A, D and B cards each share one gray and one outer Young diagram, and every card is increasing. Each family is exactly the set of all increasing fillings of its skew shape: 5, 6 and 16.
  - **Sliding.** I wrote ordinary jeu de taquin from scratch: the smaller right/below neighbour moves in, the exit is removed, and the gray corners are those with no gray square to the right or below. For every card it runs every legal order of corners to the end, then compares the outlines and labelled results. It checks the guide's tables for Problems 1–2, 3, 5, 6, 7 and 8, the three Problem 4 witnesses (text and drawings), and the preimage counts.
  - **Worked examples and diagrams.** Replays the worked examples on pp. 1, 3 and 7 state by state from the drawn grids. Reads the Problem 4 target outlines and the Problem 6 targets from the drawing and compares them with what B and D can actually reach.
  - **Undoing slides.** Undoes every single slide with the larger up/left rule, once stopping at S and once stopping naturally, when no label lies above or to the left. This covers the cards and all 37,320 slides of the 19,963 standard skew tableaux in a 4×4 box with at most 7 cells. The same family is a regression test of the order-independence theorem against my implementation.
  - **Counting arguments.** Recomputes the guide's sub-cases for 5 (A) and 16 (B), and the B comparison list.
- **`check_scale.py`** (output `check_scale.py.out`) measures squares in the delivered PDFs with PyMuPDF:
  - pages are US Letter;
  - task diagrams use 14 mm squares;
  - board cells are 30.0 mm;
  - pieces are 26.0 mm.
  All squares have equal width and height.
- **Quotes.** Every guide sentence quoted below was confirmed with `pdftotext`.

## Student packet, Grades 2–5 (pp. 1–8): checks out completely

- **Rules and example (p. 1).** The start, with the ring top left, 2 top right, 1 bottom left and 3 bottom right, is increasing. Then 1 (smaller than 2) slides up, 3 slides left, and the exit is (2,2), giving 12/3. All three drawn states match.
- **P1.** A1 gives 12/34, outline (2,2). A3 gives 134/2 and A5 gives 124/3, both outline (3,1). The intended answer is "A3 and A5", with different labels. The 2×3 recording grids fit both outlines.
- **P2.** The A shape (3,2)/(1) has exactly 5 increasing fillings, A1–A5, so no start is missing. Sorted by outline: (2,2) is A1 and A2; (3,1) is A3, A4 and A5.
- **Rules for several gray squares, and the example (p. 3).** The outer shape is (3,2) and the missing shape (2,1), with 1 at (1,3) and 2 at (2,2). The ring sits on a legal corner, (2,1). Then 2 slides left and the exit is (2,2). Afterwards the only legal corner is (1,2), since (1,1) has gray to its right, and the unchosen gray square stays. All four drawn states match.
- **P3.**
  - The D shape is (3,2,1)/(2,1). Its labels sit at (1,3), (2,2) and (3,1), all in different rows and columns, so all 6 orders are increasing; these are D1–D6.
  - There are exactly two legal corner orders: (1,2), (2,1), (1,1), and (2,1), (1,2), (1,1).
  - For each card both orders give the same labelled result: D1 1/2/3, D2 13/2, D3 12/3, D4 12/3, D5 13/2, D6 123. So the intended answer, "no", is right.
- **P4.** The 16 B starts reach exactly the outlines (3,2), (3,1,1) and (2,2,1). These are exactly the three outlines drawn, read from their coordinates, so every target is reachable (for example B8, B3 and B1), and none is impossible.
- **P5.**
  - B1–B16 are exactly the 16 increasing fillings of (3,3,2)/(2,1).
  - Each has two legal first corners, and both give the same labelled result.
  - The outline groups have 5, 6 and 5 cards.
  - The B1, B8 and B16 drawings match their cards.
- **P6.**
  - D preimages: 13/2 comes from D2 and D5, 12/3 from D3 and D4, 1/2/3 from D1, and 123 from D6. The four drawn targets are exactly these four results, so a finished arrangement does not always reveal the start.
  - B: all 16 labelled results are different. In fact each standard tableau of shapes (3,2), (3,1,1) and (2,2,1) appears exactly once. So the answer to the last question is "no".
- **Undo rules and example (p. 7).** Start from 12/3, with E at (2,2) and S at (1,1). Then 3 moves right (3 > 2) and 1 moves down, stopping at S. This restores the p. 1 start exactly. All drawn states match.
- **P7.** Each undo restores the card exactly, so the answer is "yes".

  | Start | S | E | Forward labels | Reverse labels |
  |---|---|---|---|---|
  | A2 | (1,1) | (1,3) | 1, 3 | 3, 1 |
  | A4 | (1,1) | (2,2) | 1, 4 | 4, 1 |
  | B4, upper corner | (1,2) | (2,3) | 1, 4 | 4, 1 |
  | B4, lower corner | (2,1) | (3,2) | 2, 5 | 5, 2 |
- **P8.** With the larger-neighbour rule, A1 gives 312/4, A2 213/4, A3 214/3, A4 243/1 and A5 24/13. None is increasing, so every A start fails and none still increases.
- **P9.** Losing a label, breaking the order and an endless slide are all impossible. The guide's proofs are checked below, and the regression family agrees.

## Materials (pp. 1–11): checks out completely

- **Boards.** The white cells on the boards are exactly the cards' outer shapes: A (3,2), B (3,3,2), D (3,2,1), and the 2×2 board for the pp. 1 and 7 examples.
- **Cards.** A1–A5, D1–D6 and B1–B16 each appear once, each is increasing, and each family is complete.
- **Pieces.**
  - Three gray pieces are the most any card needs (D and B).
  - Eight dark pieces comfortably cover the at most 3 new exits in a run.
  - The five number tiles cover B's labels.
- **Group cards.** The 3×3 blank group cards hold every finished outline that occurs.

## Adult guide (9 pp.): correct except items 1 and 2

- **Overview (p. 1).** Every stated fact is true, with the right hypotheses:
  - Legal corners are the gray cells with no gray right or below.
  - A slide preserves the labels and the increasing order, ends, and removes one inner and one outer cell.
  - The first fundamental theorem is stated for full labelled tableaux, with its scope limited to ordinary distinct labels.
  - Finite catalogs prove only their finite families.
  - A final tableau need not determine its start.

  The undo statement is true but has an unnecessary hypothesis; see item 1.
- **Tables and solutions.**
  - The tables for A (p. 3), D (p. 4), B with its outline groups (p. 6), the Problem 6 preimages and Problem 7 (p. 7), and Problem 8 with its violated comparisons (p. 8) all match my computation exactly.
  - So do the Problem 4 witnesses and their drawings (p. 5), the p. 3 demonstration check, and the launch example (p. 2).
- **Counting arguments.** Both are correct:
  - A: 3 + 2 = 5, with a < b, a < d, c < d.
  - B: 5 + 6 + 5 = 16, with comparisons exactly a < c, b < c, b < e, d < e. The "symmetric" case is a real symmetry, because (3,3,2)/(2,1) is its own transpose.
- **Proofs.** The "Why larger?" argument (p. 7) and the order, loss and termination arguments for Problem 9 (p. 8) are correct. For example, if u lies above the moved tile x, the cell right of u holds a tile v, because λ and μ are partitions, so u < v < x.
- **Corner orders and the altered rule.** The statements about corner orders ("once the first corner is chosen, the second is forced") and about the larger-neighbour rule are correct.
- **Page references.** All the page references for each route match the materials.

## Problems found

### 1. Guide p. 7, Problem 7 hints, and overview p. 1 (minor): the hint describes an impossible situation, and S is treated as necessary when E alone determines the undo

- **Quoted text:**
  - Guide p. 7, Hints: "ask which of the two available up/left labels could have moved last; stop at S even if another neighboring label exists."
  - Guide p. 7: "Uncover the known exit, use the larger immediate up/left neighbor, and stop at the known original corner."
  - Guide p. 1 overview: "If the original starting cell and deleted exit cell are known, insert the hole at the exit and repeatedly move the larger immediate up/left neighbor into it, stopping at the original cell. … Boundary markers carry essential information."
- **Evidence.**
  - S is a corner of the gray region, and the gray region is a Young diagram. So the squares immediately above and left of S are gray or off the board. Only S leaves the gray region during the slide, and those squares stay gray throughout the undo.
  - So when the ring gets back to S, there is never a numbered square above or left of it, and those are the only squares the backward rule looks at. The rule therefore stops at S by itself.
  - It cannot stop earlier: at every earlier backward position, the tile that moved out of that square on the way forward is still a numbered up or left neighbour.
  - Computed (`check_math.py.out`, last section): over all 37,320 single slides in the 4×4 family, and over A2, A4 and both B4 corners, a label above or left of S occurs 0 times. The undo without S always ends at S and recovers the start exactly.
  - So the hint's situation never arises, and recording S adds nothing. E, on the other hand, really is needed. Undo A2's finished 13/24 from (3,1) instead of its true exit (1,3), and you get a different legal start: gray (1,1); 3 at (1,2); 1, 4 in row 2; 2 at (3,1).
  - The student page is correct as printed. "Stop when it reaches S" coincides with the natural stop, so it is harmless.
- **Smallest fix (guide only):**
  - p. 7 hint: replace "stop at S even if another neighboring label exists" with "the ring stops by itself at S, because only gray squares or the edge lie above and left of S".
  - p. 1: replace "If the original starting cell and deleted exit cell are known" with "If the deleted exit cell is known". Replace "stopping at the original cell" with "until no label lies above or left of the hole; that square is the original cell". Replace "Boundary markers carry essential information" with "The exit marker carries essential information; S serves as a check."
  - Optionally add to the Problem 7 notes that children may discover they need only E.

### 2. Guide p. 4, Problem 3 (minor): "descending diagonal", and a table read in an unstated direction

- **Quoted text:** "The D shape has missing cells at top left, top middle and middle left; its labels lie on the descending diagonal." The table's "diagonal labels" column then lists D1 123, D2 132, D3 213, D4 231, D5 312, D6 321.
- **Evidence.**
  - D's labels sit at (1,3), (2,2) and (3,1). That is the diagonal that rises from bottom left to top right. The diagonal usually called descending runs (1,1), (2,2), (3,3), and on this card it holds a gray square, a label and a dark square.
  - The column lists labels starting at the top right; this was checked against all six cards. Read from the bottom left, the column would assign 132 to D4 and 231 to D2. It would likewise swap D3 and D5 (213 and 312), and D1 and D6.
  - D2 and D4 have different results (13/2 and 12/3), as do D3 and D5. So an adult who matches a card to the table by its labels rather than its name, and reads the diagonal the other way, gets the wrong result. The card names in the table are right, so the risk is limited to this explanatory column.
- **Smallest fix:** change "lie on the descending diagonal" to "lie on the diagonal from top right to bottom left". Change the column head "diagonal labels" to "labels, top right to bottom left".
