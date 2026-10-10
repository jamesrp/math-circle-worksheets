# Week 50 (staircases and lengths): math check

**Scope.** I checked the current student PDFs in `lowell-math-circle-year-2/week-50/`:

- `week-50-k-1.pdf`: 5 pages, Problems 1–6.
- `week-50-grades-2-3.pdf`: 5 pages, Problems 1–5.
- `week-50-grades-4-5.pdf`: 6 pages, Problems 1–7.
- `week-50-bonus.pdf`: 3 pages, Problems 1–3. Pages 1–2 are headed Grades 2-5 and page 3 Grades 4-5.

I also checked both adult guides: `week-50-facilitator.pdf` (4 pages) and `week-50-bonus-facilitator.pdf` (2 pages). I ignored the archive folder.

**Sources read.** For the base packet: `source/week-50/editable/src/make.py` and `draw.py`, and `facilitator-src/content.json`, `build.py` and `route-note.json`. For the bonus packet: `source/week-50-bonus/student/build.py` and `support.py`, and `guide.md`. I did not run or import the packet's own `verify*.py` or `checks.txt`. My scripts and their outputs are in this folder. Checked 10 October 2026.

**Result.** Every answer, count, witness and theorem in the four student packets and both guides is correct. I found **3 problems, all minor**:

- one diagram label in the worked example on page 1 of every base band;
- one question in Grades 2–3 whose wording makes it trivial;
- one launch instruction in the base guide that names a diagram feature the page does not have.

## How it was checked

**`check_diagrams.py`** (output `out_check_diagrams.txt`) reads every vector path, fill, dot and word back from the delivered PDFs using pdfplumber. It converts them to millimetres measured from S. It checks:

- **Main boards.** On every main board the rectangle measures 160.00 × 120.00 mm with equal scaling on both axes, the S and F dots sit at its corners, and the dotted diagonal (on every board except page 1) measures 200.0 mm.
- **Calibration bars.** Every 100 mm calibration bar measures 100.00 mm.
- **Gray strips.** Each gray strip is compared, vertex by vertex, with {|y − 3x/4| ≤ d} clipped to the rectangle. The strips are d = 15 on pages 3–4 of every band and d = 8 on Grades 4–5 page 5.
- **Printed paths.** For every printed path the script records its vertices, its pieces, its length, its leftward travel, its turns and its greatest vertical gap.
- **Worked example.** It measures the four pieces and the two bars of the worked example. It also measures how far each "X: n" label is from its own piece and from the gray outline.
- **Grades 4–5 Problem 6.** It finds the piece nearest to each length label on the Problem 6 route.
- **Bonus pages.** It counts the bonus dot grids and their spacing, and measures the bonus strip and its 30 mm unit bar.
- **Guide diagram.** It reads back the guide's eight-turn diagram.

**`check_math.py`** (output `out_check_math.txt`) uses exact fractions throughout. It checks:

- **Length invariant.** It builds 20,000 random rational right/up staircases. All have length 280.
- **Problem 3 and Problem 7.** It checks the printed four-step staircase, the guide's 8 × (R20, U15) staircase, and the n-step gap formula 120/n.
- **Problem 4.** It runs a breadth-first search for the fewest turns on lattices of step 5/m × 3.75/m mm, for m = 1, 2, 3, 4, 5 and 7. It runs this inside the closed ±15 strip and also inside the open one. It also computes the exact horizontal span of the strip at each height, which is the lemma the guide's lower bound uses.
- **Grades 4–5 Problem 5.** It checks the ±8 witness.
- **Leftward travel.** It checks Routes A and B. On a 20 mm lattice it enumerates 53,907 right/left/up routes and confirms that length = 280 + 2 × (leftward travel) for every one.
- **Bonus Problem 1.** It enumerates all 129 R/U/D routes for each price.
- **Bonus Problem 2.** It checks all 20 R/U words against every single blocked dot.
- **Bonus Problem 3.** It checks the quarter-unit staircase and the 44- and 184-loop routes against the strip.

## K–1: the mathematics checks out (see Problem 1 below for the page-1 example label)

- **P1:** Any right/up route works, and every one is 280 mm.
- **P2:** The solid route (R160, U120) and the dashed route (U60, R80, U60, R80) are both 280.0 mm as printed. The correct choice is "same length".
- **P3:** The printed staircase is 4 × (R40, U30). Its lower corners (40,0), (80,30), (120,60) and (160,90) lie 30 mm below the diagonal, so it lies outside the ±15 strip. Any staircase inside the strip is therefore closer, and every such staircase is still 280 mm.
- **P4:** The fewest turns is 8. See the Grades 2–3 notes.
- **P5:** This is possible. For example, Routes A and B (below) are both 360 mm.
- **P6:** The answer is no. Every route is 280 + 2 × (leftward travel) mm.

## Grades 2–3: the mathematics checks out (see Problems 1 and 2 below)

- **P2:** Solid and dashed are both 280 mm. The width and height give 160 + 120.
- **P3:** As in K–1. The guide's 8 × (R20, U15) staircase has greatest gap exactly 15 mm and lies in the closed strip.
- **P4:** The fewest turns is **8**.
  - The witness (0,0), (20,0), (20,30), …, (140,120), (160,120) has every corner at gap ±15 and 8 turns.
  - The strip's horizontal span is at most 40 mm at every height, and exactly 20 mm at y = 0 and y = 120.
  - With at most 7 turns there are at most 4 horizontal pieces. If there are 4, one of them is an end piece, so the horizontal total is at most 20 + 3 × 40 = 140 < 160.
  - The lattice search gives 8 at every resolution.
  - Edge case: the answer depends on including the boundary. In the open strip the fine-lattice minimum is 9. The page does say "Its pieces may follow the strip's boundary", so 8 is the right answer as printed.
- **P5:** Any path with leftward travel L is 280 + 2L mm. A 360 mm path therefore needs L = 40, and the 20 mm lattice alone has 16,016 such routes. No such path is shorter than 280 mm. See Problem 2 for the wording.

## Grades 4–5: the mathematics checks out (see Problem 1 for the page-1 example label)

- **P1–P4:** As above.
- **P5:** The strip is ±8 mm, as printed and as captioned. The guide's staircase U7.5, (R20, U15) × 7, R20, U7.5 has greatest gap 7.5 mm and fits inside the strip. It is still 280 mm, so the answer is no. For information (not asked): this staircase has 16 turns, which matches the lattice minimum.
- **P6:** The drawn route is exactly R80, U40, L40, U40, R120, U40 (Route A). It totals 360 mm and stays in the rectangle. Each of the six length labels is nearest its own piece: 4.9–7.0 mm from it, against at least 20 mm from any other piece. The "It goes left once" statement is correct.
- **P7:** The answer is no. With n equal steps the greatest gap is 120/n and the length is always 280.

## Bonus packet: checks out completely

- **P1:** The grid has 5 × 4 dots, so the trip is 4 right and 3 up. With diagonal price d, every route costs 7 + (d − 2)k coins, where k is the number of diagonals.
  - D = 1: the cheapest is 4, and all 4 cheapest routes use 3 diagonals.
  - D = 2: all 129 routes cost 7, with 0–3 diagonals.
  - D = 3: the cheapest is 7, with 0 diagonals (35 routes).
  - No route costs more than 10 coins.
- **P2:** There are 20 routes. Blocking (1,1) or (2,2) leaves 8. Blocking (1,2) or (2,1) leaves 11. No single blocked dot leaves 0, because RRRUUU and UUURRR share only S and F. The guide's 14-entry table and its predecessor-sum rows are exact.
- **P3:** The strip is |y − x| ≤ 1/4, clipped to the 4 × 4 square. The unit is 30.00 mm and the bar matches it.
  - The quarter staircase has length 8.
  - 44 out-and-back loops at S give 30, and 184 give 100. Both stay in the strip.
  - There is no longest route.

## Problems

### 1. All three base bands, page 1, worked example: the "C: 20" label sits on the gray outline, not beside piece C

- **Diagram:** a 40 × 30 mm gray outline with the black staircase A10, C20, B30, D10 inside it.
  - The label "C: 20" is drawn at `make.py` `example()` position (17,45).
  - Its text runs from 1.8 mm left of the outline's left edge to 5.8 mm right of it, so the gray edge strikes through the "C".
- **Evidence (`out_check_diagrams.txt`, identical on all three bands):**
  - The label centre is **2.0 mm** from the outline's left edge, which is 30 mm long, and **8.0 mm** from the 20 mm C piece.
  - A reader who pairs each label with the nearest line pairs "C: 20" with a 30 mm gray edge.
  - This is the first, unfamiliar convention example. Its job is to match each labelled piece with the bar on the right, so the pairing matters.
  - The other labels are on the correct side of their pieces. "B: 30" is 4.9 mm from B, against 5.1 mm from the gray top edge; it is close to a tie, but readable because B is the thick black line.
- **Smallest fix:** in `make.py` `example()`, change `(17,45,'C: 20')` to `(31,46,'C: 20')`.
  - This puts the label inside the outline, just right of piece C. Its centre is 6.0 mm from C, and the text clears C by 2.2 mm.
  - The next nearest line (B or the bottom edge) is then 9.9–10.1 mm away, and the label touches no line (checked in `out_check_diagrams.txt`).

### 2. Grades 2–3, page 5, Problem 5 (minor wording): "such a path" points to the 360 mm paths, which makes the question trivial

- **Quoted text:** "Allow leftward pieces as well as rightward and upward pieces. Make two very different S-to-F paths of length 360 mm. Could such a path be shorter than 280 mm? Explain your answer."
- **Evidence:** the nearest antecedent of "such a path" is "S-to-F paths of length 360 mm". On that reading the answer is a trivial "no, 360 > 280".
  - The intended question is the one the guide answers ("remainder of Grades 2-3 Problem 5"): can any path that is allowed leftward pieces be shorter than a staircase? The answer is no, because length = 280 + 2L.
  - The K–1 version (P6) asks this unambiguously.
- **Smallest fix:** replace the third sentence with "Could a path with leftward pieces be shorter than 280 mm?"

### 3. Base adult guide, page 1, "Launch, 4 minutes" (minor): the guide names a "vertical strip" that the page does not have

- **Quoted text:** "Match A and B to the horizontal strip and C and D to the vertical strip."
- **Evidence:** the student example has two horizontal bars, labelled "right pieces" (A | B = 40 mm) and "up pieces" (C | D = 30 mm). The page has no vertical strip.
  - In this packet "strip" also means the gray corridor of Problems 3–5.
  - An adult following the launch script has to translate the instruction.
- **Smallest fix:** "Match A and B to the 'right pieces' bar and C and D to the 'up pieces' bar."

## Adult guides: no mathematical errors (apart from the launch wording in Problem 3)

**Base guide overview.** Every statement is true with the stated hypotheses:

- the length invariant (finite right/up paths, collinear pieces merged);
- 160² + 120² = 200²;
- "close" defined as the greatest vertical gap |y − 3x/4|;
- closeness without convergence of length;
- 280 + 2L when leftward travel is allowed and downward travel is not.

**Base guide keys.**

- P1 and P2: correct (280/280, "same length").
- P3: 30 mm for the printed staircase. The 8 × (R20, U15) staircase has a 15 mm gap and lies in the closed strip.
- P4: the witness, its 8 turns and the seven-turn lower-bound proof are all valid. The proof is complete, including the 7-segment HVHVHVH case.
- Routes A and B: 360 mm, inside the rectangle, 40 mm leftward each.
- 4–5 P5: the ±8 witness is correct.
- 4–5 P6: correct (240 + 120 = 360).
- 4–5 P7: correct (gap 120/n, length 280).
- The page-2 guide diagram is drawn with equal scaling and reproduces the witness and the ±15 strip exactly.

**Bonus guide.**

- The price formula 7 + (d − 2)k is correct.
- The minimum number of moves, max(4, 3) = 4, is correct.
- The asymmetric-price threshold equals the sum of the two orthogonal prices. I confirmed this for (1,2), (2,1) and (2,3).
- The route counts, blocker table, predecessor rows and disjoint boundary routes are all correct.
- The quarter staircase, the 44/184 loop counts and the unboundedness argument are correct.
- The printed dimensions are correct: grid spacing 26.1 mm and 28.2 mm, unit 30 mm, half-width 7.5 mm, and 3 m of string for 100 units.
- The coin count needed is at most 10.
