# Week 101 (draft plan): Bead machines and the odd triangle

**Strand:** counting (Counting and arranging), with a chance station (Chance and machines). **Deep-math field:** combinatorics, elementary number theory (binomial coefficients modulo a prime), probability. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A bead falling through n rows of pegs makes n left/right choices, so its path is a word of n letters and the bin it lands in is the number of R's. The number of paths to bin k is the binomial coefficient C(n, k), the 2^n paths are equally likely when every peg is fair, and bin k receives a share C(n, k)/2^n (proved; a bijection between paths and words). The middle bins win but each one shrinks as rows are added (6/16, 20/64, 70/256, 252/1024 for 4, 6, 8, 10 rows), and the outer bins become rare (2 in 1024 on ten rows): the bell outline is the de Moivre–Laplace theorem, the binomial case of the central limit theorem, which is a limit statement and is only seen approximately on a real board. The second destination is parity. Colour the odd entries of Pascal's triangle and the Sierpiński triangle appears. Lucas's theorem (1878) says that modulo a prime p, C(n, k) is the product of the binomial coefficients of the base-p digits of n and k; for p = 2 this means C(n, k) is odd exactly when every binary 1 of k sits under a 1 of n (equivalently, by Kummer, adding k and n − k in binary has no carries). Consequences children can find and older children can explain: row n has 2^b odd entries, where b is the number of 1s in binary n (1, 2, 2, 4, 2, 4, 4, 8, … for rows 0 to 7, attributed to Glaisher); rows 1, 3, 7, 15 are entirely odd and rows 2, 4, 8, 16 have only their end 1s odd; the first 2^k rows hold exactly 3^k odd entries (27 of 36 in eight rows, 81 of 136 in sixteen), because that block is three copies of the block of half the size. So the odd share tends to 0 even though the picture looks full. A drawing-only route exists: since each entry is the sum of the two above, parity follows the rule "same above gives even, different above gives odd", so the pattern can be built with two colours and no numbers. Modulo 3 the analogous count of entries not divisible by 3 is the product of (digit + 1) over the base-3 digits of n (checked here for n < 81; it follows from Lucas). All of this is proved; the observed bead counts on a real board are experiments.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Odd Numbers in Pascal's Triangle](https://math.hmc.edu/funfacts/?p=515) — Francis E. Su et al., Harvey Mudd Math Fun Facts (fact suggested by Arthur Benjamin). Row n has 2^(number of 1s in binary n) odd entries, with the mod-2 binomial proof (read November 3, 2026).
- [Arithmetic Properties of Binomial Coefficients, section on Lucas's theorem](https://www.cecm.sfu.ca/organics/papers/granville/paper/binomial/html/node2.html) — Andrew Granville (name taken from the page's address; no date on the page). Lucas's 1878 digit rule modulo a prime, Glaisher's power-of-2 count, and the no-carries test via Kummer (read November 3, 2026).
- [What's odd about Pascal's triangle?](https://chalkdustmagazine.com/features/whats-odd-about-pascals-triangle/) — Graeme Foster, Chalkdust, December 2023. Colouring the even entries gives Sierpiński-like holes; the even share passes 93% by about 4,000 rows (read November 3, 2026).
- [How Randomness Can Arise From Determinism](https://www.quantamagazine.org/how-randomness-can-arise-from-determinism-20191014/) — Pradeep Mutalik, Quanta Magazine Insights puzzle, October 14, 2019. Galton board and Pascal's triangle; puzzles that re-weight a few pegs so the bins come out equal or twin-peaked (read November 3, 2026).
- Prior use with children: [Investigating Pascal's Triangle](https://nrich.maths.org/problems/investigating-pascals-triangle) — NRICH, ages 7 to 11; pattern-hunting in the triangle via digital roots, not parity (read November 3, 2026). Year 1 of this circle already ran a four-level coin-flip ball machine with tallies and path words (Handout 5, Problems 5.3–5.4), grid walks (5.6) and filled in Pascal's triangle (Handout 8, Problems 8.3–8.4), in `lowell-math-circle-year-1/lowell-math-circle/Math Circle Fall 2025/`. A search of NRICH, JRMF and the Berkeley Math Circle for a children's parity-colouring task found none.

## A kid-friendly way in

The parity triangle built by a colour rule, with no numbers. A printed triangle of hexagon cells, 16 rows, whose two edges are pre-coloured red. Rule: look at the two cells above; if they are the same colour, leave the new cell white; if they differ, colour it red. Children fill rows with red and white counters (or crayons) and watch triangles inside triangles appear. A bead station runs alongside for the chance strand: a printed four-row peg board, a coin per child (heads left, tails right), and a stacking column of cubes under each bin. Prep: print triangles and boards, count out counters and cubes; about 15 minutes. Launch (2–3 minutes): fill the first four rows of the colour triangle together on the board, asking the class which colour each new cell gets, then send one bead down the peg board with three coin flips.

## By band

- **K–1:** the colour rule on rows 1 to 8, then "what do you see?" (white upside-down triangles of growing size). At the bead station, drop beads by coin flips and stack a cube in the bin; compare the stacks.
- **2–3:** fill all 16 rows; count red cells in each row and look for a rule in 1, 2, 2, 4, 2, 4, 4, 8, …; which rows are all red, which have only two? At the bead board, the class pools 32 beads and compares with 2, 8, 12, 8, 2; count the paths to each bin to see why.
- **4–5:** fill a numbered Pascal triangle to row 15, circle the odd entries and check them against the colour triangle; explain why the colour rule matches odd and even; explain the 3^k total (the 8-row block is three copies of the 4-row block); predict the odd count of row 13 from binary 1101 and check it. Extension: the Quanta-style rigged pegs, making three equal bins on a two-row board (one peg sending two thirds left, one fair peg, one peg that always goes right).

## Checked facts

Computed in `check_counting_networks.py`, `check_week_101()`:

- bin counts C(n, k) for n ≤ 10 by listing all words; the year-1 machine's 1, 3, 3, 1; 32 beads on four rows expect 2, 8, 12, 8, 2;
- middle-bin shares 3/8, 5/16, 35/128, 63/256 (0.246) for 4, 6, 8, 10 rows; each outer bin 1/1024 on ten rows;
- odd entries per row equal 2^(binary 1s) for rows 0 to 63, with the list for rows 0 to 15; Lucas's mod-2 test for all n < 64; full rows 2^m − 1 and two-odd rows 2^m;
- 3^k odd entries in the first 2^k rows (k ≤ 6), 27 of 36 and 81 of 136, and the falling odd share;
- the base-3 digit product for entries not divisible by 3, n < 81;
- the two-row rigged board giving 1/3, 1/3, 1/3.

Cited, not computed: Lucas's theorem in general, the de Moivre–Laplace limit.

## Nearest existing themes

Year 1 Handouts 5 and 8 already did the coin-flip machine, path words and Pascal recursion, so a bead-machine week on its own would substantially repeat them; the plan therefore leads with parity and keeps the beads as a short station whose new content is pooling many beads and comparing shapes. Week 42 (fair results from a bag) and Week 44 (the bag that copies) are chance machines with different laws; AP-03 uses equally likely assignments as a reference distribution. Week 76 (substitution strips) builds the Thue–Morse word from binary parity, a cousin of the odd-count rule. New here: Lucas's digit test, a fractal produced by a local rule, and the 3^k count, which reappears as the 3^n states of the Tower of Hanoi (Week 103 draft).

## App connection

Counting and arranging: a "colour rule triangle" family where the child fills cells by the same/different rule and puzzles ask for a missing row, a cell's colour far down, or a row with exactly 8 red cells. Chance and machines: a "bead machine" family where the child sets pegs (fair, always-left, always-right, two-thirds) to hit a target bin pattern, as in Mutalik's puzzles.

## Open questions

- Whether K–1 children apply the same/different rule reliably over eight rows, or need a two-cell "look window" card.
- Whether 32 coin-flip beads per table are enough to look like the prediction; pooling across tables may be needed.
- Whether the bead station adds enough beyond Year 1 to keep, or should become a return visit only for children who missed Year 1.
