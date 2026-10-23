# Week 98 (Growing from a few seeds): math check

Scope:
- `lowell-math-circle-year-2/week-98/week-98-grades-2-3.pdf`: the Grades 2–3 packet, 5 pages.
  - p. 1: the shared rules, then a worked example on a 2-row, 3-column board: Start, One square added, Stopped. Then Problem 1: three seeds that fill a 3-by-3 board, and three that get stuck.
  - p. 2: Problem 2, the fewest seeds for a 4-by-4 board, with three different starts.
  - p. 3: Problem 3, three seeds with finishes of 3, 4, 6 and 9.
  - p. 4: Problem 4, the same seeds grown in different orders.
  - p. 5: Problem 5, a printed four-seed start and its four one-seed deletions.
- `week-98-grades-4-5.pdf`: the Grades 4–5 packet, 6 pages.
  - p. 1: the same rules and example, then Problem 1: how many final totals three seeds can make on 3-by-3.
  - p. 2: Problem 2, the same as Grades 2–3 Problem 2.
  - p. 3: Problem 3, the fewest seeds for 5-by-5 and 10-by-10.
  - p. 4: Problem 4, exposed sides before and after three circled additions.
  - p. 5: Problem 5, whether three seeds can fill 4-by-4 and four can fill 5-by-5.
  - p. 6: Problem 6, the four-seed start and its deletions again, plus a different indispensable four-seed start.
- `week-98-facilitator.pdf` (5 pages).

There is no K–1 packet, and the week does not claim one. The delivered PDFs are byte-identical to `source/week-98/reference-pdfs/`. A scratch `pdflatex` rebuild of `student/*.tex` and `guide/facilitator.tex` gives the same text as the delivered PDFs.

Sources read: `source/week-98/student/grades-2-3.tex`, `student/grades-4-5.tex`, `guide/facilitator.tex`, `guide/solutions.tex`, `README.md`, `SOURCES.md` and `QA.md`. I did not run or import the package's `check_math.py`. My scripts and their outputs are in this run folder, for `plans/review/checks/week-98/`. The page images in `render/` are working copies only. Checked October 23, 2026.

**Result: every student page in both bands is correct. Every printed diagram, worked example, answer and count in the guide is also correct. I found 2 problems, both minor and both in the guide's wording of an argument:**
1. The order-independence proof in the overview defines "closed" with the words "outside cell", one paragraph after saying "there are no outside cells". It also gives the wrong reason for a step.
2. The Grades 4–5 Problem 1 classification includes a case that cannot occur ("A third seed on that line gives 3"). The answer it gives contradicts that branch's own premise.

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 0 failures). It is written from scratch, with the printed data typed in from the pages; `check_diagrams.py` confirms that data against the PDFs. It implements the two-neighbour process on an open a-by-b grid and checks:
  - **The worked example.** The legal additions, the finish, and that nothing more can be added.
  - **Order independence.** For every state of the 2×3, 3×3, 3×4 and 4×4 boards (65,536 states on 4×4), it computes the set of finishes some legal order can reach, using dynamic programming over states. Every state reaches exactly one finish.
  - **Three seeds on 3×3.** All 84 starts. It also tests the guide's geometric classification against every start and every supporting pair.
  - **Lower bounds by search.** No 2-seed start fills 3×3 (36 starts). No 3-seed start fills 4×4 (560). No 4-seed start fills 5×5 (12,650).
  - **Constructions.** The main and opposite diagonals fill n×n for n = 1–12. It also checks the guide's three 4×4 starts.
  - **Exposed sides.** On the 3×3, 3×4 and 4×4 boards, every legal addition in every state changes the count by exactly 4 − 2k. No legal addition increases it. It also checks the three Problem 4 pictures and the full-board counts.
  - **The printed four-seed start.** That it fills; the guide's growth layers; the four deletions, in printed order. It also lists all inclusion-minimal filling starts on 3×3 and their symmetry orbits.
  - **The later rectangle question.** Exact minima on every a×b rectangle with a ≤ 4 and b ≤ 5, against the guide's bound ⌈(a+b)/2⌉.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 0 failures). It reads the delivered PDFs' words and vectors with PyMuPDF, not the sources:
  - **Every page.** US Letter size; header, footer id and page number; consecutive problem numbers.
  - **Every board.** Rows and columns from the drawn grid lines. Equal x and y pitch, so the cells are square.
  - **Marks.** Every seed dot, grey cell, + mark and open circle is placed in its board cell and compared with the data `check_math.py` uses.
  - **Labels.** The board labels.
  - **Guide.** Every guide sentence quoted below is present in the PDF text.

The general facts are proved in the guide, and I checked those proofs by hand:
- **Same finish for every order.** Take any set C that contains the seeds and has no cell outside it with two side-neighbours in it. By induction every legal addition lies in C. A finished run has no legal addition, so it is itself such a set. So every finished run is the least such set. Problem 1 concerns only the wording of this argument.
- **Exposed sides never increase.** A cell added with k filled side-neighbours removes k exposed sides and adds 4 − k, a change of 4 − 2k ≤ 0 when k ≥ 2. A start of s seeds has at most 4s exposed sides, and a full n×n board has 4n. So s ≥ n.
- **The diagonal fills.** A cell (r, c) with c − r = j + 1 has the neighbours (r, c − 1) and (r + 1, c), both at distance j from the diagonal. Both lie on the board, because c ≥ 2 and r + 1 ≤ n − j. Induction on j fills every layer.
- **Minimum implies inclusion-minimal, but not the reverse.** A removable seed would give a smaller filling start. The printed four-seed start shows the converse fails.

## Grades 2–3 (pp. 1–5): correct

- **Worked example (p. 1).**
  - The board has 2 rows and 3 columns of 10 mm cells. The seeds are at the top left, bottom left and bottom middle.
  - The only legal first addition is the top middle, which the page marks +. After that, the top right and bottom right each have one filled neighbour, so "Stopped" is right.
  - The grey shading in all three pictures matches the filled cells.
- **P1.** Both outcomes are possible with three seeds on 3×3: 14 of the 84 starts fill the board and 14 stop at once. The two boards are 3×3 with 30 mm cells.
- **P2.** The answer is 4. All 560 three-seed starts fail, and 130 four-seed starts fill (22 up to symmetry), so "three different starts" is easy to meet. The working board is 4×4 with 30 mm cells, and the three record boards are 4×4 with 10 mm cells.
- **P3.** The finishes of the 84 three-seed starts are 3 (14 starts), 4 (16), 6 (40) and 9 (14). All four requested totals are possible, and no other total occurs. The labels "3 filled squares", "4 filled squares", "6 filled squares" and "9 filled squares" sit over four 3×3 boards.
- **P4.** The answer is no. On 3×3 and 4×4, every start reaches the same finish in every legal order. "When possible" is needed: the 16 starts that finish at 4 have only one addition, so they have only one order.
- **P5.**
  - The printed start is (row, column) (1,1), (1,2), (2,3), (3,3), and it fills the board.
  - The four small boards leave out (1,1), (1,2), (2,3) and (3,3), in reading order. They finish at 6, 3, 3 and 6, so every seed is needed.
  - Four is not the fewest, because the three-seed diagonal fills.
  - The grey shading matches the seeds on all five boards.

## Grades 4–5 (pp. 1–6): correct

- **Example (p. 1).** The same as Grades 2–3, and correct.
- **P1.** Exactly four totals: 3, 4, 6, 9. The guide's classification paragraph is item 2.
- **P2.** As Grades 2–3 P2: the answer is 4.
- **P3.**
  - The answers are 5 and 10. The diagonal fills both boards. For 5×5, all 12,650 four-seed starts fail. For 10×10, the perimeter bound (40 exposed sides, so at least 10 seeds) does the work.
  - The boards are 5×5 with 20 mm cells and 10×10 with 7 mm cells. Both have square cells.
- **P4.** In each picture the circled centre is a legal addition, with k = 2, 3 and 4.
  - The exposed sides go 8 → 8, 12 → 10 and 16 → 12.
  - In the first picture the two seeds touch only at a corner, so they really have 8 exposed sides before the addition.
  - The answer to "Can any legal addition increase the number of exposed sides?" is no, by 4 − 2k.
- **P5.** No in both cases: 12 < 16 and 16 < 20, and exposed sides never increase. The searches agree: 0 of 560 starts, and 0 of 12,650. The boards are 4×4 (20 mm cells) and 5×5 (18 mm cells).
- **P6.** The start and the four deletions are the same as Grades 2–3 P5, in the same order. They finish at 6, 3, 3, 6, and four is not the fewest.
  - A different indispensable four-seed start exists. There are 9 inclusion-minimal four-seed filling starts on 3×3, in three symmetry orbits:
    - the printed start (4 placements);
    - {(1,1), (1,2), (3,2), (3,3)} (4 placements);
    - the four edge midpoints (1 placement).
  - So a child who wants an answer that is not a rotation or reflection also has one.
  - The page has one blank 3×3 board for this answer.

## Facilitator guide (pp. 1–5): correct except items 1 and 2

Everything below checks out:
- **p. 1, the overview's facts.**
  - The finish is the same for every order; the hypotheses are side neighbours only and an open boundary.
  - Exactly n seeds are needed, with s ≥ n from exposed sides and the diagonal construction.
  - The four indispensable seeds (1,1), (1,2), (2,3), (3,3) are not the fewest.
- **p. 2, the launch table.** "Fill the top middle, pointing to its left and lower neighbors. Neither right-hand cell can then fill."
- **p. 3, Grades 2–3.**
  - The main diagonal fills, and the full top row stops.
  - {(1,1), (1,3), (2,4), (4,1)}, the main diagonal and the antidiagonal all fill 4×4.
  - All four rows of the Problem 3 table are right, including the terminal shapes. Its 6-row is (1,1), (1,2), (2,3), and it finishes as the top two rows.
  - "For the three diagonal seeds, there are four legal first additions": (1,2), (2,1), (2,3), (3,2).
  - The Problem 5 growth layers are each legal in either order.
  - "Removing the four seeds in that order leaves terminal counts 6, 3, 3, 6", which matches the printed boards.
- **p. 4, Grades 4–5.**
  - The minima are 4, 5 and 10, and the diagonal-layer induction holds at the board edges.
  - 4 − 2k gives 0, −2 and −4. The before/after counts are "8 → 8, 12 → 10 and 16 → 12".
  - An isolated hole removes four sides.
  - The Problem 5 bounds are right.
- **p. 5.**
  - The quarter-turn {(1,3), (2,3), (3,1), (3,2)} is the printed start rotated, and it is inclusion-minimal.
  - "The checker finds 9 inclusion-minimal four-seed starts on 3 × 3" and "There are 14 three-seed filling starts" are both right.
  - Every minimum start is inclusion-minimal.
  - The rectangle bound s ≥ ⌈(a+b)/2⌉ is right. It equals the true minimum on every rectangle tested up to 4×5, and the guide rightly does not claim that in general.

The overview gives its coordinates before p. 3 states the (row, column) convention. Under the other reading (column, row), the examples become their mirror images across the main diagonal, which have the same properties. So nothing is wrong under either reading.

## Problems

### 1. Guide p. 1, "Every completed order has the same finish": a definition that reads as vacuous, and a misplaced "therefore" (minor)

The overview's model paragraph says: "Only side-neighbors count; there are no outside cells or wraparound edges." The next paragraph defines the key notion with the same words in a different sense: "Let C be any closed set containing the seeds, where closed means no outside cell has two neighbors in C." Read with the previous sentence, "outside cell" means a cell off the board. There are none, so every set would be closed, and the argument would prove nothing. The intended meaning is a board cell not in C.

The next sentence gives the wrong reason for a step: "A terminal run is itself closed and therefore is contained in every closed superset of the seeds." Being closed does not make a set lie inside other closed sets. The containment comes from the induction in the previous sentence ("Inductively every legal addition belongs to C"). Closedness is what makes the terminal run one of those supersets, and so the least.

The theorem is true; `check_math.py` confirms it for every state of the 3×3 and 4×4 boards. Only the explanation an adult reads is affected.

Smallest fix: change the definition to "where closed means no cell outside C has two side-neighbors in C". Replace the third sentence with: "By that induction a terminal run lies inside every closed superset of the seeds, and it is itself closed, so it is the least one."

### 2. Guide p. 4, Grades 4–5 Problem 1 classification: an impossible case with a contradictory answer (minor)

The paragraph opens: "If there is no legal addition, the total is 3. Otherwise two seeds support a first addition." In the second branch it says: "If the supporting seeds are opposite across the new cell, their closure is a full row or column of the 3 × 3 board. A third seed on that line gives 3; one in the next parallel line expands to a 2 × 3 rectangle, giving 6; one two lines away … giving 9."

On a 3×3 board, two seeds opposite across a cell are the two ends of a row or column. The only other cell on that line is the new cell itself. A third seed there would fill the new cell, which is then not an addition, and that contradicts the branch's premise. The three seeds would be a full row or column, which has no legal addition at all. All 6 such starts fall under the first sentence ("the total is 3"). In the "Otherwise" branch, a first addition always happens, so the finish is at least 4; "gives 3" there is a false outcome for the branch.

Every other case is right. `check_math.py` applies the classification to all 84 starts and to every supporting pair (92 pair cases), and finds no mismatch with the true finish.

Smallest fix: delete "A third seed on that line gives 3;". The next clause can then start "A third seed in the next parallel line expands …".

Optional, in the same paragraph: "diagonally opposite corners of a unit square, their closure is that 2 × 2 square" names one square in two ways, and the corners only make sense for cell centres. "If those two seeds are diagonal neighbors, their closure is the 2 × 2 square they span" says the same thing directly.
