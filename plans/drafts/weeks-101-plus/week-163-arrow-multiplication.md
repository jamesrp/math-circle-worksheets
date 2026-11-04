# Week 163 (draft plan): Arrow multiplication

**Strand:** symmetry, with algebra (Patterns and symmetry). **Deep-math field:** complex numbers, Gaussian integers, similarity transformations. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Think of a number as an arrow from the centre of a grid: 3 points three steps right, −1 one step left, and the arrow to the grid point two right and one up is called 2 + i. Multiplying arrows has a picture: lengths multiply and turning angles add. Multiplying by i is a quarter turn to the left, so i × i, two quarter turns, is a half turn, which is −1; and (−1) × (−1) = 1 because two half turns make a whole turn. On the grid the rule is concrete: multiplying an arrow z by a + bi means laying a copies of z nose to tail and then b copies of z turned a quarter left (negative counts point backwards), so (2 + i) × (2 − i) is two copies of 2 + i and one backwards copy of its turned version, landing exactly on 5, and (2 + i) × (2 + i) lands on 3 + 4i, the 3-4-5 right triangle. The grid points are the Gaussian integers. The squared length of the arrow to (a, b) is a² + b², and squared lengths multiply exactly (the Brahmagupta–Fibonacci identity), which is why multiplying arrows connects to sums of two squares (Week 158 draft). The units, the arrows of length 1, are 1, i, −1, −i: the four quarter turns. Gaussian integers factor uniquely into Gaussian primes up to those units (proved, as in ordinary whole numbers), and the ordinary primes behave in three ways: 2 = (1 + i)(1 − i); primes leaving 1 on division by 4 split, as 5 = (2 + i)(2 − i), 13 = (3 + 2i)(3 − 2i) and 17 = (4 + i)(4 − i); primes leaving 3 stay prime, so no grid arrow has squared length 3 or 7. All of this is proved; the concept of complex numbers is the destination, not a claim about children's algebra. Children can discover the quarter-turn rule, that two quarter turns make a reversal, the nose-to-tail product on a grid, and that 5 is a product of two tilted arrows while 3 is not.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Complex numbers](https://www.math.brown.edu/reschwar/M10/complex.pdf) — course notes on math.brown.edu (the PDF does not name its author). When two complex numbers are multiplied "their norms multiply and their 'angles' add"; i at angle π/2; (−1)(−1) = 1 via powers of an eighth-turn number (read November 4, 2026).
- [Gaussian Primes](https://thatsmaths.com/2022/01/27/gaussian-primes/) — ThatsMaths blog, January 2022. Gaussian integers as a lattice with units 1, −1, i, −i; 2 as a unit times (1 − i)²; 5 = (2 + i)(2 − i), 13 = (3 + 2i)(3 − 2i), 17 = (4 + i)(4 − i); primes of the form 4k + 3 stay Gaussian primes; the link to Fermat's two-squares theorem (read November 4, 2026).
- [Gaussian Integers: Square Dance](https://mathcircle.berkeley.edu/sites/default/files/handouts/2023/Square%20Dance%20--%20Gaussian%20Integers.pdf) — "Circle in a Box, Chapter 13", hosted by the Berkeley Math Circle (author and level not stated). Norms, units, factoring 29 and 1 + 3i, and the proof that primes 1 mod 4 are sums of two squares; algebraic, with no rotation picture (read November 4, 2026).
- [A Missing Piece: Early Elementary Plane Rotations](https://www.math.utah.edu/~palais/AMissingPiece/index.html) — Bob Palais, web supplement to a Notices of the AMS Doceamus column, February 2014. Only the title and venue could be confirmed from this page; the argument that rotations belong early in school is known to me only through a secondary blog summary and is not relied on here (read November 4, 2026).
- Prior use with children: none found at K–5. I searched for complex numbers as rotations in math circle and elementary materials. The nearest are NRICH [Complex Rotations](https://nrich.maths.org/node/62908) (ages 16–18: multiply points by −1 and by i and describe the effect) and high-school circle handouts on Gaussian integers such as the one above (read November 4, 2026).

## A kid-friendly way in

Arrow cards on a big grid. Each table has a laminated grid mat with a marked centre and a set of straight arrows cut from card at lengths 1, √2 (one diagonal step), √5 (two-and-one) and 2, all starting at the centre. Moves: "turn" means a quarter turn to the left; "times 2" means two arrows nose to tail; "times i" means one turned arrow. The whole-room version is a floor grid in tape where a child is the arrow, facing out from the centre. Prep: one printed grid mat per table, arrow cards cut from a printed sheet, masking tape for one floor grid; about 25 minutes. Launch (2–3 minutes): a child stands on the floor centre facing the "1" wall; the room says "times i" and they make a quarter turn left; "times i" again and they face backwards: the room names this "minus 1"; two more and they face front again.

## By band

- **K–1:** the floor and mat games: quarter turns, half turns, "times 2" by stepping twice; how many quarter turns make a half turn, a whole turn; does "turn around" twice bring you back? No reading beyond the move cards' pictures.
- **2–3:** the arrow 1 + i on the mat; multiply by 1 + i again and again (arrow plus its turned copy, nose to tail) and draw the spiral 1, 1 + i, 2i, −2 + 2i, −4, …, 16; where does it come back to the "1" line, and how long is it then?
- **4–5:** multiply grid arrows with the nose-to-tail rule; find (2 + i) × (2 − i) and (2 + i) × (2 + i); measure lengths with a ruler and compare with the product; which whole numbers on the "1" line are products of two tilted arrows (5, 13, 17 yes; 3, 7 no), linking to the two-squares chart.

## Checked facts

Computed in `check_number_symmetry_2.py`, `check_week_163()`:

- i² = −1, i⁴ = 1, (−1)(−1) = 1; times i sends grid point (a, b) to (−b, a); times (1 + i) sends (a, b) to (a − b, a + b);
- the nose-to-tail rule agrees with complex multiplication on a grid of examples; (2 + i)(2 − i) = 5, (2 + i)² = 3 + 4i with length 5, (1 + i)(1 − i) = 2, (1 + i)² = 2i, (3 + 2i)(3 − 2i) = 13, (4 + i)(4 − i) = 17, (1 + 2i)(2 + i) = 5i, (2 + i)(3 + i) = 5 + 5i;
- powers of 1 + i: 1, 1 + i, 2i, −2 + 2i, −4, −4 − 4i, −8i, 8 − 8i, 16;
- squared lengths multiply exactly for all grid arrows with coordinates −4 to 4, and angles add (floating point, three examples);
- squared lengths of grid arrows up to 25 are 1, 2, 4, 5, 8, 9, 10, 13, 16, 17, 18, 20, 25 (never 3 or 7); 8 arrows have squared length 5 and 4 have length 1.

## Nearest existing themes

Atlas GA-04 (steer a root arrow whose doubled angle points at a target) and GA-06 (complex branches) use complex numbers, but no week does, so this would be the first week for the concept complex-numbers. Week 4 (stars and wheels) and Week 116 draft (kaleidoscopes) are about turns as symmetries; here turns become numbers that multiply. Week 3 and Week 117 draft compose moves; here composing turns adds angles. Week 158 draft (two squares) is the companion: squared lengths of grid arrows are exactly its buildable totals.

## App connection

Patterns and symmetry region (or Numbers), an "arrow machine" family: a grid with an arrow from the centre and move buttons (turn, stretch, add a copy); puzzles: "reach the point 5 on the 1-line using only arrows of length √5", "how many times do you multiply by 1 + i to land on the 1-line again?" (4, at −4; 8 to return to the positive side at 16), "make an arrow of squared length 13".

## Open questions

- Whether the nose-to-tail rule is readable by grades 4–5 without algebra; the mat may need a worked example on a non-target arrow before Problem 1. Untested.
- Negative counts ("one backwards copy") may be a larger hurdle than the turning; a reviewer should decide whether 2–3 use only positive counts.
- The K–1 entry is turning games rather than multiplication; is that enough substance, or should K–1 join the 2–3 spiral with adult recording?
