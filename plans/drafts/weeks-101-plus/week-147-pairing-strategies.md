# Week 147 (draft plan): Pairing strategies

**Strand:** games (Games and choices). **Deep-math field:** positional games, Ramsey-type theorems. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In a Maker–Breaker game the players take turns claiming cells of a board; Maker wins by owning every cell of some winning line, and Breaker wins by stopping that (Breaker never needs a line of their own). A pairing strategy is a proof that Breaker wins: if Breaker can set aside two cells inside every winning line, with no cell set aside twice, then answering each Maker move in the partner cell leaves Maker with at most one cell of every pair, so never a whole line. On a strip of squares where Maker needs 3 neighbouring squares, the pairs (1, 2), (3, 4), (5, 6), ... do it, because every run of three contains a whole pair; needing only 2 in a row, Maker wins on any strip of 3 or more squares. On the 3 by 3 board, Maker moving first wins, Maker moving second loses, and ordinary tic-tac-toe (both players trying to make a line) is a draw, with 16 full boards where nobody has a line. A pairing needs two cells for each line, so it is impossible on 4 by 4 (10 lines, 16 cells < 20) but possible on 5 by 5 (12 lines, 24 ≤ 25 cells; one is found here). For n^k boards (Golomb and Hales, 2002), a pairing needs n ≥ 2/(2^(1/k) − 1), giving n = 5, 8, 11, 14 in dimensions 2 to 5; pairings are known for 5 and 8 and were reported for 11 and 14, and whether one always exists at the threshold is open; 3 by 3 by 3 cannot end in a draw, and 4 by 4 by 4 is a first-player win by computer search (Patashnik). The Hales–Jewett theorem (1963) says that for any n and any number of players, n-in-a-row on a board of high enough dimension can never end in a draw; then strategy stealing (an extra move never hurts the first player) shows the first player wins, though no one can say how. On the infinite square grid with k in a row: Breaker wins for k ≥ 9 (a pairing strategy exists) and for k = 8 (Zetters, a pseudonym of A. Brouwer); Maker wins for k = 5, which follows from Allis's computer solution of gomoku; k = 6 and 7 are open (Csernenszky's 2010 survey). Proved: the pairing argument, Hales–Jewett, strategy stealing. Checked here: all the small boards. Open: 6 and 7 in a row. Children can discover that a blocker can win by a plan made before the game starts, find a pairing themselves, and see by counting why some boards have none.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Hypercube Tic-Tac-Toe](https://library.slmath.org/books/Book42/files/golomb.pdf) — Solomon W. Golomb and Alfred W. Hales, in *More Games of No Chance*, MSRI Publications 42, 2002 (read November 4, 2026). Pairing strategies and the necessary condition; pairings for n = 2, 5, 8 (11 and 14 reported); 3 by 3 is a draw, 3 by 3 by 3 cannot be drawn, 4 by 4 by 4 is a first-player win (Patashnik); the conjecture that the second player draws for large n, and the simple threshold formula's first failure at k = 6,847,196,937.
- [The Chooser-Picker 7-in-a-row-game](https://arxiv.org/pdf/1004.2460) — András Csernenszky, Publicationes Mathematicae, 2010 (read November 4, 2026). Status of k-in-a-row on the infinite board: Breaker wins for k ≥ 9 (Pollak and Shannon, later a pairing strategy) and k = 8 (Zetters); Maker wins for k = 5 by Allis's result; 6 and 7 open.
- [Hales–Jewett theorem](https://en.wikipedia.org/wiki/Hales%E2%80%93Jewett_theorem) — Wikipedia, secondary pointer (read November 4, 2026). Hales and Jewett, "Regularity and positional games", Trans. AMS 106 (1963); no draws in high dimension; strategy stealing gives a first-player win with no known practical strategy.
- Prior use with children: [Noughts and Crosses](https://nrich.maths.org/1224) — NRICH, ages 7 to 11 (read November 4, 2026). Children play, look for good strategies and judge the claim that correct play never loses; first of a sequence with Fifteen and Jam. No K–5 Maker–Breaker or pairing activity was found (searched "Maker Breaker game pairing strategy activity students handout tic-tac-toe math circle").

## A kid-friendly way in

Two games on printed strips and boards with two colours of counters. First the strip game: a strip of 12 squares; Maker needs neighbouring squares of their colour, Breaker only blocks. Then tic-tac-toe as a Maker–Breaker game on 3 by 3, 4 by 4 and 5 by 5 boards. Breakers may draw "domino" pairs on a clear sheet over the board before playing, and must always answer in the partner square. Prep: print strips and boards at 25 mm squares, clear sleeves and dry-erase pens, about 30 counters of each colour per pair; about 15 minutes. Launch (3 minutes): on a big strip, the adult plays Breaker against the room for "two in a row" (the room wins by playing in the middle of a gap), then for "three in a row" with dominoes drawn on the strip, and asks: can Maker ever win this one?

## By band

- **K–1:** The strip game. With "two in a row" Maker always wins; with "three in a row" the dominoes stop every attempt. Children take both roles and try to beat the dominoes. No reading.
- **2–3:** Maker–Breaker tic-tac-toe on 3 by 3 (who wins, and does going first matter?), then 4 by 4 and 5 by 5 with "four in a row" and "five in a row". Find a domino plan for 5 by 5 that blocks every line, and check it against the 12 lines with a line card.
- **4–5:** Explain why a domino plan always works. Count lines and squares to show 4 by 4 has no domino plan. Play 3 by 3 by 3 on three stacked boards and try to fill it with no line (impossible). Hear the Hales–Jewett story and the open cases 6 and 7 in a row.

## Checked facts

All in `check_logic_games_2.py`, function `check_week_147()`:
- Tic-tac-toe is a draw; 16 full boards (5 X, 4 O) have no line for either; 8 lines.
- Maker–Breaker 3 by 3: Maker first wins; Maker second loses.
- Strips of 2 to 12 squares: two in a row is a Maker win exactly from 3 squares; three in a row is always a Breaker win, and the pairs (1, 2), (3, 4), ... meet every run of three.
- Lines ((n + 2)^k − n^k)/2: 8 (3 by 3), 10 (4 by 4), 12 (5 by 5), 49 (3 by 3 by 3); 4 by 4 has 16 squares < 20, 5 by 5 has 25 ≥ 24, and a 12-pair plan for 5 by 5 exists.
- The Golomb–Hales threshold gives 5, 8, 11, 14 for dimensions 2 to 5.
- Cited, not computed: 3 by 3 by 3 never drawn, 4 by 4 by 4 a first-player win, existence of the pairings in higher dimensions (Golomb and Hales); infinite-board results (Csernenszky); Hales–Jewett (Wikipedia).

## Nearest existing themes

Draft 113 (magic squares) shows Pick 15 is tic-tac-toe; the scouting README set aside "Tic-tac-toe in disguise" because its theorem was an exhaustive search. Here the theorem is the pairing argument, which is a proof children can carry out. The scouting draft "Hex" (no draws, strategy stealing) and "Patterns you cannot avoid" (Ramsey thresholds) are close cousins: Hales–Jewett is a Ramsey-type theorem, so if all three are built, order them Hex, this, then patterns. Weeks 7, 8 and 81 analyse take-away games by winning positions; a pairing strategy is a different kind of proof (a plan fixed in advance). New: Maker–Breaker games, pairing strategies, the counting obstruction to pairing.

## App connection

Games and choices region, possible family "Block the line": the child plays Breaker against an app Maker, and in a "plan" mode draws dominoes before play; the app then plays every Maker strategy against the plan and shows a win or the first line that gets through. Puzzles: "Draw a domino plan for this strip"; "Find a 12-domino plan for 5 by 5"; "Why can no plan work on 4 by 4?". Small boards are solved instantly.

## Open questions

- Is the 5 by 5 pairing puzzle too hard for 2–3 without a hint (start with the two diagonals)?
- Does the overlap with draft 113's Pick 15 need a scheduling note?
- 4 by 4 Maker–Breaker with four in a row is believed to be a Breaker win by other means; it is not checked here and should not be stated to children without a check.
- Board size and counters: 25 mm squares on 5 by 5 fit a page; the 3 by 3 by 3 stack needs three boards side by side.
