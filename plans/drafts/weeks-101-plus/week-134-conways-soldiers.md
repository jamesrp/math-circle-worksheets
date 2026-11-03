# Week 134 (draft plan): Peg jumps and Conway's soldiers

**Strand:** games (Games and choices). **Deep-math field:** combinatorics (invariants and monovariants), combinatorial games. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In peg solitaire a peg jumps over a neighbour into an empty hole and the jumped peg is removed. Two kinds of "can't" proofs govern it. A colouring invariant: colour the holes with three colours so that every line of three neighbouring holes has all three ((x + y) mod 3 on a square grid, (row + column) mod 3 on a triangle board). A jump empties two holes and fills one, and those three holes have three different colours, so every colour count changes by exactly one, and the parities of N₀ + N₁ and N₁ + N₂ never change. This decides where a lone last peg can possibly be: on the 33-hole cross starting from the centre only 5 holes are possible. A weight monovariant: in Conway's soldiers, soldiers fill every square on and below a line and jump only orthogonally; they can send one soldier 1, 2, 3 or 4 rows above the line (needing 2, 4, 8 and 20 soldiers) but never 5. Give a square at taxicab distance d from the target the weight r^d with r = 1/φ ≈ 0.618, so that r + r² = 1. A jump toward the target keeps the total weight, every other jump lowers it, the target alone weighs 1, and the whole infinite army below the line weighs exactly φ^(5 − n) for a target in row n, which is exactly 1 for row 5. Finitely many soldiers weigh less than 1, so row 5 is out of reach. The same weights show that on a single line a soldier can get 1 step past the edge but never 2. Proved: both arguments, and that 20 soldiers is the minimum for row 4 (the weights alone only give at least 19; the extra step is cited). Checked here: the weight sums, the bounds 2, 4, 8, armies that actually reach rows 1 to 3, the colour invariant on every solved small board, and which small boards can be cleared to one peg. The planning note in `plans/topic-scouting/README.md` set this aside ("impossibility needs golden-ratio weights; 4–5 only"); this draft answers that with K–1 and 2–3 entries built on the puzzles and the colouring, keeping the golden weights for 4–5.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Five steps into the void](https://people.math.carleton.ca/~kcheung/math/books/giam-ON/html/sec-5-steps.html). Joe Fields, *A Gentle Introduction to the Art of Mathematics*, section 9.2. Conway's soldiers: 2, 4, 8 and 20 soldiers for rows 1 to 4, and the golden-ratio weight proof that row 5 is impossible (read November 3, 2026).
- [Peg Solitaire](https://www.jaapsch.net/puzzles/pegsolit.htm). Jaap's Puzzle Page. The three-colouring argument on the 33-hole board and the five possible finishing holes from a central start (read November 3, 2026).
- Prior use with children: [Math Club: Invariants Continued](https://schoolnova.org/classes/ay2023/adv_math_club/adv_math_club-2024-02-11-file1.pdf). SchoolNova advanced math club handout, February 11, 2024, level not stated. One-dimensional and two-dimensional Conway's soldiers with weights in geometric progression (read November 3, 2026).
- Prior use with children: [Peg Solitaire](https://www.gamesforyoungminds.com/blog/2018/4/13/peg-solitaire). Kent Haines, Games for Young Minds, 2018. Peg solitaire for ages 6 and up, smaller starting puzzles for young children, and questions about where the last pegs end (read November 3, 2026).

## A kid-friendly way in

Small peg puzzles with counters on printed boards: a row of 4 holes, a row of 6, a 10-hole triangle and a 15-hole triangle, each hole with a coloured dot in the three-colour pattern (not explained at first). The goal: jump until one counter is left. A second board is a large grid with a thick line across it for Conway's soldiers, with counters as soldiers. Prep: print boards, sort counters, about 20 minutes. Launch (2 to 3 minutes): on a large row of 4 holes with the second hole empty, show a legal jump (over a neighbour, into an empty hole, take the jumped counter away) and clear it to one counter together.

## By band

- **K–1:** rows of 4 and 6 holes with a chosen hole empty, then the 10-hole triangle starting with an edge hole (not a corner) empty. Each child who finishes puts a sticker of the last hole's colour on a class chart. The class question: on the 10-hole triangle, can anyone finish if a corner starts empty? (No one can; the adult says it has been checked every way.)
- **2–3:** the 15-hole triangle, which can be finished from any start hole; record the colour of the last hole and compare with the empty start hole (the colour rule predicts which finishes are possible). Then Conway's soldiers: get a soldier 1, 2 and 3 rows past the line using as few soldiers as you can, and check whether anyone beats 2, 4 and 8.
- **4–5:** why the colours work (each jump touches three holes of three colours). Then soldiers on a line aiming two steps past the edge: the target square weighs 1, the next 0.618, then 0.382, 0.236, 0.146, …; the soldiers' weights (from 0.382 on) add up towards 1 but never reach it, and a jump toward the target never adds weight; then the 2D proof that row 5 is impossible. Class build: reach row 4 with 20 soldiers, working from a picture of the start.

## Checked facts

Computed in `check_symmetry_games.py`, `check_week_134()`:

- r + r² = 1 for r = 1/φ; the full army's weight for a target in row n is φ^(5 − n) (exactly 1 for n = 5);
- the fewest soldiers whose weights can reach 1: 2, 4, 8 for rows 1 to 3 (met by armies found by search, for example 5 on the line and 3 just below it for row 3), and 19 for row 4, where 19 weigh exactly 1;
- on a line, soldiers at 0, −1, −2, … reach 1 but not 2;
- rows of holes with one empty: a row of 4 finishes from its 2nd or 3rd hole, a row of 6 from its 2nd or 5th, rows of 5 and 7 never; the 3-by-3 square and 2-by-3 rectangle never finish from any single empty hole;
- the 10-hole triangle finishes exactly from its six non-corner edge holes; the 15-hole triangle from all 15 holes (from the top hole the last peg can be in 4 places);
- every finish found keeps the start's colour parities.

Cited, not computed: 20 as the exact minimum for row 4, and the five finishing holes on the 33-hole board.

## Nearest existing themes

Week 1 (Tiling lab) already uses a colouring to prove impossibility, and Weeks 11, 49 and 98 use monovariants (chip firing, Ducci differences, perimeter). New here: weights from the golden ratio, an infinite total that equals exactly the target's weight, and a one-player jumping game whose "can't" answers are invariants. The scouting decision was right that the full Conway proof is 4–5 only; the case for reconsidering is that the puzzles and the colour chart give K–1 and 2–3 real work, and the 2–3 soldier challenges (2, 4, 8) are reachable goals with a satisfying pattern. Contrast Week 7 (take-away games) and the scouting games, which are two-player.

## App connection

Games and choices. A "Peg jumps" family: tap a peg, then the hole it jumps to. Puzzles: "Leave one peg on this triangle"; "Finish with the last peg on the star hole" (some stars are impossible, certified by the colour count); "Get a soldier to row 3 with 8 soldiers". The app can show running colour counts as an optional lens. Fit A for the peg puzzles (an obvious tap-and-check solve), B for the soldiers.

## Open questions

- Are counters on paper stable enough, or do children need pegboards or egg cartons so jumped counters are easy to remove?
- Is the colour sticker chart convincing for 2–3 with only a few finishes each, or does it need class pooling across tables?
- The 4–5 weight argument uses an infinite sum; decide how to present "creeps towards 1" without decimals overload (perhaps a picture of halving-like strips).
- Reaching row 4 with 20 soldiers needs a worked picture in the guide; it has not been rehearsed.
