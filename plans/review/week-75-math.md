# Week 75 math check: Twists on a cylinder

Packet checked: `lowell-math-circle-year-2/week-75/week-75-students.pdf` (GGT75-S-v1, 4 pages, one shared Grades 4–5 band) and `week-75-facilitator.pdf` (GGT75-FAC-v1, 3 pages), against `source/week-75/student/students.tex` and `guide/facilitator.tex`. All pages were rendered and inspected.

Script: `plans/review/checks/week-75/check_week75.py` (finds the repository four folders up). Output: `plans/review/checks/week-75/check_week75.out`, with 0 failures. The script does not use the package's own checkers.

## What was verified

- **Printed geometry (PDF vector data).**
  - The cut-out is exactly 6 × 2.4 in at 100%. Its dotted lines sit at heights 1/4, 1/2 and 3/4. A and B lie on the rims, vertically aligned half a turn from the seam.
  - Page 1 seam example: the P segment reaches the right edge at the same height as the left-edge entry (y = 195.66 pt).
  - Page 2 example: exit and entry are at the same height. The lifted line crosses the copy boundary at that height and ends exactly one copy to the right (winding +1).
  - Both Problem 2 lift boards: the B copies sit at k + 1/2 for k = −1, 0, 1, 2, and A is at 1/2 of copy 0. The board therefore holds windings +2 and −1.
  - Page 3 twist diagram: the arrow shift equals the height fraction at 1/4, 1/2, 3/4 and 1. The twisted route ends one copy right.
- **Winding.** On wiggly piecewise-linear (PL) upward routes, the signed seam count equals the copy of the lift endpoint. 2197 routes were tested for each of windings +2 and −1.
- **Twists (P3–P5).** Checked with exact rationals:
  - T_k fixes both rims pointwise, T_j T_k = T_(j+k), and T_−k is the inverse of T_k.
  - T_k adds k to the winding.
  - All 28 words of length 2–4 give windings −4…4. The guide's examples (++− → +, +−− → −, +−−+ → empty) are correct.
  - Exactly C(6,3) = 20 six-twist words act as the identity.
- **Fewest crossings (P6–P7), upper bound.** Straight lifts give exactly |a−b|−1 interior crossings for every pair a ≠ b in −8…8. A bowed copy gives 0 crossings for equal windings.
- **Fewest crossings, lower bound for upward routes.** An exhaustive search covered PL difference functions (3 interior knots, step 1/2) and rejected touches and shared pieces. The minimum is max(|a−b|−1, 0) for |a−b| = 0…5.
- **Fewest crossings, lower bound for general simple arcs.** This checks the guide's claim about arcs that wiggle up and down. In an embedded 4×3 cylinder-grid graph, all 2468 simple A–B paths were enumerated, with windings −3…3. For every pair of windings, the number of shared interior vertices is at least max(|a−b|−1, 0).
- **Printed answers.**
  - Problem 6 table: (0,1) 0, (0,2) 1, (0,3) 2, (−1,1) 1, (−1,2) 2, (2,4) 1.
  - Problem 7: (2,7) gives 4 and (5,5) gives 0.
  - One-route twist examples: 1→2, 1→0, 0→0.
  - A common twist preserves the minimum. This was checked for all a, b in −5…5 and k in −4…4.
- **Guide overview and proofs.** I checked the annulus model, the lift-endpoint characterization of winding and the invariance of winding under fixed-endpoint slides. The straight-line interpolation slide is correct: each intermediate route is a graph over height, so it stays simple. The lower-bound arguments are also correct: the intermediate-value argument for upward routes, and cut, straighten and reglue followed by integer barriers for general arcs. Each statement has the right hypotheses: fixed shared endpoints, interior points only, no touches or shared pieces, and minimum over representatives.

## Findings

**1. Students, page 4, Problems 6–7: "crossings" has two readings, and the seam reading changes the answers.**

- **Location.** Pages 1–2 use "crossing" only for seam crossings: "a rightward crossing counts +1", "Your partner checks the seam crossings". Problem 6 then says "Make the number of crossings between the rims as small as possible. Your partner tries to remove another crossing without changing either winding." Its table puts the column "Fewest crossings" next to "Sketch or seam-crossing record". Problem 7 repeats "the fewest crossings".
- **Evidence.** The intended quantity is the number of times the two strands cross each other, max(|a−b|−1, 0); the guide's table gives 0, 1, 2, 1, 2, 1. Seam crossings are also "between the rims", though. Read that way, the fewest total seam crossings for two routes is |a| + |b|, which gives 1, 2, 3, 2, 3, 6, and 9 and 10 for Problem 7. "Remove another crossing without changing either winding" also makes sense under that reading. The shared note ("Do not count A or B…") points to strand crossings, but it never names them.
- **Smallest fix.**
  - Problem 6: "Make the number of places where the two strands cross each other as small as possible. Your partner tries to remove another of these crossings without changing either winding."
  - Table heading: "Fewest strand crossings".
  - Problem 7: "Predict the fewest strand crossings…" in both places.

**Adult guide:** it checks out completely. The overview's facts and hypotheses, every answer, hint, construction and proof, and all numerical examples are correct.

**Not counted (outside the math scope):** the guide asks for yarn "about 60 inches long", but `source/week-75/student/README.md` says "about 1.2 metres" (about 47 in). Both are enough, because the longest route required, winding 4, is about 24.1 in on the 6 × 2.4 in cylinder. Physical fit and handling remain unrehearsed, as the package states.
