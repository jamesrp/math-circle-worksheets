# Week 104 (draft plan): The sixteen-card square

**Strand:** counting (Counting and arranging), with a logic flavour (Codes and logic). **Deep-math field:** combinatorial design theory (orthogonal Latin squares). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Two Latin squares of order n are orthogonal when, laid on top of each other, every ordered pair of symbols appears exactly once; such a pair is a Graeco-Latin (Euler) square. The playing-card form: put the 16 cards J, Q, K, A of four suits in a 4-by-4 grid so every row and column has each rank once and each suit once (Ozanam posed it in 1694). Checked by computer here: there are 6912 such arrangements; requiring both long diagonals as well leaves 1152, which is 144 up to turning and flipping the square. Of the 576 Latin squares of order 4 (the rank pattern alone), only 144 have any suit pattern to pair with; the "add one and wrap round" pattern (i + j mod 4) has none. Order 3 works (72 arrangements of nine cards) but never with both diagonals; order 2 never works; order 5 works, diagonals included, with ranks i + j and suits i + 2j mod 5. Euler (1782) asked for 36 officers of six ranks from six regiments in a 6-by-6 square, failed, and conjectured that no orthogonal pair exists for any order 2, 6, 10, 14, …. Tarry proved order 6 impossible by checking cases (around 1900–1901), and Bose, Shrikhande and Parker (announced 1959) disproved the rest of the conjecture: orthogonal pairs exist for every order except 2 and 6. Rather and colleagues (Physical Review Letters, 2022) showed that the 36 officers can be arranged if the officers are quantum-entangled mixtures of ranks and regiments, which corresponds to a special four-party entangled state; this changes the rules and does not contradict Tarry. Children can discover that two separate conditions (ranks, suits) must each be a Latin square, that some rank patterns cannot be completed, that 2-by-2 is impossible by a short argument, and that adding the diagonals makes 3-by-3 impossible.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Euler Squares](https://old.maa.org/node/116660) — Elaine Young, MAA Convergence, May 2011. Ozanam's 1694 sixteen-card problem, Euler squares as Graeco-Latin squares, and "144 solutions, not including symmetrical transformations" (read November 3, 2026).
- [Shrikhande: Euler's spoiler turns 100](https://bhavana.org.in/shrikhande-eulers-spoiler-turns-100/) — Nithyanand Rao, Bhāvanā 1(4), October 2017. Euler's 1782 conjecture, Tarry's case check (dated 1901 there), Bose, Shrikhande and Parker's 1959 disproof for all orders except 2 and 6, and the New York Times front page (read November 3, 2026).
- [Thirty-six entangled officers of Euler](https://www.arxiv.org/abs/2104.05122) — Suhail Ahmad Rather, Adam Burchardt, Wojciech Bruzda, Grzegorz Rajchel-Mieldzioć, Arul Lakshminarayan, Karol Życzkowski, Phys. Rev. Lett. 128, 080507 (2022). Orthogonal quantum Latin squares of order 6 and the AME(4,6) state (read November 3, 2026).
- [Euler's 243-Year-Old 'Impossible' Puzzle Gets a Quantum Solution](https://quantamagazine.org/eulers-243-year-old-impossible-puzzle-gets-a-quantum-solution-20220110) — Daniel Garisto, Quanta Magazine, January 10, 2022. Plain account of the quantum solution and the classical history (read November 3, 2026).
- Prior use with children: [Printable Latin square puzzle](https://dr-mikes-math-games-for-kids.com/blog/?p=1153) — Michael Hartley, Dr Mike's Math Games for Kids, 2016 (updated 2024). Sixteen cards (aces to fours of four suits) in a 4-by-4 with every row, column and diagonal holding each number and suit once (read November 3, 2026).

## A kid-friendly way in

Real cards: the 16 face cards and aces from one deck per pair (or printed cards). For K–1, a 3-by-3 version with nine shape cards: three shapes (circle, square, triangle) in three colours, cut from coloured card. Prep: sort cards from old decks, print or cut nine shape cards per pair, print a 4-by-4 mat; about 15 minutes. Launch (2–3 minutes): on the board, place three cards of one row of the 3-by-3 shape version, show a legal row (every colour once, every shape once) and an illegal one, then let children finish.

## By band

- **K–1:** the nine shape cards on a 3-by-3 mat with rows and columns each showing every colour and every shape once. Then: can you make a 2-by-2 with two colours and two shapes? (No.)
- **2–3:** the 16-card square with rows and columns. Then add the two diagonals as a harder challenge. A partner game: one child places the ranks only (a Latin square of letters on sticky notes); can the other always add suits? (Not for every rank pattern.)
- **4–5:** prove 2-by-2 impossible; show that the 3-by-3 shape square can never satisfy both diagonals; explore which 4-by-4 rank patterns can take suits, starting from the "slide one" pattern (none); build a 5-by-5 with five colours and five shapes using a "step by one, step by two" rule; hear the story of the 36 officers, Euler's guess, the 1959 surprise and the quantum version.

## Checked facts

Computed in `check_counting_networks.py`, `check_week_104()`:

- 2, 12 and 576 Latin squares of orders 2, 3, 4; no orthogonal pair of order 2;
- 72 nine-card arrangements of order 3, none with both diagonals;
- 6912 sixteen-card arrangements; 1152 with both diagonals, which form 144 classes under the 8 turns and flips; 144 rank patterns with a suit partner; the cyclic pattern has none;
- the order-5 construction with diagonals.

Cited, not computed: Tarry's order-6 impossibility, Bose–Shrikhande–Parker, the quantum construction. Discrepancy to settle: Young's page gives 144 "not including symmetrical transformations" for the rows-and-columns puzzle, but the computed count of 144 arises for the version with diagonals; rows and columns alone give 6912 = 48 × 144, and the symmetry group used by Young may include relabelling ranks and suits. The guide should quote only the computed numbers.

## Nearest existing themes

Week 5 (tower cities) is built on Latin squares with edge clues; this week's new step is a pair of them and orthogonality. Week 36 (making threes) works in the nine-tile plane over the integers mod 3, which is the same structure as the order-3 Graeco-Latin square (its parallel classes of lines); AD-01 and Week 36 sort attribute cards. So the 3-by-3 shape square is close to Week 36's material, and the plan should use it only as the K–1 entry. New here: orthogonality, a famous impossibility (order 6) next to a famous surprise (all other orders), and a real 2022 research twist.

## App connection

Codes and logic: a "two-attribute square" family. The child drags cards into a grid with live checks for rank and suit per row and column; puzzles give a partly filled square to complete, ask whether a given rank pattern can take suits, or turn on the diagonal rule. Week 5's Latin-square family could carry it as a second layer.

## Open questions

- Settle the 144 discrepancy against Ozanam's or Rouse Ball's original wording before quoting it to children.
- Whether 2–3 children can hold two conditions at once with 16 cards, or need the ranks placed first as a separate step.
- Whether real playing cards are acceptable at the school; printed cards are a safe alternative.
