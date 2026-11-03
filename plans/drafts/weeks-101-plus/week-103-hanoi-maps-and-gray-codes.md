# Week 103 (draft plan): Tower maps and one-switch codes

**Strand:** counting (Counting and arranging), with a networks view (Maps and networks). **Deep-math field:** combinatorics, graph theory (state graphs, Hamiltonian paths), binary and ternary codes. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In the Tower of Hanoi (three pegs, n discs, never a larger disc on a smaller) the fewest moves from one peg to another is 2^n − 1 (1, 3, 7, 15, 31), proved by noticing that the largest disc must move at least once, and before it does the other n − 1 discs must all sit on the third peg. In the optimal solution the disc moved at step k is one more than the number of times 2 divides k, the ruler sequence 1, 2, 1, 3, 1, 2, 1, 4, …, and this is exactly the bit that changes at step k of the binary reflected Gray code (000, 001, 011, 010, 110, 111, 101, 100), which lists all 2^n binary words changing one digit at a time. The smallest disc moves on every odd-numbered move and always the same way round the pegs. The fresh angle for this circle is the state map: draw every legal arrangement as a dot and join two dots when one move changes one into the other. With three pegs there are 3^n arrangements and 3(3^n − 1)/2 moves between them (9 and 12 for two discs, 27 and 39 for three); the three "all on one peg" arrangements are corners with two neighbours, every other arrangement has three, and the map is the Sierpiński graph, a triangle of three copies of the previous map joined by single moves of the largest disc (Klavžar and Milutinović; see the Hinz–Klavžar–Zemljič survey). The shortest route corner to corner along one side has 2^n − 1 steps. A second fresh angle: if discs may move only between neighbouring pegs (left–middle or middle–right, never left to right directly), moving the tower from left to right takes 3^n − 1 moves (2, 8, 26, 80), and since there are only 3^n arrangements the route passes through every one exactly once, a Hamiltonian path that amounts to a ternary Gray code. All of these are proved; the code and map facts are also checked here by computer for small n. Children can find the move counts, the 1, 2, 1, 3 pattern, the triangle shape of the two-disc map, and the "every arrangement" property of the neighbour-pegs puzzle.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [A001511: the ruler function](https://oeis.org/A001511) — OEIS. Terms 1, 2, 1, 3, 1, 2, 1, 4, …; comments by Andreas Hinz (disc moved at step n of the optimal Hanoi solution) and Adam Kertesz (bit flipped in the binary reflected Gray code) (read November 3, 2026).
- [A survey and classification of Sierpiński-type graphs](https://users.fmf.uni-lj.si/klavzar/preprints/Ssurveyrevised.pdf) — Andreas M. Hinz, Sandi Klavžar, Sara Sabrina Zemljič, preprint dated 2016. The three-peg Hanoi graph is isomorphic to the Sierpiński graph, 3^n states; for two symbols the Gray code gives the path isomorphism (read November 3, 2026).
- [Tower of Hanoi, the Hard Way](https://www.cut-the-knot.org/recurrence/LongHanoi.shtml) — Alexander Bogomolny, cut-the-knot, after an observation of Kai Birger Nielsen. The longest non-repeating solution, T(n) = 3T(n − 1) + 2, so 3^n − 1 moves, every move through the middle peg (read November 3, 2026).
- Prior use with children: [Tower of Hanoi](https://nrich.maths.org/problems/tower-hanoi) — NRICH, ages 11 to 14. Fewest moves for 1 to 4 discs, the pattern when a disc is added, the general rule and the 64-disc legend (read November 3, 2026).

## A kid-friendly way in

The scouting list set Hanoi aside because it is widely met at home and school and its K–1 core is brief. This plan answers both points by making the map, not the move count, the object. Materials: three nesting cups or three sizes of block per pair; a set of nine picture cards showing every two-disc arrangement; floor tape or a large sheet for the class map; three paper "lamp" switches (cards with ON/OFF sides). Prep: print the nine cards and a 27-card set for older tables, about 20 minutes. Launch (2–3 minutes): with two cups on a three-spot mat, a child makes one legal move and the class finds the picture card for the new arrangement; place the two cards side by side and draw a line between them.

## By band

- **K–1:** move two cups and lay the nine cards on the floor, joining cards one move apart with tape; walk the map from "both on the left" to "both on the right" and count steps (3). Then the neighbour-pegs rule (no jumping from the left spot straight to the right spot): walk it again (8 steps, visiting every card).
- **2–3:** solve three discs (7 moves) and record which disc moves each time; build the 27-card map as a class; find the three corners and why they have only two neighbours; solve three discs with the neighbour-pegs rule and count (26), and check the route used every card.
- **4–5:** prove 2^n − 1 is the fewest; match the disc-move list 1, 2, 1, 3, 1, 2, 1 with three lamp switches that must show all eight patterns changing one switch at a time; explain why the map is three copies of the smaller map; explain why the neighbour-pegs puzzle needs 3^n − 1.

## Checked facts

Computed in `check_counting_networks.py`, `check_week_103()`:

- 2^n − 1 moves and the ruler sequence for n ≤ 6; Gray code words and changed bits equal the ruler sequence; the 3-bit list 000, 001, 011, 010, 110, 111, 101, 100;
- the smallest disc moves 2^(n−1) times, always the same way round;
- state maps for n ≤ 5: 3^n states, 3(3^n − 1)/2 moves, three corners of degree 2, others degree 3, corner-to-corner distance 2^n − 1;
- neighbour-pegs version: 3^n − 1 moves from left to right, reaching all 3^n states; two discs: 9 states, 3 moves, 8 moves with neighbour pegs.

Cited, not computed: the isomorphism with Sierpiński graphs for all n.

## Nearest existing themes

Week 2 (lamp lab) toggles lamps but by pressing lines, with linear algebra over two elements; Week 46 measures Hamming distance between boards; Week 30's balanced ternary uses powers of 3; Week 54 hides binary uniqueness in partitions; the Week 41 return visit asks for visit-once tours. The scouting README's "first reserve for counting" note is the honest overlap: the move count alone is familiar. New here: the state map as a Sierpiński graph, a visit-every-state route (the neighbour-pegs puzzle), and the link between disc moves and a one-switch-at-a-time code. The 3^n count meets Week 101's 3^k odd entries.

## App connection

Counting and arranging (or Maps and networks): a "tower map" family where the child moves discs and the map lights up the current dot; puzzles ask "reach the far corner in the fewest moves", "visit every dot with neighbour pegs only", or "which disc moves on move 12?". A Codes and logic puzzle: light all eight lamp patterns flipping one switch at a time.

## Open questions

- Whether K–1 children can match a physical cup arrangement to its picture card quickly enough for a nine-card map; the cards need very clear peg positions.
- Whether the 27-card map fits on a classroom floor and stays legible; a printed map to colour might be better for 2–3.
- How much of the 4–5 Gray-code link to put on the page versus leaving it to the facilitator.
