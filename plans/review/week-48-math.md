# Week 48 (Inside and outside covers): math check

Scope:

- Base packet in `lowell-math-circle-year-2/week-48/`:
  - `week-48-k-1.pdf` (5 pp., Problems 1–6, footer F48-K-v2);
  - `week-48-grades-2-3.pdf` (5 pp., Problems 1–6, F48-23-v2);
  - `week-48-grades-4-5.pdf` (6 pp., Problems 1–7, F48-45-v2);
  - `week-48-facilitator.pdf` (4 pp.: three guide pages and the route update).
- Bonus companion in the same folder: `week-48-bonus.pdf` (3 pp., Problems 1–3, F48B-S) and `week-48-bonus-facilitator.pdf` (2 pp., W48-BONUS-FAC-v1).

I ignored the archive folders. My scripts and their outputs are in this run folder (for [checks/week-48/](checks/week-48/) once committed). Checked October 10, 2026.

**Result: every student problem in every band is correct as printed, every diagram matches its text, and every bound, count, witness and optimum in both guides is right. I found 3 problems:**

1. Bonus Problem 2: the two witness grids are labelled "First pair" and "Third pair", which answers "Which pair cannot be true?".
2. Guide, K-1 Problem 4: "Exactly four … can become partial" reads as a limit, but eight can.
3. Guide preparation: "at least 8 paper 15 mm squares" is too few to build Grades 4–5 Problem 5 in paper, which needs 12.

## How it was checked

All scripts and their outputs are in this run folder. Run `pdf_extract.py` first. The scripts use only Poppler (`pdftocairo -svg`, `pdftotext`) and the Python standard library. None of them imports or reads the packet's own builders or checkers (`make.py`, `draw.py`, `verify*.py`, `student/verify.py`, `facilitator-src/verify_math.py`).

- **The PDFs match their sources.** All six delivered PDFs are byte-identical (MD5) to their copies in `source/week-48/editable/reference-pdfs/` and `source/week-48-bonus/reference-pdfs/`.
- **`compare_source.py` compares the sources with the PDFs** (87 checks, 0 failures). Every TeX gray polygon and every TeX board, mapped from TikZ millimetres with one translation per page, lands on the polygon and board read from the PDF. Every TeX problem statement appears verbatim in the PDF text. The bonus builder's L placements, card values and grid sizes match the PDF.
- **`pdf_extract.py` reads every diagram from the delivered PDFs** and writes `pdf_geometry.json` (55 checks, 0 failures).
  - **Boards.** It reads each grid's lines, checks equal spacing and equal scaling in both axes, and expresses each gray outline in big-square units. It checks that the gray fill coincides with the outline.
  - **Samples and legend.** It reads the page-1 whole/partial/outside sample cells (gray fractions 1, 1/2 and 0, with the "outside" cell showing an edge touch) and the 30 mm = 4 × 15 mm legend.
  - **Bonus.** It reads the three L shapes and their clipped grid lines (including what part of each grid is visible), the example card, the card values, the witness grids and their labels, and the labels in each 2 × 2 cell.
  - **Numbering.** Problems are numbered consecutively in every packet.
- **`check_base.py` checks every base task exactly** (62 checks, 2 failures, which are items 2 and 3). Each gray polygon is clipped against every closed grid cell with exact fractions; a cell is whole when the clipped area is the cell's area, outside when it is 0 (so edge and corner touches add nothing), and partial otherwise.
  - It enumerates all 120 pairs for K-1 P2 and all 560 triples for 4–5 P5.
  - It builds explicit bulged diamonds for K-1 P4 and rectangle witnesses for the shape-building tasks.
  - It tests refinement monotonicity on 286 random simple polygons.
- **`check_bonus.py` checks every bonus task exactly** (38 checks, 1 failure, which is item 1).
  - It counts the three placements and surveys all 64 translations by eighths.
  - It intersects the cards.
  - For Problem 3 it builds the L-corridor for 199 widths and the triangular-wave polygons for N = 1, 2, 3, 5, 10, 25, checking each is simple, has the stated area, keeps the cell pattern and has the stated boundary length.
- **Visual check.** I also looked at every page in `render/` (80 dpi, plus one 150 dpi crop). It is for inspection only, and no script uses it.

## Diagrams (all bands): check out completely

- Every main board is 120.0 mm square, with 30.0 mm big cells (4 × 4) or 15.0 mm small cells (8 × 8, bold every second line). The scale is equal in both axes.
- The shapes, in big units with y measured down from the top-left corner, are:
  - P1 and P3 triangle (0,4), (4,4), (4,0): area 8;
  - 2–3 and 4–5 P2 and P4, and K-1 P4, diamond (0,2), (2,0), (4,2), (2,4): area 8;
  - K-1 P2 and 4–5 P5 trapezoid (1/2,1/2), (7/2,1/2), (3,7/2), (1,7/2): area 15/2.
- The triangle is the same on P1 and P3, and the diamond the same on P2 and P4, in every band.
- 4–5 P6:
  - the "before" square and its 2 × 2 split are both 30 mm, and the diagonal cell's children are, row by row, outside, partial, partial, whole;
  - the P7 thumbnails (23 mm, 4 × 4 and 8 × 8) are the same triangle, and they are labelled "not to scale".
- The trapezoid's two bottom corner cells hold only 1/48 of a big square of gray: a sliver 2.5 mm wide at most. It is visible at actual size (150 dpi crop in `render/`), so the key's "uses all 16 big cells" is what a child can see.

## K-1: checks out completely

The guide's P4 sentence is item 2.

- **P1:** 6 whole, cover 10.
  - Another reading allows tiles placed off the grid. It needs 10 tiles too: the 10 points (4i/3, 4j/3) with i + j ≤ 3 lie in the triangle and are pairwise more than 1 apart in the L∞ distance, so no axis-parallel unit square holds two of them.
- **P2:**
  - The coarse cover is all 16 cells, with 4 whole.
  - Each corner cell splits into 0 whole, 1 partial and 3 outside. Each top or bottom middle cell gives 2/0/2, and each side middle cell 0/2/2.
  - Over all 120 pairs, the most small tiles removable is 6, reached exactly by the 6 pairs of corner cells. The cover left is 16 − 6/4 = 14.5.
- **P3:** fine bounds 28 and 36 small cells (7 and 9). Each partial big cell gives 1 whole, 2 partial and 1 outside child.
- **P4:**
  - The diamond has 24 outside small cells. 16 of them lie in the four outside corner big cells, where any gray would change a big status. The other 8 lie one in each partial big cell, each touching the diamond at a single corner.
  - Bulging the boundary at four of those corners makes exactly those four cells partial, changes no other small cell and keeps every big status. Doing it at all eight also works.
- **P5:**
  - A width-3 rectangle of height 7/6 has 3 whole and 3 partial cells and area 3.5. Height 11/6 gives 5.5.
  - With 3 whole and 3 partial cells every area is strictly between 3 and 6, so both requests are possible.
- **P6:** yes. Height 23/12 keeps the same cells and has area 5.75. Any shape with these markings has area below 6, so it can always grow.

## Grades 2–3: checks out completely

- **P1:** 6 and 10.
- **P2:**
  - The coarse diamond has 4 whole cells (the central four) and 12 cover cells.
  - "More than 3" and "less than 13" are both certain.
- **P3:** 7 and 9 big-square units.
- **P4:** 24 whole and 40 cover small cells, so 6 and 10. The uncertain area falls from 8 to 4.
- **P5:** width-4 rectangles of heights 9/8 and 15/8 have 4 whole and 4 partial cells, with areas 4.5 and 7.5.
- **P6:** neither is possible. With 4 whole and 4 partial cells, 4 < area < 8. Every rectangle surveyed (heights 1 + k/96) agrees.

## Grades 4–5: checks out completely

- **P1–P4:** the same as Grades 2–3.
- **P5:**
  - The trapezoid starts at 4 and 16, a gap of 12.
  - Over all 560 triples of big cells, the least gap after three splits is 9. Only the 4 triples drawn from the top and bottom middle cells reach it, giving bounds 5.5 and 14.5.
  - Measuring the gap as a count of uncertain cells instead of an area picks the same cells.
- **P6:** no and no.
  - Monotonicity holds for every single-cell split on 286 random simple polygons.
  - The printed example goes from inside 0 to 1/4 and from cover 1 to 3/4.
- **P7:** the exact area is 8, which lies in [6, 10] and in [7, 9].

## Adult guide (base)

Every answer is correct. Items 2 and 3 are about what the guide tells adults, not about wrong answers.

- **Overview.** It is true as stated, with the right limits:
  - whole-cell sums are lower bounds and cover sums are upper bounds;
  - edge and corner contacts can be dropped (every point of these closed polygons lies in a closed cell that has positive gray);
  - nested refinement cannot lower the inside bound or raise the cover;
  - equality in the limit needs a measurability (Jordan content) hypothesis;
  - a small tile has area 1/4.
- **Key table.** All four rows are right: 6/10, 4/12, 28/36 small → 7/9 and 24/40 small → 6/10.
- **Problem keys.** Each checks out:
  - the P1 row counts 0,1,2,3 whole and 1,2,3,4 cover;
  - the P3 child pattern and the gaps 4 → 2 and 8 → 4;
  - K-1 P2: corners, 6 tiles, 14.5;
  - the K-1 P5/P6 rectangles 7/6, 11/6 and 23/12, and the claim that 6 is a supremum;
  - 2–3 P5: 9/8 and 15/8;
  - 2–3 P6: 4 < area < 8;
  - 4–5 P5: the cells (2,1), (3,1), (2,4), (3,4) as (column, row), the bounds 5.5 and 14.5, gap 12 → 9, the four-row type table and the optimality argument;
  - the 4–5 P6 proof;
  - 4–5 P7: 8.
- **Preparation.** The 120/30/15 mm figures match the PDFs.

## Bonus student pages

Problems 1 and 3 check out. Problem 2 is item 1.

- **P1.**
  - The L has area 3. The placements give [3,3] aligned, [1,5] half a square sideways and [0,8] half a square both ways.
  - Every cover cell is drawn and fully visible inside the clipped grid. The grid cells are 56 pt (19.76 mm) in both axes.
  - Over all 64 translations by eighths, only the aligned grid is exact. The gaps are 0, 4 and 8. So "moving a grid" does not always improve the bounds.
- **P2.**
  - The example card is right: a half-gray square gives "0 to 1".
  - The pairs intersect to [4,8], nothing (at most 5 and at least 6) and [4,4].
  - The 6 × 4 witness grids hold a 2 × 2 square and a 2 × 3 rectangle.
- **P3.**
  - The boards are 2 × 2 with 80 pt cells: top-left "white", the other three "partial".
  - The corridor (0,0), (2,0), (2,2), (2−t,2), (2−t,t), (0,t) has cell areas t, 2t − t² and t, total 4t − t², perimeter 8, and keeps the pattern for every 0 < t < 1. So areas below 1 and above 2 are both possible (15/16 and 39/16).
  - The wave construction keeps area 15/16 and the cell pattern, stays simple, and has waved-edge length √(1 + N²/4), so the answer to "keep making the boundary longer" is yes.
  - The "marked/unmarked" wording refers to the "partial"/"white" labels. It does not affect the mathematics.

## Bonus guide: checks out completely

- **Overview.**
  - True as stated: translation is not refinement, the [3,3], [1,5] and [0,8] example, the intersection rule, the corridor area 4t − t² with infimum 0 and supremum 3, and unbounded perimeter at fixed area and mask.
- **Solutions.**
  - All right: the three placements, the three card combinations and the witnesses, the corridor at t = 1/4 and 3/4, both perimeters 8, the wave heights between 1/8 and 3/8, and the length √(1 + N²/4) with perimeter 7 + √(1 + N²/4).
  - The tooth argument is valid: each wave adds 1/2 of vertical travel.
- **Figures.**
  - 56 pt = 19.8 mm, 27 pt = 9.5 mm and 80 pt = 28.2 mm all match the PDF.
  - KK11/3333/445 is 11 children, so 4 pairs and 1 trio make 5 kits. That is 60 tiles and 10 pencils. Twelve tiles cover the largest page-1 cover (8).

## Problems found

### 1. Bonus p. 2, Problem 2: the witness-grid labels give away which pair is impossible

- **Student text:** "Each pair of cards reports on one shape. Make the narrowest range card that keeps every possible area. Which pair cannot be true? For each possible pair, draw a shape whose area fits both cards."
- **Diagram:** the only two drawing grids on the page are captioned "First pair" and "Third pair".
- **Guide (bonus p. 1):** "Page 2 now supplies two 6-by-4 witness grids … matched to the first and third card pairs".
- **Evidence (`check_bonus.py`, P2, the one FAIL line):**
  - The pairs intersect to [4,8], empty and [4,4], so the possible pairs are the first and third.
  - Those are exactly the pairs named under the grids.
  - A child who reads the captions knows the second pair is the impossible one before comparing "3 to 5" with "6 to 7".
- **Why it matters:** "Which pair cannot be true?" is the problem's central question, and the page answers it.
- **Smallest fix:**
  - Caption each grid "Pair: ____" so the child writes in the pair number.
  - Change the guide sentence to "two 6-by-4 witness grids, one for each possible pair (the first and third)".

### 2. Guide p. 2, K-1 Problem 4: "Exactly four … can become partial" states a false limit

- **Student page (K-1 p. 4):** "Change the diamond so four outside small squares become partly gray. Keep every big square whole, partial, or outside as it was."
- **Guide text:** "Choose four such children in different big cells and bulge the nearby diagonal boundary slightly into each … Exactly four previously outside small cells can become partial, while every big-cell status stays unchanged."
- **Evidence (`check_base.py`, K-1 P4):**
  - Each of the 8 partial big cells has one outside small child, touching the diamond at one corner. The other 16 outside small cells lie in the outside corner big cells, where any gray changes the big status.
  - Bulging at all 8 corner points makes 8 outside small cells partial and keeps every big status. This construction is checked exactly: a simple polygon, no other cell changes.
  - So at most 8 can change, not 4. "Exactly four … can become" reads as that limit.
- **Why it matters:** an adult could tell a child who finds a fifth or sixth such cell that it is impossible. The construction itself is right.
- **Smallest fix:** "This makes exactly four previously outside small cells partial while every big-cell status stays unchanged. Up to eight could change this way, one in each partial big cell."

### 3. Guide p. 1, preparation: too few small paper squares for Grades 4–5 Problem 5

- **Guide text:** "Per table: … 16 paper 30 mm squares and at least 8 paper 15 mm squares. For complete fine covers, shade rather than prepare 40 loose tiles."
- **Student pages:**
  - K-1 P2: "split two big tiles into four small tiles each". That needs 8 small squares.
  - 4–5 P5: "Split exactly three big squares into four small squares each". That needs 12.
- **Evidence (`check_base.py`, the materials FAIL line):** 3 × 4 = 12 > 8.
  - A Grades 4–5 table that builds its refinement in paper, as the K-1 table does, runs out after two splits.
- **Smallest fix:** "at least 12 paper 15 mm squares (8 for K-1 Problem 2, 12 for Grades 4–5 Problem 5)".

## Files

All in this run folder, with their saved outputs:

- `common.py`: shared helpers (Poppler readers, exact clipping and area). It finds the repository four folders up from `plans/review/checks/week-48/`, or by searching upward from the run folder. I tested both locations: a mock committed copy produced identical outputs and `pdf_geometry.json`.
- `pdf_extract.py` → `pdf_geometry.json`, `pdf_extract.out`.
- `compare_source.py` → `compare_source.out`.
- `check_base.py` → `check_base.out`. Its two FAIL lines are items 2 and 3.
- `check_bonus.py` → `check_bonus.out`. Its one FAIL line is item 1.
- `render/`: page images used for visual inspection only. They need not be committed.
