# Week 55 (few sums and equal spacing): math check

Scope:
- `lowell-math-circle-year-2/week-55/week-55-students.pdf`: one combined packet headed Grades 3–5 on all 10 pages (US Letter landscape), Problems 1–10. It is the only band. The guide states that there is no K–1 sumset packet.
- `week-55-facilitator.pdf`: 9 pages (W55-F-v1).

Sources read: `source/week-55/student/students.tex`, the student README and `MATH-NOTES.md`, `source/week-55/guide/facilitator.tex` and `provenance/research.md`. I did not run or import `verify_math.py`, `verify_pdf.py` or `guide/verify.py`. pdfLaTeX is not installed here, so I could not rebuild. Every printed value was therefore read from the delivered PDFs themselves (with `pdftotext` and from 254 dpi renders) and cross-checked against the source. My scripts and their outputs are in this folder. Checked October 10, 2026.

**Result: every answer, count, grid entry, route catalogue, theorem and proof step in the packet and the guide is correct, and every diagram encodes what its text says. I found 2 problems, both minor. One is a page-1 rule whose other reading changes the Problem 5 answer from 7 to 4. The other is grey grid lines drawn across the numbers in the page-8 dots. The guide has no errors.**

## How it was checked

- **`check_math.py`** (output `out_check_math.txt`, 0 failures):
  - Parses every printed input from `students.tex` (`\pair`, `\cards`, `\arraygrid`, `\blankpair`). Confirms that each trial row (e.g. "A 0 1 2 B 0 3 6") appears in the delivered student PDF text.
  - Recomputes every answer for Problems 1–10. The kit problems are enumerated over all legal 0–9 designs:
    - P3: all 14,400 ordered 3+3 designs.
    - P4: every 2+3, 2+4 and 3+4 design.
    - P5: all 45 two-card B.
  - Checks every monotone route in the three page-8 grids.
  - Tests the general theorem exhaustively over all 4,190,209 ordered pairs of nonempty subsets of {0,…,10}:
    - the lower bound m+n−1 and the upper bound mn;
    - equality when m,n ≥ 2 if and only if both inputs are progressions with one common gap (4,079 equality cases);
    - the singleton case (all 44,913 such pairs attain the bound).
  - Checks the guide's sharpness constructions for 1 ≤ m,n ≤ 12, its index choice i = min(k, m−1), and its local-square identity at every equality case.
  - Compares every table row, catalogue entry and example in the delivered guide (via `pdftotext`) with this computation.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`, 0 failures):
  - Reads word boxes from the delivered student PDF and pixels from 254 dpi renders.
  - All 20 result lanes on pp. 1–7 have labels 0–18, 20 cell borders exactly 12.0 mm apart, and are 18 mm tall.
  - Finds all 27 dots on p. 8. Every dot is round (8.8–9.0 mm, so the scaling is equal) and is equally spaced across and up (20 mm in the demonstration, 17 mm in the tasks).
  - Every dot's number equals its row card plus its column card. Rows increase upward and columns rightward.
  - The demonstration's three bold arrows join exactly 1→3→7→11.
  - It also records, for each dot, whether the grey grid lines show inside the circle (Problem 2 below).

## Student packet (Grades 3–5, pp. 1–10): the mathematics checks out (see Problems 1–2 for two minor points)

- **Launch (p. 1):** A={1,4}, B={0,3}. The three tries are 1+3=4 (counter), 4+0=4 (already occupied) and 1+0=1 (counter). "Positions so far" shows 1 and 4, which is correct for those three tries. The full result set is {1,4,7}, and the example is not one of the task trials.
- **P1:** {0,2}+{1,3} = {1,3,5} (3) and {0,2}+{1,4} = {1,3,4,6} (4). The first trial has fewer.
- **P2:**
  - {0,1,2}+{0,1,2} = {0,…,4} (5).
  - {0,1,3}+{0,1,3} = {0,1,2,3,4,6} (6).
  - {0,1,2}+{0,3,6} = {0,…,8} (9).
  - The first has strictly the fewest and the third strictly the most.
- **P3:** over all 0–9 designs the minimum is 5 and the maximum 9. The distribution is 5:120, 6:756, 7:3812, 8:7328, 9:2384. All 120 minimal designs are common-gap progressions. Four blank records are printed, and the guide says children may change inputs between trials.
- **P4:** the minima are 4, 5 and 6 for 2+3, 2+4 and 3+4, which is m+n−1 in each case. Every minimal design is common-gap. The predicted rule "A cards + B cards − 1" is the true minimum.
- **P5:** with A={0,3,6}, exactly seven of the 45 two-card B give four totals: B={t,t+3} for t=0,…,6. Eight answer slots are printed, which is room for all seven. The largest total is 15, which fits the lane.
- **P6:** the four pairs have counts 4, 6, 4, 4. Every input is equally spaced under the page's definition, and the fewest possible for 3+2 is 4. So the answer is "no": {0,2,4}+{0,3} gives 6.
- **P7:** {4}+{0,1,3}={4,5,7}, {2}+{0,2,4}={2,4,6} and {0}+{1,4,6,9}={1,4,6,9}. The count always equals the number of B cards, for every one-card A and every nonempty B in 0–9. B need not be equally spaced, and {0,1,3} and {1,4,6,9} are not.
- **P8:**
  - Demonstration A={1,5}, B={0,2,6}: the bold route R,U,R gives 1,3,7,11, as printed.
  - Left grid A={0,2,5}, B={1,3,4}: all 6 routes visit 5 strictly increasing, different totals. The two repeated values (3 and 6) sit at positions that no single route can both visit. The full sumset has 7 values, so a route need not visit every total.
  - Right grid A={1,3,5}, B={0,2,4,6}: all 10 routes visit 6 different totals, and here every route visits the whole sumset {1,3,5,7,9,11}.
  - So: no repeats; 5 totals on every left route and 6 on every right route; strict increase explains it.
- **Count example (p. 9):** A={1,4}, B={0,2,5,8}. m=2, n=4, m+n−1 = 2+4−1 = 5 and m×n = 2×4 = 8, all printed correctly. The example's actual count is 6, which the page correctly does not state.
- **P9:** no and no. These are the two bounds, proved for all sizes; whole-number cards are a special case of the integer theorem.
- **P10:** yes, with each input having at least two cards (stated). The converse ("any two equally spaced inputs with the same gap give exactly m+n−1") is true. The page correctly excludes the one-card case, where P7 shows that equality does not force spacing.

### 1. Page 1, shared rules: "Each input has different numbers" has a second reading that changes Problem 5's answer

- **Text (p. 1, opening rules):** "Each input has different numbers."
- **Intended meaning:** no number repeats *within* an input, while A and B may share numbers. The guide says so ("the same value may occur in both inputs"), and the printed trials rely on it.
- **Other reading:** a child can read the sentence as "the inputs have different numbers from each other", meaning A and B never share a number. Each problem's answer under that reading (`out_check_math.txt`, "Other reading"):
  - P3 and P4 are unchanged: min 5 / max 9, and minima 4, 5, 6.
  - P5's "Find every two-card B" changes from 7 answers to 4: {1,4}, {2,5}, {4,7}, {5,8}. {0,3}, {3,6} and {6,9} share a number with A={0,3,6}.
  - A child working under that reading would leave out three answers that the guide's catalogue requires, without being wrong about the rule they read.
- **Mitigation:** pp. 2, 6 and 7 print trials whose A and B share numbers: 2a and 2b have A = B, 2c and the second p. 6 pair share 0, and the second p. 7 pair shares 2. An attentive child may infer the intended reading before reaching P5.
- **Smallest fix:** replace the sentence with "No number repeats within an input; A and B may share numbers."

### 2. Page 8: the grey grid lines are drawn across the numbers in 24 of the 27 dots

- **Diagram:** all three page-8 grids (the demonstration and both Problem 8 grids).
  - In `\arraygrid`, each dot's two grey segments are drawn just before that dot. The segments go to the dot below and the dot to the left, which were drawn *earlier*.
  - So each segment runs on top of the earlier dot's white fill, up to its centre.
  - Every dot that has a neighbour above shows a grey line through the upper half of its number, and every dot that has a neighbour to the right shows one through the right half. Only the top-right dot of each grid is clean.
- **Evidence (`out_check_diagrams.txt`, "draw order"):**
  - Sampling inside each circle above and to the right of the numeral gives grey ≈198 exactly where the draw order predicts, and white (255) elsewhere. That is 24 of 27 dots.
  - In a high-resolution render, the bottom-left "1" of each task grid carries a vertical and a horizontal stroke through it.
  - All numbers remain correct and are readable at 100% (the line is thin and 45% grey). This is a legibility defect, not a wrong value.
- **Smallest fix:** in `\arraygrid`, draw all the grey segments in one `\foreach` pass and then all the dots in a second pass (or put the segments on a background layer). The printed geometry is otherwise unchanged.

## Adult guide (pp. 1–9): checks out

Everything in the guide is correct:
- **Overview:** the bounds, the sharp-minimum theorem with its m,n ≥ 2 hypothesis, the singleton exception, the no-wrap caveat (ℤ/3 + ℤ/3 has 3 < 5 values) and the proof map. "Pages 7–8" correctly point to its P9 and P10 pages.
- **Problems 1–4:** every table row, the P3 chain certificate, and the P3 adult key (every 3×3 minimum is common-gap; a maximum needs every pair sum different).
- **P5:** the catalogue and its shift-overlap completeness proof (shift 3 → 2 coincidences, shift 6 → 1, all others 0). The continuations are also right: A={0,2,4} gives eight B={t,t+2}, t ≤ 7, and A={0,1,3} gives none.
- **P6–P8:** the P6 and P7 tables, the three P8 grid tables, the RRUU/UURR/RRRUU examples, and the route catalogues (3, 6 and 10 routes, each list exact). Its demonstration value set {1,3,5,7,11} is also correct.
- **P9 and P10:** the P9 example result set {1,3,4,6,9,12}, the lower-path count n+(m−1), and the minimum and maximum constructions for every positive m,n (including the 3+4 kit example {0,1,2}+{0,3,6,9} = {0,…,11}). The P10 necessity proof (shared m+n−2 vertices, one middle value each, a_{i+1}+b_j = a_i+b_{j+1}) and its sufficiency proof are both complete.
- **Return visits:** the signed example {−2,0,2}+{−3,−1,1} = {−5,−3,−1,1,3}.
- **Preparation figures:** the kit and print figures it gives (19 cells of 12 × 18 mm = 228 mm; 9 mm dots; ten 792 × 612 pt pages; 24/48/12 pattern blocks, which is 4 × the Week 1 guide's 6/12/3 per K–1 child) match the delivered PDFs.

I could not check the guide's source citation "Tao–Vu Lemma 2.1 … max(|A|,|B|)" against the book sample, which is not in this checkout. The mathematical statement itself is true in any group.
