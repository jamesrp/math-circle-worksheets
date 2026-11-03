# Week 110 (draft plan): Fibonacci coins

**Strand:** number and games (Numbers; Games and choices). **Deep-math field:** numeration systems, combinatorial game theory. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Zeckendorf's theorem (published by Zeckendorf in 1972; Lekkerkerker had it about twenty years earlier): every positive whole number is a sum of distinct Fibonacci numbers from 1, 2, 3, 5, 8, 13, … with no two neighbours in the list, and in exactly one way. Existence comes from the greedy rule (take the largest coin that fits; what is left is smaller than the next-lower Fibonacci number, so the next coin chosen is never a neighbour). Uniqueness comes from a size bound: any no-neighbour set whose largest coin is F is worth less than the next Fibonacci number after F, so two different sets cannot have the same total. Without the neighbour rule, uniqueness fails (8 = 5 + 3 = 5 + 2 + 1; 16 has four ways). Two games rest on this theorem. Fibonacci Nim (described by Whinihan, Fibonacci Quarterly, 1963, crediting Gaskell): one pile, the first player may take any number but not all, and afterwards each move takes at most twice the previous move; taking the last counter wins. The player to move wins exactly when the smallest coin in the pile's Zeckendorf representation is within the current limit, and taking that coin is a winning move; so the first player loses exactly when the starting pile is a Fibonacci number (proved; checked here for piles up to 59). The Zeckendorf game (Baird-Smith, Epstein, Flint and Miller) starts with n ones and lets players merge or split by Fibonacci rules (1 + 1 → 2, 2 + 2 → 1 + 3, two of F → the coin two below plus the coin one above, neighbours F + next → the one after). Every game ends at the Zeckendorf representation of n, whoever plays, and for n > 2 the second player can always win, but the published proof is non-constructive: no one has written down the winning strategy. Children can discover the no-neighbour coin system, the uniqueness, and the losing Fibonacci piles.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [What is Zeckendorf's Theorem?](https://math.osu.edu/sites/math.osu.edu/files/henderson_zeckendorf.pdf) — Nik Henderson, 2016, hosted by Ohio State mathematics. Statement and proof of existence (induction) and uniqueness; Zeckendorf's 1972 paper (read November 3, 2026).
- [Global Fibonacci Nim](https://arxiv.org/pdf/1509.08527) — Urban Larsson and Simon Rubinstein-Salzedo, arXiv 1509.08527, 2015. Fibonacci Nim as studied by Whinihan (1963) and the Zeckendorf winning move (read November 3, 2026).
- [The Fibonacci Quilt Game](https://par.nsf.gov//servlets/purl/10220217) — Steven J. Miller and Alexandra Newlon, 2019. Summarises the Zeckendorf game rules, that it always ends at the Zeckendorf decomposition, and that Player 2 wins for n > 2 by a non-constructive proof (read November 3, 2026).
- [Fibonacci nim](https://en.wikipedia.org/wiki/Fibonacci_nim) — Wikipedia, secondary pointer for the rules and the Fibonacci-pile losing starts (read November 3, 2026).
- Prior use with children: none found. Searched "Fibonacci Nim math circle OR classroom game children worksheet" and "Zeckendorf representation children activity"; the one circle worksheet opened (UW Math Circle 2023 fall week 2) has take-away games but not Fibonacci Nim.

## A kid-friendly way in

Coins worth 1, 2, 3, 5, 8 and 13 (card or poker chips with stickers), laid in a row in that order. The rule: pay an amount using at most one of each coin and never two coins that sit next to each other in the row. Children pay every amount from 1 to 20 (exactly those can be paid with these coins) and discover that each amount has only one legal payment. Then Fibonacci Nim with a pile of 20 counters. Prep: print coin sheets, cut six coins per child, 25 counters per pair; about 20 minutes. Launch (2–3 minutes): pay 11 on the board with real coins: 8 + 3 is legal, while 8 + 2 + 1 breaks the rule because 2 and 1 are neighbours; then let pairs try 7.

## By band

- **K–1:** pay amounts 1 to 12 with the coin row and the neighbour rule; then the Zeckendorf game from 6 ones (counters merged by moving onto coin spots), which always ends in the same place.
- **2–3:** pay 1 to 20 and hunt for an amount with two legal payments (none exists); Fibonacci Nim from piles of 8 to 20; which starting piles should you refuse to go first on?
- **4–5:** why no amount has two payments (the "next coin is worth more than all smaller no-neighbour coins together" argument with coin rows); the winning Nim move "take your smallest coin"; the Zeckendorf game with the news that the second player has a winning plan nobody has found.

## Checked facts

Computed in `check_number.py`, `check_week_110()`:

- every n from 1 to 143 has exactly one no-neighbour representation, equal to the greedy one (e.g. 20 = 13 + 5 + 2, 12 = 8 + 3 + 1);
- without the neighbour rule: 8 and 13 have three ways, 16 has four;
- coins 1, 2, 3, 5, 8, 13 with the rule pay exactly the amounts 1 to 20;
- Fibonacci Nim: the losing starting piles from 2 to 59 are exactly 2, 3, 5, 8, 13, 21, 34, 55; the "take the smallest Zeckendorf coin" move wins whenever allowed, and positions where it is not allowed are losses; from 20 the first player takes 2;
- Zeckendorf game for n = 3 to 12: every play ends at the Zeckendorf representation, and the second player wins.

Cited, not computed: the general theorems and the n > 2 result for the Zeckendorf game.

## Nearest existing themes

Week 30 (two-pan weight kits) proves uniqueness for balanced ternary; this is a second "one way only" number system with a different reason. Week 8 (rook race and Nim) ends with Wythoff's queen game, whose losing pairs are tied to the golden ratio but are not stated through Fibonacci sums there, so the overlap is in spirit only; Week 7's take-away games and Year 1's take-away stones use fixed move sets, whereas Fibonacci Nim's move limit changes each turn. Year 1 used Fibonacci strips, and the grades 2–3 plan (plans/grades-2-3-year-a.md) records that Fibonacci numbers were less engaging for most of that group; here the numbers arrive as coins and game piles rather than as a sequence to extend, which is the bet a pilot should test.

## App connection

Numbers region for a "Fibonacci purse" family: pay a price with no-neighbour coins, or prove a price has one payment by finding it; Games and choices region for Fibonacci Nim against the app, which reveals the limit after each move. Example puzzles: "pay 19 with the neighbour rule"; "you face 18 counters and may take up to 4: can you win?"

## Open questions

- Whether the doubling move limit is too much bookkeeping for 2–3; a limit marker (a card showing "you may take up to …") may be needed. Untested.
- Whether to run the Zeckendorf game at all, or keep it as a 4–5 extension.
- Prior engagement data on Fibonacci themes is negative for one group; a home pilot should check interest before committing a session.
