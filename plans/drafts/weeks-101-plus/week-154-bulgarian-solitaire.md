# Week 154 (draft plan): Bulgarian solitaire

**Strand:** counting (Counting and arranging). **Deep-math field:** partitions, discrete dynamical systems, potential (energy) arguments. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Split n cards into piles. One move takes one card from every pile and puts the taken cards together as a new pile (empty piles vanish). The state is a partition of n (pile sizes, order ignored), and since there are finitely many partitions, every start eventually repeats and so falls into a cycle. When n is triangular, n = 1 + 2 + ... + k, every start reaches the staircase k, k − 1, ..., 1, which the move leaves unchanged (Brandt, 1982; popularised by Gardner's 1983 Scientific American column); Knuth checked for k ≤ 5 that at most k(k − 1) moves are needed and conjectured it in general, and Igusa (1985) and Bentz (1987) proved it; the start (k − 1, k − 1, k − 2, ..., 2, 1, 1) needs exactly k(k − 1). For other n, write n = (k − 1)k/2 + r with 0 < r < k: every start ends in a cycle made of the staircase k − 1, ..., 1 with r extra cards sitting one per row on a staircase of k rows, and the move rotates those extras; the number of different cycles equals the number of necklaces of k beads, r black, up to rotation, and every cycle length divides k (Brandt; restated by Drensky). A proof children can follow uses the "lying-down" picture: draw piles as rows of a bar diagram, tip it 45 degrees, and give each card a height; a move never raises the total height, and it stays level only when the cards already form the steepest staircase (the cradle or potential-energy argument of Toom and Björner, as presented by Drensky). Checked by computer here: for totals up to 20 every cycle count matches the necklace formula, and for k up to 7 the longest run to the staircase is exactly k(k − 1). Children can discover that 6, 10 and 15 cards always end in the same staircase, that 4, 7 or 8 cards loop instead, and that some shapes can never appear after a move.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Bulgarian Solitaire and the Mathematics Around It](https://arxiv.org/pdf/1503.00885.pdf) — Vesselin Drensky, arXiv 1503.00885, about 2015. The triangular case via the cradle model, Toom's slowest start, Knuth's check and the Igusa and Bentz proofs, the cycle and necklace count for other totals, Brandt (1982) and Gardner (1983) references (read November 4, 2026).
- [A Short Survey of the Game Bulgarian Solitaire and Related Games](https://arxiv.org/pdf/2607.17194) — Romeo Meštrović, arXiv 2607.17194, 2026. Brandt's theorem, the k² − k bound (Igusa 1985), Etienne's (1991) description of the cyclic partitions (read November 4, 2026).
- Prior use with children: [UW Math Circle, Week 11](https://sites.math.washington.edu/~mathcircle/circle/files/26wi-week11.pdf) — University of Washington Math Circle, winter 2026, group worksheet: play with 6 beans, list the partitions of 6, tabulate end states for 1 to 10 beans, predict 20 and 21, use rotated Young diagrams to explain triangular endings (read November 4, 2026).

## A kid-friendly way in

Each pair gets a handful of counters or a short deck of cards and a strip of paper "shelves". Make piles, do the move (one from every pile into a new pile), and draw the piles as a bar picture after each move, tallest first. Prep: count out bags of 6, 7, 8, 10 and 15 counters; print recording strips with small squares; about 15 minutes. Launch (2–3 minutes): with 5 counters (a non-task total), make piles 3 and 2, do one move together (take one from each, new pile of 2: piles 2, 2, 1), and draw the bar picture.

## By band

- **K–1:** with 6 counters, start from one tall pile and do the move until something happens; build the final staircase from blocks. Try another start and see whether it lands on the same staircase.
- **2–3:** a class table for totals 3 to 10: which totals stop and which loop; how many moves the slowest start of 6 or 10 needs; predict the end for 15 and test it.
- **4–5:** draw the tipped bar picture and explain why a triangular total must end in the staircase; for 8 cards find both cycles and describe them as extra cards travelling around the staircase; find the shapes of 6 that no move can produce.

## Checked facts

Computed in `check_networks_counting_2.py`, `check_week_154()`:

- partitions: 11 of 6, 42 of 10, 176 of 15;
- from one pile of 6: 6 → 5,1 → 4,2 → 3,2,1 in three moves; slowest start of 6 is 2,2,1,1 (six moves); of 10, 3,3,2,1,1 (twelve moves); for k = 1 to 7 the slowest start needs exactly k(k − 1);
- 4 cards: one cycle 3,1 → 2,2 → 2,1,1 → 3,1; 8 cards: two cycles, of lengths 4 and 2; totals 1 to 20: number of cycles equals the necklace count, each cycle length divides k;
- the three shapes of 6 no move produces: 2,2,1,1; 2,1,1,1,1; 1,1,1,1,1,1.

Cited, not computed: the general theorems for all n.

## Nearest existing themes

Week 54 (partitions and rebuilding) uses partitions, bar diagrams and the transpose; here the same pictures become states of a process, and the tipped diagram is a new move. Week 49 (four towers and differences) and Week 11 (chip-firing) repeat a rule until it settles, with a quantity that never grows as the proof; draft Week 108 (hailstones) iterates a rule where settling is open. Year 1's figurate numbers and draft Week 111 (staircase numbers) make triangular totals familiar. New here: partitions as a state space, fixed points versus cycles, and a potential-energy proof on a bar picture.

## App connection

Counting and arranging: a "piles machine" where the child arranges piles of blocks, presses the move, and the board keeps a filmstrip of shapes; puzzles ask "start so that the staircase takes exactly 6 moves", "find a shape that can never appear", or "how many different loops does 8 have?".

## Open questions

- Whether K–1 can keep track of "one from every pile" without losing counters; a tray with marked pile spots may help.
- Whether the tipped-diagram proof is reachable in grades 4–5 in one session or belongs to a return visit.
- Drensky's paper says every start reaches the staircase in exactly k(k − 1) moves; the check shows this is the maximum, not the time for every start, so the guide must state the bound carefully.
