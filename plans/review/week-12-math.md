# Week 12 (Catalan bijections): math check

Scope: `lowell-math-circle-year-2/week-12/week-12-k-1.pdf` (6 pp., Problems 1–6), `week-12-grades-2-3.pdf` (6 pp., Problems 1–6), `week-12-grades-4-5.pdf` (6 pp., Problems 1–6) and `week-12-facilitator.pdf` (10 pp.; p. 10 is the 4 October route update). I also checked the return-visit companion in the same folder: `week-12-return-visit.pdf` (4 pp., Problems 1–4) and `week-12-return-visit-facilitator.pdf` (5 pp.). Archive folders were ignored. My scripts and their outputs are in this folder, for `checks/week-12/`. Checked October 10, 2026.

**Result: no mathematical errors on any student page, in either guide's overview, or in any stated answer, list, count, proof or extension. Every diagram matches its text. I found 2 problems, both in the base adult guide. The K–1 Problem 4 hint gives a one-dot comparison as the test for duplicates, which is false. The route update describes Grades 2–3 Problems 3–5 in the wrong direction.** Two layout notes outside the math check follow at the end.

## How it was checked

- All six delivered PDFs are byte-identical (MD5) to the reference copies in `source/week-12/editable/reference-pdfs/` and `source/week-12-return-visit/reference-pdfs/` (`check_files.out`).
- `pdfgeo.py` is my own reader. It uses pdfplumber only to read path operators and words, and classifies circles, Bézier arcs, polylines and rectangles in page coordinates. No packet builder or checker is imported.
- `catalan.py` checks the mathematics independently of the PDFs (178 checks, `catalan.out`). It uses three separate generators:
  - every perfect matching of 1..2n by brute force, filtered by an interleaving test;
  - every U/D string of length 2n, filtered by prefix heights;
  - ordered trees built from compositions of the root's branches, not from the first-return split the guide uses.

  For n ≤ 6 the three counts agree: 1, 1, 2, 5, 14, 42, 132. The pairing code and the tree walk are bijections onto Dyck words. Uniqueness of the inverses is checked by search over all matchings or trees, not by the stack rule, for n ≤ 5. Even with crossing pairings allowed, the codes of all pairings are exactly the Dyck words (n ≤ 5). Peaks equal leaves, maximum height equals tree depth and deepest arc nesting, and returns to zero equal root children (n ≤ 6). The first-return split and the tree split are bijections (n ≤ 6). It then recomputes every answer the pages imply and every numbered claim in both guides.
- The four diagram checks read every drawing from the PDFs and solve each problem from what they read:
  - `check_k1.py` (19 checks) reads all 41 circles: dot counts, equal angular spacing from the top, the labels 1..n clockwise, and every printed chord.
  - `check_23.py` (27 checks) reads every dot row, label and arc. It also reads every grid: cell count, squareness, and the start and end dots. It reads every path as a U/D word, every step letter, every box and every printed code.
  - `check_45.py` (18 checks) rebuilds every tree from its node circles and edges as an ordered tree, with the parent being the higher end and children ordered by x. It reads the four walk arrows (direction from the arrowhead, number and letter from the nearest label), the example path and its step letters, the boxes, the printed roots and the codes.
  - `check_rv.py` (22 checks) reads all 21 counter boards (letter, colour, 60° positions, the A/B/C panel letter) and the ten ceiling boards (8 × 2 square cells, dashed line exactly at height 2, labels 0 1 2, S and E). It also reads every page-4 path, the blue marks, the cards and the Input/Output/Start/Target captions.
- `check_guide.py` (30 checks) reads every pairing, path and tree in the guide galleries (pp. 6–8) and compares each with its printed code. It also scans both guides' text for every pairing record (17 in the base guide, 5 in the return-visit guide) and every U/D word (25 and 12). Each record must be a complete noncrossing pairing; the base guide's "13|24 crosses" is the one intended exception. The only non-Dyck words must be the five the guide calls invalid.

## K–1: checks out completely

- **Example (p. 1):** the two drawings are 12|34 and 14|23, the only two noncrossing pairings of four dots. With crossings allowed there are three.
- **P1–P2:** there are exactly five six-dot pairings: 12|34|56, 12|36|45, 14|23|56, 16|23|45 and 16|25|34. By 1's partner (2, 4, 6) the split is 2 + 1 + 2. Each page has a large mat and 6 record circles.
- **P3:** the six record circles carry 14, 14, 16, 16, 13 and 15, read from the PDF. 14 has exactly two completions (14|23|56|78, 14|23|58|67), and so does 16 (16|23|45|78, 16|25|34|78). 13 and 15 have none: they leave 1 and 5 dots, or 3 and 3, on the two sides. Each start appears exactly as often as it has completions, or once when it has none.
- **P4:** 14 eight-dot pairings. By 1's partner (2, 4, 6, 8) they split 5 + 2 + 2 + 5. The page has 7 circles plus "blank paper".
- **P5:** the circles have 10, 3, 4, 5, 6 and 7 dots. The even ones can be paired (42, 2 and 5 ways; adjacent pairs always work) and the odd ones cannot.
- **P6:** no. Every noncrossing pairing of 4, 6, 8, 10 or 12 dots joins at least two pairs of circular neighbours. The answer is the same whether or not 8–1 counts as neighbours, since an innermost pair i, i+1 always exists. With crossings allowed, 31 eight-dot pairings avoid neighbours (e.g. 13|24|57|68), so the noncrossing rule is what makes it true.
- All circles are regular, with dots at exact multiples of 360°/n from the top, and labelled 1..n clockwise.

## Grades 2–3: checks out completely

- **Rules example (p. 1):** the ten-dot row is 14|23|5-10|67|89, noncrossing.
- **P1:** five pairings. The page has a large row (24 mm spacing) and 6 small rows.
- **Code example (p. 2):** the drawn pairing is 12|36|45|78. The letters under the dots read UDUUDDUD, the grid path is UDUUDDUD, and each of the 8 step letters sits above its own step.
- **P2:** the drawn pairings are 16|25|34, 14|23|56 and 12|34|56, with codes UUUDDD, UUDDUD and UDUDUD. Each path stays at or above 0, ends at 0 and fits its 6 × 3 square grid. Each pairing has six boxes.
- **P3:** the drawn paths are UUDUDD, UDUUDD, UUDDUUDD and UUUDUDDD. Each has exactly one noncrossing pairing: 16|23|45, 12|36|45, 14|23|58|67 and 18|27|34|56. With crossings allowed, the same paths have 3, 1, 3 and 17 further pairings, so "without crossings" is what makes the answer "no".
- **P4:** five paths, with six empty 6 × 3 grids.
- **P5:** UUUDDUDD gives 18|25|34|67 and UUDUDUDD gives 18|23|45|67. UDDUUDUD goes below 0 at letter 3. UUUUDDUD has five U and ends at height 2. Even allowing crossings, neither invalid string is the code of any pairing.
- **P6:** 14 pairings, with 16 rows.

## Grades 4–5: checks out completely

- **Rules example (p. 1):** the tree reads UUDUDDUUDD. The root has two children; the left has two leaf children and the right has one.
- **P1:** five three-edge trees, with 6 printed roots. By the number of root children (1, 2, 3) they split 2 + 2 + 1.
- **Walk example (p. 2):** the arrows read 1 U away and 2 D back on the left edge, then 3 U away and 4 D back on the right. The grid path is UDUD with matching step letters. "Walk code: UDUD".
- **P2:** the four drawn trees read UUUUDDDD, UDUDUDUD, UUDUDDUD and UDUUUDDD, with 8 boxes each.
- **P3:** UUDDUD, UDUUDD, UUDUDUDD and UUUDDUDD each describe exactly one tree, so the answer to "two different trees?" is no.
- **P4:** the valid codes are UUUUDDDD, UDUDUUDD and UUUDUDDD. UUDDDUUD first goes below 0 at letter 5, DUUUDDUD at letter 1, and UUDUDUDU ends at height 2.
- **P5:** 14 trees, with 16 printed roots.
- **P6:** 42 trees with five edges and 132 with six.

## Adult guide

The overview is true with the hypotheses it states: fixed labels, no crossings, and ordered (plane) rooted trees. It covers the three bijections and their forced inverses (stack rule; rightmost child at U, parent at D), C(0) = 1 with the first-return recurrence, parity, the fixed-chord criterion (even counts on both sides), and the inevitable circular-neighbour pair.

Every key matches my computations:

- **K–1:** the P2 list and 2/1/2 split, the P3 completions and trapped counts, the P4 5/2/2/5 split, the P5 parity argument, and the innermost-pair proof in P6.
- **Grades 2–3:** the ten-dot example, the P2 codes and height sequences, the P3 pairings and the crossing argument for forced closing, and the P5 validity reasons and pairings.
- **Grades 4–5:** the P2 codes and readable features, the P3 descriptions, the P4 letter positions, and the P5–P6 counts C(4) = 5+2+2+5, C(5) = 14+5+4+5+14 and C(6) = 42+14+10+10+14+42.
- **Galleries:** every one of the 5 + 14 + 4 gallery drawings on pp. 6–8 (pairing, path and tree) has its printed code.
- **Extensions:** maximum height equals depth equals nesting, peaks equal leaves, and four points with crossings give UUDD twice.

### 1. K–1 Problem 4 hint: a one-dot comparison is given as the duplicate test (guide p. 4)

- **Quoted text:** "Group by 1's partner: 2, 4, 6, 8 give 5, 2, 2, 5 completions. Hint: compare only the partners at a single numbered dot to check for duplicates."
- **Evidence:** two drawings are the same pairing only when every dot has the same partner. For every dot d, the 14 eight-dot pairings fall into groups of 5, 2, 2 and 5 by d's partner. So 22 pairs of different pairings agree at any chosen dot (`catalan.out`). For example, 12|34|56|78 and 12|38|45|67 agree at dot 1 but differ. Two different pairings can agree at up to 4 of the 8 dots. An adult using the hint as written would tell a child that a correct new drawing is a repeat. A single-dot comparison can only show that two drawings are different.
- **Smallest fix:** "Hint: two drawings are the same only if every dot has the same partner. Sort the drawings by 1's partner, then compare partners dot by dot within each group."

### 2. Route update: Grades 2–3 Problems 3–5 are described in the wrong direction (guide p. 10)

- **Quoted text:** "Grades 2-3 can use their pairings to rebuild codes (P3-5), then collect eight-dot pairings (P6)."
- **Evidence:** P3 ("Draw a pairing for each path") and P5 ("Draw the pairing whenever it is possible") rebuild pairings from codes, which is the inverse map. Only P4 starts from the children's pairings ("Match your paths to your six-dot pairings"). Writing codes from pairings is P2. An adult preparing a return visit from this line would set up the forward encoding the children have already done, not the inverse question that P3 and P5 ask.
- **Smallest fix:** "Grades 2-3 can rebuild pairings from codes and decide which codes are legal (P3-5), then collect eight-dot pairings (P6)."

## Return visit: checks out completely

- **P1 (pp. 1–2):** the boards read A = RBRBRB, B = RRRBBB and C = RRBRBB clockwise from the top, the same on the large board and all 6 workspace copies, with letters matching counter colours. The unlike noncrossing pairings number 5, 1 and 2, exactly the guide's lists. An unlike pairing exists exactly when the R and B counts agree (all words up to 10 dots).
- **P2–P3 (p. 3):** ten 8 × 2 square boards with the dashed ceiling exactly at height 2. There are 8 ceiling-2 paths, the guide's 8, which correspond to the compositions of 4. With five pairs there are 16. In general there are 2^(n−1) paths (n ≤ 7), and every ground block is U(UD)^(r−1)D. Ceilings 1, 2, 3 and 4 give 1, 8, 13 and 14 for four pairs, and ceiling 3 excludes only UUUUDDDD.
- **P4 (p. 4):** the example input UDUUDD becomes UUDUDD. The blue marks cover steps 2–3 (DU, then UD), and the cards read D U → U D. The target UUUUDDDD is drawn as captioned. The starts are drawn as captioned and lie 6, 4 and 1 moves from the target by BFS over legal swaps. Both printed routes are legal one-swap chains. The distance to the mountain equals half the summed height gap, which equals the number of D-before-U pairs, for every path with n ≤ 6. Every legal swap changes this score by exactly one.
- **The guide's limit:** "A score alone does not give the distance between two arbitrary paths" is right. Score differences fail for 42 ordered pairs at n = 4. The true distance, half the summed height gap between the two paths, holds for all pairs with n ≤ 5, so that extension does need its own argument.

## Notes outside the math check (not counted)

- **Base guide p. 3, timing menu:** "Choose depth: K-1 P3 or P6 … P4/P6 in K-1 … are surplus work." This lists K–1 P6 both as a depth choice and as surplus. K–1 P5 (parity) appears in no route, here or in the p. 10 update.
- **K–1 pp. 2–5, large mats:** the bottom label of each large mat ("4", "5", "5", "6") is 12.6 mm below its own dot and 11.9 mm above the top dot of the middle record circle, directly above that circle's own "1". The labels are correct, and the 12.5 mm gap keeps them clear of 20 mm discs, so they cannot simply move inward. Lowering the record rows by a few millimetres would remove the near-tie (`check_k1.out`).
