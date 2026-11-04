# Week 206 (draft plan): Folding the square root of two

**Strand:** number, with analysis (app region "Numbers"). **Deep-math field:** irrationality, infinite descent, best rational approximations (Pell's equation). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

No fraction a/b squares to exactly 2; equivalently, two equal squares of whole-number side never make one whole-number square (2b² = a² has no solution in positive integers). Stanley Tennenbaum's picture proof (early 1950s, first printed in John H. Conway's essay in the collection Power): if two b-by-b squares had the same area as one a-by-a square, place both small squares in opposite corners of the big one; the doubly covered middle square (side 2b − a) must equal the two uncovered corner squares (side a − b) in area, giving a smaller pair of the same kind, and so on forever, which whole numbers cannot do. The folding version (credited by Fermat's Library to Conway and Guy): if a square of side 12 had a diagonal of exactly 17, folding one side onto the diagonal makes a smaller isosceles right triangle with legs 5 and hypotenuse 7, so √2 would be 7/5, then 3/2, then 1/1, which is false. Both arguments use the same step (a, b) → (2b − a, a − b), and it keeps a² − 2b² the same size with the opposite sign. Run backwards it is Theon of Smyrna's ladder (about 100 CE): side and diagonal numbers (s, d) → (s + d, 2s + d) give (1, 1), (2, 3), (5, 7), (12, 17), (29, 41), (70, 99), with d² − 2s² alternating −1 and +1, so these near-misses are the best approximations 3/2, 7/5, 17/12, 41/29, 99/70, off from √2 by exactly 1/(s(d + s√2)). In square-cutting form (Week 32's move): cutting the biggest possible squares from a 1-by-√2 rectangle removes 1 square, then 2, then 2, then 2, forever, because the leftover after each "2" round has the same shape again (its sides shrink by √2 − 1 ≈ 0.414 each round), while any rectangle with whole-number sides must stop. Real A4 paper (297 by 210 mm) gives 1, 2, 2, 2, 2, 2 and stops at a 3 mm square, because 297/210 is a fraction close to √2; US letter (11 by 8.5 inches) gives 1, 3, … and so is visibly a different shape. Halving a 1 : √2 sheet keeps its shape, which is why A-series paper uses it (A0 is one square metre; Germany adopted the series as DIN 476 in 1922). Proved: irrationality of √2, the identities above, and that the continued fraction of √2 is 1, 2, 2, 2, …. Children can discover that 25 + 25 tiles miss 49 by one and 144 + 144 miss 289 by one but never hit, that A-paper cut into squares keeps giving "two again", and in grades 4–5 why the overlap picture forbids an exact answer.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Irrationality from The Book](https://ar5iv.labs.arxiv.org/html/0909.4913). Steven J. Miller and David Montague, arXiv 0909.4913 (2009). Tennenbaum's proof with the overlapping squares, (2b − a)² = 2(a − b)², its discovery in the early 1950s and first printing in Conway's article in Power (read November 4, 2026).
- [The Root of the Matter: Approximating Roots with the Greeks](https://old.maa.org/press/periodicals/convergence/the-root-of-the-matter-approximating-roots-with-the-greeks-method-motivation-and-verification). Matthew Haines and Jody Sorensen, MAA Convergence, June 2018. Theon of Smyrna (about 100 CE), the side and diagonal rule, the pairs up to (169, 239) and 2x² − y² = ±1 with alternating sign (read November 4, 2026).
- [Irrationality of √2, a geometric proof (annotated)](https://fermatslibrary.com/s/irrationality-of-the-square-root-of-2-a-geometric-proof). Fermat's Library annotated paper, with a biography of Tom M. Apostol. The descent by smaller isosceles right triangles and the folding version credited to Conway and Guy: a 12-inch square with a 17-inch diagonal folds to legs 5 and hypotenuse 7 (read November 4, 2026).
- [International standard paper sizes](https://www.cl.cam.ac.uk/~mgk25/iso-paper.html). Markus Kuhn, University of Cambridge. Ratio √2 so halving keeps the shape; A0 one square metre; A4 210 by 297 mm; Lichtenberg's letter of 1786; DIN 476 in 1922; US letter does not keep its shape (read November 4, 2026).
- Prior use with children: [Math Activity](https://pi.anandology.com/math-activity/print.html). Anand Chitipothu, origami course at Center for Learning, January to March 2025 (ages not stated): students compare A4 and A5 sheets, ask what makes similar halves possible, and meet "square-root-of-two" through folding (read November 4, 2026). No K–5 handout on proving irrationality was found.

## A kid-friendly way in

Materials per table: about 300 square tiles or cubes (for 2–3), A4 paper if available, otherwise US letter trimmed to 7.78 by 11 inches (11/√2 is about 7.78), plain letter paper for comparison, scissors, 15 cm origami squares, a printed overlap card (a big square with two smaller squares drawn in opposite corners). Prep: trim paper, print cards, about 20 minutes. Launch (3 minutes): fold the short edge of an A-sheet onto its long edge, cut off the square, and hold up the leftover strip; fold and cut the biggest squares from the strip, and the group counts "two". Ask: what will the next strip give?

Suggested hour: 0–5 launch; 5–25 square-cutting race on A-paper and letter paper (all bands); 25–45 band questions; 45–60 Tennenbaum's overlap picture for 4–5, tiles for 2–3, and Theon's ladder.

## By band

- **K–1:** Cut the biggest squares from an A-sheet and then from a letter sheet, counting squares each round and laying them out in rows by round. Do the two papers give the same counts? Fold an A-sheet in half: is the half the same shape (lay it on the whole, corner to corner along the diagonal)?
- **2–3:** With tiles, build two equal squares and try to rebuild all their tiles as one square. Which pairs come closest (2 + 2 vs 3 × 3; 5 + 5 vs 7 × 7)? Find the next near-miss.
- **4–5:** Prove that two equal tile squares never make one square, using the overlap card (the middle overlap must equal the two empty corners). Then fold the 12-and-17 square and explain where 5 and 7 come from. Use Theon's ladder to predict the next near-miss and check its error.

## Checked facts

- `check_week_206()`: Theon's pairs (1, 1), (2, 3), (5, 7), (12, 17), (29, 41), (70, 99), (169, 239), with d² − 2s² = −1, +1, −1, …; the error formula 1/(s(d + s√2)) holds for each; 17/12, 41/29 and 99/70 are off by about 0.0025, 0.0004 and 0.00007.
- `check_week_206()`: 2b² is never a square for b up to 20,000; 2·5² = 7² + 1, 2·12² = 17² − 1, 2·2² = 3² − 1, 2·29² = 41² + 1.
- `check_week_206()`: the overlap step (a, b) → (2b − a, a − b) flips the sign of a² − 2b² and shrinks b, for every b < 300 and b < a < 2b; it takes (17, 12) to (7, 5), (3, 2), (1, 1), (1, 0), and it is exactly Theon's rule reversed.
- `check_week_206()`: biggest squares from A4 (297 by 210): 1, 2, 2, 2, 2, 2, leftover strips 87, 36, 15, 6, 3 mm, ending with a 3 mm square; US letter (22 by 17 half-inches): 1, 3, 2, 2; a 60-digit approximation of √2 gives 1 followed by 29 twos; each round shrinks by √2 − 1 ≈ 0.414.
- `check_week_206()`: 297/210 ≈ 1.41429, 11/8.5 ≈ 1.294, and 11/√2 ≈ 7.78 inches for trimming letter paper.

## Nearest existing themes

There is real overlap to name. Week 93 (Squaring a rectangle) produces 3/2, 17/12, 577/408 by averaging, and atlas AD-10 (triangular squares) uses x² − 2y² = 1 and multiplication by 3 + 2√2; AD-12 constructs √2 with compass, GA-11 notes that √2 cannot be built from 1 by adding and splitting, and Week 50 does the "√2 = 2" staircase paradox. Draft 170 (rep-tiles) already folds A4 and letter paper to show the 1 : √2 rectangle is rep-2, and draft 126 makes a √2 square by dissection. What is new here is the proof of irrationality itself, which no week or draft gives: Tennenbaum's overlap, the fold descent, and the never-ending square-cutting count. The square-cutting task is a return visit to Week 32 (Squares inside rectangles: Euclid's algorithm), turned from "it always stops" to "here it never stops", and that is the strongest distinct angle. Keep A-paper's halving property (draft 170's point) to a one-minute aside.

## App connection

Region "Numbers", possible home in the existing "Squares in Tile gardens" family (Week 32): the child cuts the biggest square from a rectangle again and again, and a counter row records 1, 2, 2, …. Puzzle 1: "Which of these sheets never stops?" (an exact 1 : √2 sheet drawn by the app against 297 by 210). Puzzle 2: "Build two equal tile squares that come within one tile of a square" (5 and 7, 12 and 17). A Tennenbaum level slides two squares into a big one and shows the overlap and the corners.

## Open questions

- Material fit: A4 may not be on hand in Bellingham; trimmed letter paper must be cut accurately (1 mm matters by the fourth round). Rehearse how many rounds children can cut before strips are too thin.
- Is the overlap proof accessible to 4–5 without algebra, using only "the overlap area equals the two empty corners" with tiles?
- The fold with a 12-inch square is an imagined object (it cannot have a 17-inch diagonal); check whether children follow a proof about an impossible square.
- Decide whether to merge the A-paper material with draft 170 or keep it here.
