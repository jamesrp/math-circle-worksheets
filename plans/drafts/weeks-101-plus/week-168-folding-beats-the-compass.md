# Week 168 (draft plan): Folding beats the compass

**Strand:** shape (Shapes and spaces). **Deep-math field:** geometric constructions, origami axioms, field theory. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Compass and straightedge can bisect any angle but cannot trisect every angle, and cannot double a cube (make a length ∛2 from a length 1): the lengths they reach are exactly those built from 1 by adding, multiplying, dividing and taking square roots, and ∛2 is a root of x³ − 2, which has degree 3, not a power of 2 (Wantzel, 1837). Paper folding is strictly stronger. Its basic moves (Huzita's six operations and a seventh found by Hatori in 2002; Jacques Justin had listed all seven in 1989) include one the compass has no analogue of: a single fold that places two given points onto two given lines at once. That fold solves cubic equations: Margherita Beloch showed in the 1930s that origami can solve any cubic, and with one fold at a time origami solves all cubics with rational coefficients. Hisashi Abe's 1980 fold trisects any acute angle, and Peter Messer's fold doubles the cube. The lengths reachable by origami are exactly the algebraic numbers whose splitting field over the rationals has degree 2^a·3^b. Children meet the power of folding through three exact folds. Haga's fold: fold the bottom-left corner of a square up to the midpoint of the top edge; the folded bottom edge meets the right edge 1/3 of the way up, so one fold makes thirds with no measuring. More generally a corner landing at distance q along the top edge marks a point 2q/(1 + q) down the far edge: q = 1/3 gives 1/2 and q = 1/4 gives 2/5. The equilateral triangle: crease the vertical centre line, then fold so the bottom-left corner lands on that line with the crease through the bottom-right corner; the landing point is at height √3/2 and makes an equilateral triangle with the bottom edge. Abe's trisection: with two low horizontal creases at heights h and 2h, fold so the corner lands on the lower crease and the left end of the upper crease lands on the angle's line; the folded positions of the corner and of the lower crease's end lie on the two trisecting lines. An approximate method needs no tricks: pinch a guess for 1/3, pinch halfway to the right edge, then halfway back to the left edge; each round divides the error by 4. Proved: Wantzel's impossibility, the origami results cited. Checked here: Haga's fold, the triangle, Abe's fold for five angles, the pinch rule.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [From flapping birds to space telescopes](https://static.usenix.org/event/usenix08/tech/slides/lang.pdf), Robert J. Lang, talk slides hosted by USENIX (2008 conference) (read November 4, 2026). Abe's trisection diagram; Messer's cube doubling; the Delian problems impossible with compass and unmarked straightedge; Huzita's six operations, Hatori's seventh (2002), Justin's 1989 list; one-fold origami solves all cubics with rational coefficients.
- [Origami and constructible numbers](https://courses.csail.mit.edu/6.885/fall07/lectures/L23_hull.pdf), Tom Hull, lecture slides hosted with MIT course 6.885 (fall 2007) (read November 4, 2026). The basic operations; Beloch's 1930s result that origami solves any cubic; Abe's 1980 trisection as solving a cubic; the 2^a·3^b degree criterion.
- [Dividing a segment into equal parts by paper folding](https://www.cut-the-knot.org/pythagoras/PaperFolding/SegmentDivision.shtml), Alexander Bogomolny, Cut-the-Knot (read November 4, 2026). Haga's construction: fold a corner to a point at 1/k of the opposite side, giving 2/(k + 1) on the far side; proof by similar triangles.
- Prior use with children: [Haga's Origamics](https://bpb-us-e2.wpmucdn.com/sites.wustl.edu/dist/b/4012/files/2023/02/2012-01-29-bickel-origamics.pdf), Washington University in St. Louis Math Circle file dated January 29, 2012 (read November 4, 2026). Students fold a corner to points on a square and study the flaps; Haga's theorem is left for them to discover.
- Prior use with children: [Making Sixty](https://nrich.maths.org/6355), NRICH, ages 14 to 16 (read November 4, 2026). Fold a 60° angle and an equilateral triangle from a sheet and prove why; the fold here is adapted for younger children.

## A kid-friendly way in

Origami paper squares (15 cm, two colours), printer-paper strips, pencils, a printed angle sheet (a square with an angle drawn from the bottom-left corner, for 4–5), a protractor for checking. Prep about 15 minutes: cut squares and print angle sheets. Launch (2–3 minutes): fold a square in half and in quarters with everyone ("halves are easy"), then ask the group to fold exactly a third without a ruler; take guesses, then show Haga's one fold and check it by folding the square along the new mark: the two parts match one-to-two.

Suggested hour: 0–5 halves and the thirds challenge; 5–20 Haga's fold and checking it; 20–35 equilateral triangle; 35–55 other landing points and the pinch game (2–3) or Abe's trisection (4–5); 55–60 share which fractions appeared.

## By band

- **K–1:** Fold halves and quarters; try thirds by eye and compare the pieces. Copy the "magic fold" step by step with an adult and check that the three strips match. Fold the equilateral triangle and check that its three sides are the same length by turning it.
- **2–3:** Haga's fold with other landing points: the midpoint, the 1/4 mark, the 1/3 mark. Which marks appear on the far edge, and can you get fifths? The pinch game: start from a bad guess for a third, alternate halving to the right and to the left, and watch the pinches settle.
- **4–5:** Trisect a printed angle with Abe's fold and check with a protractor. Why is the triangle fold exactly equilateral (which lengths are copies of the square's side)? Story: the compass problems the ancient Greeks could not solve, and the one fold the compass cannot imitate.

## Checked facts

In `check_shape_2.py`, `check_week_168()`: reflection geometry for Haga's fold gives exactly 2/3 down the far edge for a midpoint landing, and 2q/(1 + q) for q = 1/2, 1/3, 1/4, 1/5 (so 1/2 and 2/5); the equilateral landing point (1/2, √3/2) is at distance 1 from both bottom corners and inside the square; Abe's fold, solved numerically with h = 0.2, puts the folded corner at θ/3 and the folded crease end at 2θ/3 for θ = 30°, 45°, 60°, 75°, 80°; the pinch game from 1/2 has error 1/24 after one round and divides it by 4 each round; no fraction p/q with p, q < 30 cubes to 2. Impossibility and origami theorems are cited.

## Nearest existing themes

Week 28 (Flat folds) studies which crease patterns fold flat (Maekawa, Kawasaki); draft 124 (One straight cut) folds to align edges for a cut. Atlas AD-12 is the compass side: ruler-and-compass lengths and the impossibility of ∛2. Week 85 (Drawing machines) is another physical construction tool. New here: folding as a construction method more powerful than the compass, exact thirds and fifths by one fold, trisection.

## App connection

Shapes and spaces, near Flat folds (Week 28). Board: a square sheet; the child drags a corner onto a target point and the app shows the fold and where the folded edge crosses the others, with a fraction label on the edge. Puzzles: "Mark exactly 1/3 of the side in one fold"; "Make a 60° corner"; "Mark 2/5 with two folds". Flat folds could carry it with a "drag corner to point" move.

## Open questions

- Abe's fold needs a precise simultaneous placement; test whether grades 4–5 can do it on 15 cm paper, and choose h so the corner lands inside the square for the angles used (h = 0.2 of the side is too high for 30°).
- Whether the WU circle's "Haga's Origamics" activities (folding to an arbitrary point) suit 2–3 as an opening exploration.
- How much of the "compass cannot" story to tell when the atlas AD-12 family has not been run.
