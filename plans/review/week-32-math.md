# Week 32 (squares inside rectangles): math check

Scope: everything current in `lowell-math-circle-year-2/week-32/`, archive folders excluded:

- `week-32-k-1.pdf` (F32-K-v2, 5 pp., P1–P5)
- `week-32-grades-2-3.pdf` (F32-23-v2, 5 pp., P1–P6)
- `week-32-grades-4-5.pdf` (F32-45-v2, 5 pp., P1–P6)
- `week-32-facilitator.pdf` (5 pp.: the guide on pp. 1–4 and a route update on p. 5)
- the bonus companion `week-32-bonus.pdf` (W32-BON-v1, 3 pp., P1–P4) and its guide `week-32-bonus-facilitator.pdf` (W32-BON-FAC-v1, 5 pp.)

Sources read:
- `source/week-32/editable/student-src/`: `make_packets.py` and `draw.py`
- `source/week-32-bonus/student-src/bonus.tex`
- `worksheet-workflow/context.md`, for the size of the current K–1 table

The delivered PDFs are byte-identical (same MD5) to the reference copies in both source folders. I did not run, import or read the packet's own checkers: `verify.py`, `verify_revision.py`, `facilitator-src/check_math.py` with `checks.json`, `math/independent-check.py` and `writer-check.py`. I also did not read the packet's review or answer notes. Checked October 10, 2026.

**Result:**
- **Mathematics:** every student problem has the answer its page implies, and nothing it asks for is impossible. Every list, table, count and proof in both adult guides is correct.
- **Problems found:** 4, numbered in page order below.
  1. The K–1 P5 work grid can hold either answer rectangle, but not both at once (diagram, minor).
  2. The Grades 2–3 P6 work grid can't hold any complete answer: every valid trio needs at least 171 cells, and the grid has 144 (diagram, moderate).
  3. Grades 4–5 P6 asks children to "Find every rectangle that ties", but the winner is unique, so nothing ties (wording, minor).
  4. The base guide gives two different cutout counts for the K–1 table: 12 on p. 1 and 16 on p. 5 (materials arithmetic, minor).

## How it was checked

My scripts and their saved outputs are in this folder, to be copied to `checks/week-32/`. Each script finds the repository from its own location: four folders up from there, or three from `tmp/review-runs/week-32/`. They need only Python 3 with `pypdf` and Poppler's `pdftotext`.

- **`common32.py`** reads the delivered PDFs directly:
  - a small content-stream interpreter tracks the transformation matrix, line width, grey level and dash state of every painted path, using pypdf only to decompress the streams;
  - it finds every outlined board, the thin grey grid lines inside it and every free work grid;
  - it measures cell counts and the spacing in both directions;
  - `pdftotext -bbox` gives the side labels above and to the left of each board, and its captions.
- **`math32.py`** holds independent brute-force mathematics:
  - The biggest-square rule is simulated literally on a cell grid. At each step the code checks that the uncovered cells form one rectangle, then covers the largest square at its end. This is cross-checked against plain repeated subtraction, with no division and no gcd.
  - Equal-square tilings, minimum-count square tilings (any sizes, or sizes restricted to {2, 3}) and the size multisets of all k-piece tilings are found by exhaustive first-empty-cell search.
  - It also covers rectangles made from n identical squares, packing several rectangles onto a work grid, recipes (group counts), continued-fraction values and the guide's backward reconstruction.
- **`check_students32.py`** → `out_check_students32.txt` (123 checks, 2 failures, which are Problems 1 and 2). It covers:
  - the shared 5 × 2 launch example in all three bands;
  - every board's cell counts, labels and square cells (equal spacing in both axes, 0.7, 0.62 or 1 cm as drawn);
  - every work grid;
  - every answer for K–1 P1–P5, 2–3 P1–P6, 4–5 P1–P6 and bonus P1–P4;
  - page bounds.
- **`check_guides32.py`** → `out_check_guides32.txt` (73 checks, 1 failure, which is Problem 4). For every mathematical claim in both guides it does two things:
  - confirms that the quoted sentence is in the delivered PDF;
  - recomputes the claim.

  This covers the overview invariants (b < a < 120, a, b ≤ 60), the equal-tile criterion (search, a, b, s ≤ 18), all keys, the 49-cell P6 table parsed from the PDF, the recurrence, the scaling extension, every bonus area decomposition, the projection obstructions, the {2,3} tileability, the height-5 strip bound, and recipe uniqueness up to scale (a, b ≤ 60).

## K–1 (5 pp.): mathematics checks out; see Problem 1 for the P5 work grid

- **p. 1 launch example (same in all three bands):** 5 × 2, 5 × 2 with a shaded 2 × 2 at its left end, then 3 × 2. All use 0.7 cm square cells, and the labels match. The rule's first cut of 5 × 2 is a 2-square that leaves 3 × 2, as captioned.
- **Boards:** every board is 1 cm square cells, with labels matching the cell counts: 6×4, 8×4, 7×4, 8×5, 9×6, 10×6, 6×4, 8×6, and four 3×3.
- **P1:** 6×4 → 4,2,2 (last 2); 8×4 → 4,4 (last 4).
- **P2:** 7×4 → 4,3,1,1,1; 8×5 → 5,3,2,1,1. Both end at 1, so they match.
- **P3:** 9×6 → 6,3,3 (last 3); 10×6 → 6,4,2,2 (last 2). They differ.
- **P4:** the equal squares that tile, found by search, are {1,2} for both 6×4 and 8×6, so the biggest is 2.
- **P5:** a search over every area-36 rectangle finds exactly two shapes made of four 3×3 squares, 3×12 and 6×6. Their sequences are 3,3,3,3 and 6, so the last squares do not match. The work grid uses the same 1 cm cells as the printed squares.

## Grades 2–3 (5 pp.): mathematics checks out; see Problem 2 for the P6 work grid

- **P1:** 10×6 → 6,4,2,2; 8×5 → 5,3,2,1,1.
- **P2:** 12×8 → 8,4,4 (last 4); 12×9 → 9,3,3,3 (last 3).
- **P3:** 12×8 takes sizes 1, 2, 4 (biggest 4); 10×6 takes 1, 2 (biggest 2).
- **P4:** 7×6, 8×6 and 9×6 end at 1, 2 and 3, already in board order. 6×10 → 6,4,2,2 ends at 2, not the extrapolated 4.
- **P5:** last square = largest identical tile for every a, b ≤ 25 (tile search).
- **P6:** with sides from {3, 6, 9, 12}, the rectangles that end at 3 are:
  - 3×3, 6×3, 9×3 and 12×3, all with first square 3;
  - 9×6, first square 6;
  - 12×9, first square 9.

  So a valid trio exists. The 6-first and 9-first rectangles are forced, and only the 3-first rectangle can vary.

## Grades 4–5 (5 pp.): mathematics checks out; see Problem 3 for the P6 wording

- **P1:** the same as 2–3 P1. The last squares are 2 and 1.
- **P2:** 15×9 → 9,6,3,3 (last 3); 14×8 → 8,6,2,2,2 (last 2). The rule is gcd.
- **P3:** 12×8 takes {1,2,4} and 15×9 takes {1,3}, by search over every s up to the long side.
- **P4 diagram:**
  - The 14×8 board is drawn at 0.62 cm, equal in both axes, labelled 14 and 8.
  - The shaded 8×8 sits flush at its left end and is labelled "8 by 8".
  - The separate 6×8 board is labelled 6 and 8.
- **P4 answers:** common measures are {1,2} before and after the cut. Common divisors of (a, b) equal those of (a − b, b) for all b < a < 80.
- **P5:** true for all a, b ≤ 30.
- **P6:** over all 49 rectangles, distinct sizes peak at 5, at 13×8 only (8,5,3,2,1,1). Under the other reading, "most pieces", the maximum is 9, at 9×8, 15×2, 15×7 and 15×8; the page's "different square sizes" excludes that reading. Both 15×8 work grids hold any candidate.

### Problem 1 (minor, K–1 p. 5, worksheet Problem 5): the work grid cannot hold both answer rectangles

- **Text:** "Find every rectangle you can make with four 3 by 3 squares, counting turns as the same shape. Will their last squares match under the biggest-square rule?" Below it is the only work grid on the page, 12 × 8 cells at 1 cm.
- **Evidence (`out_check_students32.txt`, K–1 P5):**
  - The complete answer is 3×12 and 6×6. Each fits on the grid alone, but an exhaustive placement search finds no way to draw both.
  - 12 > 8, so the 3×12 must lie along the 12-cell side. That leaves 8 − 3 = 5 rows, and the 6×6 needs 6.
  - A child who records 3×12 first and then tries 6×6 below it finds that it "doesn't fit". The two-shape answer has nowhere to be recorded together.
- **Smallest fix:** in `make_packets.py` K–1 page 5, change `p.workgrid(1,9,12,8)` to `p.workgrid(1,9,12,9)`. 12 × 9 is the smallest 12-wide grid that holds both. The grid then ends at 18 cm, still clear of the ruled lines at 21 cm.

### Problem 2 (moderate, Grades 2–3 p. 5, worksheet Problem 6): the work grid cannot hold any complete answer

- **Text:** "Make three rectangles with different first squares and the same last square of side 3. Choose each starting side from 3, 6, 9 and 12." The only workspace is one free grid of 12 × 12 cells at 1 cm.
- **Evidence (`out_check_students32.txt`, 2–3 P6):**
  - Every valid trio must contain 9×6 and 12×9, which are the only 6-first and 9-first rectangles, plus one of 3×3, 6×3, 9×3 or 12×3. That needs at least 54 + 108 + 9 = 171 cells, and the grid has 144.
  - More concretely, once 12×9 is drawn only 3 full rows remain, so 9×6 cannot be added. Drawn the other way round, 12×9 cannot be added.
  - A child who draws one forced rectangle first is likely to conclude that the other is impossible, which is the opposite of the intended finding. The page doesn't say other paper may be used, unlike bonus P4.
- **Smallest fix:** in `make_packets.py` Grades 2–3 page 5, change `p.workgrid(1,11.5,12,12)` to `p.workgrid(1,11.5,12,15,.8)`. A 12 × 15 grid is the smallest 12-wide grid that holds a valid trio, for example 12×9 on top with 9×6 and 3×3 below it. At 0.8 cm cells it occupies the same 12 cm of height as now. Alternatively, add "You may use separate graph paper."

### Problem 3 (minor, Grades 4–5 p. 5, worksheet Problem 6): the page asks for ties, and there are none

- **Text:** "Which rectangle produces the most different square sizes under the biggest-square rule? Find every rectangle that ties."
- **Evidence (`out_check_students32.txt`, 4–5 P6 table):**
  - 13×8 is the only one of the 49 rectangles with 5 sizes. Every other cell is at most 4.
  - The guide agrees: "The unique winner is 13×8".
  - "Find every rectangle that ties" presupposes at least one tie. A child whose complete, correct search finds none is told by the page that something is missing.
- **Smallest fix:** replace "Find every rectangle that ties." with "Is any other rectangle as good? Explain how you know." This keeps the exhaustive-search demand.

## Bonus companion (3 pp., Grades 2–5): checks out completely

- **Boards:** all 1 cm square cells. P1 has 6×5, 6×5, 4×3 and 4×3. They carry no side labels; P2's "6 × 5" matches the drawn 6-wide, 5-tall board. P3 has 5×5, 6×5 and 7×5, with matching captions. P4 has three dashed 8×4 work grids.
- **P1:**
  - 6×5: greedy 5,1,1,1,1,1, which is 6 squares; the fewest is 5 (3,3,2,2,2).
  - 4×3: greedy 3,1,1,1, which is 4 squares; the fewest is 4.
- **P2:** an exhaustive search finds no tiling of 6×5 with 1, 2, 3 or 4 squares. The only 5-piece size multiset is {3,3,2,2,2}.
- **P3:** only 6×5 can be tiled with sizes {2,3}. 5×5 and 7×5 cannot, by exhaustive search.
- **P4:**
  - The recipe example is 2,2,1,1 in a 5×2 strip, which gives recipe 2,2.
  - The smallest rectangles are 3×2 for recipe 1,2, 8×3 for 2,1,2 and 7×4 for 1,1,3. Each fits an 8×4 grid.
  - Every rectangle with a given recipe is a multiple of one coprime pair, so the answer to "different-sized rectangles?" is yes.

## Base adult guide (`week-32-facilitator.pdf`): correct throughout, apart from the materials count in Problem 4

- **Overview:**
  - The invariant, the termination and "last square = gcd" are all true.
  - So is "identical whole-grid squares of side s tile ⇔ s divides both sides".
  - So is the limit that greedy is not claimed minimal; 6×5 shows greedy really isn't minimal.
- **Keys:** all six K–1 table rows match, and each row's square areas sum to the rectangle's area. Every other key matches too: K P4–P5 (including the 1×4 / 2×2 completeness argument), 2–3 P1–P6 and 4–5 P1–P5.
  - The 2–3 P6 remark "Other choices with gcd 3 and three distinct shorter sides also work" is true. Only the 3-first rectangle can vary.
- **P6 table:** all 49 entries in the delivered table match my count. The unique winner 13×8, the 12×7 example and the remainder recurrence (checked for all a, b < 80) are all correct.
- **Extension:** 20×12 → 12,8,4,4, and scaling multiplies every square side (k = 2–4, a, b ≤ 30).

### Problem 4 (minor, base guide p. 1, "Materials and preparation"): the K–1 cutout count is for three children, and the table has four

- **Text (p. 1):** "provide four 3-by-3 cutouts per child for K P5 (12 cutouts for the current KK1 group)".
- **Evidence (`out_check_guides32.txt`, Materials):**
  - `worksheet-workflow/context.md` puts two kindergartners and two first graders at the K–1 table. Four cutouts each makes 16.
  - The guide's own route update (p. 5) says "sixteen matching 3-by-3 cutouts give each of four children a set".
  - An adult who prepares from p. 1 cuts one set too few.
- **Smallest fix:** in `facilitator-src/guide.json`, change "(12 cutouts for the current KK1 group)" to "(16 cutouts for the current K–1 table of four)".

## Bonus adult guide (`week-32-bonus-facilitator.pdf`): checks out completely

- **Minimum tilings:** 6×5 needs 5 and greedy uses 6; 4×3 needs 4.
- **Witness:** the 5-piece witness coordinates are disjoint and cover 30 cells.
- **Area decompositions:** all hold. Nothing sums to 12 with one or two squares, and 4+4+4 is the only three-piece sum. With sides at most 5, nothing sums to 30 with one or two squares, 25+4+1 is the only three-piece sum and 16+9+4+1 the only four-piece sum.
- **Projection argument:** correct. 5+2 and 4+3 cannot both fit in 6×5, and three 2×2 squares cannot fit in 4×3.
- **P3:** 25 = 4·4 + 9·1 and 35 = 4·2 + 9·3 are the unique area splits. The boundary and packing arguments are correct, and so is "a height-5 strip holds at most ⌊w/3⌋ side-3 squares" (search, w = 3–12).
- **P4:** the smallest rectangles, their size lists and the enlargements 6×4, 16×6 and 14×8 are right. The backward rebuild 2×1 → 3×2 → 8×3 is right, and in general a rebuild followed by greedy returns the recipe. The final count is ≥ 2 for every nonsquare, [1] is the only square recipe, and the ratio is unique up to scale.
- **Materials:** the stock covers each single task.
