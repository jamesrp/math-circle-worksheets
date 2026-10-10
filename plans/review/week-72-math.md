# Week 72 (A robot that remembers area): math check

Scope:
- `lowell-math-circle-year-2/week-72/week-72-students.pdf`: one shared Grades 4–5 packet of 5 pages. Problems 1–4 are on pp. 1–4, and p. 5 holds the apparatus (memory strip, extensions and move cards).
- `week-72-facilitator.pdf`: the adult guide, 3 pages.

Sources read: `source/week-72/student/students.tex` and `guide/facilitator.tex`, plus the package's README, MATHEMATICS.md and SOURCES.md. I did not run or import any checker from the package. My scripts and their saved outputs are in `plans/review/checks/week-72/`. Checked October 10, 2026.

**Result: every answer, count, construction and theorem in the packet and guide is correct. Every board, outline, label and apparatus size matches its text. I found 1 problem, a minor diagram artifact on student p. 1.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 68 checks, 0 failures) simulates the robot from the printed card rules alone.
  - **Problems 1–4.** It enumerates the 6 two-E/two-N routes and all 24 orders of E, N, W, S. It walks the four P3 outlines in both directions and from every starting corner, and it checks both P4 witnesses: their memories at each vertical move, that they stay on the board and the strip, and how many cards they use. It also checks the uniform every-integer plan for k = −60…60: the route ends at (2,2) with memory k, stays in 0 ≤ x, y ≤ 2, and reaches the ring only at the end.
  - **Group law.** It confirms the Heisenberg law as matrix multiplication, its associativity, the generators acting by right multiplication, the inverse, the central states, and the symmetric-coordinate law with t = z − xy/2.
  - **General claims, checked finitely.** Over all 87,381 words of length ≤ 8 it checks four facts:
    - memory equals algebraic area (the winding-number sum) on all 5,341 closed words, repeated and self-crossing ones included;
    - memory equals the shoelace signed area on every simple closed word;
    - translating a closed loop leaves its memory unchanged;
    - for an open word, the signed area of the path closed by a straight chord is z − xy/2.
  - **Guide text.** It reads the delivered guide PDF and compares the P1 table, the P2 answer, witnesses and counts, the P3 answers, the P4 table and the apparatus sizes with the computation.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 64 checks, 1 failure, which is Problem 1 below) uses pymupdf to read the delivered student PDF's vector drawings and text positions. It places each board on its own grid lines and column and row labels, then checks:
  - the four launch panels;
  - the P1, P2 and P4 boards: square cells, the labels, O at (0,0) and the ring at (2,2);
  - the four P3 outlines, read back as lattice polygons and re-walked to get their memories;
  - the p. 5 apparatus: 21 ticks at 7.200 mm labelled −10…10, two 11-tick extensions at the same spacing, and an 8 × 4 grid of 18.00 mm cards with 8 each of E, W, N and S.
- The Duchin–Mooney source could not be fetched (arxiv.org is blocked by the egress proxy) and is not in the repository. The guide's p. 3 page references and the claim "Duchin–Mooney use the coordinate t = z − xy/2" are therefore unchecked against the source. The conversion itself is internally correct: `check_math.py` verifies the stated symmetric law from t = z − xy/2.

## Problems found

### 1. The p. 1 "start" panel draws a stray north arrow (minor, diagram)

- **Where:** student p. 1, the shared launch panels before Problem 1, first panel, captioned "start: memory 0".
- **What is wrong:** the source calls `\examplepanel{(0,0)--(0,0)}{(0,0)}{start: memory 0}` (`students.tex` line 37). TikZ draws the zero-length path with its Stealth tip. The delivered PDF has a 1.8 pt stroke and a filled arrowhead pointing up, just under the start dot. That is 0.13 grid units, about 0.6 mm, sitting on the "0" label. At 300 dpi it reads as a tiny ↑ (N) mark. No move has been made in this panel, so the panel shows an arrow the caption says did not happen. This is also the panel that teaches the conventions.
- **Evidence:** `check_diagrams.py.out`: `FAIL p1 panel "start: memory 0": no move drawn -> found 1 segment(s) of total length 0.13 units and 1 arrowhead(s); head points up`. The other three panels match EE → (2,0), EEN → (2,1) and EENE → (3,1) exactly.
- **Smallest fix:** draw only the dot in the start panel. Either give that panel a `\draw` with a single coordinate, as in `\examplepanel{(0,0)}{(0,0)}{start: memory 0}`, or draw it without the arrow line. This is untested here because pdfLaTeX is not installed. Re-render to confirm no arrowhead remains.

## Student packet

All four problems check out, apart from Problem 1 above.

- **Launch example (p. 1):** EE ends at (2,0) with memory 0, EEN at (2,1) with memory 2, and EENE at (3,1) with memory 2. The captions are correct.
- **P1:** there are exactly 6 routes, and all end at the ring (2,2). Their memories are EENN 4, ENEN 3, ENNE 2, NEEN 2, NENE 1 and NNEE 0, so five memories, {0,…,4}, are possible. The page has 7 answer lines, and the board has 0–3 columns with square cells.
- **P2:** all 24 orders return to O. The possible memories are exactly −1, 0 and 1, occurring 4, 16 and 4 times. No other memory occurs, so the "Can any other memory occur?" question has the answer no. Every route stays within |x|, |y| ≤ 1, inside the −2…2 board.
- **P3:** the outlines read back from the PDF are 2-by-1 rectangles with left columns 0, 2 and −3, and the L with corners (0,0), (2,0), (2,1), (1,1), (1,2), (0,2). Each start dot is at the bottom-left corner. The rectangles give +2 counterclockwise and −2 clockwise; the L gives +3 and −3. Each value equals the signed area, so horizontal translation does not change the memory. The answer is the same from any starting corner.
- **P4:** both targets are reachable, and every integer is reachable at (2,2). The shortest routes for 7 and for −3 both have 8 moves. The board runs −1…4 on both axes, with O at (0,0) and the ring at (2,2).
- **Apparatus (p. 5):** ticks are 7.2 mm apart and cards are 18 mm. An extension overlapping one tick adds 10…20 or −20…−10, as the guide says.

## Adult guide

The guide checks out completely: the overview's facts and their stated limits, and every solution, hint and extension. The details:

- **Overview:**
  - The memory is the sum of x Δy over vertical steps.
  - EN gives memory 1 and NE gives 0.
  - A simple closed loop gives its signed area, positive counterclockwise. Translation never changes a loop's memory.
  - A self-crossing or repeated loop gives its algebraic area, not the area of the union; ENWSENWS gives 2.
  - The unit-loop construction reaches every integer.
  - For an open path, the chord-closed area is z − xy/2.
- **P1:** the E-positions 12, 13, 14, 23, 24 and 34 give the six table words in order.
- **P2:** the witnesses NESW, EWNS and ENWS give −1, 0 and +1, and the counts are 4, 16 and 4. The argument that the visited columns lie in {0,1} or {−1,0} holds for all 24 orders.
- **P3:** the routes EENWWS and EENWNWSS give 2 and 3. The differences 2−0, 4−2 and (−1)−(−3) are correct. The cancellation proof, and the formula h·ΣΔy = 0 for horizontal translation, are correct.
- **P4:** EEEENWNW ends at (2,2) with memory 7, recording 4 and then 7 at its vertical moves. NNNENESS ends there with memory −3, recording 0, 0, 0, 1, −1, −3. After NNNEN the robot is at (1,4) with memory 1. Both routes stay on the printed board and the −10…10 strip, and they use at most 8 cards of each kind. The uniform plan is correct for every k, stays in 0 ≤ x, y ≤ 2, and first reaches the ring at its last step.
- **Extension:**
  - Matrix multiplication gives the stated law, so it is associative, and right multiplication by the generators gives the card rules.
  - The states (0,0,k) are central.
  - The symmetric law follows from t = z − xy/2.
  - EENN has memory 4 and symmetric height 2.
  - The closing chord contributes −xy/2.
  - At column −2, N then S takes the memory to −2 and back to 0.

Outside the packet: `source/week-72/MATHEMATICS.md` gives the order of the six counters as "the order in `topics.json`". That file is not in the package or the source ZIP, so the reference is stale. The values 4, 3, 2, 2, 1, 0 are correct in the guide's EENN…NNEE order.
