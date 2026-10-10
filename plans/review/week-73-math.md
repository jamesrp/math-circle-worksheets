# Week 73 (The gentlest stretch): math check

Scope:
- `lowell-math-circle-year-2/week-73/week-73-students.pdf`: one shared Grades 4–5 packet, 4 pages, Problems 1–6. I treat it as the only band.
- `week-73-facilitator.pdf`: 3 pages.

Sources read: `source/week-73/student/students.tex` and `guide/facilitator.tex`, plus the package README, MATHEMATICS.md and the student and guide READMEs. I did not run or import the package's own checkers. My scripts and their saved outputs are in `plans/review/checks/week-73/`. Checked October 10, 2026.

**Result: every answer, bound, construction and numerical claim in the packet and the guide is correct, and every diagram encodes what its text says. I found 1 problem, and it is minor: on pp. 1–3 the inner side labels "right" (old sheet) and "left" (square) sit 1.4–2.3 mm apart in the gap between the two figures.**

## How it was checked

- **`check_math.py`** (output `check_math.py.out`, 27 checks, 0 failures) uses exact rational arithmetic throughout. It covers:
  - **Five-pin game:** the max over all 10 pairs, at 6,241 interior positions of the new O (step 1/40).
  - **Fan maps:** it builds the exact affine map for each of the four triangles. Because the sheet is convex, the worst stretch of a piecewise-affine map is its largest piece operator norm, and the script uses that.
  - **Every pair of 13 dots:** the 5 originals plus 8 first-level halfway dots, all 78 pairs, at every grid position.
  - **Disk test:** the two-disk midpoint inequalities.
  - **Rule F:** the identity for F on 20,000 exact displacements, and where the dotted lines go.
  - **A second optimal rule:** it confirms that "one valid rule" is the right wording.
  - **Targets:** every Problem 5/6 target, plus a sweep of all quarter-unit targets up to 10 × 10.
  - **0.735 mm claim:** the guide's measurement figure.
- **`check_diagrams.py`** (output `check_diagrams.py.out`, 61 checks, 3 failures, all three being the label-spacing finding below) reads paths and text boxes from the delivered student PDF. It checks:
  - the sheet and square sizes (0.94 in per unit, equal axes);
  - the centre O and its four spokes;
  - the corner dots and labels;
  - the quarter-unit grids, which line up with the outlines;
  - that the stretch example prints at 2.000 cm and 3.000 cm;
  - the p. 2 midpoint example;
  - the p. 3 dotted grid (7 interior verticals at half-unit spacing and one mid-height horizontal);
  - the p. 4 rectangles (4×1 → 6×2 and 4×1 → 2×3 at one shared 0.6 in scale) and the placement of their "top" and "left" labels.

## Grades 4–5 shared packet (pp. 1–4): mathematics checks out; one label-layout problem

- **Stretch example (p. 1):** 2 cm → 3 cm gives stretch 1½. Both segments print at exactly 2 cm and 3 cm.
- **P1:** with A–D fixed, AD and BC always stretch exactly 2 (1 → 2). AB and CD stretch ½, and the diagonals √17 → √8 stretch 0.686.
  - Each O-to-corner ratio is below √8/(√17/2) = 1.372.
  - So every interior O scores exactly 2 when all 10 pairs are tested. That is the intended tie, and it holds at all 6,241 grid positions.
- **P2:** O must be interior. For each interior O the four affine triangle maps glue into a legal side-preserving map. The centered fan is exactly F(x,y) = (x/2, 2y) on all four triangles.
  - **Exact tests:** among all 78 pairs of the 5 original and 8 halfway dots, only two pairs ever beat 2: O with the bottom-side midpoint and O with the top-side midpoint. Exactly one position survives every test, (1,1).
  - **Halfway dots alone:** pairs made only of halfway dots never detect an off-center O. This is why the guide's hint to offer side midpoints matters.
  - **Fan check:** every off-center fan has worst stretch above 2, and the centered fan's worst stretch is exactly 2.
  - **Example:** the p. 2 M and N are exact midpoints in both triangles.
- **P3:** F is a legal homeomorphism. The dotted lines x = k/2 go to x = k/4, and y = ½ goes to the square's middle line.
  - F is not the only valid rule. For example, (a(x), 2y) with a of slope 1 on [0,1] and slope 1/3 on [1,4] also has worst stretch 2.
  - So the open "make a rule" wording is appropriate.
- **P4:** for F, 4(p² + q²) − (p²/4 + 4q²) = 15p²/4 ≥ 0, so every pair passes, including diagonal pairs and pairs between grid lines. No rule can do better: (x,0) and (x,1) are 1 apart, and their images lie on the bottom and top sides, at least 2 apart.
- **P5:** the optimum is max(W/4, H) in general:
  - 6 × 2 gives 2, with rule (3x/2, 2y) and a vertical boundary pair as the forced pair.
  - 2 × 3 gives 3, with rule (x/2, 3y) and the same kind of pair.
  - The drawn shapes are exactly 4×1, 6×2 and 2×3 at one scale.
- **P6:** the optimum is exactly 1½ if and only if W ≤ 6 and H ≤ 1½ with at least one equality. The quarter-unit sweep matches this on all 29 grid targets. The 4×1 sheet itself scores 1, so it is not an accidental answer.

### 1. Pages 1, 2 and 3, the sheet pairs (minor): the inner "right" and "left" labels read as one floating pair

- **Diagram:**
  - In `\fanboard` (pp. 1–2), the old sheet's `\node[rotate=90] at(4.36,1){right}` and the square's `\node[rotate=90]at(-.35,1){left}` both sit in the 60.9 pt gap between the two figures.
  - Page 3 has the same layout at 4.32 and −.35.
- **Evidence (`check_diagrams.py.out`):**
  - On pp. 1–2 the two words are only 3.9 pt (1.4 mm) apart. On p. 3 they are 6.6 pt (2.3 mm) apart.
  - Each word is about 18 pt from its own figure and about 32 pt from the other. Rendered, they look like a stacked "right / left" pair in mid-gap.
  - The attribution is correct, and the outer "left: 1 unit" and "right: 2 units" labels allow elimination. But the side correspondence is the essential hypothesis of every problem, and p. 3 has no corner letters to fall back on.
- **Smallest fix:** move each inner label toward its own edge.
  - Old sheet: `at(4.2,1){right}` in `\fanboard` and on p. 3.
  - Square: `at(-.2,1){left}` in both places.
  - This puts each word about 8–18 pt from its own edge, with about 24 pt between the two words. The C/B and D/A corner letters are not affected.

## Adult guide (pp. 1–3): checks out completely

- **Overview:** the definitions, the optimum 2, the general target answer max(W/4, H), the "every interior O ties at 2" fact and the claim that "two side-midpoint tests single out the centre" are all true under the stated hypotheses. Those hypotheses are Euclidean distance, side-preserving homeomorphism, worst stretch as a supremum, and an interior O.
- **Answers:** every answer and number matches my computation:
  - P1: 10 = 6 + 4 pairs, √17/2, √17 → √8.
  - P2: the disk inequalities, their sum (u−1)² + (v−1)² ≤ 0, and the legality argument for the fan.
  - P3: the dotted-line images.
  - P4: the identity, the "double then compress" argument and the lower bound.
  - P5: the rules and optima.
  - P6: the 6×1 and 3×1½ rules and the complete characterization.
- **Measurement note:** the 0.735 mm figure is right: O′ = (1.25, 1) gives 0.7348 mm. This is also the largest excess any of the 78 first-level dot pairs gives at that position.
- **Limits stated:** "one valid rule" and "does not classify all optimal homeomorphisms" are both accurate.
