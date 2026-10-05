# Week 31 (hidden orchard): math check

Scope: everything current in `lowell-math-circle-year-2/week-31/`, archive folders excluded:

- `week-31-k-1.pdf` (F31-K-v2, 5 pp., P1–P5)
- `week-31-grades-2-3.pdf` (F31-23-v2, 5 pp., P1–P6)
- `week-31-grades-4-5.pdf` (F31-45-v2, 5 pp., P1–P7)
- `week-31-facilitator.pdf` (5 pp.: the guide on pp. 1–4 and a route update on p. 5)
- the bonus companion `week-31-bonus.pdf` (W31-BON-v1, 4 pp., P1–P6) and its guide `week-31-bonus-facilitator.pdf` (W31-BON-FAC-v1, 5 pp.)

Sources read:
- `source/week-31/editable/student-src/`: `make_packets.py` and `draw.py`
- `source/week-31-bonus/student-src/bonus.tex`

The delivered PDFs are byte-identical (same MD5) to the reference copies in both source folders. I did not run or import any of the packet's own checkers: `verify.py`, `verify_revision.py`, `facilitator-src/check_math.py`, `writer-check.py` or `math/independent-check.py`. I also did not read the packet's review or answer notes. Checked October 5, 2026.

**Result:**
- **Mathematics:** read as intended, every student problem has the answer its page implies, and nothing it asks for is impossible. Every list, table, count and proof in both adult guides is correct, with one exception.
- **Problems found:** 5, numbered in page order below.
  1. The "(4, 2)" label in the shared Grades 2–3 / 4–5 coordinate example sits beside the wrong row (diagram, minor).
  2. The 4–5 P1 sentence is ambiguous, and one reading has no answer (wording, minor).
  3. On bonus pp. 2–3 the 4 × 4 grids sit so close together that they read as one dot field. Read that way, P4's expected "no" is false (diagram, moderate).
  4. Bonus P1 reuses the letter B, which the base packet uses for "blocker" (wording, minor).
  5. One example in the base guide's optional extension is wrong (mathematical error, minor).

## How it was checked

My scripts and their saved outputs are in [checks/week-31/](checks/week-31/). Each script finds the repository from its own location: four folders up from there, or three from `tmp/review-runs/week-31/`. They need PyMuPDF (`python3 -m pip install pymupdf`).

- **`pdf31.py`** reads the delivered PDFs' vector content and text positions:
  - filled dots, stroked rings, the filled lookout square, lines, boxes and text spans;
  - it groups dots into lattices joined by axis-aligned steps of one spacing, and maps rings, line ends and labels to lattice coordinates.
- **`orchard31.py`** holds independent brute-force mathematics:
  - "dots strictly between P and T" is computed by scanning the bounding box for collinear lattice points, with no gcd, so the gcd rule can be tested against it;
  - first points, hide counts and ray groups;
  - triangle side and interior dots, and congruence classes;
  - a breadth-first search over ordered card rows; the full mediant-insertion tree; and the wedge-search procedure.
- **`check_students31.py`** → `out_check_students31.txt` (188 checks, 2 failures, both Problem 1):
  - every board's size, spacing in both directions, axis labels and O label;
  - every ring, thread and arrow read back from the PDFs;
  - every answer for K–1 P1–P5, 2–3 P1–P6, 4–5 P1–P7 and bonus P1–P6.
- **`check_guides31.py`** → `out_check_guides31.txt` (91 checks, 1 failure, which is Problem 5). For every mathematical claim in both guides it does two things:
  - confirms that the quoted sentence is in the delivered PDF;
  - recomputes the claim.

  This covers the visible-dot catalog, all keys, the 2–3 P2 table, the P4/P6 proofs, Pick's theorem with "empty ⇔ area ½" over every triangle in a 6 × 6 dot square, and the Stern–Brocot invariant and coefficient-descent proof.
- **`bonus_layout31.py`** → `out_bonus_layout31.txt` measures what happens on bonus pp. 2–3 if the separate grids are read as one field (Problem 3).

## K–1 (5 pp.): checks out completely

- **p. 1 launch examples:**
  - Both 5 × 5 grids use a 9 mm spacing in both directions.
  - The "hidden" thread runs exactly from O to (4, 2) through the ring at (2, 1), which is the only dot between them.
  - The "visible" thread runs O → (3, 2) and passes no dot.
  - The T and B labels sit within half a spacing of their rings.
- **P1:** the 0–4 board (20 mm spacing) has 13 visible dots: (1,0); every dot of row 1; (1,2),(3,2); (1,3),(2,3),(4,3); (1,4),(3,4).
- **P2:**
  - Board 1's rings are (2,4), (3,3), (4,2) and (4,4). All are hidden; their nearest blockers are (1,2), (1,1), (2,1) and (1,1).
  - Board 2's rings are (0,4), (2,2), (4,0) and (4,3). Only (4,3) is visible. The others are blocked first by (0,1), (1,1) and (1,0).
- **P3:** on the 0–6 board, 9 targets have exactly one dot between (all gcd 2) and 5 have exactly two (all gcd 3).
- **P4:**
  - (1, y) is visible in every row.
  - Row 1 is the only row with only visible dots.
  - So the answer to "a hidden dot in every row?" is no: row 1 has none.
- **P5:** (1,0), (0,1) and (1,1) tie, each hiding 5 dots. Every other first dot hides at most 2.

## Grades 2–3 (5 pp.): mathematics checks out; see Problem 1 for the p. 2 label

- **p. 1:** the examples are the same as K–1 and check out the same way.
- **P1:** the 0–6 board (20 mm) has 25 visible dots.
- **p. 2 coordinate example:** the 7 mm grid is equal in both directions. The ring is at (4,2), and the arrows run O → (4,0) → (4,2), which matches "4 across" and "2 up".
- **P2:** all targets lie on the printed board. Their blockers:
  - (6,4): (3,2)
  - (6,3): (2,1), (4,2)
  - (5,3), (5,2) and (4,1): none
  - (4,4): (1,1), (2,2), (3,3)
- **P3:** the lists are the same as K–1 P3.
- **P4:** the five groups are the multiples of (1,1), (2,1), (3,2), (1,2) and (1,0) that fit on the board. Each named direction is its ray's first dot.
- **P5:**
  - (12,8) is hidden behind (3,2), with 3 blockers; (10,7) is visible; (15,5) is hidden behind (3,1), with 4 blockers; (11,1) is visible.
  - "No common factor > 1" matches brute-force visibility on 0–25, axes included.
- **P6:** row 1 is entirely visible. Every row y ≥ 1 also has infinitely many visible dots; only row 0 would be a wrong answer.

## Grades 4–5 (5 pp.): mathematics checks out; see Problem 1 (p. 2 label) and Problem 2 (P1 wording)

- **P1:** hidden targets on the board have 1, 2, 3, 4 or 5 blockers, so three different counts are available.
- **P2:** first dots and blockers:
  - (6,4): first (3,2)
  - (6,3): first (2,1), blockers (2,1) and (4,2)
  - (5,3): first is (5,3) itself, no blockers
  - (6,6): (1,1) … (5,5)
  - (6,0): (1,0) … (5,0)
  - (0,6): (0,1) … (0,5)
- **P3:**
  - (12,8), (15,10) and (21,14) all have first dot (3,2), with 3, 4 and 6 blockers.
  - (25,15) has first dot (5,3) and 4 blockers.
  - (13,8) is visible, with 0 blockers.
- **P4:** the answer is yes, both directions hold. For 1 ≤ a, b ≤ 40:
  - every common divisor q > 1 gives the blocker (a/q, b/q);
  - every blocker t(a,b) has a lowest-terms denominator > 1 that divides a and b.
- **P5:**
  - The groups are {(3,2),(6,4)}, {(2,1),(4,2),(6,3)} and {(1,1)…(6,6)}.
  - First-dot groups partition the board.
- **P6:** first dot = (a/d, b/d) and blockers = exactly k(a/d, b/d) for k = 1…d − 1. I checked this for every target on 0–30 (blocker list on 0–20), axes included.
- **P7:**
  - Row 1 is entirely visible, and it is the only such row.
  - The dots (n, n), n ≥ 2, are all hidden.
  - (100,100) and (100,0) each have exactly 99 blockers.

### Problem 1 (minor, Grades 2–3 p. 2 and Grades 4–5 p. 2): the "(4, 2)" label sits beside row 3, not beside the ringed dot

- **Text and diagram:** the example under "(4, 2) means 4 across and 2 up from O." This example defines the across/up convention for both packets.
- **Evidence (`out_check_students31.txt`, both `info` lines):**
  - The label's centre is level with height 2.79 on the grid, i.e. with row 3.
  - It is 2.2 cm (3.1 spacings) to the right of the ring at (4, 2). Nothing labels the ring itself.
  - A child reading across from the label meets the row-3 dots, not the circled dot.
- **Smallest fix:** in `make_packets.py` `coord()`, move the `(4, 2)` node from `(5.9, y+2.15)` to beside the ring, e.g. `(4.7, y+2.7)`. The ring is at `(3.8, y+2.7)` and "2 up" stays at `(5.0, y+3.4)`.

### Problem 2 (minor, Grades 4–5 p. 1, worksheet Problem 1): one reading of the sentence makes the task impossible

- **Text:** "Find three visible targets and three hidden targets with different numbers of blockers. Mark each blocker."
- **Evidence:**
  - Every visible target has 0 blockers. If "with different numbers of blockers" is read as applying to all six targets, no answer exists.
  - The guide (p. 4) intends the other reading: "Hidden examples with distinct counts: (2,2) has (1,1); (3,3) has (1,1),(2,2); …"
- **Smallest fix:** "Find three visible targets. Then find three hidden targets that have different numbers of blockers, and mark each blocker."

## Bonus companion (4 pp., Grades 2–5): mathematics checks out; see Problems 3 and 4

- **P1 board:**
  - 7 × 7 dots at 20 mm.
  - Lookout L is the filled square at (0,0) and lookout R the heavy ring at (1,0).
  - Target rings sit on every dot of rows 3 and 6.
- **P1 answers:**
  - Row 3 reads 1,1,B,1,1,B,1 and row 6 reads 1,1,1,0,0,1,1.
  - Only (3,6) and (4,6) are hidden from both lookouts.
- **P2:** no target on row 4 is hidden from both, checked for −300 ≤ x ≤ 300; parity explains why.
  - Across rows 1–30, a row has a doubly hidden target exactly when its height is not a prime power.
  - On row 6, double hiding happens at across ≡ 3 or 4 (mod 6).
- **P3:** the corners read from the rings are:
  - A (0,0),(1,0),(0,1): empty, area ½.
  - B (0,0),(1,2),(3,1): clear sides, with (1,1) and (2,1) inside; area 5/2.
  - C (0,0),(2,0),(0,2): side dots (1,0), (0,1) and (1,1), nothing inside; area 2.
  - D (0,0),(1,1),(2,1): empty, area ½.

  No dot of another grid touches any printed triangle.
- **P4:** a 4 × 4 grid holds 124 empty triangles, all with area ½. They fall into 4 congruence shapes, with squared sides {1,1,2}, {1,2,5}, {1,5,10} and {2,5,13}. So three different shapes fit, and the intended answer is "no".
- **p. 4 worked example:**
  - The cards are (2,1) + (1,1) = (3,2), and that pair is a legal neighbour pair (|det| = 1).
  - The 6.5 mm grid is equal in both directions.
  - The arrow runs O → (3,2), which matches "3 across" and "2 up".
- **P5:**
  - The fewest insertions that contain both (4,3) and (3,4) is 7. The page prints 8 blank boxes.
  - All 16,383 cards producible within 14 levels are coprime and keep |det| = 1 with both neighbours, so (4,2) never appears.
- **P6:** the wedge procedure reaches every one of the 23 coprime targets with 1 ≤ a, b ≤ 6. The cards with coordinates ≤ 6 are exactly those 23, each produced once.

### Problem 3 (moderate, bonus pp. 2–3, worksheet Problems 3–4): the separate 4 × 4 grids sit so close that they read as one field, and read that way P4's answer is "yes"

- **Text:**
  - p. 1: "The regularly spaced orchard continues beyond the printed grid."
  - P4: "Make three empty triangles with different shapes on these grids. Find their areas in grid squares. Can an empty triangle have area larger than half a grid square?"
- **Evidence (measured from the PDF; `out_check_students31.txt` `info` lines and `out_bonus_layout31.txt`):**
  - Within each grid the dots are 20.0 mm apart.
  - Between grids that sit side by side, the facing columns are only:
    - 5.8 mm apart (p. 2, A–B);
    - 6.2 mm apart (p. 2, C–D);
    - 4.9 mm apart (p. 3, the top pair).
  - On p. 3 the lower grid's top row is exactly 20.0 mm below the upper grids' bottom row, but its columns are offset by 1.62 spacings.
  - Each pair therefore looks like one 8-column field with one squeezed column. Nothing on the page says the grids are separate.
  - Within one grid, every empty triangle has area ½. If dots from both top grids on p. 3 are used, a triangle can have no printed dot on its sides or inside and still have a different area:
    - Grid 1 (3,2) with grid 2 (1,0) and (1,1) uses only the two columns on each side of the gap. Its area is 0.62 grid squares.
    - Grid 1 (0,3), (1,3) with grid 2 (0,0) has area 1.5.
    - The sliver grid 1 (3,0), (3,1) with grid 2 (0,0) has area 0.12.
  - These are counterexamples to the intended "no" that exist only because of the layout.
  - In P3 the corners are fixed, every printed triangle lies inside its own grid, and no foreign dot touches it. So the P3 answers are unaffected; the risk is in P4, where children choose the corners.
- **Smallest fix:** keep the grids at least one dot spacing apart and mark each as its own grid. In `bonus.tex`:
  - set the tabular column gap to at least 2 cm (`\begin{tabular}{c@{\hspace{2cm}}c}`);
  - add a light frame inside `\smallgrid`, e.g. `\draw[gray!50] (-.3,-.3) rectangle (3.3,3.3);`.

  Alternatively, print one larger single grid for P4.

### Problem 4 (minor, bonus p. 1, worksheet Problem 1): the record code B means the opposite of the base packet's B

- **Text:** "Mark B if both can see it, 1 if exactly one can see it, and 0 if neither can see it."
  - The base packet, which this encore revisits, says on p. 1 of every band: "B marks a blocker."
- **Evidence:**
  - In the bonus, B is the code for a target that both lookouts see.
  - A returning child who writes B for "blocked", as in the base packet, records the opposite outcome in the one table the guide grades: "row 3 records 1,1,B,1,1,B,1 …".
- **Smallest fix:**
  - Use "2" (or the word "both") for "both can see it".
  - In the bonus guide's P1 key, change "1,1,B,1,1,B,1" to "1,1,2,1,1,2,1".

## Base adult guide (`week-31-facilitator.pdf`): correct throughout, apart from one example in the optional extension (Problem 5)

- **Overview:** all of these are true, with the stated scope of the first quadrant including axes:
  - visibility ⇔ the open segment holds no lattice point;
  - the first point is (a/d, b/d) and the blockers are exactly k(a/d, b/d), k = 1…d − 1;
  - gcd(a, 0) = a, so on each axis only the unit point is visible;
  - "every intermediate lattice point is present" holds because each blocker of a 0–6 target lies on the 0–6 board.
- **Catalog (p. 2):** all seven rows match the enumeration, for 13 and 25 visible dots.
- **Keys:** every list matches my enumeration. That covers K P2–P5 (including the "hides at most two" argument), 2–3 P1–P6 (including the P2 table and the five P4 groups) and 4–5 P1–P7.
- **Proofs:** the P4 converse via t = r/s in lowest terms and the P6 completeness argument are valid; the axis case is covered. The caution that a blocker's coordinates need not divide the target's is right: (4,2) blocks (6,3).
- **Timing and route note (p. 5):** the problem numbers it names match the packets.

### Problem 5 (minor, base guide p. 4, "Optional extension and primary source"): the example of a changed sight line does not change

- **Text:** "Move O to (1,1) on a fresh grid and ask which sight lines change. Work with displacement coordinates (x-1,y-1); for example (3,3) remains hidden behind (2,2), while (4,3) is now visible."
- **Evidence (`out_check_guides31.txt`):**
  - gcd(4,3) = 1, so (4,3) is already visible from O = (0,0).
  - From (1,1) its displacement is (3,2), which is also visible.
  - Nothing changes, yet "is now visible", set against "remains hidden", presents it as a sight line that changed. That is the opposite of what the example is meant to show.
  - The "(3,3) remains hidden behind (2,2)" half is correct.
  - On the 0–6 board, 19 dots change from hidden to visible, e.g. (4,2): hidden behind (2,1) from O, displacement (3,1) from (1,1).
  - 10 dots change the other way, e.g. (3,5): visible from O, displacement (2,4), so hidden behind (2,3).
- **Smallest fix:** replace "(4,3)" with "(4,2)": "… while (4,2), hidden from O behind (2,1), is now visible." Optionally add "and (3,5) is now hidden behind (2,3)."

## Bonus adult guide (`week-31-bonus-facilitator.pdf`): checks out completely

Every mathematical statement is true with the stated hypotheses, and every solution matches my enumeration:

- **Visibility:** the translated criterion gcd(|a−c|, |b−d|) = 1, checked for lookouts in 0–2² and targets in −4…7². The doubly-hidden condition for (0,0) and (1,0), the prime-power rows and the residues 3 and 4 mod 6 at height 6 all hold, as does the (1,2)/(2,3) blocker pair for (3,6).
- **Empty triangles:** Pick's theorem with its stated assumptions, and "empty ⇔ area ½", checked over every triangle in a 6 × 6 dot square. So is "visible sides do not exclude interior dots", with B as the witness: edge displacements (1,2), (3,1) and (2,−1).
- **P3 and P4 keys:** the P3 solutions for A–D are correct. The three P4 shapes, (0,0),(1,0),(0,1); (0,0),(2,1),(1,1); and (0,0),(3,1),(2,1), are empty, with squared sides {1,1,2}, {1,2,5} and {1,5,10}. The base-1, height-1 area arguments for the last two are right.
- **P5 key:** the final row (1,0),(2,1),(3,2),(4,3),(1,1),(3,4),(2,3),(1,2),(0,1) has increasing slopes and |det| = 1 for every neighbour pair. The coprimality argument, determinant preservation and the (1,1)+(1,3) = (2,4) caution are all correct.
- **P6:** the wedge procedure and the coefficient-descent completeness proof are correct, including integer coefficients and that A = B forces T = u + v. The count of 23 bounded coprime targets is right.
- **Spacing:** "Working grid spacing is 20 mm" matches the PDF.

## Not checked

- The cited sources are not available locally, so I could not verify their page and section references. These are Crisman, *Number Theory: In Context* §24.6.1, and *Math Circle by the Bay* pp. 129–134 and viii–x.
- Physical thread accuracy, pegboard fit and timing are outside a math check, and both guides already mark them untested.
