# Week 137 (draft plan): The Game of Life

**Strand:** logic (Codes and logic), with a dynamics flavour. **Deep-math field:** cellular automata, dynamical systems, computability. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Conway's Game of Life (published in Martin Gardner's Scientific American column, October 1970) is a grid of cells, each alive or empty, updated all at once: a live cell with 2 or 3 live neighbours (of its 8) survives, an empty cell with exactly 3 is born, and everything else is empty next time. Proved facts at child scale: the 2-by-2 block and the beehive never change (still lifes), the row of three alternates with a column of three (the blinker, period 2), and the five-counter glider returns to its own shape after 4 generations, moved one diagonal step. Gardner reports Conway's conjecture that no pattern grows without limit; it was false, refuted the same year by Gosper's glider gun. Two deeper theorems frame the destination. First, the Garden of Eden theorem (Moore 1963, Myhill 1963): a cellular automaton has patterns with no parent ("orphans") exactly when two different finite patterns of the same size have the same child ("twins"). Life has orphans; the smallest known ones fit in 10 by 10, none exist in 7 by 7 (Beer, arXiv 2022, computer proof), and whether any fit in 8 by 8 or 9 by 9 is open. On a finite ring the theorem is plain pigeonhole: if two patterns share a child, some pattern has no parent. Second, Life can simulate a universal computer (stated in the LifeWiki summary; the classic construction is in Berlekamp, Conway and Guy's Winning Ways, 1982, not opened here), so by Turing's halting theorem no method decides in general whether a pattern eventually dies out. Children can discover the still lifes and oscillators, classify small starts, find parents for given patterns, and (4–5) prove that a one-dimensional "Rule 90" ring can never make an odd number of black cells, so every ring pattern with an odd number of black cells is an orphan.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Mathematical Games: The fantastic combinations of John Conway's new solitaire game "life"](https://embed.cocalc.com/share/download/943c068a27466910dfee6f6258d6a7d012683819/cocalc-examples/think-complexity-2ed/papers/gardiner70fantastic.pdf) — Martin Gardner, Scientific American 223, October 1970, pp. 120–123 (read November 3, 2026). The three rules, counters on a board, the blinker and glider, the R-pentomino, Conway's growth conjecture and $50 prize.
- [Cultivating the Garden of Eden](https://arxiv.org/pdf/2210.07837) — Randall D. Beer, arXiv 2210.07837 (identifier dates it to October 2022) (read November 3, 2026). Statement of the Moore–Myhill theorem (orphans exist exactly when twins exist), no Life orphans in 7 by 7, known orphans from 10 by 10, 8 by 8 and 9 by 9 open.
- [Rule 90](https://mathworld.wolfram.Com/Rule90.html) — MathWorld, Wolfram Research (read November 3, 2026). Rule 90 from one black cell gives Pascal's triangle mod 2, the Sierpiński triangle; introduced by Wolfram in 1983.
- [Conway's Game of Life](https://conwaylife.com/wiki/Conway's_Game_of_Life) — LifeWiki (read November 3, 2026). Secondary pointer: Life has the power of a universal Turing machine; Gosper's MIT group won Conway's prize in November 1970 with the glider gun.
- Prior use with children: [Math Circle handout, Conway's Game of Life](https://sites.math.washington.edu/~mathcircle/circle/archive/2011-12/ws_2012_winter/life.pdf) — University of Washington Math Circle, winter 2012 (read November 3, 2026). Run given patterns, then hunt for still lifes, oscillators, gliders, patterns that grow forever and long-lived patterns. Audience age not stated; no K–5 use found.

## A kid-friendly way in

The whole room is one machine. A large grid (masking tape on the floor in 30 cm squares, about 10 by 10, or a 1-inch grid poster) and two colours of counters or paper plates. Each generation has two passes so nobody has to change cells "at once": first, every child with a cell checks its neighbours and puts a small marker on cells that will be born or die; second, everyone applies the markers together. Prep: tape the grid or print posters, sort counters into cups, print a rule card with three pictures (lonely, happy, crowded) and a birth picture; about 20 minutes. Launch (3 minutes): place a row of three, count neighbours of one end cell and the middle together, mark, apply, and watch it turn into a column. Then ask what happens next.

## By band

- **K–1:** Place three counters anywhere in a 3-by-3 square on a table board and run them with an adult counting neighbours aloud; sort the starts into "vanish", "becomes a square" and "blinks". Build the block and the blinker and act them out on the floor grid. No reading; the rule card is pictures.
- **2–3:** Which four-counter shapes settle down, and into what? (The square stays; the straight four, the S and the L become the six-cell beehive; the T grows for nine generations into four blinkers.) Then: find a parent, a pattern whose next generation is a given picture (a single counter; a block; a blinker), and invent a start that lasts longer than a partner's.
- **4–5:** Track the glider through four generations and explain why it moves; then the one-row world. On a ring of 7 cups, Rule 90 colours a cup next time when exactly one of its two neighbours is coloured. Run it, then ask: can every ring pattern be made? Children find there are 128 rings but only 64 can ever appear, and explain why a ring with an odd number of coloured cups never appears (each coloured cup "feeds" two neighbours). Extension: Rule 90 from one coloured cell on a long strip draws the Sierpiński triangle, row by row on squared paper.

## Checked facts

All in `check_logic.py`, function `check_week_137()`:
- Block and beehive are still; blinker has period 2; the glider repeats its shape after 4 generations, one diagonal step on, passing through 4 different five-cell shapes.
- Three counters in a 3-by-3 square: 84 placements; 62 die out, 16 become the block, 6 (the straight rows and columns) blink.
- Tetrominoes: O is a block at once; I and S become a beehive by generation 2, L by generation 3; T becomes a traffic light (four blinkers, 12 cells, period 2) from generation 9.
- A single counter has a parent: three in a diagonal line.
- Rule 90 from one cell: row n is Pascal's row n mod 2, with 2^(number of 1s in n's binary form) black cells, checked to row 31.
- Rule 90 rings of 3 to 11 cups: every child has an even number of coloured cups; a pattern and its opposite are twins; on odd rings the orphans are exactly the odd patterns. Ring of 7: 128 patterns, 64 children, each with exactly 2 parents. Ring of 6: only 16 children, 48 orphans.
- Cited, not computed: Life orphans and the 7-by-7 result (Beer); universality (LifeWiki); the 1970 conjecture and its refutation (Gardner, LifeWiki).

## Nearest existing themes

Week 17 (Machine memory) is a finite automaton reading a word; here every cell is a tiny automaton and the interest is the global pattern. Week 11 (Chip-firing) and Week 98 (Growing from a few seeds, bootstrap percolation on a grid) are the closest: both are local grid or graph rules run to a fixed point, and Week 98's "fill a cell with two filled neighbours" is a monotone cousin of Life's birth rule. New here: rules that destroy as well as create, periodic and moving patterns, and the orphan/twin theorem. Week 76 (Substitution strips) and Year 1's Pascal recursion touch the Rule 90 extension; the Sierpiński triangle should be framed as a return visit to Pascal mod 2, not a new discovery. No catalog week or scouting draft uses Life itself.

## App connection

Codes and logic region, possible family "Life lab": the board shows a small grid; a child taps cells to place counters and presses Step. Puzzles: "Make a pattern that is still the same after one step using exactly 6 counters" (beehive, or other still lifes); "Find a parent: tap cells so that the next step is this picture"; "Make the glider reach the flag in 8 steps." A ring variant runs Rule 90 with the question "Can you make this ring?" where some targets are orphans and the app accepts a "No pattern makes it" answer with the parity reason. No existing family carries this; Seed plots (Week 98) shares the grid board and could share code.

## Open questions

- Does the two-pass marking routine on a floor grid keep a group of 8 to 12 children synchronised, or does it collapse into adults running it? Rehearse with 4 people first.
- Age fit of the K–1 neighbour count: counting 8 neighbours, including diagonals, may be the hardest part; a 3-by-3 "window" card that frames the neighbours could help.
- Whether the 4–5 ring proof lands without notation; it may need a physical "each coloured cup gives a token to both neighbours" act-out.
- Undecidability is stated from cited universality plus Turing's theorem, not from a source that states it for Life directly; find one before a guide states it.
