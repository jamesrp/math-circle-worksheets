# Week 196 (draft plan): Ringing every order of the bells

**Strand:** symmetry (Patterns and symmetry). **Deep-math field:** group theory and graph theory (permutations, Hamiltonian cycles in Cayley graphs, cosets). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In English change ringing, n bells sound once each in some order (a row), and from one row to the next every bell may move at most one place, so a change is a set of swaps of neighbouring places that do not overlap (2 kinds of change on 3 bells, 4 on 4, 7 on 5). An extent rings all n! rows exactly once and returns to rounds (1 2 … n). Arthur White (Mathematical Proceedings of the Cambridge Philosophical Society, 1983) states the problem in modern terms: the rows are the elements of the symmetric group S_n, the allowed changes are generators, and an extent is a Hamiltonian cycle in the Cayley graph they make. An extent exists for every n, by a construction from 1668 that ringers call plain changes and computer scientists call the Steinhaus–Johnson–Trotter order: take an extent on n − 1 bells and let the biggest bell weave from one end to the other through each of its rows, one neighbour swap at a time. Every step is a single neighbour swap, so plain changes is a Hamiltonian cycle on the permutohedron (24 corners and 36 edges for 4 bells). The simplest method, plain hunt, alternates "swap every pair you can" with "swap the inner pairs"; it comes home after 2n changes having rung 2n different rows. On 3 bells that is all 6, so plain hunt is the extent; on 4 it rings only 8 of 24, and these 8 shapes form a group (the hunting group, dihedral of order 8, in Sarah Hart's Gresham lecture). Plain Bob Minimus (changes x 14 x 14 x 14 x 12, three times) rings all 24: each block of 8 rows (a lead) is its first row with the 8 hunting shapes applied, so the three leads are three cosets of the hunting group, and they cannot share a row. That is the group theory of methods: proving an extent "true" (no repeats) becomes checking that the lead heads lie in different cosets. A parity fact sits underneath: a single neighbour swap changes the number of out-of-order pairs by one, so with single swaps the rows alternate even and odd. Proved: all of the above. Counted here: 1 round trip through all 6 rows on 3 bells; 44 round trips through all 24 rows using single swaps only, and 5396 when all four kinds of change are allowed (each cycle counted once). Hard questions remain for particular methods on more bells: Hart notes that Stedman's question about an extent of Stedman Triples was settled only in 1994, and Knuth's April 2026 note describes a still unsuccessful computer search for a particular kind of peal of Erin Triples with bobs. Children can discover that three bells give six orders, that plain hunt rings them all, that the same dance on four bells comes home too soon, and a way to fix it.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Ringing the changes](https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/ringing-the-changes/80DB875677C4004FB7768D41C57C1D49). Arthur T. White, Mathematical Proceedings of the Cambridge Philosophical Society 94 (2), 1983, 203–215. Abstract page only: extents as Hamiltonian cycles in coloured Cayley graphs of the symmetric group, Plain Bob for any number of bells, all minimus methods (read November 4, 2026).
- [The Mathematics of Bell Ringing](https://www.gresham.ac.uk/sites/default/files/2021-01-05-1300_HART_Bells_P.pdf). Sarah Hart, Gresham College lecture slides (file dated January 2021). The rule that each bell moves at most one place, extents, Plain Bob Minimus, the hunting group of order 8 and its three cosets in S₄, and Stedman Triples solved in 1994 (read November 4, 2026).
- [Erin Triples With Bobs](https://cs.stanford.edu/people/knuth/papers/erin-bobs.pdf). Donald Knuth, note dated April 18, 2026 (revised April 22). Plain changes (1668) swaps two adjacent bells at each step; full peals are Hamiltonian cycles on the 5040 rows of 7 bells; an open search (read November 4, 2026).
- Prior use with children: [Ding Dong Bell](https://nrich.maths.org/node/55605). Toni Beardon, NRICH, February 2011, ages 11 to 18. Braid and network diagrams, the 24 rows of four bells, plain hunt returning early, Plain Bob as a Hamiltonian circuit (read November 4, 2026).
- Prior use (adults, physical format): [Experiencing Group Structure: Observing, Creating and Performing the Plain Hunt on 4](https://archive.bridgesmathart.org/2018/bridges2018-659.pdf). Susan Gerofsky, Eva Knoll, Avalon Campbell-Cousins and Tara Taylor, Bridges 2018 workshop. "Body ringing", in which people stand in a line and swap places, plus card swapping and handbells; no age range given (read November 4, 2026). No K–5 source was found (searched math circle, NRICH and Bridges pages for change ringing with children).

## A kid-friendly way in

Children are the bells. Three or four children stand on taped floor spots, each holding a number card (or a different shaker, cup or handbell, so a row can be heard). A legal change: neighbours trade places, and several pairs may trade at once. A scribe child lays the new row with small number cards on a long "ladder" strip, one row per rung, so the record is one recoverable list. Prep: tape spots, print four sets of number cards and ladder strips, about 15 minutes. Launch (2 to 3 minutes): three children on spots; show a legal trade (1 and 2), an illegal one (1 jumps over 2 to swap with 3), and that the goal is to make every different line-up exactly once and end where you started.

## By band

- **K–1:** three bells (children or toy animals on three spots). How many different line-ups are there? Make each one once, trading only neighbours, and come home. Lay each line-up as picture cards on the ladder. They find 6, and that alternating "front pair, back pair" does it. No reading.
- **2–3:** four bells. First try plain hunt (all pairs that can trade, then the middle pair, again and again): it comes home after 8 rows, not 24. Then the main problem: ring all 24 line-ups once each and come home. The table pools its rows on a wall chart of 24 printed row cards, turning each card over when it is rung, so repeats show at once.
- **4–5:** why there is always a way: build the 4-bell extent from the 3-bell one by letting bell 4 walk across each 3-bell row (plain changes), and say why it works for 5 bells too. Then Plain Bob Minimus as a code of changes: why does no row repeat? (Each lead is its first row with the same 8 plain-hunt moves applied, and the three first rows differ in a way the 8 moves never undo.) Parity extension: with single swaps only, why must the rows alternate between "even" and "odd" line-ups?

## Checked facts

Computed in `check_symmetry_number_3.py`, `check_week_196()`:

- 2, 4 and 7 kinds of change on 3, 4 and 5 bells;
- plain hunt returns after 2n changes with 2n different rows (n = 3 to 6); all 6 rows on 3 bells, 8 of 24 on 4 (listed), 10 of 120 on 5;
- Plain Bob Minimus rings 24 different rows and returns; each lead equals its first row with the 8 hunting shapes applied; bell 1 hunts through places 1, 2, 3, 4, 4, 3, 2, 1;
- the Steinhaus–Johnson–Trotter order lists all 6, 24 and 120 rows with one neighbour swap between consecutive rows, last to first included;
- the permutohedron of order 4 has 24 corners and 36 edges, and single swaps change parity;
- round trips through every row: exactly 1 on 3 bells; 44 on 4 bells with single swaps; 5396 with all four kinds of change.

Cited, not computed: White's Cayley-graph formulation, the hunting-group cosets as Hart presents them, the 1994 Stedman Triples result.

## Nearest existing themes

Week 3 (Shuffle machines) treats a permutation as a machine and finds its return time from its loops; its return visit already asks for the fewest neighbour swaps that sort a row (the inversion count) and finds that "rotate" and "reverse" reach only 8 of 24 orders of four cards (a different set of 8 from plain hunt's, also a dihedral group). Draft 117 (commutators) uses parity and generated groups; draft 103 (Hanoi maps and Gray codes) lists states changing one thing at a time, and plain changes is the permutation version of a Gray code; draft 105 (knight's tours) is the other Hamiltonian-cycle week. New here: visiting every arrangement exactly once, with several swaps allowed at once, and cosets used as a proof that nothing repeats. The overlap with the Week 3 return visit (neighbour swaps, parity) is real; this week asks for coverage, not sorting.

## App connection

Patterns and symmetry. A "Bell tower" family: a row of bells on the board, tap between two neighbours to mark a trade (several marks allowed), then ring; the ladder fills in and a repeated row flashes. Puzzles: "Ring all 6 rows of three bells and come home"; "This 4-bell ladder has 5 missing rows: fill them so every row appears once"; "Plain hunt came home after 8: change one rung so it continues". The Week 3 Cup swaps family already has permutation machinery to share. Sound is a bonus, not required.

## Open questions

- Can 2–3 children manage a 24-row extent physically, or should bodies do plain hunt and the extent move to cards on a table? Rehearse the floor version with four adults.
- Is the wall chart of 24 row cards the right recoverable record, or should children pool partial extents?
- Five bells (120 rows) is likely too long for one hour; decide whether it appears only in the guide.
- The coset explanation is the adult destination; check that a 4–5 child can follow "same 8 moves, different starting rows" without group language.
