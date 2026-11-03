# Week 105 (draft plan): Knight's tours on small boards

**Strand:** networks (Maps and networks). **Deep-math field:** graph theory (Hamiltonian paths and cycles, bipartite graphs), heuristics. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Join two squares of a board when a knight can jump between them; a knight's tour is a route along these links visiting every square exactly once (a Hamiltonian path), and it is closed if the last square is a knight's move from the first (a Hamiltonian cycle). A knight always lands on the other colour of a checkerboard, so the knight graph is bipartite: a closed tour alternates colours and needs an even number of squares, and an open tour on a board with one more square of one colour (5-by-5 has 13 and 12) must start and end on the larger colour. Schwenk (1991) settled closed tours on rectangles: with m ≤ n, the m-by-n board has a closed tour unless m and n are both odd, or m is 1, 2 or 4, or m = 3 and n is 4, 6 or 8. Open tours are a different question; checked here by exhaustive search: the 3-by-3 board has none (the centre has no moves at all, and the outer eight squares form a single knight loop), 3-by-4 has 16 directed open tours (8 up to reversal) starting only from its four corners and the two end squares of the middle row, 4-by-4, 3-by-5 and 3-by-6 have none, 3-by-7 has 104, and 5-by-5 has open tours from a corner. Warnsdorff's rule (1823), always jump to the square with the fewest onward exits, is a greedy heuristic, not a theorem: with the tie-break used here it completes tours from the corners of 3-by-4, 5-by-5 and 8-by-8, but from a corner of 3-by-7 it gets stuck after 15 squares although 8 tours start there; Marateck (2008) counted its failures on 8-by-8 over all orderings of moves. Children can discover the 3-by-3 loop, the start squares of 3-by-4, that some boards resist every attempt, and the colouring reason for some impossibilities. Proving that a board like 4-by-4 has no open tour is a case search, not a short argument, and should be presented as "we checked every route by computer".

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Closed Knight Tour Problem in Higher Dimensions](https://www.math.u-bordeaux.fr/~sgolenia/Fichiers/chess.pdf) — Joshua Erde, Bruno Golénia, Sylvain Golénia, preprint version of April 20, 2012. Restates Schwenk's 1991 theorem on which rectangles have closed tours, with its three exception families (read November 3, 2026).
- [How good is the Warnsdorff's knight's tour heuristic?](https://arxiv.org/pdf/0803.4321) — Samuel L. Marateck, arXiv 0803.4321, 2008. Warnsdorff's 1823 rule, its failures on 8-by-8 over the 40,320 orderings of the eight moves (read November 3, 2026).
- Prior use with children: [Knight's Tour](https://www.dr-mikes-math-games-for-kids.com/knights-tour.html) — Michael Hartley, Dr Mike's Math Games for Kids. An online tour puzzle that unlocks larger boards; the page says tours exist on any board 5-by-5 or larger (read November 3, 2026). NRICH's knight pages found by search ("A Knight's Journey", ages 14 to 18) are about shortest knight routes, not tours.

## A kid-friendly way in

A floor or table board of paper squares (3-by-3 and 3-by-4, squares about 10 cm), a cardboard knight with an L-shaped "move card" that shows the jump, and numbered counters 1 to 12. Children place counter 1, jump, place counter 2, and so on; a square with a counter is used. Prep: tape or print the boards, cut the move card, count counters; about 15 minutes. Launch (2–3 minutes): on a board drawn on the whiteboard, show the knight's L jump from a corner, mark both legal landings, and number a first three visits.

## By band

- **K–1:** on the 3-by-3 board, hop the knight from a corner and lay counters until it comes home; notice the middle square never gets a counter. Then try the 3-by-4 board with an adult reading the move card if needed.
- **2–3:** find a 3-by-4 tour; collect, as a class, every square a tour can start from (six of the twelve); try 4-by-4 and decide whether to keep trying. Colour the board and notice the knight's colour changes every jump.
- **4–5:** explain why no board with an odd number of squares has a closed tour, and on 5-by-5 why an open tour must start on a corner colour; test Warnsdorff's rule as a strategy on 5-by-5 and 3-by-7; use Schwenk's list to predict which rectangles have closed tours and find one on 3-by-10 or 5-by-6 (both exist, by computer search during drafting; finding one by hand is long).

## Checked facts

Computed in `check_counting_networks.py`, `check_week_105()`:

- 3-by-3: centre isolated, outer eight squares a single loop;
- 3-by-4: 16 directed open tours from six start squares, no closed tour; no open tours on 4-by-4, 3-by-5, 3-by-6; 104 on 3-by-7, 8 from a corner; no closed tour on 3-by-8;
- every knight move changes colour; 5-by-5 has 13 squares of the corner colour;
- Warnsdorff with lowest-row-then-column tie-break: full tours from the corner of 3-by-4, 5-by-5, 8-by-8; stuck after 15 squares on 3-by-7.

Found during drafting but not in the check script (searches too slow for the 60-second budget): closed tours on 3-by-10 and 5-by-6. Cited, not computed: Schwenk's theorem in general, Marateck's 8-by-8 failure counts.

## Nearest existing themes

Week 10 (bridges) asks for a walk using every road once (Euler), and this week asks for every square once (Hamilton); the contrast is worth naming in the guide, since one has a simple test and the other does not. Week 62 meets two-colourable networks; Week 8 uses a rook; the Week 41 return visit already asks for nine-cell tours that visit every room once on a portal board. New here: the knight graph, colouring as an obstruction to tours, a complete classification theorem (Schwenk) beside small boards where only search decides, and a greedy heuristic that usually but not always works.

## App connection

Maps and networks: a "knight tour" family where the child taps squares to jump and the board numbers the visits; puzzles ask for a tour of a given board, a tour starting from a marked square, "show this square cannot start a tour" (by trying, with undo), or a closed tour. The app can show the move graph as dots and lines after a tour is found.

## Open questions

- Whether K–1 children can execute the L-move reliably; the move card should be tested against a floor board's square size.
- Whether 3-by-4 is too easy or too hard for 2–3 as the main board; 3-by-7 may be a better second board than 4-by-4.
- How to present impossibility found by computer search honestly and still leave children feeling the search was worthwhile.
