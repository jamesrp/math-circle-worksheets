# Week 25 (row and column shadows): math check

Scope: everything current in `lowell-math-circle-year-2/week-25/`, archive folders excluded:

- `week-25-k-1.pdf` (W25-K-v3, 8 pp., P1–P6)
- `week-25-grades-2-3.pdf` (W25-23-v2, 6 pp., P1–P5)
- `week-25-grades-4-5.pdf` (W25-45-v2, 7 pp., P1–P5)
- `week-25-facilitator.pdf` (20 PDF pages: an unnumbered overview, printed pp. 1–18, and an appended route note). Guide page numbers below are the printed ones.
- The bonus companion `week-25-bonus.pdf` (W25-BON-v1, 4 pp., P1–P4) and its guide `week-25-bonus-facilitator.pdf` (W25-BON-FAC-v1, 5 pp.).

Sources read: `source/week-25/editable/src/` (`build_packets.py`, `examples.py`), `facilitator-src/build_guide.py`, and `source/week-25-bonus/student-src/bonus.tex`. The delivered PDFs are byte-identical to the reference copies in both source folders. I did not use the packet's own answer files, verifiers or checker scripts, and I opened no use logs or session records. Checked October 5, 2026.

**Result: no mathematical errors in any student band, including the bonus. The base adult guide has one wrong statement in a held hint (minor). There is also one label-only numbering issue, which is not mathematical. Every answer, count, route and diagram in both guides is correct.**

## How it was checked

My scripts and their saved outputs are in [checks/week-25/](checks/week-25/). Each script finds the repository from its own location. Run `extract.py` first; the check scripts run it themselves if `extracted.json` is missing.

- `common.py`: my own enumeration of all 0/1 pictures with given margins (row-subset search), the list of legal switches, and breadth-first switch distances.
- `extract.py` → `extracted.json`, `extract.out`: reads every board back out of the vector drawings in the three student PDFs and the guide. For each board it records grid size, cell size on both axes, row letters, column numbers, circled counts and counters. All 80 student boards have square cells at one scale (22 mm; 20 mm on 4–5 p. 3; 8 mm for the small switch examples). The 78 guide answer sketches also have square cells, at 7–10 mm. All labels are A, B, C / 1, 2, 3…. Wherever counters and counts are both printed, they agree.
- `check_students.py` → `check_students.out`: solves every student problem from the extracted margins and pictures. It also checks that the K–1 example sweeps stay in their own row or column and end at that line's circled count.
- `check_guide.py` → `check_guide.out`: checks every guide board, with the caption read from the PDF, against the complete solution sets, switch lists, routes and distances. It also checks the general claims (uniqueness criterion, two-row distance and diameter formula, the count C(s, k), connectivity), the verification numbers on p. 18 and the cross-references between guide pages.
- `check_bonus.py` → `check_bonus.out`: reads the bonus grids, counters, dashed diagonals with their d-labels, candidate pictures and bold margins from the PDF. It then computes the diagonal signatures, the adaptive minimax depth over cell questions, every prechosen cell set of size 1–5, and the four margin boards.

## K–1: checks out completely

- **p. 1 example:** A1 and A2 give rows 2, 0 and columns 1, 1. The dashed row sweeps and dotted column sweeps each stay in their own line and end at its circled count.
- **P1:** the three pairs have 2, 2 and 3 pictures, so "two different pictures" works for each.
- **P2:** rows 1, 2 and rows 2, 1 (columns 1, 1, 1) have exactly 3 pictures each. Three grids are printed for each.
- **P3 (pp. 4–5):** exactly 6 pictures, on 4 + 2 grids.
- **P4:** on p. 5, rows 3, 1 with columns 2, 1, 1 have one picture (111/100), so the answer is no. On p. 6, rows and columns 2, 1, 0 have one picture (no); rows and columns 2, 1, 1 have five (yes).
- **P5–P6:** with four counters, the 2×3 board has 9 margin classes with a single picture and 3 with more than one. The 3×3 board has 45 and 27. Both kinds exist on both shapes, so P6 can be done.

## Grades 2–3: checks out completely

- **P1:** 3, 1 and 2 pictures, so the answers are yes, no, yes.
- **P2:** exactly 5 pictures, with 6 grids printed. The guide (p. 9) says the spare grid is intentional.
- **P3, p. 3:** 100/000/001 has exactly one alternative, 001/000/100. Reaching it moves exactly two counters.
- **P3, p. 4:** the example 10/01 → 01/10 is correct. The four pictures have 0, 1, 3 and 0 switches. 110/001/100 has the switches (A, B; columns 1, 3), (A, B; columns 2, 3) and (B, C; columns 1, 3).
- **P4:** from 1100/0011, four pictures are one switch away. Exactly one picture, 0011/1100, needs two, so the bottom grid has a unique answer.
- **P5:** a unique four-counter picture exists on both shapes. Among four-counter pictures, "unique" is exactly "has no switch".

## Grades 4–5: checks out completely

- **P1:** exactly 6 pictures, on 3 + 3 grids.
- **P2:** the six pictures are switch-connected, with greatest shortest distance 2. Each picture has 4 neighbours one switch away.
- **P3:** the distance is 3, which fits the two intermediate grids on p. 5. The margins allow 20 pictures.
- **P4:** fewest switches 2; 6 pictures; greatest shortest distance 2.
- **P5:** on every 2×n board for n ≤ 8 (501,078 ordered same-margin pairs), all pictures with the same margins are connected. The distance equals the number of columns with a top counter in the start and none in the target, and the diameter is min(k, s − k).

## Bonus companion: checks out completely

- **Opening example:** the dashed lines are the column-minus-row diagonals: d1 = C1; d2 = B1, C2; d3 = A1, B2, C3; d4 = A2, B3; d5 = A3. Each label sits at the lower end of its line. The pictured A1, A2, B3, C1 gives 1, 0, 1, 2, 0, as printed. Both P1 working grids carry the same lines.
- **P1:** of the six one-per-row-and-column pictures, exactly one pair has the same diagonal shadows: 100/001/010 and 010/100/001, both (0, 1, 1, 1, 0). The answer is yes.
- **P2:** the six candidates are numbered as in the guide. The adaptive worst-case minimum is 3, and the guide's A1 → B2 / A2 → B1 strategy achieves it.
- **P3:** no set of 1, 2 or 3 prechosen cells separates the six, and 81 of the 126 four-cell sets do, including A1, A2, B1, B2. The minimum is 4.
- **P4:** (3,3,0)/(3,3,0) and (3,3,1)/(3,3,1) are impossible. (3,2,1)/(2,2,2) has exactly the three pictures the guide lists. (2,2,2)/(3,3,0) has only 110/110/110.
- **Cell sizes:** the P1, P3 and P4 working cells are 22 mm and square.

## Base adult guide

The overview's facts are correct and correctly limited:

- **Uniqueness:** unique ⇔ no legal switch ⇔ row sets pairwise nested. This holds on all 14,160 boards of sizes 2×2 to 2×6, 3×3, 3×4 and 4×3.
- **Two-row distance:** the distance is |S \ T| and the diameter is min(k, s − k).
- **Limits:** the overview says the two-row formula does not extend to three rows. The p. 17 example confirms this: 100/010/001 and 100/001/010 have the same top row but are one switch apart.

The p. 16 nested-row proof is complete. On p. 17, the count C(s, k) with its feasibility conditions matches enumeration for every two-row margin up to 7 columns, and the 2×2 margins (2,0)/(2,0) have no picture. On p. 18, "9 unique and 3 ambiguous classes on 2-by-3; 45 unique and 27 ambiguous classes on 3-by-3" and "4,864 boards" are both right.

Every answer board is a valid picture with the stated counts. Every "complete list" is exactly the complete solution set:

- K–1 P1: 2, 2 and 3 pictures.
- K–1 P2: two catalogs of 3.
- K–1 P3: 6 pictures.
- K–1 P4: two forced pictures and 5 pictures.
- G2–3 P1: 3, 1 and 2 pictures.
- G2–3 P2: 5 pictures.
- G4–5 P1: 6 pictures.
- G4–5 P4: 6 pictures.

Every caption matches its picture. The switch counts and switch results on p. 10 are right, and so are the routes on pp. 11, 13 and 14, with their stated columns. The internal references are also correct: "guide page 6", "page 7", "page 16", "page 11" (the 12 → 23 → 34 boards are the G2–3 P4 boards), "pages 15–17" and "page 18".

There is one error, a wrong statement in a hint (problem 1 below).

## Bonus adult guide: checks out completely

- **P1:** the d1–d5 signature list is right.
- **P2:** the adaptive strategy and the "four histories < six" lower bound are right.
- **P3:** the four-cell answer is right. The case analysis for three cells is right: (3,0,0), (2,1,0) and (1,1,1) with a repeated column each leave a switch whose four corners are all unqueried; the transversal case leaves the two pictures that avoid all three cells. `check_bonus.py` confirms this for all 84 three-cell sets.
- **P4:** the realizations and the capacity numbers (2+2+0 = 4 < 6; 2+2+1 = 5 < 6) are right.
- **Hedge:** the guide says the capacity bound is necessary and does not claim it is sufficient, which is correct as worded.

## Located problems

### 1. Base guide p. 11, Grades 2–3 Problem 4, held hints: a valid lower-bound argument is called invalid (minor)

- **Quoted text:** "Counting four moved counters is not by itself a lower bound, because a route could move counters more than once."
- **Evidence:** the start 1100/0011 has four occupied cells (A1, A2, B3, B4) that are empty in the target 0011/1100. Every switch empties exactly two cells. So any route needs at least 4/2 = 2 switches, however often it moves a counter. Moving a counter more than once only adds switches, so the stated reason points the wrong way. `check_guide.py` confirms that "(cells occupied in start but empty in target) / 2 ≤ switch distance" holds for all 32,698 same-margin pairs on 2×4, 2×6, 3×3 and 3×4 boards. The guide's own top-row argument is correct; the risk is that an adult rejects a child's correct "four counters must move and a switch moves only two" proof.
- **Smallest fix:** replace the sentence with: "A child may also count counters: four occupied cells must be emptied, and each switch empties exactly two, so at least two switches are needed. Moving a counter twice only adds switches."

### 2. K–1 pp. 5–6 and Grades 2–3 pp. 3–4: two different tasks share one problem number (low; label only, not mathematical)

- **K–1:** p. 5 has "**Problem 4:** Can you make two different pictures with these counts?" and p. 6 has "**Problem 4:** Make two different pictures for each pair of grids, if you can."
- **Grades 2–3:** p. 3 has "**Problem 3:** Move exactly two counters from the filled picture…" and p. 4 has "**Problem 3:** A switch moves the two counters to the empty corners shown…"
- **Continuation pages:** these also repeat the heading with reworded text: K–1 p. 5 "Problem 3", 2–3 p. 3 "Problem 2", 4–5 p. 2 "Problem 1" and 4–5 p. 5 "Problem 3".
- **Effect:** the guide's headings treat each pair as one problem ("K-1 Problem 4 / Student pages 5-6"; "Grades 2-3 Problem 3 / Student pages 3-4"), so no answer is misattributed. But "Problem 4" or "Problem 3" alone is ambiguous at the table.
- **Smallest fix:** mark the repeated-task pages "Problem N (continued)". For the two pairs of different tasks, either renumber (K–1 P4–P7; 2–3 P3–P6) and update the guide's headings, or label the parts 4a/4b and 3a/3b in both packet and guide.

## Observations that are not errors

- **Grid counts reveal the answer:** K–1 P2 and P3 and Grades 4–5 P1 print exactly as many grids as there are pictures (3 + 3, 6, 6). The grid count therefore gives away the answer, though not the completeness argument the pages ask for. Grades 2–3 P2 prints one spare grid on purpose. This is a design choice for the card, not a correctness issue.
- **Shorter bonus P3 argument:** a shorter lower bound for bonus P3 is available if wanted. Each cell is occupied in exactly 2 of the 6 pictures, so three cells give six answer strings with total weight 6. Six different 3-bit strings need total weight at least 0+1+1+1+2+2 = 7.
- **Capacity bound:** for P4 of the bonus, the capacity bound with equal totals is also sufficient, by Gale–Ryser; this was checked on every 3×3 margin. The guide does not need this.
- **Page numbering:** the appended route-note page of the base guide is numbered 20, following printed page 18. This is layout only, and nothing refers to it.
