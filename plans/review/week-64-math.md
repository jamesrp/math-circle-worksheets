# Week 64 (straight paths on strange surfaces): math check

Scope:
- `lowell-math-circle-year-2/week-64/week-64-students.pdf`: one shared packet, 9 pages, Problems 1–9. Pages 1–6 are headed Grades 3–5 and pp. 7–9 Grades 4–5. I treated it as the single band.
- `week-64-facilitator.pdf`: 12 pages.

Sources read: `source/week-64/student/generate.py` (exact coordinates, gluing arrows, start dots, sector data) and the guide TeX files in `source/week-64/guide/`. I did not run or import the packet's `verify.py` files or rely on `student-checks.json`. Every diagram check reads the **delivered** PDFs. Checked October 10, 2026.

**Result: every answer, length, corner class, cone angle, trajectory, first return, development and proof in the packet and guide is correct, and every diagram encodes what its text says. I found 1 problem, a minor misworded hint in the guide (p. 3).**

## How it was checked

Scripts and saved outputs are in `plans/review/checks/week-64/`. Each script finds the repository from its own location.

- **`geom64.py`** (output `geom64.out`, 134 checks, 0 failures) reads the student PDF's drawing primitives with PyMuPDF and checks:
  - **Octagons:** all eight are regular, with sides equal to 0.01 pt and every angle 135°. Their vertices are (±1, ±a), (±a, ±1) in side-2 units. Widths are 3.94/1.63, 5.35, 4.65/1.40 and 4.02 in.
  - **Edge gluings:** on every octagon each letter labels two opposite sides, and the printed arrows agree as vectors, so each pair is glued by a translation. The convention is identical on all eight octagons.
  - **p. 1:** P, Q and R sit at (−.65, 0), (−.3, 1.6) and (.2, −1.45), each with a horizontal rightward arrow. In the convention example, X lies on the right C edge and its mate X on the left C edge at the same height, and the resumed segment is parallel to the arrival segment.
  - **p. 3 example:** copy 2 is copy 1 translated by one width, and the two pieces lie on one straight line through the shared C edge.
  - **p. 4:** corner numbers sit next to their corners. Corner classes computed from the printed letters and arrows give {1,…,8} and {9,…,12}.
  - **p. 5:** sectors measure 135.00° and 90.00°, and the scale bar is exactly 72 pt. Each of the 12 pieces is an orientation-preserving copy of its numbered corner, with the same letter on each side and the same arrow sense. So no piece needs flipping. Following matching rays closes one 8-cycle (1, 6, 3, 8, 5, 2, 7, 4) and one 4-cycle.
  - **pp. 6–9:** each L is three equal squares with equal x/y scale and an eighth grid of 42 lines. The squares are named A, B, C, and p, q, r, s each mark two translated outer edges. The printed gluing gives right = (A B) and up = (A C).
  - **Dots and arrows on pp. 6–9:** dots sit at local (½, ¼) on pp. 6, 7 and 9 and at (¼, ½) on p. 8. Travel arrows point (1,0) and (0,1) on p. 6, (1,1) on p. 7 and (2,1) on p. 8. The p. 9 mini-arrows have ratios 1:2, 2:3, 3:1 and 3:2, under matching labels.
- **`math64.py`** (output `math64.out`, 61 checks, 0 failures) uses the gluings read by `geom64.py`. It computes the dynamics exactly, with Q(√2) arithmetic for the octagon and Fractions for the L.
  - It runs the rightward flow for P1–P3 and samples 6,935 rational interior starts for P2, plus three irrational heights.
  - It checks P3's equal-chord condition, its uniqueness, the developments and that the copies do not overlap.
  - It checks the vertex chains, the cone angles and the Euler characteristics.
  - It follows every L trajectory for P6–P9, with event times, square sequences and dot visits.
  - It tests the P9 universal claim on 5,400 (direction, start) pairs. These are all 45 coprime directions (p, q) with 0 ≤ p, q ≤ 8, axis directions included, from 40 starts in each of the three squares. Each one closes within at most 3 whole blocks or hits a corner.
  - It reads the guide's p. 4 figure from the PDF and checks guide values against `pdftotext` of the delivered guide.

## Student packet (pp. 1–9): checks out

- **Convention example (p. 1):** S = (.7, −.5) heads up-right to X = (a, .271) on the right C edge. It resumes at (−a, .271) on the left C edge, parallel to the arrival.
- **P1:** P closes with one crossing (C), length 2a = 2 + 2√2. Q closes with crossings B then D, and R with D then B, each of length 2b = 4 + 2√2. None hits a corner. Q and R are distinct loops of the outer family: Q's lower chord is at 1.6 − b and R's upper chord at b − 1.45.
- **P2:** there are exactly two closed lengths, 2a for |y| < 1 and 2b for 1 < |y| < a. Only y = ±1 hits a corner, and the horizontal position does not matter. At the printed size these are 5.35 in and 5.35√2 ≈ 7.57 in.
- **P3:** the two chords are equal only at y = b/2. That height meets the D edge exactly at its midpoint, and the trip closes with two chords of length b each. Every other D-edge start height gives unequal chords. A middle-band trip from a C edge has only one stretch, so the wording forces the outer family.
  - The two-copy development works: copy 2 at (b, b) puts its SW B edge on copy 1's NE B edge, and the line from (−b/2, b/2) to (3b/2, b/2) ends at copy 2's SE D midpoint. No copies overlap.
- **P4:** each shape has one group: octagon {1–8}, square {9–12}. The endpoint matches are A 8~5, 1~4; B 1~6, 2~5; C 3~6, 2~7; D 4~7, 3~8; E 12~11, 9~10; F 10~11, 9~12.
- **P5:** the octagon gives 8 × 135° = 1080°, three full turns. The square gives 4 × 90° = 360°, one turn. The pieces support exactly this assembly.
- **P6:** right from A or B and up from A or C each have length 2. Up from B and right from C each have length 1. No path hits a corner.
- **P7:** all three dots lie on one orbit. First returns come after 3 blocks (length 3√2), with dot order A→B→C→A from A and its cyclic shifts from B and C.
- **P8:** A alone is shortest: 1 block, √5, with events r, u, r at 3/8, 1/2, 7/8. B and C share a 2-block orbit (B→C→B), exactly twice as long.
- **P9:**
  - (1,2) closes after 1 block, with events u r u.
  - (2,3) hits A's top-right corner at block-time ¼.
  - (3,1) closes after 3 blocks, with events r r u r and labels A→C→B→A.
  - (3,2) closes after 2 blocks, with events r u r r u and labels A→B→A.
  - The universal answer is yes: the block permutation argument holds, and it is confirmed on 5,400 cases.

## Adult guide: mathematically correct throughout, apart from one misworded hint (Problem 1)

- **Overview (p. 1):** every stated fact holds under its stated hypotheses.
  - Translation gluing, with no reflection or turn.
  - Two horizontal families, 2a for −1 < y < 1 and 2b for 1 < y < a.
  - One vertex class, 1080° = three turns, χ = 1 − 4 + 1 = −2 and genus 2. The classification step is flagged as adult context.
  - For the L: right = (A B), up = (A C), 12 sectors forming one 1080° point, and genus 2 with a different metric.
  - The rational-direction return holds in the square model only. It is not transferred to the octagon.
  - Hyperbolic octagons have 45° corners.
- **Background (pp. 8–11):**
  - The v_i ↔ v_{i+5}, v_{i+1} ↔ v_{i+4} rule, the four-row translation table and its point maps are correct.
  - The middle- and outer-band loop derivations are correct: L = 2(b − y) + 2y = 2b, the chords are equal exactly at y = b/2, and the comparisons 4.828, 6.828 and difference 2 are right.
  - The octagon vertex chain is correct, as are the 24 eighth-turn pieces and the 720° concentrated excess.
  - The L event table (times 1/2 … 11/4, squares B, B, A, C, C, A) and the (2,1) blocks are correct.
  - The 12-sector chain is correct: every step is a single edge match, and F = 3, E = 6, V = 1.
  - The finite-permutation return proof is correct, with the right assumptions and scope.
- **Keys (pp. 3–7):** every table, length, order, tour and hint answer matches my computation. That includes:
  - the P1 crossing table;
  - the P2 classification and printed inches;
  - the P3 seam-start and optional three-copy developments. The guide figure on p. 4 is read from the PDF: copies at (0,0), (b,b), (2b,0), path at y = b/2 with marks at 0, b/2, 3b/2, 2b;
  - the desk estimate for the three-copy layout: 11.23 × 7.94 in against "about 12 by 8";
  - the P4 tours 1→6→3→8→5→2→7→4→1 and 9→10→11→12→9;
  - the P5 order 1, 6, 3, 8, 5, 2, 7, 4 with seams B, C, D, A, B, C, D, A, and the square seams E, F, E, F;
  - the P6–P9 tables;
  - the square-centre warning: (½, ½) in direction (1,1) hits a corner at ½.

### 1. Guide p. 3, Problem 1, hint 3 (minor): the hint's trigger cannot happen on these paths

- **Quoted text:** "3. When the route crosses its starting horizontal line, keep going until it reaches the actual starting dot."
- **Evidence:**
  - All three P1 routes are horizontal. They run along their own lines and never cross them.
  - Each one comes back onto its starting line at the left boundary. For P that is the left C edge. For Q it is the NW D edge, and for R the SW B edge, each after the second crossing (`math64.out`, P1 lines).
  - An adult following the hint literally waits for an event that never occurs. The intended action, continuing past the re-entry edge to the dot, is correct.
- **Smallest fix:** "3. When the route comes back onto its starting line at a left edge, keep going until it reaches the actual starting dot."
