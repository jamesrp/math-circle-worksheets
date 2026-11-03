# Week 102 (draft plan): Domino diamonds

**Strand:** counting (Counting and arranging). **Deep-math field:** enumerative combinatorics, perfect matchings, statistical mechanics of tilings. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The Aztec diamond of order n is the staircase-shaped region of unit squares whose centres satisfy |x| + |y| ≤ n; it has 2n(n + 1) squares (4, 12, 24, 40 for n = 1 to 4). Elkies, Kuperberg, Larsen and Propp (1992) proved that it has exactly 2^(n(n+1)/2) domino tilings: 2, 8, 64, 1024, so each order multiplies the count by 2^n (by 4, then 8, then 16). Their paper gives several proofs (via alternating-sign matrices and monotone triangles) and shows that any tiling can be reached from any other by local moves; the local move is the flip, which turns two parallel dominoes filling a 2-by-2 block through a quarter turn. Checked here by listing every tiling for n ≤ 4: flips connect all tilings; each tiling has between n and n(n + 1)/2 available flips; the farthest-apart tilings for n = 1, 2, 3 are 1, 5 and 14 flips apart (1, 1 + 4, 1 + 4 + 9), and for n = 4 one tiling already has another 30 flips away. Sorting tilings by how the top two squares are covered splits order 2 into 6 + 2, order 3 into 56 + 8 and order 4 into 960 + 64, and the "two standing dominoes" pile always has the previous order's count; that is an observation on small cases here, not a proof. The second theorem is about shape, not number. Jockusch, Propp and Shor (1998) proved that for large n almost every tiling (chosen uniformly at random) is frozen into brick-wall patterns in the four corners, and that the boundary of the disordered middle approaches the circle of radius n/√2 inscribed in the diamond: the arctic circle theorem. Children can discover the counts for small orders, the flip move, the fact that some tilings are stuck with few flips and others have many, and, from a printed large random tiling, that the corners are orderly and the middle is not. The proofs of the general count and of the circle are beyond the circle's reach and are cited.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Alternating-Sign Matrices and Domino Tilings (Part I)](https://emis.univie.ac.at/journals/JACO/Volume1_2/x9m7n00g384067u3.html) — Noam Elkies, Greg Kuperberg, Michael Larsen, James Propp, Journal of Algebraic Combinatorics 1 (1992), pp. 111–132. Abstract states the 2^(n(n+1)/2) count and its two proofs (read November 3, 2026).
- [Alternating sign matrices and domino tilings (arXiv math/9201305)](https://arxiv.org/abs/math/9201305) — same authors, arXiv version. Abstract adds that the paper shows how one tiling can be reached from another by local changes (read November 3, 2026).
- [Random Domino Tilings and the Arctic Circle Theorem](https://www.arxiv.org/abs/math/9801068) — William Jockusch, James Propp, Peter Shor, arXiv math/9801068, 1998. Frozen outer regions and the circle of radius n/√2 (read November 3, 2026).
- [Dominoes, Dimers and Determinants](https://users.monash.edu.au/~normd/documents/Dominoes-Monash-Talk.pdf) — Norm Do, Monash University seminar talk, August 28, 2012. A readable survey stating both theorems with pictures coloured by domino orientation (read November 3, 2026).
- Prior use with children: [Tiling problems: from dominoes, checkerboards and mazes to discrete geometry](https://mathcircle.berkeley.edu/sites/default/files/archivedocs/2011_2012/lectures/1112lecturespdf/BMC_Adv_Feb14_2012_Tiling.pdf) — Adrien Kassel, Berkeley Math Circle (advanced), February 14, 2012. Domino counting problems for strips and boards, mentions the arctic circle; older students, not K–5 (read November 3, 2026). No K–5 Aztec diamond activity was found on NRICH or JRMF; JRMF's Domino Dissection is a pip-matching logic puzzle, not a tiling count.

## A kid-friendly way in

Card or foam dominoes exactly two squares of a printed board (3 cm squares work), and printed Aztec diamonds of orders 1, 2 and 3 on a checkerboard background. Children tile, then find a different tiling, then learn the flip: two dominoes side by side in a 2-by-2 block may turn together. Prep: print boards, cut or count out 12 dominoes per pair (order 3 needs 12); about 20 minutes the first time, reusable. Launch (2–3 minutes): tile the order-1 diamond (a 2-by-2 square) both ways on the board, show the flip between them, then put up the order-2 outline and ask how many ways there might be.

## By band

- **K–1:** tile orders 1 and 2 with real dominoes; make a tiling no neighbour has; find a spot where a flip works and do it. Count found tilings with stickers on a class poster.
- **2–3:** find all 8 tilings of order 2 and prove the list complete by sorting on the top two squares (6 with one flat domino, 2 with two standing); in each tiling count the possible flips (between 2 and 3). Then, pooling across tables, sort order-3 tilings the same way and compare the "two standing" pile with the order-2 total.
- **4–5:** organise counts 2, 8, 64 and predict the next; explain the doubling pattern in exponents (1, 3, 6, 10: triangular numbers). Find two order-2 tilings five flips apart and argue no pair is farther. Look at a printed computer-made random tiling of a large diamond, coloured by orientation, and describe where it is orderly.

## Checked facts

Computed in `check_counting_networks.py`, `check_week_102()`:

- square counts 4, 12, 24, 40 and tiling counts 2, 8, 64, 1024 (all tilings listed), ratios 4, 8, 16;
- flips connect every tiling for n ≤ 4; flips available range from n to n(n + 1)/2; farthest pairs 1, 5, 14 flips for n ≤ 3, and 30 from one order-4 tiling;
- top-two-squares splits 6 + 2, 56 + 8, 960 + 64;
- contrasts: 2-by-n strips give 1, 2, 3, 5, 8, 13, 21 tilings and the 4-by-4 square 36; order 3 has 12 squares of each checkerboard colour.

Cited, not computed: the general 2^(n(n+1)/2) formula, the general flip connectivity, the arctic circle theorem.

## Nearest existing themes

Week 1 (tiling lab) and its encore tile with rhombi on a triangular grid, count the six tilings of a small hexagon and study flips; Week 14 flips polygon triangulations; Week 25's switches connect pictures with equal row and column counts. Year 1 counted strips filled with singles and doubles (Fibonacci), the same numbers as 2-by-n domino strips. The flip-connectivity idea therefore repeats Week 1's reasoning move on a new grid. New here: a count that grows by powers of 2 rather than the Fibonacci or hexagon numbers, sorting by a boundary piece to prove a list complete, and the arctic circle as a picture of a theorem about typical shapes.

## App connection

Counting and arranging: a "domino diamond" family on a square grid. The child drags dominoes, taps a 2-by-2 block to flip, and puzzles ask "reach this target tiling in the fewest flips", "find the tiling with the most flips available" or "how many tilings start with two standing dominoes on top?". Week 1's rhombus-tiling family could share the flip interaction.

## Open questions

- Whether a printed large random tiling is needed and who makes it; generating one needs a domino-shuffling script that is not yet written.
- Whether order 3 (12 dominoes, 64 tilings) is a fair pooled task for 2–3 or too much bookkeeping; the top-two-squares sort may need printed half-filled boards.
- Whether this is better as a Week 1 return visit than a new theme, given the shared flip idea.
