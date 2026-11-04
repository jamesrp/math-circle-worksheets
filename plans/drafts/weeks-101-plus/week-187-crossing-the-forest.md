# Week 187 (draft plan): Can the fire cross the forest?

**Strand:** networks (Maps and networks), with chance. **Deep-math field:** probability (percolation, phase transitions). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Percolation: colour each cell of a board green (a tree) with chance p, independently, and ask whether green cells that share an edge form a path from the top edge to the bottom edge. On a rhombus-shaped board of hexagons (a Hex board) with a fair coin, the crossing chance is exactly 1/2, on every size of board. The reason is the Hex theorem (see the Hex scouting draft): on any full board exactly one of "green crosses top to bottom" and "white crosses left to right" happens, and swapping the colours and reflecting the rhombus turns one event into the other, so they have equal chances (Werner, Lectures on two-dimensional critical percolation, notes this holds for every rhombus size). For p below 1/2 the crossing chance falls toward 0 as the board grows, and above 1/2 it rises toward 1: the critical value for site percolation on the triangular lattice (hexagon cells) is exactly 1/2 (Kesten 1980 proved the matching statement for bond percolation on the square lattice; the triangular site case follows by the same kind of argument, Kesten and Wierman). Smirnov (2001) proved Cardy's formula: at p = 1/2 the crossing chance of any shape has a limit as the cells shrink, and that limit does not change under conformal (angle-preserving) maps. On a square board where only side-neighbours count, the fair coin is not fair: two squares touching only at a corner do not connect, so both colours can fail to cross at once, the colour-swap argument breaks, and the critical value for square site percolation is about 0.5927, known only numerically. Checked here: exactly one crossing on every 2-by-2, 3-by-3 and 4-by-4 hex colouring, so 1/2 exactly; on the 4-by-4 hex board the crossing chance is 0.111, 0.276, 0.5, 0.724, 0.889 for p = 0.3 to 0.7, and simulated 11-by-11 boards give about 0.12, 0.5 and 0.88 for p = 0.4, 0.5, 0.6 (sharper); a 4-by-4 square board crosses only 22,193 of 65,536 coin colourings (0.339). Children can discover that a fair coin crosses half the hex boards, that more trees help sharply, and that the cell shape matters.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Lectures on two-dimensional critical percolation](https://ar5iv.arxiv.org/html/0710.0856) — Wendelin Werner, arXiv 0710.0856, 2007. The rhombus symmetry argument giving crossing probability exactly 1/2 for every rhombus size, p_c = 1/2 for the triangular lattice (Kesten and Wierman), and Smirnov's proof of Cardy's formula (read November 4, 2026).
- [Planar percolation with a glimpse of Schramm–Loewner Evolution](https://www.ihes.fr/~duminil/publi/2013lecture_notes_percolation.pdf) — Vincent Beffara and Hugo Duminil-Copin, arXiv 1107.0158, 2011. Theorem 1.1 (critical point 1/2 for triangular site percolation), Kesten's 1980 square-lattice bond result, Smirnov's 2001 theorem and conformal invariance (Theorem 1.3) (read November 4, 2026).
- [An Introduction to Percolation](https://uregina.ca/~kozdron/Research/Talks/regina_percolation.pdf) — Michael J. Kozdron, University of Regina colloquium, September 28, 2007. Kesten (1980) with Harris (1960) for p_c = 1/2, the numerical value 0.592746 for square-lattice site percolation, and Cardy (1992) and Smirnov (2001) (read November 4, 2026).
- Prior use with children: [HandsOn 27 – Growing a Scattered-Seed Forest](https://archive.physionet.org/tutorials/epn/html/chp71act1.htm), a percolation tutorial activity (grade not stated): flip a coin for each square of a 5-by-5 grid, start a fire on the left, spread only through side-neighbours, pool class results, then repeat with a die (trees on 1–4) (read November 4, 2026). No K–5 report found.

## A kid-friendly way in

Coin forests. Printed hex boards (rhombus of hexagons about 2.5 cm across; 5-by-5 for K–1, 7-by-7 or 9-by-9 later) with green tops and bottoms; for each cell, flip a coin and put a green dot sticker on heads. Then a "fire" (a finger, or a red crayon) starts on the top edge and spreads only to green cells that share an edge: does it reach the bottom? Every board goes on a class tally. Then use a die: green on 1–4, or green on 1–2. Prep: print boards, buy dot stickers, find coins and dice; about 15 minutes. Launch (2–3 minutes): a pre-filled board on the board; trace the fire, show a cell that touches only white and stops; then flip coins for a 3-by-3 board together and ask everyone to guess how many boards in the room will cross.

## By band

- **K–1:** fill 5-by-5 boards by coin and sticker, trace the fire with a finger, and put each board in a "crossed" or "stuck" pile. Try to make a board by choice where neither green crosses top to bottom nor white crosses side to side.
- **2–3:** pool the class tally for the coin (about half), then for green on 1–4 and green on 1–2. What happens on a bigger board? Compare a square board with the same coin: do squares cross as often?
- **4–5:** explain why the fair coin gives exactly half on hex boards (one of the two crossings always happens, and colour-swap-and-flip matches them); find why squares break the argument (corner touches); predict and test how sharp the change is on 9-by-9 boards.

## Checked facts

Computed in `check_networks_3.py`, `check_week_187()`:

- exactly one of the two crossings on every 2-by-2, 3-by-3 and 4-by-4 hex colouring, so the fair-coin crossing chance is exactly 1/2;
- 4-by-4 hex crossing chance at p = 0.3, 0.4, 0.5, 0.6, 0.7: 0.111, 0.276, 1/2, 0.724, 0.889; and 0.352 on 2-by-2 at p = 0.4;
- simulated 11-by-11 hex boards (seeded, 2000 each): about 0.12, 0.51, 0.88 at p = 0.4, 0.5, 0.6;
- 4-by-4 square board with side-neighbours only: green crosses top to bottom on 22,193 of 65,536 coin colourings (0.339), and some colourings have neither crossing.

Cited, not computed: p_c = 1/2 for triangular site percolation, Kesten's theorem, Smirnov's theorem, the square-lattice value 0.5927.

## Nearest existing themes

The Hex scouting draft (plans/topic-scouting/hex.md) proves "someone always wins Hex" by filling boards; this plan uses exactly that theorem, so the two should be paired and Hex played first. New here: random filling, the exact 1/2 as a symmetry consequence, the threshold as p changes and board size grows, and the hex-versus-square contrast. Week 98 (Growing from a few seeds) is bootstrap percolation: deterministic filling from chosen seeds and the fewest seeds that fill a grid; nothing there is random. Week 16 (Three-color triangles, Sperner) is the discrete cousin of the Hex theorem. Draft 175 (chaos game) also pools everyone's random trials into one class picture.

## App connection

Maps and networks (with Chance and machines): a "forest fire" family. The child sets a slider for the share of trees, presses "grow" to fill a hex board at random, and presses "burn" to watch the fire spread; a running tally plots crossings against the slider and against board size. Puzzles: place the fewest trees by hand so the fire crosses; colour a full board where nobody crosses (impossible on hexes, possible on squares).

## Open questions

- Sticker counts: a 7-by-7 board is 49 coin flips; check timing at K–1 or start with 4-by-4 boards and a class tally.
- Whether the class tally (perhaps 20 to 30 boards) is enough to see "about half" convincingly; pooled bar charts on the wall may help.
- Whether 4–5 children can follow the colour-swap argument without first playing Hex.
