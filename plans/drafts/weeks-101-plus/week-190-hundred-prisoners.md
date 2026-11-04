# Week 190 (draft plan): Follow the loop to find your card

**Strand:** logic (Codes and logic), with chance by counting. **Deep-math field:** permutation cycles, cooperative strategy, harmonic numbers. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The boxes problem (Anna Gál and Peter Bro Miltersen, 2003, with the solution credited to Sven Skyum; later popularised by Peter Winkler): 2n numbered boxes hide the cards 1 to 2n in a random order. Each of 2n players, alone and without leaving a trace, may open n boxes and must find their own card; the team wins only if everyone succeeds. Opening boxes at random, each player succeeds with chance 1/2 and the team with (1/2)^(2n), which for 100 players is about 8 × 10^−31. The loop strategy: open the box with your own number, then the box named by the card inside, and so on. Following arrows from box to card number splits any shuffle into loops (Week 3), and your card is the last one on the loop through your own box, so you succeed exactly when your loop has at most n boxes, and everyone succeeds exactly when the shuffle has no loop longer than n. Because at most one loop can be longer than half, the chance of failure is the sum over L = n + 1, …, 2n of the chance of a loop of length exactly L, which is 1/L. So the team wins with chance 1 − (1/(n + 1) + … + 1/(2n)) = 1 − (H_2n − H_n): 5/12 (about 42%) for 4 players, 23/60 (about 38%) for 6, about 35% for 10, and about 31.2% for 100. This chance falls as n grows but never below its limit 1 − ln 2 ≈ 30.7%. The strategy is optimal (Curtin and Warshauer, 2006; cited, not checked). If one helper may look in every box first and swap two cards, the team always wins, because one swap cuts a long loop into two loops of at most half (checked for 6 and 8 boxes). Proved: the loop criterion, the 1/L count, optimality. Children can discover that the strategy works for everyone exactly when no loop is too long, find loops in shuffled decks, and see why the players' fates are tied together: they all win or lose on the same few shuffles.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Prisoners and the Swap: Less than Half is Enough](https://arxiv.org/html/2407.07190v1) — Uri Mendlovic, arXiv 2407.07190, June 2024 (read November 4, 2026). Gál and Miltersen as the origin with Skyum's solution; all succeed if and only if no cycle is longer than 50; about 31%; optimality proved by Curtin and Warshauer (Mathematical Intelligencer, 2006); Winkler's simpler version.
- [100 prisoners problem](https://en.wikipedia.org/wiki/100_prisoners_problem) — Wikipedia, secondary pointer (read November 4, 2026). The formula 1 − (H_2n − H_n) ≈ 0.3118 for 100, the monotone decrease to 1 − ln 2 ≈ 0.30685, random choice (1/2)^100, the swap variant.
- [100 prisoners](https://datagenetics.com/blog/december42014/index.html) — Nick Berry, DataGenetics, December 2014 (read November 4, 2026). A general-audience explanation: about 31.18%, a loop of length L appears with chance 1/L.
- Prior use with children: [The Prisoner Problem](https://think-maths.co.uk/resources/prisoner-problem/) — Think Maths, Key Stages 3 to 5 (read November 4, 2026): a 4-prisoner, 4-card version where students test arrangements or use cycles and find a 42% survival chance against 1 in 16 at random. No K–5 use was found (searched "prisoners boxes cycles classroom activity cards").

## A kid-friendly way in

A cup row. Ten paper cups numbered 1 to 10 face down on a strip, a card numbered 1 to 10 under each, dealt from a shuffled deck. "Follow the loop": lift cup 3, read its card (say 7), lift cup 7, and so on until you find the card 3. Children then colour each loop on a recording strip (all cups of one loop get one colour sticker) and write down the loop lengths. The game: a team of 4 with 4 cups, each may lift 2 cups, everyone must find their own card. Play many shuffles with random lifting, then with the loop rule, and tally team wins on a class chart. Prep: number cups and cards for 4- and 10-cup kits per table and print loop strips; about 20 minutes. Launch (3 minutes): with 6 large cups on the floor, the room follows one loop together, then a child guesses how many cups the next loop will have.

## By band

- **K–1:** Follow loops in a 4- or 6-cup row and put one colour of sticker on each loop. How many loops? Which is longest? Play the 4-player team game with the loop rule and tally wins with cubes. No reading.
- **2–3:** Shuffle 10 cups many times and record the longest loop each time. How often is no loop longer than 5? Then explain why "every player finds their card" is the same as "no loop is longer than 5", and why random lifting almost never wins for a team.
- **4–5:** Count exactly with 4 cups: list the 24 orders by loop pattern (1 that moves nothing, 6 single swaps, 3 double swaps, 8 loops of 3, 6 loops of 4) and find that 10 of 24 win. Why can only one loop be longer than half? A helper who peeks and swaps two cards: show that one swap always saves the team.

## Checked facts

All in `check_logic_3.py`, function `check_week_190()`:
- Brute force over all orders agrees with 1 − (H_2n − H_n) for 4, 6 and 8 boxes; 5/12 for 4, 23/60 for 6, 0.354 for 10, 0.3118 for 100; the chance falls with n and stays above 1 − ln 2 ≈ 0.30685.
- The loop patterns of the 24 orders of 4: 1, 6, 3, 8, 6.
- A loop of exact length L > n appears in a 2n-shuffle with chance 1/L (checked for 6 boxes).
- Random lifting: 1/16 for 4 players; (1/2)^100 is between 7 × 10^−31 and 8 × 10^−31.
- One swap always removes every loop longer than half (6 and 8 boxes).
- Cited, not computed: optimality of the loop strategy (Curtin and Warshauer, via Mendlovic).

## Nearest existing themes

Week 3 (Shuffle machines) is the base: arrow loops of a permutation and loop names. This week reuses that skill and adds a new question, how long the loops of a random shuffle are, and a strategy that turns loops into a team win. Week 63 (Cards away from home) counts orders with no fixed point, a different loop statistic, and Week 43 (Shuffling picture cards) asks whether a shuffle is fair; here the shuffle is assumed fair. Week 131 (draft, Collecting every sticker) also meets harmonic numbers. The topic-scouting README set this aside as "chance, which has reserves". The answer: the plan is not a chance week. Its mathematics is a cooperative strategy and a permutation fact (everyone succeeds exactly when no loop is longer than half), and its probability is a count of orders by loop pattern, done exactly at 4 cups and observed at 10, so it belongs in Codes and logic and leans on Week 3 rather than on the chance reserves.

## App connection

Codes and logic region, or a loop puzzle in Week 3's "Shuffle machines in Cup swaps" family: a row of face-down cups; tapping a cup reveals its card and draws an arrow to the next cup. Puzzles: "Colour every loop of this shuffle"; "Find a shuffle of 6 where every player wins with 3 lifts"; "Swap two cards so no loop is longer than 4"; a "team run" button that plays 100 random shuffles and counts wins, so children see about 4 in 10 for 4 cups and about 1 in 3 for 10.

## Open questions

- Does the team game make sense to K–1 children if the "everyone must succeed" rule feels unfair? A cooperative framing (all find their card to open a treasure box) may help.
- Hiding the cards fairly between players at a table: an adult resets cups after each player, which slows play; test whether 4 cups keep it quick.
- The 4–5 count of the 24 orders needs the loop-pattern idea from Week 3; schedule after Week 3.
- The prisoners framing of published sources is not suitable for children; keep "players and cups".
