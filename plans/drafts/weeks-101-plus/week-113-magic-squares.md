# Week 113 (draft plan): One magic square

**Strand:** number and symmetry (Numbers; Patterns and symmetry). **Deep-math field:** combinatorics, symmetry groups. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A normal magic square of order n holds 1, 2, …, n² so that every row, column and both diagonals add to the same total, which must be n(n² + 1)/2 (all numbers add to n²(n² + 1)/2, shared over n rows): 15, 34 and 65 for n = 3, 4, 5. Theorem (classical; a full proof fits in a page): for n = 3 there is exactly one magic square up to the 8 symmetries of the square (4 turns and 4 flips), the Lo Shu, 4 9 2 / 3 5 7 / 8 1 6; counted with its turns and flips it gives 8 squares. The object proof children can follow uses the eight triples from 1 to 9 that add to 15. In a magic square each of the 8 lines is such a triple, and there are exactly 8 triples, so every triple is a line. The centre lies on 4 lines and only 5 is in 4 triples, so 5 is the centre; each corner lies on 3 lines and only 2, 4, 6, 8 are in 3 triples, so the evens are the corners; the odds 1, 3, 7, 9 (each in 2 triples) fill the edges. Choosing where 2 goes (4 corners) and which neighbouring corner gets 4 (2 choices) fixes everything, which is the 8 symmetries. A by-product: the game "Pick 15" (players take number cards 1 to 9 in turn; the first to hold three cards adding to 15 wins) is tic-tac-toe played on the Lo Shu, since its winning triples are exactly the square's lines. For n = 4 there are 880 magic squares up to symmetry, 7040 in all, first enumerated by Frénicle de Bessy in 1693; Dürer's 1514 engraving Melencolia I shows one whose bottom row holds the year as 15 14. Larger counts are only known exactly for small n; for n = 3 everything is proved and checked here.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Squaring the magic squares of order 4](https://arxiv.org/pdf/1302.1163) — Barbero, Cerruti and Murru, arXiv 1302.1163, 2013. "There are exactly 880 normal magic squares of order 4" up to the square's symmetries, 7040 in total, enumerated by Frénicle in 1693 (read November 3, 2026).
- [Solving Magic Squares](https://mathpages.com/home/kmath295.htm) — MathPages. An algebraic proof that the order-3 square is unique up to rotation and reflection, with 5 at the centre; order 4 count 7040 (read November 3, 2026).
- [Magic squares course notes](https://www.math.stonybrook.edu/~moira/courses/mat336-sp2020/Material/MagicSquares.pdf) — Stony Brook MAT 336 materials (no author printed). Dürer's Melencolia I (1514) and a Lo Shu image from a 13th-century source (read November 3, 2026).
- Prior use with children: [NRICH "Magic Squares"](https://nrich.maths.org/969) — ages 5 to 7. Place 1 to 9 so rows, columns and diagonals share a total; find several and say what they have in common (read November 3, 2026).

## A kid-friendly way in

Number tiles 1 to 9 on a 3 by 3 mat with a line-checker card (a strip with three windows that slides along each row, column and diagonal). Children try to make every line add to the same total. Then the Pick-15 card game in pairs, and only afterwards the reveal that it is tic-tac-toe in disguise. Prep: print and cut tile sets and mats, one per pair; 9 number cards per pair; about 20 minutes. Launch (2–3 minutes): place 1 to 9 in order on a big mat (1 2 3 / 4 5 6 / 7 8 9), add one row and one diagonal together aloud (6 and 15), and say the goal is to make all 8 lines match.

## By band

- **K–1:** rows-only version first: split 1 to 9 into three rows that each add to 15, using tiles and counting on; then try adding columns. Pick 15 with the cards and a counting line.
- **2–3:** find a full magic square; then find a different one and decide whether it is "really" different (turn or flip the mat); list all triples that add to 15 on cards.
- **4–5:** prove there is only one up to turning and flipping, using the triple cards (which number is in 4 triples, which in 3); explain why Pick 15 is tic-tac-toe; check Dürer's square and find its other groups of four that add to 34.

## Checked facts

Computed in `check_number.py`, `check_week_113()`:

- magic totals 15, 34, 65 for n = 3, 4, 5;
- searching all 362880 placements of 1 to 9 finds exactly 8 magic squares, all with 5 in the centre, and they are exactly the 8 turns and flips of the Lo Shu;
- exactly 8 triples from 1 to 9 add to 15; 5 is in 4, each even number in 3, each odd number other than 5 in 2; these triples are exactly the Lo Shu's 8 lines;
- the rows-only puzzle has 2592 solutions (so the K–1 warm-up has many answers);
- the grid's 8 lines are 8 of the 12 lines of the plane mod 3 (link to Week 36);
- Dürer's square 16 3 2 13 / 5 10 11 8 / 9 6 7 12 / 4 15 14 1 uses 1 to 16, is magic with total 34, has 15 14 in its bottom row, and its four corners and its centre four also add to 34.

Cited, not computed: 880 and 7040 for order 4, Frénicle's 1693 date.

## Nearest existing themes

Week 36 (making threes) uses nine tiles as the plane over the integers mod 3 with 12 lines; with grid positions read as coordinates mod 3, the 8 rows, columns and diagonals of a 3 by 3 grid are 8 of those 12 lines, and the guide should name this link. Week 37 (mirror twins) counts labellings up to rotations. NRICH and many classrooms use 3 by 3 magic squares as arithmetic practice; new here is the uniqueness proof by counting triples, the symmetry count of 8, and the Pick-15 isomorphism. The risk of duplicating ordinary school practice is real, so the guide should keep the "how many are there, really?" question central.

## App connection

Patterns and symmetry region: a "magic mat" family where the child drags tiles and the board lights lines that hit the target; puzzles: "complete this square from three given tiles" or "is this square a turned copy of that one?" A Pick-15 opponent in Games and choices could reveal the tic-tac-toe board after a win.

## Open questions

- Arithmetic load: adding three numbers repeatedly may dominate for K–1; the line-checker card and a number line may help. Untested.
- Whether Pick 15 is better as the launch hook (play first, discover the square later).
- How far to take 4 by 4 squares; 880 is cited, and a child-checkable sub-question (Dürer's extra groups of 34) may be enough.
