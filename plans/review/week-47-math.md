# Week 47 (Gentle-step landscapes): math check

Scope:

- Base packet in `lowell-math-circle-year-2/week-47/`:
  - `week-47-k-1.pdf` (5 pp., Problems 1–7, footer F47-K-v3);
  - `week-47-grades-2-3.pdf` (5 pp., Problems 1–7, F47-23-v3);
  - `week-47-grades-4-5.pdf` (5 pp., Problems 1–7, F47-45-v3);
  - `week-47-facilitator.pdf` (4 pp.: three guide pages and the route update).
- Bonus companion in the same folder: `week-47-bonus.pdf` (3 pp., Problems 1–3, F47B-S) and `week-47-bonus-facilitator.pdf` (2 pp.).

I ignored the archive folders. My scripts and their outputs are in [checks/week-47/](checks/week-47/). Checked October 5, 2026.

**Result: every student problem in every band is correct as printed, and every answer, witness, route and count in both guides is right. I found 5 problems, all in what the adults are told, and none changes a printed answer:**

1. The Grades 2–3 Problem 6 key doesn't say that its forcing pair is the only one on the board.
2. In bonus Problem 3, whether the gray towers count changes which budgets work.
3. The guide's K–1 Problem 7 example needs height 4, but the board in use stops at 3.
4. The overview's envelope claim is missing its hypothesis.
5. One symbol in a Grades 4–5 proof is undefined.

## How it was checked

All scripts and their outputs are in [checks/week-47/](checks/week-47/). Run `pdf_extract.py` first. The scripts use only Poppler (`pdftocairo -svg`, `pdftotext -bbox`) and the Python standard library. None of them imports or reads the packet's own builders or checkers.

- **The PDFs match their sources.** All six delivered PDFs are byte-identical (MD5) to their copies in `source/week-47/editable/reference-pdfs/` and `source/week-47-bonus/reference-pdfs/`.
- **`compare_source.py` compares the sources with the PDFs** (93 checks, 0 failures). The TeX sources (`src/*.tex`) give the same problem statements, boards, clue discs, star, shaded marks and box rows as the PDFs. The bonus builder's literal data also matches.
- **`pdf_extract.py` reads every diagram from the delivered PDFs** and writes `pdf_geometry.json` (158 checks, 0 failures).
  - **Base marker boards.** It reads the number of sites, levels and labels and the site/level spacing, and finds a grid point at every site and level. Every clue disc sits exactly on a grid point and prints the level it sits on. The star is centred over site 2, offset 0.00 pt. In 4–5 P6 the shaded discs are read site by site.
  - **Box rows.** It reads the values, which boxes are shaded (fixed) and the site labels.
  - **Launch strip.** The towers 1,2,2,1 give markers at levels 1,2,2,1, and these give the boxed row 1,2,2,1. The "jump too big" towers 1,3,2 really have a jump of 2.
  - **Bonus.** It reads the squares, the edges joining square centres, the letters, the clue values, the start/finish rows, the marker board and the budget list.
  - **Numbering.** Problems are numbered consecutively in every packet.
- **`check_base.py` enumerates every base task exactly** (82 checks, 1 failure, which is item 3). It reads the clues from `pdf_geometry.json`, not from the author's text.
  - Heights are not capped by the drawing. The cap used (largest clue + number of sites) can never bind, and the tallest completion is compared with each board's top separately.
  - It includes breadth-first searches for the move problem and surveys of every two-clue puzzle on the K–1 P6 board and the Grades 2–3 P6 board.
  - It checks the overview theorem exhaustively on 55,980 clue sets: every row of 1–6 sites, every clue set with heights 0–4.
  - It parses every tuple and count in the guide and checks them.
- **`check_bonus.py` enumerates every bonus task** (37 checks, 0 failures).
  - It enumerates every completion of the row and both rings, all 120 legal rows of P2 with breadth-first search between all 120 × 120 pairs, and all 49 budget rings.
  - It checks the bonus overview's four theorems exhaustively on 1,512 clue sets on seven small graphs: a path, two rings, a star, a branched tree, a ring with a chord and a 2 × 3 grid.
- **Visual check.** I also looked at every page in `render/` (70 dpi; it is for inspection only, and no script uses it).

## Diagrams (all bands): check out completely

- Every task board has a 22 mm site pitch and a 20 mm level pitch. The only exception is the P4 board, at 25 mm, exactly as the guide says.
- The boards are:
  - P1: five sites, levels 0–4, clues h(0)=h(4)=1;
  - P2: five sites, levels 0–4, clues h(0)=0 and h(4)=2, star over site 2;
  - P4: five sites, levels 0–3, no clues;
  - P5: seven sites, levels 0–5, clues h(0)=1, h(4)=3, h(6)=1;
  - K–1 P6: five sites, levels 0–3, clues h(0)=h(4)=1;
  - 2–3 P6: seven sites, levels 0–6, empty;
  - 4–5 P6: seven sites, levels 0–5, clue h(3)=2.
- Every completion of every printed task fits inside its drawn board.

## K–1: checks out completely

The guide's P7 example is item 3.

- **P1:** 18 completions. The tallest marker is 3, and the board goes to 4.
- **P2:** the star can be 0, 1 or 2, so the highest is 2 and the lowest 0.
- **P3:** with 0 _ _ _ 4 there is exactly one landscape, (0,1,2,3,4).
- **P4:** the first set (0 at site 0, 3 at site 2) and the third (0 at 1, 3 at 3) are impossible. The second (3 at 0, 0 at 4) has 4 completions: (3,2,1,0,0), (3,2,1,1,0), (3,2,2,1,0) and (3,3,2,1,0). All four fit the 0–3 board.
- **P5:** 10 completions. The board and two rows give the three slots.
- **P6:** going from (1,2,1,2,1) to (1,0,0,0,1) takes at least 5 moves, by breadth-first search with heights capped at 3 or at 10. There are 16 different 5-move routes. Lowering the middle first, to (1,2,0,2,1), is illegal, so the order matters.
- **P7:** open-ended. Any consistent pair works.

## Grades 2–3: checks out completely

The guide's P6 key is item 1.

- **P1:** 18 completions. The middle can be 0, 1, 2 or 3, so both questions have the answer yes.
- **P2:** the star can be exactly 0, 1 or 2.
- **P3:** for right-clue heights r = 0, 1, 2, 3 and 4 there are 9, 12, 9, 4 and 1 completions, and none for r ≥ 5. Only r = 4 forces every marker.
- **P4:** the same as K–1.
- **P5:**
  - The fewest is (1,0,1,2,3,2,1) with 10 blocks, and the most is (1,2,3,4,3,2,1) with 16. Each is the unique landscape with that total.
  - A child who counts only the white columns gets 5 and 11 for the same two landscapes. No fix is needed.
- **P6:**
  - The board allows 679 consistent two-clue sets.
  - Exactly two of them force a unique landscape: h(0)=0, h(6)=6 and h(0)=6, h(6)=0. This holds whether or not the top line is treated as a ceiling.
  - Any non-forcing pair answers the second request.
- **P7:** the other clue can be 0 to 5. The rule max(0, a−d) … a+d holds for all d, a ≤ 6.

## Grades 4–5: checks out completely

- **P1–P4:** the same as Grades 2–3.
- **P5:** the pointwise lowest landscape is (1,0,1,2,3,2,1) and the pointwise highest is (1,2,3,4,3,2,1). Both are themselves landscapes.
- **P6:** the shaded discs are exactly the allowed heights: 0–4 at sites 1 and 5, and 1–3 at sites 2 and 4. Sites 0 and 6 allow 0–5, which fits the 0–5 board.
- **P7:** yes, every such row can be filled. On all 55,980 rows checked, a completion exists exactly when every pair of clues satisfies |a_c − a_d| ≤ |c − d|. In every one of those cases L and U are completions.

## Adult guide (base)

Every answer is correct. Items 1 and 3–5 are about what the guide says, not about wrong answers.

- **Overview.**
  - The overview is true: a completion exists exactly under the pairwise condition, every completion lies between L and U, and L and U minimise and maximise the total. With no clues there is no greatest completion.
  - The claim that L and U are themselves legal needs the pairwise condition, which the paragraph does not state (item 4).
- **Key.** Every item checks out:
  - P1's four examples and the 0–3 range;
  - P2's witnesses;
  - P3's slack for r = 0–3;
  - P4's completion (3,2,1,0,0);
  - P5's two envelopes, totals 10 and 16, the third answer (1,1,1,2,3,2,1) and "exactly 10 completions";
  - the K–1 P6 route, legal at every step, and the 5-move lower bound;
  - the 2–3 P6 examples;
  - the 2–3 P7 range 0–5 and the max(0, a−d) … a+d rule;
  - the 4–5 P6 range 0 through 5;
  - the 4–5 P7 lower-envelope proof, which is complete.
- **Preparation.** The guide's spacing figures (22, 20 and 25 mm) match the PDFs.

## Bonus student pages

Problems 1 and 2 check out. Problem 3 is item 2.

- **P1.**
  - On the row A–B–C–D–E with A=0 and D=3, B=1 and C=2 are forced and E can be 2, 3 or 4: three completions.
  - The ring A–B–C–D–E–A with A=0 and D=3 is impossible, because A–E–D is only 2 steps.
  - The ring with A=0 and D=2 has exactly three completions, (0,0,1,2,1), (0,1,1,2,1) and (0,1,2,2,1). B=1 and C=2 occur together.
- **P2.**
  - The shortest route is 8 moves, which equals the sum of the height changes. This holds with heights capped at 4 or at 12.
  - There are 120 legal rows with A=G=1. For all 120 × 120 pairs, the shortest legal route equals the sum of height changes, so the answer to "ever require extra moves" is no.
- **P3.** There are 49 rings, with totals 2–10 occurring 1, 4, 6, 8, 11, 8, 6, 4 and 1 times. Budgets 2, 5, 8 and 10 work and 11 doesn't, counting the gray towers.

## Bonus guide: checks out completely

Item 4 applies to it too.

- **Overview.** The overview's theorems hold on all 1,512 small-graph clue sets checked:
  - an extension exists exactly under the distance condition;
  - L and U are legal;
  - every total from sum L to sum U occurs;
  - the shortest legal route equals the sum of the changes.
- **Lowering-step proof.** The proof is valid.
- **Solutions and arithmetic.**
  - The solutions, including the 8-move route (legal at every step, never above 4), the witnesses and the counts 1,4,6,8,11,8,6,4,1 (49 in all), are right.
  - The kit arithmetic is right: 60 cubes, 35 markers and 10 clue markers for five kits, and KK11/3333/445 is 11 children.
  - The dimensions are right: squares of 21.9 and 24.0 mm, and a marker board of 24.3 × 20.1 mm.

## Problems found

### 1. Guide p. 3, Grades 2–3 Problem 6: the key doesn't say that its forcing pair is the only one

- **Student page (Grades 2–3 p. 5):** "Choose two clues on the seven-site board that force exactly one whole landscape."
- **Guide text:** "On sites 0-6, h(0)=0 and h(6)=6 force (0,1,2,3,4,5,6). To gain 6 in six steps, every step must rise by 1. … These are examples, not a required classification of all invented pairs."
- **Evidence (`check_base.py`, 2–3 P6):**
  - On the printed board (sites 0–6, heights 0–6) there are 679 consistent two-clue sets. Exactly two of them force one landscape: h(0)=0, h(6)=6 and its mirror h(0)=6, h(6)=0.
  - A clue placed away from an end always leaves its outer neighbour at least two heights.
  - A natural near-miss is h(1)=0, h(5)=4. It is forced between the clues, "every step must rise by 1", but it still has 6 landscapes: site 0 can be 0 or 1, and site 6 can be 3, 4 or 5.
- **Why it matters:**
  - The guide presents its pair as one example among others and gives the adult no check on the end sites. An adult could therefore accept a steep pair away from the ends as forcing.
  - Children are not told that the pair is in fact the whole answer (up to mirror image).
- **Smallest fix:** replace the last sentence with: "On this board these are the only forcing pairs, with the mirror h(0)=6, h(6)=0. A clue away from an end leaves the end site at least two choices, so both clues must sit at sites 0 and 6, six levels apart. For example, h(1)=0, h(5)=4 fixes sites 1–5 but still allows 6 landscapes."

### 2. Bonus p. 3, Problem 3: whether the gray towers count changes which budgets work

- **Student text:** "Build this ring with exactly 2, 5, 8, 10, and 11 cubes. Which budgets work? Find the smallest and largest possible totals. … Gray towers stay at 1".
- **Guide (p. 2):** "Least ring (1,0,0,1,0,0), total 2. Greatest (1,2,2,1,2,2), total 10. … Budget 11 is impossible."
- **Evidence (`check_bonus.py`, P3):**
  - The key counts the cube in each gray tower. Then the totals are 2–10, and budgets 2, 5, 8 and 10 work.
  - The gray squares already print their height "1", so a child may treat them as given and count only the cubes they add. Then the totals are 0–8, so 10 fails as well as 11, and the extremes are 0 and 8.
  - Both readings fit the printed sentence.
- **Why it matters:** a child who says "10 doesn't work" or "smallest 0, largest 8" is right under the second reading, but an adult following the key would correct them.
- **Smallest fix:** on the page, write "Gray towers stay at 1 cube each and count in the total." Alternatively, add to the guide: "If a child counts only the white towers, every total is 2 less (0–8), so 10 also fails. Accept that with its reason."

### 3. Guide p. 2, K–1 Problem 7: the example puzzle doesn't fit the board the child is using

- **Student page (K–1 p. 5):** "Replace the old clues with two new clues for a friend to solve." P7 has no board of its own. The only board on the page is Problem 6's, which has levels 0–3 and the old clues at h(0)=h(4)=1.
- **Guide text:** "For example, clues h(0)=0 and h(4)=4 force (0,1,2,3,4); h(0)=h(4)=1 allow many answers."
- **Evidence (`check_base.py`, K–1 P7, the one FAIL line):**
  - Height 4 is above that board's top level.
  - On that board, every consistent two-clue puzzle with heights 0–3 has more than one answer: 130 consistent puzzles, none forcing. So no forcing example can be built there at all.
- **Smallest fix:** "For example, on the Problem 2 board (levels 0–4), clues h(0)=0 and h(4)=4 force (0,1,2,3,4); on the Problem 6 board every legal pair of clues allows more than one answer."

### 4. Guide p. 1 overview (and bonus guide p. 1): the envelope claim is missing its hypothesis

- **Text (base):** "The simultaneous least and greatest completions are L(i) = max(0, max_c(a_c - |i - c|)) and U(i) = min_c(a_c + |i - c|). Every legal completion lies between them. Both envelopes are themselves legal…"
- **Text (bonus):** "Assuming at least one clue, the least and greatest extensions are L(v)=… and U(v)=…. Both are legal."
- **Evidence (`check_base.py`):**
  - In all 55,980 clue sets checked, L and U are completions whenever a completion exists. Without the pairwise condition they are not.
  - For example, take P4's first, impossible set, h(0)=0 and h(2)=3. The formulas give L = (1,2,3,2,1), which breaks h(0)=0, and U = (0,1,2,3,4), which breaks h(2)=3.
- **Smallest fix:** begin the sentence "When the pairwise condition holds, the simultaneous least and greatest completions are…". In the bonus guide, write "When an extension exists, both are legal."

### 5. Guide p. 3, Grades 4–5 Problem 7: the symbol f_c is undefined

- **Text:** "For completeness, the upper envelope U is also 1-Lipschitz: if every f_c changes by at most one between adjacent sites, their finite minimum does too."
- **Evidence:** f_c appears nowhere else in either guide. The argument is correct, with f_c(i) = a_c + |i − c|.
- **Smallest fix:** "if every upward tent a_c + |i−c| changes by at most one between adjacent sites, their finite minimum does too."

## Files

All in this run folder, with their saved outputs:

- `common.py`: shared helpers. It finds the repository four folders up from `plans/review/checks/week-47/`, or by searching upward from the run folder. I tested both locations.
- `pdf_extract.py` → `pdf_geometry.json`, `pdf_extract.out`.
- `compare_source.py` → `compare_source.out`.
- `check_base.py` → `check_base.out`. Its one FAIL line is item 3.
- `check_bonus.py` → `check_bonus.out`.
- `render/`: 70-dpi page images used for visual inspection only. They need not be committed.
