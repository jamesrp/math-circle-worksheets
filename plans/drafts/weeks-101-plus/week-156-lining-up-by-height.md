# Week 156 (draft plan): Lining up by height

**Strand:** counting (Counting and arranging). **Deep-math field:** extremal combinatorics (Erdős–Szekeres theorem, pigeonhole), permutations, random permutations. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In any line of n² + 1 people of different heights, you can pick n + 1 of them, keeping their order in the line but skipping others, whose heights only go up or only go down (Erdős and Szekeres, 1935; more generally mn + 1 people give m + 1 going up or n + 1 going down). The bound is sharp: n descending blocks of n, with the blocks rising (for n = 3, heights 3 2 1 6 5 4 9 8 7), has no rising or falling run of n + 1. Two short proofs reach children. The labelling proof: give each person the pair (longest rising run ending with them, longest falling run ending with them); any two people get different pairs, because if the later one is taller they extend the earlier one's rising run, and if shorter they extend the falling run; with no run longer than n, only n × n pairs exist, so n² + 1 people is too many (pigeonhole). The card-pile proof: deal the line as patience sorting, putting each card on the leftmost pile whose top card is higher, or on a new pile; each pile is a falling run, and the number of piles equals the longest rising run (Aldous and Diaconis, Lemma 1), so n² + 1 cards give more than n piles or a pile of more than n. Checked by computer: every order of 5 has a run of 3 and exactly 4 orders of 4 avoid it; exactly 1764 = 42² orders of 9 avoid a run of 4 (the square of the number of ways to fill a 3-by-3 standard Young tableau, as the Robinson–Schensted correspondence predicts). For a random shuffle of n, the longest rising run is about 2√n for large n (Vershik and Kerov; Logan and Shepp), with fluctuations described by Baik, Deift and Johansson; for small lines it is well below 2√n (an exact average of 7601/2016 ≈ 3.77 for 8, against 5.66). Children can discover that 5 always force a run of 3, build the 9-person line with no run of 4, and in grades 4–5 follow one of the two proofs.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Erdős–Szekeres Theorem](https://wiki.artofproblemsolving.com/wiki/index.php/Erd%C5%91s%E2%80%93Szekeres_Theorem) — Art of Problem Solving wiki. The mn + 1 statement, the 1935 attribution and the labelling proof (whose key step, that two people's labels differ, the page leaves implicit) (read November 4, 2026).
- [Increasing or decreasing subsequence](https://www.cut-the-knot.org/pigeonhole/seq.shtml) — Alexander Bogomolny, Cut the Knot. A full pigeonhole proof with the case split for two people with equal labels; references to Proofs from THE BOOK and Gardner (read November 4, 2026).
- [Longest increasing subsequences: from patience sorting to the Baik-Deift-Johansson theorem](https://www.stat.berkeley.edu/~aldous/Papers/me86.pdf) — David Aldous and Persi Diaconis, Bulletin of the AMS 36 (1999), 413–432. Patience sorting, greedy piles equal the longest increasing subsequence, E[L_n] ~ 2√n, Ulam and Hammersley (read November 4, 2026).
- [The monotone sequence theorem: literature](https://blog.computationalcomplexity.org/2008/11/monotone-sequence-theorem-literature.html) — William Gasarch, Computational Complexity blog, November 14, 2008. History: Erdős and Szekeres 1935, rediscovery by the Kruskals, the labelling proof versus the original recurrence, and a card-pile proof in the comments (read November 4, 2026).
- Prior use with children: [Problem Set 18](https://sites.math.washington.edu/~mathcircle/circle/2013-14/advanced/mc-13a-h25.pdf) — UW Math Circle, advanced group, May 1, 2014: prove Erdős–Szekeres with Robinson–Schensted, and a two-player digit game where the loser is first to make a rising run of 4 or falling run of 3 (read November 4, 2026). Nothing for K–5 found in searches of NRICH and circle handouts for "increasing subsequence" and "line up by height".

## A kid-friendly way in

Children line up holding big number cards (or use a row of cups of different heights, or cards 1 to 10 on a table). "Pick some people, keep their order, and make them go up" is acted out by the picked people stepping forward. Then the patience game with a short deck of number cards 1 to 10 dealt into piles. Prep: print number cards 1 to 16 large, and small card sets 1 to 10 per pair; about 15 minutes. Launch (2–3 minutes): five volunteers stand in a muddled line; the room finds three who go up, stepping forward; then the room tries to rearrange the five so nobody can find three going up or three going down.

## By band

- **K–1:** with 4 and then 5 children or cups, find three going up or three going down; try to arrange so there are none. Four works (2 1 4 3), five never does.
- **2–3:** build the longest line of cards with no rising or falling run of 3, then of 4; play patience sorting and compare the number of piles with the longest rising run found by hand.
- **4–5:** prove that 5 always give a run of 3 using the label pairs (or the card piles); extend to 10 people and runs of 4; shuffle and record the longest rising run for many 8-card deals and compare with 3.77.

## Checked facts

Computed in `check_networks_counting_2.py`, `check_week_156()`:

- every order of 5 contains a rising or falling run of 3; the 4 orders of 4 avoiding it are 2143, 2413, 3142, 3412;
- 1764 = 42² orders of 9 avoid both a rising run of 4 and a falling run of 4 (runs may skip people); 3 2 1 6 5 4 9 8 7 is one; the hook length formula gives 42 tableaux of shape 3-by-3 and 2 of shape 2-by-2;
- label pairs are all different, in every order of 6;
- greedy patience piles equal the longest rising run for all 5040 orders of 7, and each pile is a falling run;
- 42 orders of 5 have no rising run of 3 (a Catalan number);
- average longest rising run over all orders of 8: 7601/2016 ≈ 3.77, against 2√8 ≈ 5.66.

Cited, not computed: the theorem for all n, the 2√n rate, Baik–Deift–Johansson.

## Nearest existing themes

The scouting draft patterns-you-cannot-avoid (Ramsey numbers) shares the theme "big enough forces a pattern" and the pigeonhole step; Erdős–Szekeres is a cousin and could be its return visit rather than a separate week. Week 19 (no card inside another) uses chains and antichains in a poset, and the theorem follows from the same ideas (people ordered by line position and height). Week 23 (sorting machines) and Week 90 (sliding number arrays, tableaux) touch the Robinson–Schensted world that explains the 42². New here: rising and falling runs in a line, a sharp threshold with an explicit extreme line, and the patience-sorting game as both an algorithm and a proof.

## App connection

Counting and arranging: a "line-up" family where the child drags characters into a line and the app highlights the longest rising and falling runs; puzzles ask for a line of 9 with no run of 4, or to find a run of 3 in a given line of 5. A patience-sorting mini-game deals cards and lets the child choose piles, scoring fewest piles.

## Open questions

- Whether "keep the order but skip people" is clear to K–1 without stepping forward; a pilot should check the acted version.
- Whether this should stand alone or merge with the Ramsey scouting draft as one theme with two visits.
- Whether 2–3 children can find a longest rising run reliably by hand in a line of 10, or need patience piles to check.
