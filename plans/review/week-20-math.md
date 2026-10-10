# Week 20 (averaging and the maximum principle): math check

Scope: everything current in `lowell-math-circle-year-2/week-20/`, archive folders excluded:

- `week-20-k-1.pdf` (GA20-K-v3, 7 pp., P1–P7)
- `week-20-grades-2-3.pdf` (GA20-23-v2, 6 pp., P1–P6)
- `week-20-grades-4-5.pdf` (GA20-45-v3, 7 pp., P1–P7)
- `week-20-facilitator.pdf` (26 pp.: the guide on pp. 1–25 and a route update on p. 26)
- the bonus companion `week-20-bonus.pdf` (W20-BON-v1, 5 pp., P1–P6) and its guide `week-20-bonus-facilitator.pdf` (W20-BON-FAC-v1, 5 pp.)

Sources read: `source/week-20/editable/src/build_packets.py` (node coordinates and edge lists), and `facilitator-src/content.py` only to locate the fix below. The six delivered PDFs are byte-identical (same MD5) to the reference copies in `source/week-20/editable/reference-pdfs/` and `source/week-20-bonus/reference-pdfs/`. I did not run or import any of the package's own checkers (`build_packets.py`'s sympy check, `check_worked_examples.py`, `facilitator-src/check_math.py`, `verify*.py`, the bonus `independent-check.py` and `guide-independent-check.py`), and did not read the review or answer notes. Checked October 10, 2026.

**Result:**
- **Student pages:** every problem in all three bands and the bonus has the answer its page implies. Nothing asked for is impossible, and every "find every way" task has exactly as many answers as the guide says. On K–1 the number of recording diagrams matches: 10 for P3, 8 for P4, and 6 plus the large board for each P7 board.
- **Adult guides:** every answer, list, count, proof, hint and extension in both guides is correct.
- **Problems found:** 1 (minor, base guide): three cross-references send the adult to guide p. 3 for arguments that are on p. 4.

## How it was checked

My scripts and their saved outputs are in this folder. Each script finds the repository by walking up from its own location, so it runs from `plans/review/checks/week-20/` or from `tmp/review-runs/week-20/`. They need only Python 3 and Poppler (`pdftocairo`, `pdftotext`, `pdfinfo`).

- **`extract_boards.py`** → `boards.json`, `out_extract_boards.txt`. It reads every board out of the delivered PDFs, not the `.tex`:
  - It converts each page to SVG and classifies the vector paths: squares, circles, joining lines, dots, small cubes, dashed mats, cards and the dashed outline.
  - It reads word positions with `pdftotext -bbox`.
  - A line is an edge when both ends lie on two different vertex borders. In the guide and bonus, lines run centre to centre under opaque vertices; a line that passes under another vertex is split there.
  - It records the numeral inside each vertex and, in K–1, the dots or cubes drawn inside it.
  - It covers all student pages, the 4 + 5 bonus/guide boards, and every solution diagram in the base guide (pp. 5–24).
- **`check_math.py`** → `out_check_math.txt` (231 checks, 3 failures, all Problem 1 below). For every board it computes the filling by exact rational Gaussian elimination and reports the nullity, so "no second filling" is proved over the reals, not just over a search range. It also:
  - enumerates every bounded "find all" task;
  - tests every single-square change on 2–3 P1;
  - confirms each guide diagram is isomorphic to its student board (same squares, values and lines) and that its printed circle values pass every check;
  - confirms each quoted guide sentence appears in the delivered PDF before recomputing it;
  - tests the overview's theorems on random graphs: the weak bound on 3,000 random anchored graphs, under both readings of "reach", and the strong (equality-propagation) form in 10,348 circle checks.
- **`check_bonus.py`** → `out_check_bonus.txt` (35 checks, 0 failures). It computes:
  - exact expected scores, plus 200,000 simulated walks from each start;
  - both tick rules with exact fractions for 60 ticks;
  - every state in 0..6⁴ under the neighbour-only rule;
  - every roughness score;
  - the energy-minimisation proof against 7,954 random competitors;
  - the gap-square and squared-paper geometry.

## Geometry common to all bands

- **Shapes:** every circle is round and every square vertex is square, so scaling is equal in both axes.
- **Sizes:** K–1 working vertices are 85.7 pt = 3.02 cm, matching the guide's "about 3 cm". K–1 recording copies are 30.2 pt (P3, P7) and 34.6 pt (P4). Grades 2–3 and 4–5 vertices are 49 pt. Bonus working vertices are 85 pt (30 mm), as the bonus guide asks.
- **Neighbours:** every circle has at least one neighbour. The most neighbours of any circle are 3 in K–1, 3 in Grades 2–3 and 4 in Grades 4–5, which matches the guide's prerequisites ("two or three equal piles", "divide by 2 or 3", "average up to four neighbors").
- **K–1 counts:** every K–1 square shows exactly as many dots as its numeral, and every example shape and sharing mat shows the right number of cubes. The mats hold 3, 3 on p. 1, then 3, 3 and 4, 4 on p. 2.

## K–1 (7 pp.): checks out completely

- **p. 1 example:** 0 and 6 share into two mats of 3, and the circle is 3.
- **P1:** the circles are 1, 3, 2, 4 in reading order.
- **p. 2 example:** the chain 2–3–4–5 works at both circles. The check panels are 2 + 4 → 3, 3 and 3 + 5 → 4, 4.
- **P2:** (1,2), (2,1), (2,4), (4,2). Each is unique (nullity 0).
- **P3:** with circle 2 and squares 0–3 there are exactly 10 ordered fillings, of 3 shapes: (0,3,3), (1,2,3) and (2,2,2). The page has 10 recording boards.
- **P4:** with three different cards from 0–4 there are exactly 8 ordered fillings: {0,1,2}, {1,2,3}, {2,3,4} and {0,2,4}, each with its reversal. The page has 8 recording boards.
- **P5:** the fillings are (1,2) and (2,3), both unique, so no 5-cube circle is possible. Brute force over circles 0..20 confirms that these are the only whole fillings.
- **P6:** the triangle's circles are all 2 and the four-cycle's circles are all 3. Both are unique, so the answer is "no".
- **P7:** the triangle and the 4-circle path each have exactly 6 fillings with 0–5, all of them constant.

## Grades 2–3 (6 pp.): checks out completely

- **P1:** the circles are 4, 4, 5, 5 in reading order. The only single-square changes (searched over 0..60) that raise a circle by exactly 2 are +4 to either square on a two-neighbour board and +6 to any one square on a three-neighbour board.
- **p. 2 example:** checks out, and its arrows point to the right circles.
- **P2:** (3,6), (5,8), (3,3), and tree circles 4 then 6. All are unique.
- **P3:** the path is 3, 5, 7 and the tied diamond 5, 5. No circle exceeds every square, so the answer is "no".
- **P4:**
  - Upper board: 3, 6, 6. Two circles equal the biggest square, 6.
  - Lower board: 0, 0, 3. Two circles equal the smallest square, 0.
  - So both questions have the answer "yes", each on one board.
- **P5:** (6,9); tree 5, 7; diamond 7, 7. Each has nullity 0, so no second filling exists.
- **P6:** the four-cycle and the 3-circle path each have exactly 6 fillings with 0–5, all of them constant.

## Grades 4–5 (7 pp.): checks out completely

- **p. 1 example:** correct.
- **P1:** (5,10); tree 5, 7; tied diamond 8, 8. All are unique, so a second filling cannot be found.
- **P2:** the upper board's circles are 3, 6, 7, 8. The circle joined to 0 is 3, and the circle with four neighbours, including the diagonal, is 6. The lower diamond's circles are 6, 6. No value reaches 13, or even 11.
- **P3:** the illustration fills as 4, 6, 8 with 6 on top. The stated theorem is true under the page's hypotheses, whether "reach" allows passing through squares or not (random-graph test).
- **P4:** both boards fill as 4, 8, 8.
  - Upper board: two circles equal the largest square, 8.
  - Lower board: no circle equals 12.
- **P5:** the two printed boards are identical, with left 6, upper 10 and lower 8. The filling is unique.
- **P6:**
  - The upper triangle has 5 fillings with 0–4.
  - The lower board is two joined pairs inside one dashed outline (no line between them), so it has 5 × 5 = 25 fillings.
- **P7:** the boards fill as 1/2; 1, 2; 1; and 1/3, 2/3. The cards are drawn as 1/2, 1/3 and 2/3: equal 86.4 pt bars cut into equal parts, with 1, 1 and 2 parts shaded. These are exactly the three fractions needed.

## Bonus companion (5 pp., Grades 2–5): checks out completely

- **P1:**
  - The upper board is the path 0–A–B–6, and C is joined to squares 0, 3 and 6.
  - The exact expectations are A = 2, B = 4 and C = 3. Simulation gives 1.999, 3.998 and 3.000.
  - Twelve-walk sample means from A range from 0 to 5.5, so the page rightly asks for an estimate, not equality.
- **p. 2 example:** 0, 3, 6 → 3, 3, 3 under the neighbour-only tick.
- **P2:**
  - The printed four-cycle reads TL 0, TR 6, BR 0, BL 6, which matches the table's tick-0 row.
  - It goes 0,6,0,6 → 6,0,6,0 → 0,6,0,6, so it first returns after two ticks.
  - Among all whole states in 0..6, exactly 42 first return after two ticks, all of the form a,b,a,b with a ≠ b. So "a different starting state" exists.
- **P3:** the neighbour-only rule swaps 0,6 forever. The own-and-neighbour rule settles at 3, 3 after one tick.
- **P4:**
  - The next three boards are 4,2,4,2; 8/3,10/3,8/3,10/3; 28/9,26/9,28/9,26/9.
  - No value equals 3 in 60 ticks.
  - The formula 3 ∓ 3(−1/3)^t holds throughout.
- **p. 4 example:** 0–1–3 scores 1 + 4 = 5. The two gap squares are 19.8 pt and 39.7 pt (ratio 2.000), and the larger is cut 2 × 2. The squared paper on pp. 4–5 is 14.17 pt (5 mm) in both directions.
- **P5:** the scores for x = 0–6 are 36, 26, 20, 18, 20, 26, 36, so the unique minimum is 18 at 3.
- **P6:** of the 49 pairs, the unique minimum is 12 at (2,4).
- **Bonus guide:** every claim is correct. That covers the A/B equations, the 1/3 and 2/3 stopping chances, the (1/2)^n survival bound, the 0,3 scaling extension, the alternating-state analysis and its formula, both score identities, the (B−A)²/L path bound and the energy-minimisation proof.

## Base adult guide: correct throughout, apart from three page references (Problem 1)

- **Overview (p. 1) and adult tools (p. 4).** The following are true with the stated hypotheses:
  - the maximum principle for circle groups and the squares touching them, including equality propagation;
  - existence and uniqueness when every circle reaches a square;
  - constants on circle-only components;
  - the equal-gap rule on paths;
  - the signed-difference uniqueness proof, which the guide rightly says does not prove existence.
- **Keys (pp. 5–24):** every list and count matches my computation:
  - K–1: 10 and 8 fillings, the 13 ordered triples with repeats, 10 again with circle 1, and the forced-check numbers on p. 9;
  - Grades 2–3: the P1 change rule, the +1 tree equal to P5's middle tree, and 36 for the two P6 boards together;
  - Grades 4–5: the 3,6,7,8 board, 625 four-tuples, and the path integrality criterion.
- **Diagrams:** every guide diagram is the student board with correct values.
- **Other figures:** the supply count of 73 sheets (4 × 7 + 4 × 6 + 3 × 7) and the route note on p. 26 are also correct.

### Problem 1 (minor, base guide pp. 9, 16 and 18): three cross-references point to page 3, but the argument is on page 4

- **Text:**
  - K–1 P5, p. 9: "The equal-gap argument on page 3 fixes these pairs."
  - Grades 2–3 P5 hints, p. 16: "ask how two proposed fillings differ at each place, then use page 3."
  - Grades 4–5 P1, p. 18: "The general proof is held until Problem 5, but is available on page 3."
- **Evidence (`out_check_math.txt`, last section):**
  - Guide p. 3 is "Preparation and the hour" (materials, launch and timing).
  - The "Averages and equal gaps" and "Uniqueness" arguments are on p. 4, "Adult mathematical tools". The guide's own navigation also places the tools on pp. 3–4, and its footers number p. 4 as "4 / 25".
  - The archived guides have the same layout, so these references have never pointed to the argument.
  - An adult who follows them finds no argument. No answer is affected.
- **Smallest fix:** in `source/week-20/editable/facilitator-src/content.py`, change "page 3" to "page 4" in the three strings at lines 62, 115 and 129.
  - For the Grades 2–3 hint, "then use the Problem 3 argument (or page 4)" would also be correct, since the difference board is finished by the same maximum argument.
  - Then rebuild the guide.

## Not checked

- **Source citations:** the Doyle and Snell section and page references (guide p. 25: "sections 1.1.5 and 1.2.2, especially PDF pages 11 and 17"), the Rozhkovskaya and *Math Circle by the Bay* references, and the bonus guide's source page ranges. The books are not available in this checkout.
- **Physical fit:** cube supply, mats and fair-draw slips are untested, as both guides state.
