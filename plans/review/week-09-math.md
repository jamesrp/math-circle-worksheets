# Week 9 (bouncing paths): math check

Scope: `lowell-math-circle-year-2/week-09/week-09-k-1.pdf` (F09-K-v4, 8 pp., Problems 1–7), `week-09-grades-2-3.pdf` (F09-M-v4, 8 pp., Problems 1–8), `week-09-grades-4-5.pdf` (F09-U-v4, 8 pp., Problems 1–8) and `week-09-facilitator.pdf` (F09-FAC-v4, 10 pp.). Sources: `lowell-math-circle-year-2/source/week-09/src/` (`gen.py` and the generated `k-1.tex`, `grades-2-3.tex`, `grades-4-5.tex`) and `guide-src/` (`facilitator.tex`, `paths.tex`, `chart45.tex`). I did not use the packet's own `gen.py` assertions or `guide-src/check.py`. The return visit (`week-09-return-visit.pdf`, F09-RV-v1, 7 pp., with `week-09-return-visit-facilitator.pdf`, RV9-FAC-v1, 5 pp.) is a companion and was also checked (last section). The archive folders were not checked. My scripts and their outputs are in [checks/week-09/](checks/week-09/). Checked October 10, 2026.

**Result: every answer in all three student bands is correct, and every problem can be done as stated. All 73 boards match their text: sizes, "w by h" labels, dots, copy and fold lines, and equal scaling. The return visit and its guide also check out. The adult guide has 4 problems, and none changes a printed answer. One matters in the session (item 1): the K–1 rule for which way to go after a bounce says "keep going up". In each Problem 1 floor walk it sends the walker the wrong way at the two side walls met while coming down, and it has no rule for the bounce off the near end. In Problem 2 it gives a wrong move or contradicts itself at 5 of the 9 bounces. Items 2–4 are minor.**

## How it was checked

- `pdfgeom.py` is my own standard-library PDF reader. It finds the pages, inflates their content streams and interprets the path operators, so every stroke and fill can be measured in points.
- `extract.py` uses it to read every board out of the delivered PDFs (output `extract.out`, `pdf_geometry.json`):
  - **Boards.** 34 boards in K–1, 26 in 2–3 and 13 in 4–5, plus the 4–5 chart. For each it reads the columns and rows, the square size, and whether all four walls are thick. It also reads thick copy lines, dashed fold lines, dots and answer boxes, and the label under the board.
  - **Pictures.** The K–1 target pictures, the path drawn in each rules picture, and the 17 path thumbnails in the guide.
- `expected.py` is my transcription of every board, typed from the rendered pages.
- `billiards.py` is my own simulator. It walks the ball square by square, with no lcm formula. It also unfolds a straight line on a sheet of copies, folds it back and counts self-crossings.
- `check_answers.py` (output `check_answers.out`) runs 245 checks with 0 mismatches:
  - **Boards against the transcription.** Every board matches. Squares are 0.75 in (K–1) or 0.5 in (2–3, 4–5), equal in both directions; the two rules pictures are 0.5 in and 0.4 in. Every "w by h" label names the drawn width and height. Each rules picture's arrow follows the ball. All 17 guide thumbnails equal the simulated path, with the dot at the start, the ring at the stopping corner and the caption's corner and count.
  - **Problems.** It solves every problem from the board sizes read out of the PDFs, and enumerates every "find all" and "is there" question.
  - **Guide.** It checks each answer, hint, overview fact and section 5 statement against the computation. Every quoted sentence is first confirmed to be in the delivered guide. Its NOTE lines are items 1–4 below, plus one loose word I do not count ("doubled" for 20 by 30 in the 4–5 struggling route).
- `rv_check.py` (output `rv_check.out`) checks the return visit: 36 checks, 0 mismatches.
- `source_vs_pdf.py` (output `source_vs_pdf.out`) confirms that the PDFs carry the source text I read: all 23 problem statements, the three sets of opening rules, and every walled board size in the generated TikZ. pdfLaTeX is not installed here, so I could not test a clean rebuild. This comparison stands in for it.

Notation: TR, TL and BR are top right, top left and bottom right; "BR 3" means the ball stops at the bottom right after 3 bounces. "w by h" is w squares wide and h high, as the pages define it.

## K–1: all answers correct

- **P1 (floor grid, 3 by 5).**
  - From the left dot: the far right corner, 6 bounces, 15 steps.
  - From the right dot: the far left corner, 6 bounces.
  - Each path crosses itself at 4 points, (1,1), (1,3), (2,2) and (2,4) from the left dot, and never retraces a segment.
- **P2.** 2 by 2 TR 0; 1 by 3 TR 2; 2 by 1 BR 1; 2 by 3 BR 3; 3 by 3 TR 0; 3 by 2 TL 3.
- **P3.** 1 by 4: 3; 1 by 5: 4; 2 by 5: 5; 3 by 4: 5.
- **P4.** 1 by 2, 2 by 4 and 3 by 6 are all TL 1. 2 by 3 and 4 by 6 are both BR 3.
- **P5 (3 by 3 grids).** Every table fits. Top left: 1 by 2 and 3 by 2. Bottom right: 2 by 1 and 2 by 3. Top right: 1 by 1, 1 by 3, 2 by 2, 3 by 1 and 3 by 3. So the two grids beside each of the first two pictures take exactly the two answers.
- **P6.** No table returns to the dot. This holds for every table up to 200 by 200, not only on the 4 by 4 grids.
- **P7.** Each big square is exactly lcm(w, h) on a side for the small table beside it (2, 3, 4). So the line from the dot to the far corner folds onto the whole ball path, and the panels fold flat in one piece:
  - 2 by 2 square: the 1 by 2 path, TL 1.
  - 3 by 3 square: the 1 by 3 path, TR 2.
  - 4 by 4 square: the 2 by 4 path, TL 1.

## Grades 2–3: checks out completely

- **P1.** 2 by 3 BR 3; 3 by 2 TL 3; 1 by 4 TL 3; 3 by 4 TL 5; 4 by 3 BR 5; 3 by 5 TR 6.
- **P2.** 1 by 2, 2 by 4 and 3 by 6 are TL 1. 1 by 3 and 2 by 6 are TR 2. 4 by 6 is BR 3; as the guide says, it is a copy of 2 by 3, not of 1 by 3.
- **P3.** 5 by 10 TL 1; 8 by 12 BR 3.
- **P4 (6 by 6 grids).**
  - BR after 1 bounce: 2 by 1, 4 by 2, 6 by 3.
  - TR after 4: 1 by 5, 5 by 1.
  - TL after 7: 5 by 4 only.
  - TR after 3: no table of any size, because every TR stop has an even number of bounces (checked to 120 by 120).
- **P5.** A game. Any table up to 6 by 6 fits the 14 by 15 grid.
- **P6.** Exactly six tables up to 6 by 6: 1 by 2, 2 by 4 and 3 by 6 (TL), and 2 by 1, 4 by 2 and 6 by 3 (BR).
- **P7.**
  - The 6 by 6 sheet is 3 by 2 copies of 2 by 3. The line to the opposite corner crosses 3 thick lines (x = 2, y = 3, x = 4). It passes through 4 tables, which are edge-connected, and folds to the 2 by 3 path, BR 3.
  - The 3 by 3 sheet is 3 copies of 1 by 3. The line crosses 2 thick lines, passes through all 3 tables and folds to the 1 by 3 path, TR 2.
- **P8.** There is none (checked to 200 by 200).

## Grades 4–5: checks out completely

- **P1.** 2 by 3 BR 3; 3 by 2 TL 3; 1 by 4 TL 3; 3 by 4 TL 5; 6 by 4 TL 3; 3 by 5 TR 6.
- **P2.** The 36-box chart, with widths 1–6 left to right and heights 1–6 bottom to top as printed, equals the guide's table entry for entry.
- **P3.** The 8 by 9 sheet is 4 by 3 copies of 2 by 3. The line first meets a crossing of thick lines at (6, 6), 3 tables across and 2 up, inside the sheet. Before that it crosses x = 2, y = 3 and x = 4. It passes through 4 edge-connected tables and folds to BR 3.
- **P4.** The sheet for 4 by 3 has lines at x = 4, 8, 12 and y = 3, 6, 9, 12. The first crossing is at (12, 12), 3 across and 4 up, and fits the 13 by 13 grid. The line crosses 5 lines on the way. The ball stops BR after 5.
- **P5.** 6 by 10 TR 6; 8 by 12 BR 3; 12 by 9 BR 5; 7 by 5 TR 10; 5 by 8 TL 11; 20 by 30 BR 3. Tracing 6 by 10 takes 30 steps.
- **P6 (14 by 12 grid).**
  - TL after 13: 13 by 2, 11 by 4, 7 by 8 (1 by 14 is too tall).
  - TR after 8: 9 by 1, 7 by 3, 3 by 7, 1 by 9, 14 by 6.
  - BR after 11: 12 by 1, 10 by 3, 8 by 5, 6 by 7, 4 by 9, 2 by 11.
  - BR after 10: none of any size (checked to 60 by 60).
- **P7.** True for every table (checked to 200 by 200).
- **P8.** For every table up to 60 by 60: the ball stops on the right exactly when L/w is odd, at the top exactly when L/h is odd, after L/w + L/h − 2 bounces, where L = lcm(w, h).

## Adult guide

These are all correct:

- **Answers and hints.** Every answer in section 4 and every hint's arithmetic.
- **Launch.** The launch walk: three steps reach the right-hand wall at (3, 3).
- **Jump-rope tables.** 3 by 1 far right 2; 3 by 2 far left 3; 3 by 3 far right 0; 3 by 4 far left 5; 2 by 5 near right 5; 1 by 5 far right 4.
- **Counts.** The floor-grid squares; the 111 sheets to print; 441 squares against 224 per page; 303 diagonal steps for the 36 chart tables.
- **Explanations.** The parity explanations for TR after 3 and BR after 10. The one-bounce argument, including the first bounce at height w and the second wall when h ≠ 2w. The reversal argument for "never home", and the halfway-crossing argument for 4–5 P7.
- **Claims to listen for.** All seven in section 6.
- **Section 5.** These were tested by enumeration:
  - the folding map (φw, φh) reproduces every simulated path up to 20 by 20, with the stop at lcm(w, h);
  - the corner and bounce rule in lowest terms;
  - the characterisation "a multiple (kp, kq) of a coprime pair with p + q = n + 2 and the right parities" (all corners, n ≤ 24, tables up to 60 by 60);
  - the sheet staircase of p + q − 1 tables;
  - the rescaling of direction (b, a) to slope 1 on an aw by bh table;
  - the 3-D box, with its stop at lcm(w, h, d) and never home, for all boxes up to 12 × 12 × 12.

The problems are below.

### 1. K–1: "keep going up" gives the wrong move at a side wall met on the way down (pp. 2 and 4)

- **Quoted text:**
  - p. 2, "How a child walks the path": "After a side wall, keep going up the grid but slant the other way; after the far end, keep slanting the same way but come back down the grid."
  - p. 4, Problem 1 hint (1): "“Which way were you slanting before the wall? Keep going up the room and slant the other way.”"
  - p. 4, Problem 2 hint (2): "Move the counter one square at a time and stop at each wall: “Which way now? Keep going up, and turn away from the wall.”"
- **Evidence (`check_answers.out`, NOTE lines):**
  - **Floor walk from the left dot.** The bounces are R at (3,3) going up, T at (1,5), L at (0,4) going down, R at (3,1) going down, B at (2,0), and L at (0,2) going up.
    - At the third bounce the printed rule ("keep going up the grid but slant the other way") sends the walker from (0,4) to (1,5). That is straight back along the step just taken. The ball goes to (1,3).
    - The rule is wrong again at (3,1).
    - It says nothing about the bounce off the near end at (2,0).
    - The walk from the right dot is the mirror image: R at (3,4) and L at (0,1) going down, B at (1,0).
  - **The guide's own picture.** The thumbnail on p. 4 is drawn correctly, so the rule contradicts it. The p. 2 test ("Walk the floor grid from each dot") would also go wrong at bounce three.
  - **Problem 1 hint (1).** It is about side walls. It is wrong at 2 of the 4 side-wall bounces in each walk, the ones met going down.
  - **Page 2 tables.** Problem 2's hint is given "at each wall". Its 9 bounces are:
    - 2 side walls met going down, L at (0,2) on 2 by 3 and R at (3,1) on 3 by 2. "Keep going up" sends the counter back along the step it came in on.
    - 3 top walls, on 2 by 1, 2 by 3 and 3 by 2. There "keep going up" contradicts "turn away from the wall".
    - 1 bottom wall, on 3 by 2. The vertical direction comes out right by accident, and nothing says which way to slant.
    - 3 side walls met going up, where it works.
  - **Pages 3–5.** The same happens on 2 by 5 (two side walls going down and the top), 3 by 4 (one side wall going down, the top and the bottom), 2 by 3 and 4 by 6 (one side wall going down and the top each).
  - **The correct rule.** A side wall reverses only left and right. An end wall reverses only up and down. The 2–3 hint states it correctly as a question ("At a side wall, which changes: going up or down, or going left or right?").
  - **Why it matters.** A K–1 parent volunteer who follows the printed sentence will move the ball, or direct the walker, the wrong way at the third bounce of the very first floor walk. Problem 1 and Problem 2 are the core of the K–1 hour.
- **Smallest fix:**
  - p. 2: "After a side wall, keep going the same way along the grid (up or down) but slant the other way; after either end, keep slanting the same way but turn back along the grid."
  - P1 hint (1): "…Keep going the same way along the room (up or down) and slant the other way."
  - P2 hint (2): "…“Which way now? Turn away from the wall you hit, and keep the other direction the same.”"

### 2. "Measure the squares": the first squares on each page 1 are drawn smaller (p. 2)

- **Quoted text:** "1. Measure the squares: 3/4 inch on the K–1 pages, 1/2 inch on the others. Smaller squares mean the printer scaled the page; reprint at 100%."
- **Evidence:** the first grid on page 1 of every packet is the rules picture beside the opening text. In K–1 it is the 5 by 3 picture, with 0.5 in squares. In 2–3 and 4–5 it is the 7 by 3 picture, with 0.4 in squares. Every board in a numbered problem measures 0.75 in (K–1) or 0.5 in (2–3, 4–5), so the stated sizes are right for those boards. An adult who measures the first squares on page 1, as the test invites, will find smaller squares on a correctly printed page and reprint for nothing.
- **Smallest fix:** "Measure a square of a numbered problem: 3/4 inch on the K–1 pages, 1/2 inch on the others (the small picture beside the opening rules is drawn smaller on purpose)."

### 3. Tape quantity when the outside walls are doubled (pp. 1–2)

- **Quoted text:**
  - Materials table: "Masking tape, about 60 ft (18 m)".
  - Step 2: "…That gives 3 by 5 squares of 18 inches, using about 60 ft of tape."
  - Step 3: "Make the outside walls stand out (double tape, or a second colour)."
- **Evidence:** the single-tape grid uses 24 ft of perimeter, 2 × 7½ ft of long lines and 4 × 4½ ft of cross lines, 57 ft in all, so step 2 is right. Doubling the outside walls, the first option in step 3, adds another 24 ft, for 81 ft. That is a third more than the materials list.
- **Smallest fix:** "Masking tape, about 60 ft (18 m; about 80 ft if you double the outside walls)".

### 4. Section 5: the bounce sequence is the central word of a Christoffel word, not a whole one (p. 10)

- **Quoted text:** "The order of side and end hits along the path is a cutting sequence (a Christoffel word), built by the Euclidean algorithm on w and h."
- **Evidence:** reduce the table to p by q. Its bounce sequence has p + q − 2 letters (side and end hits) and is a palindrome. A Christoffel word of that slope has p + q letters and is not a palindrome. For every table up to 24 by 24, the bounce sequence equals the lower Christoffel word with its first and last letters removed, and it never equals a whole Christoffel word. Example, 2 by 3: the bounces are side, end, side; the lower Christoffel word for 3 across and 2 up is xxyxy, whose central word xyx matches. This is background reading only, but an adult who looks up "Christoffel word" will find words two letters longer.
- **Smallest fix:** "…is a cutting sequence (the central word of a Christoffel word: drop its first and last letters), built by…"

## Return visit (companion): checks out completely

- **Problem 1 (two bounces, 4 by 4, S = (1,1)).** The board positions were read from the PDF: Finish A at (2,3), Finish B at (3,3), 12.5 mm squares, 8 boards per finish.
  - Following the reflected ray exactly with fractions gives Finish A: LR, LT, RL, RT, BL, BR, BT, TB. Finish B gives LR, LT, RL, BR, BT, TB. A separate search over all directions finds no other two-bounce route. So Finish A has exactly as many boards as words.
  - All 16 contact points the guide gives are exact, and so are the squared lengths (LT and BL tie at 25).
  - Finish B's LB/BL and RT/TR rays hit the corners (0,0) and (4,4).
  - The guide's general claims hold for 9,264 pairs of S and F on the half-unit lattice of four rectangles: same-wall words never work; LR, RL, BT and TB always work; for adjacent walls exactly one order works unless the ray hits their corner.
  - The launch picture is S (1,1), contact (4,2), F (1,3), with equal angles.
- **Problem 2 (6 by 4, 22 mm squares).** The letters are A–E at height 3, F–J at 2 and K–O at 1.
  - Corners: A, C, E, G, I, K, M, O.
  - Loops: B, D, F, H, J, L, N. Each first returns heading NE after 24 steps.
  - H is back at its dot heading SE after 12 steps.
  - The rule for other boards holds for every board up to 8 by 8: corner iff x − y is divisible by gcd(a, b), loop 2 lcm(a, b).
  - The launch strip shows (2,1) NE, then (3,2) NW, then (2,3) SW. The workspace boards are 6 by 4 with 18 mm squares.
- **Problem 3 (crossings).**
  - The four boards (12.5 mm squares) have 1, 3, 6 and 1 crossings, at exactly the points the guide lists.
  - (u − 1)(v − 1)/2 holds with no retraced segment for every table up to 30 by 30.
  - On the 12 by 12 workspace the tables with ten crossings are exactly 3 by 11, 11 by 3, 5 by 6, 6 by 5, 10 by 12 and 12 by 10.

## Not checked

- The archived versions.
- Physical readiness, none of it rehearsed:
  - the floor walk;
  - counters on 0.75 in squares;
  - whether a marker line shows through 4 folded layers;
  - the cutting and folding.
- A clean rebuild (pdfLaTeX is not installed here). The text and board comparison in `source_vs_pdf.py` stands in for it.
- Bibliographic and lineage statements: Gardner's "paper pool" column, Tabachnikov's chapter 1, the Lowell Fall 2025 handout, and Math Circle by the Bay's preface pages.
- The section 6 "claims to listen for" sit in a three-column table that the text extraction interleaves. I confirmed their wording on the rendered page and checked them only by computation.
