# Week 155 (draft plan): Weird dice

**Strand:** counting and number (Counting and arranging; Numbers). **Deep-math field:** generating functions, factoring polynomials (cyclotomic polynomials). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Two ordinary dice give the sums 2 to 12 in 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1 of the 36 equally likely rolls. The Sicherman dice, one labelled 1, 2, 2, 3, 3, 4 and the other 1, 3, 4, 5, 6, 8, give exactly the same counts, and they are the only other pair of six-sided dice with positive whole-number faces that do (Sicherman found them in 1977; Gardner published them in February 1978; Gallian and Rusin, 1979, proved uniqueness in a general theory). The proof turns a die into a polynomial: a die with faces a, b, ... becomes x^a + x^b + ..., and multiplying two such polynomials adds exponents, so the product lists every sum with its count. The ordinary die is x + x² + ... + x⁶ = x(1 + x)(1 + x + x²)(1 − x + x²), and these factors cannot be split further with whole-number coefficients. Any pair of dice with the ordinary sums must share out the two copies of each factor between the two dice; each die needs exactly one x (no face 0, and each die's smallest face is 1), and putting 1 into each polynomial must give 6 faces, which forces one (1 + x) and one (1 + x + x²) into each die (they are worth 2 and 3 at x = 1, while 1 − x + x² is worth 1); the only freedom is where the two copies of 1 − x + x² go, and the choices give the ordinary pair and x(1 + x)(1 + x + x²) with x(1 + x)(1 + x + x²)(1 − x + x²)², which are exactly the Sicherman dice. The same reasoning shows that four-sided dice have one other pair (1, 2, 2, 3 and 1, 3, 3, 5) and three-sided dice none. Allowing a face 0 only shifts numbers between the dice (0, 1, 1, 2, 2, 3 with 2, 4, 5, 6, 7, 9). The proof is complete; the general theory for n-sided dice is in Gallian and Rusin. Children can discover that the sum table cannot tell the dice apart, that doubles can (4 of 36 rolls instead of 6), and in grades 4–5 that a sum table is a multiplication of "face lists".

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Cyclotomic Polynomials and Nonstandard Dice](https://www.cs.umd.edu/~gasarch/BLOGPAPERS/nonstandarddice.pdf) — Joseph A. Gallian and David J. Rusin, Discrete Mathematics 27 (1979), 245–259. Sicherman's pair and "exactly one more pair", the factorisation x(1 + x)(1 + x + x²)(1 − x + x²), general results for dice of other sizes (read November 4, 2026).
- [Sicherman Dice](https://sicherman.net/sdice.html) — George Sicherman's own page. The January 27, 1977 letter to Martin Gardner, the February 1978 Mathematical Games column, and a uniqueness statement for sets of dice (read November 4, 2026).
- Prior use with children: [Sicherman Dice](https://mathematicscentre.com/taskcentre/241sichr.htm) — Mathematics Centre task 241, Years 4 to 10: pairs build the addition table for standard and special dice and compare frequency tables; a teacher's report of use with Year 6 and 7 classes; extensions to four-sided dice and to zero and negative faces (read November 4, 2026).

## A kid-friendly way in

Blank wooden or foam cubes and a marker (or round stickers over ordinary dice) to make one ordinary pair and one Sicherman pair per table, plus a 6-by-6 addition grid to fill. Prep: label or sticker four dice per table for six tables, print grids; about 20 minutes. Launch (2–3 minutes): show the strange dice, roll them a few times, and ask "would you rather play a board game with these or with ordinary dice?"; record the votes and the reasons.

## By band

- **K–1:** roll the weird pair and move a counter up a 2-to-12 race track (one counter per sum); then the same race with ordinary dice. Which sums win?
- **2–3:** fill the 6-by-6 addition table for both pairs and count each sum; then design dice: change the faces on one die and find what the other must be so the totals still match (with blank cubes and a table, not formulas).
- **4–5:** find another pair for four-sided dice; then meet the face-list multiplication, (x + x²)(x + x²) style, as a short-hand for the addition table, factor the ordinary die's list and recombine the pieces.

## Checked facts

Computed in `check_networks_counting_2.py`, `check_week_155()`:

- sum counts 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1 out of 36 for both pairs;
- exhaustive search: the only pairs of positive six-sided dice with these counts are ordinary and Sicherman; four-sided: ordinary and (1, 2, 2, 3) with (1, 3, 3, 5); three-sided: only ordinary;
- x + ... + x⁶ = x(1 + x)(1 + x + x²)(1 − x + x²); the Sicherman polynomials are x(1 + x)(1 + x + x²) and x(1 + x)(1 + x + x²)(1 − x + x²)²;
- 0, 1, 1, 2, 2, 3 with 2, 4, 5, 6, 7, 9 also matches; faces total 15 and 27 against 21 and 21; doubles 4 of 36 against 6;
- an ordinary die with 0, 0, 0, 6, 6, 6 makes every total 1 to 12 equally likely (3 of 36 each).

Cited, not computed: that the four factors cannot be split further (standard facts about cyclotomic polynomials).

## Nearest existing themes

Week 24 (three random decks) compares two decks by who wins, and its nontransitive cycle is about pairs beating each other; here two different pairs are indistinguishable by sums. Week 55 (few sums) studies the addition table of two sets and how many different totals appear; this week keeps the counts, not only the set of totals. Week 42 and Week 131 use dice for fairness and waiting times. New here: generating polynomials, the concept "polynomials" (unused in the catalog), and a uniqueness proof by factoring.

## App connection

Numbers, or Counting and arranging: a "dice workshop" where the child edits the faces of two dice and the app draws the sum histogram beside the ordinary one; puzzles ask to match the ordinary histogram with a 4 on neither die, to make every total from 1 to 12 equally likely when a face may be 0 (ordinary die with 0, 0, 0, 6, 6, 6), or to find the four-sided pair.

## Open questions

- Whether 2–3 can search for the other die systematically without formulas; a "subtract the table" method on movable cards might work and should be tried at home first.
- Whether the factoring step is too abstract for grades 4–5 without algebra; a version with "number strips" multiplied as long multiplication without carrying might bridge it.
- Which game best shows the doubles difference (Monopoly-like "roll again on doubles").
