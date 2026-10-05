# Week 16 (three-colour triangles / Sperner): math check

Scope:
- `lowell-math-circle-year-2/week-16/week-16-k-1.pdf` (F16-K-v2, 6 pp., Problems 1–6).
- `week-16-grades-2-3.pdf` (F16-23-v2, 7 pp., Problems 1–6; p. 2 is a second copy of Problem 1).
- `week-16-grades-4-5.pdf` (F16-45-v2, 7 pp., Problems 1–6; p. 2 is a second copy of Problem 1).
- `week-16-facilitator.pdf` (12 pp.: overview, solutions, proofs, and the p. 12 route note).
- The return-visit companion in the same folder: `week-16-return-visit.pdf` (W16-RV-draft, 4 pp., Problems 1–4) and `week-16-return-visit-facilitator.pdf` (RV-16-FAC-v1, 5 pp.).

The archive folders were ignored, and I opened no use logs or session records. The four base PDFs are byte-identical (MD5) to `source/week-16/editable/reference-pdfs/`, and the two return-visit PDFs to `source/week-16-return-visit/reference-pdfs/`. I read `source/week-16/editable/src/generate.py`, `facilitator-src/build_guide.py` and `source/week-16-return-visit/student/generate.py` for coordinates and data only. I did not run or import the packet's own `check_math.py`, `math_checks.json`, `math-checks.json` or `independent_checks.py`. My scripts and their outputs are in [checks/week-16/](checks/week-16/). Checked October 5, 2026.

**Result: every answer, count, witness, route, table and proof in the three base bands and the adult guide is correct. Every board diagram matches its text: dots, edges, letters, side rules, the star and equal scaling. The return visit is also mathematically correct. I found 2 problems, both minor. One is a page of the return visit that reads as impossible when it is used on its own. The other is a cell-numbering sentence in the base guide that one figure does not follow.**

## How it was checked

- **`sperner16.py`** is this review's own model. It covers lattice boards of side 2–4 and the fan board (the side-2 board with each cell split at its centroid). Cells are numbered strip by strip from the bottom, left to right, which is the guide's stated convention. It enumerates legal fillings under any side rule. It also computes all-three cells, doors (R–B edges), the door graph with its components, and random edge-to-edge triangulations made by random cell and edge splits.
- **`pdfgeom16.py`** is a standard-library reader for the delivered PDFs. It handles pdfTeX object streams and the guide's ASCII85+Flate streams. It interprets the content streams (q/Q/cm, paths and paint colours), and reads text with `pdftotext -bbox`.
- **`check_math.py`** (output `out_check_math.txt`: 93 checks, 0 failures) does three things:
  - It enumerates every board: 8, 192, 648 and 13,824 legal fillings for side 2, side 3, the fan board and side 4, plus both exception rules.
  - It recomputes every answer and compares the printed guide text (via `pdftotext`) with the enumeration. That covers all row codes, counts, distributions, the 16-row table, routes and the local and row tables.
  - It tests the general theorem, the incidence identity and the path-pairing argument on 4,000 random labellings of 400 random triangulations.
- **`check_diagrams.py`** (output `out_check_diagrams.txt`: 207 checks, 0 failures) handles the student pages and the guide figures.
  - Each student board is matched dot by dot to its lattice or fan board. The drawn lines must equal the board's edge set exactly. The big triangle must be equilateral with equal x/y scale. Printed letters and their tints are read at the dots. "R or Y", "B or Y" and the bottom rule are located on the correct sides. The script also measures the Problem 3 triangle sheets, the Problem 4 rows and the door examples.
  - All 17 guide figures are read back the same way, with their letters, gray cell numbers, shaded cells and door bars. Each is compared with the printed row code and with the computed all-three cells and doors.
- **`check_return_visit.py`** (output `out_check_return_visit.txt`: 37 checks, 0 failures) covers the return visit:
  - every star choice;
  - all 256 four-label mesh fillings;
  - both diagonals for all 81 square corner labellings;
  - signed counts on all 192 fillings and on 3,000 random triangulation labellings, plus the mirror image;
  - the recolouring argument on 2,401 random no-RBY labellings;
  - the student diagrams (dots, edges, squares and their diagonals, and the sign-example arrows read from the arrowheads).
- All four scripts were also run from a copy laid out as `plans/review/checks/week-16/`. They found the repository four folders up and reproduced the same outputs.

## K–1 (6 pp.): checks out

- **P1 (side 2):** all 8 legal fillings have exactly one all-three cell, and each of the 4 cells can be that cell. The guide's four witnesses RBB/YB/Y, RRB/YB/Y, RRB/RY/Y and RRB/RB/Y (read from the p. 3 figures) make cells 1, 2, 3 and 4 respectively.
- **P2 (side 3):** none of the 192 legal fillings has zero all-three cells. The counts are 1, 3 and 5 in 108, 72 and 12 fillings.
- **P3:** the maximum is 5. RBRB/RYB/RB/Y gives cells 2, 3, 4, 7 and 9.
- **P4 (fan board, printed RRB/YB/Y):** the maximum is 7. Exactly three of the 81 centre choices reach it: lower-left B, lower-right Y, top R, and any letter at the central dot. The regional bounds 2+2+2+1 in the guide's proof hold, each with the stated unique centre. The central region gives exactly 1 for every centre.
- **P5 (side 4):** each of the 16 cells is the only all-three cell in some filling (176–232 fillings per cell). All 16 row codes in the guide table are legal and make exactly the stated cell.
- **P6 (bottom side may use Y):** there are 52 zero-cell fillings, so four exist. The guide's four codes are legal, distinct and zero-cell, and each has bottom row RRYB. Every zero-cell filling has a Y on the bottom, which supports the guide's hint.
- **Diagrams:** every board is equilateral, 5.25 in on a side, with exactly the right edges, corner letters R, B and Y, and correct side labels. The P4 inserted dots sit at the cell centroids. The tightest spacing is 1.3124 in on P5, matching the guide's 1.3125 in, and P5 has 15 vertices, as stated. No K–1 board ever needs more than 10 counters of one letter (15 per set are prepared).

## Grades 2–3 (7 pp.): checks out

- **P1:** the minimum is 1, the maximum 5, and only 1, 3 and 5 occur.
- **P2:** the printed board RBRB/RRB/RB/Y obeys the side rules and has 9 doors, three of them the bottom edges. The routes are: entrance 1 – cells 1, 2, 3 – entrance 2; and entrance 3 – cells 5, 4, 8, 7, 9, which stops in cell 9, the only all-three cell. There is no internal component, so entrances 1 and 2 lead back outside.
- **Door example:** the triangle is labelled R (top), R and B, and its two thick bars lie on exactly its two R–B edges. The dashed route crosses both bars.
- **P3:** there are 10 classes under turns and flips (the multisets of three letters), drawn on 12 equilateral triangles. One door occurs only for RBY, two for RRB and RBB, and three never.
- **P4:** the rows have 2–6 edges, R to B. The possible door counts are {1}, {1,3}, {1,3}, {1,3,5} and {1,3,5}, so the count is always odd.
- **P5:** 6,192 side-4 fillings have exactly three all-three cells. In every legal filling the number of outside doors is odd, so the outside-started routes can never all end outside.
- **P6:** across all 648 fan-board fillings the counts are 1, 3, 5 and 7, never 0.

## Grades 4–5 (7 pp.): checks out

- **P1:** the possible counts are exactly 1, 3 and 5.
- **P2:**
  - The printed board RRBRB/YBRB/RBB/RB/Y obeys the side rules. It has 14 doors, boundary doors on bottom segments 2, 3 and 4, and all-three cells 2, 8 and 16.
  - There are exactly three components: segment 2 – cells 3, 2; segment 3 – cells 5, 4, 10, 11, 12, 6, 7 – segment 4; and the internal open path cells 8, 9, 13, 14, 16. They use 2, 8 and 4 doors, there is no loop, and cell 1 has no door.
- **P3:** as in Grades 2–3, only RBY has exactly one door.
- **P4:** the rows are RB with 3 edges, RR with 4, RB with 5, RR with 6 and RB with 7. The counts are {1,3}, {0,2,4}, {1,3,5}, {0,2,4,6} and {1,3,5,7}, so the parity is odd exactly when the ends differ. I checked this for every row of 1–12 edges.
- **P5:** the count is odd on the fan board. On random edge-to-edge triangulations it was always odd, and T + 2U = b + 2I always held.
- **P6:** the star sits under the middle bottom dot (2,0). There are 208 zero-cell fillings and every one has Y at the star. The witness RRYBB/RRYB/RRY/RY/Y breaks only the star's old rule.

## Adult guide (12 pp.): mathematics checks out; see Problem 2 for one sentence

- **Overview (p. 1) and proof (p. 11):** the parity theorem, the door classification, the incidence identity T + 2U = b + 2I and the pairing and path arguments are all correct. The hypotheses (edge-to-edge, no holes or T-junctions, corner and side rules) and limits are stated correctly. Each statement held in the random-triangulation test, and closed door loops occurred there, as the overview allows. With Y allowed on a side, even totals occurred.
- **"Why five is the upper bound" (p. 5):** rotating and renaming (R→B→Y→R) maps legal fillings to legal fillings and keeps the count, and it can always send the centre to Y. With centre Y, every one of the 64 fillings satisfies count = [L≠M] + [L=B] + [M=R] + 2[V=R and U=B]. Every group claim holds, and the table (RR 1, RB 1, BR 3, BB 1) is right.
- **Figures:** all 17 figures (pp. 3–9) read back exactly as their printed codes. The shading equals the computed all-three cells in every figure. The door bars on pp. 8–9 (9 and 14) sit exactly on the R–B edges. The side-lattice numbering follows the stated convention.
- **Preparation arithmetic:** 135 = 3 × 45, 180 = 4 × 45 and 90 = 2 × 45 are correct, and so is the "12 little cells" on the fan board. The p. 2 and p. 12 counter totals differ only because they are written for three and four K–1 children.

## Return visit (4 pp. + 5 pp. guide): mathematics checks out; see Problem 1 for page 2

- **P1 (star):** only G at the centre leaves no RBY cell. R, B and Y each make exactly one.
- **P2:** 27 of the 256 four-label fillings have no RBY. Each of them has G at the single interior dot, and their any-three counts are 3 in 18 fillings and 5 in 9, so the minimum is 3. The guide's witness RRBB/RGB/YY/Y has three one-letter cells, three two-letter cells and one each of RBG, RYG and BYG.
  - The recolouring argument held every time: G→R exposes an original BYG cell, G→B an RYG cell and G→Y an RBG cell. So did "each type occurs an odd number of times".
- **P3:** switching the diagonal changes the count for 12 of the 81 corner labellings and never changes its parity. The parity equals that of the number of R–B sides. The guide's examples RBRB (4 doors, 0/0), RBYY (1, 1/1) and RBRY (2, 0/2) are right. The left squares carry diagonal 1–3 and the right squares 2–4, as the guide says.
- **P4:** the signed counts (+, −) are (1,0), (2,1) and (3,2) in 108, 72 and 12 fillings. On random triangulations + minus − was always 1, and always −1 for the mirror image. A missing-colour refinement of any two-label triangle always adds one + and one −. Both example triangles have all three arrows counterclockwise, and their captions ("R → B → Y: +", "R → Y → B: −") match the counterclockwise reading from R.
- **Measurements:** the dot rings are 7.11 mm across, as stated. The spacings are 38.1 mm (p. 2), 35.6 mm (p. 4) and 59 mm (star), all at least 18 mm.

## Problems found

### 1. Return visit, page 2, Problem 2 (minor): the page alone gives no fourth letter, so its first task is impossible

- **Quoted text:** the page is headed "Week 16 / Three-color meshes / Grades 2–3 and up". It reads: "Problem 2: Fill the blank dots so no small triangle has R, B and Y. Among those fillings, how few small triangles can have three different letters?"
  - The rule that makes the task possible appears only on page 1, which is headed "Grades K–1 and up": "Keep the corner letters. A dot on a side uses one of that side's corner letters. Inside, use R, B, Y or G."
- **Evidence:** with only R, B and Y, each of the 192 legal fillings of this board has at least one RBY cell (`out_check_math.txt`, side-3 distribution {1: 108, 3: 72, 5: 12}). So a group handed only "its" page cannot carry out the first sentence, and "those fillings" is an empty set. With G allowed inside, 27 of 256 fillings work (`out_check_return_visit.txt`).
  - Pages 3 and 4 each restate their own rule ("Use only R, B and Y"), which makes the missing rule on page 2 easier to overlook.
  - The adult guide (p. 2) already says "Offer pages 1–2 together so page 1's shared rules remain visible beside the free mesh". As printed together, the problem is correct.
- **Smallest fix:** add one line above Problem 2 on page 2: "Side dots use that side's corner letters. The middle dot may be R, B, Y or G." Alternatively, give pages 1–2 one shared band header so they are not handed out separately.

### 2. Adult guide, page 3 (sentence) and page 4 (fan figure) (minor, cosmetic): the stated cell-numbering rule does not describe the fan figure

- **Quoted text** (guide p. 3): "In guide diagrams, small gray numbers name cells; light shading marks the all-three cells. … Numbering runs left-to-right within each horizontal strip, then upward."
- **Evidence:** in the p. 4 "Problem 4 maximum 7" figure (`out_check_diagrams.txt`, fan numbering line), the numbers go region by region: 1–3 lower-left, 4–6 central, 7–9 lower-right, 10–12 top.
  - Read by height from the bottom, and left to right at each height, the numbers are 1, 7; then 3, 2, 9, 8; then 4, 6; then 5; then 10; then 12, 11.
  - Every side-2, side-3 and side-4 figure does follow the stated rule. No sentence in the guide refers to a fan cell by number, so no answer is affected.
- **Smallest fix:** add "(the fan board is numbered region by region: lower-left, central, lower-right, top)" after the sentence, or drop the numbers from the fan figure.

## Checked, not counted

- The door example on Grades 2–3 p. 3 and Grades 4–5 p. 3 is an isosceles triangle with sides 63.7, 63.7 and 86.4 pt, while the board cells are equilateral. It is drawn at equal x/y scale and is a schematic, not an intended regular figure, and doors do not depend on shape. Its labels, door bars and route are correct.
