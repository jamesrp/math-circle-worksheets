# Week 152 (draft plan): Who is most important?

**Strand:** networks and chance (Maps and networks; Chance and machines). **Deep-math field:** Markov chains (stationary distributions, Perron–Frobenius), ranking. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A walker moves around a directed network: at each chair it picks one of the outgoing arrows at random and follows it. If every chair can reach every other (the network is strongly connected), there is exactly one way to share out one unit of "importance" so that each chair's share equals the sum of the shares sent to it, where each chair splits its share equally among its arrows; this is the stationary distribution, and by the ergodic theorem for Markov chains it is also the long-run fraction of time the walker spends at each chair, from any start. If the network also has loops of lengths with no common factor, the chance of being at each chair after many steps settles to the same numbers. Ranking chairs by this share is the idea of PageRank (Brin and Page, 1998): a page is important when important pages link to it, not merely when many pages do. Real webs are not strongly connected (dead ends, traps), so PageRank adds a jump: with probability about 0.15 the surfer leaves for a page chosen uniformly at random. The jump makes every entry of the transition matrix positive, and the Perron–Frobenius theorem then guarantees a unique positive ranking, which the power method (repeat the sharing step) finds. Checked here on Bryan and Leise's four-page web: the shares are 12/31, 4/31, 9/31, 6/31 (0.387, 0.129, 0.290, 0.194; with the 0.15 jump, 0.368, 0.142, 0.288, 0.202), and page 3, with the most incoming links, ranks only second because its single outgoing link gives all its weight to page 1. In the six-chair room used below, chair C has the most arrows in but chair A is visited most. Children can discover that counting arrows in is a decent guess but can be wrong, that a trap swallows the walker unless something lets it escape, and that long runs give stable fractions while short runs are noisy. The theorems are cited; the small numbers are computed.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The $25,000,000,000 Eigenvector: The Linear Algebra behind Google](https://npflueger.people.amherst.edu/272-18spring/BryanLeise.pdf) — Kurt Bryan and Tanya Leise, SIAM Review 48 (2006), 569–581. The sharing rule as an eigenvector, non-uniqueness for disconnected webs, the jump fix with m = 0.15, Perron–Frobenius, the four-page example and its scores (read November 4, 2026).
- [PageRank: Standing on the shoulders of giants](https://arxiv.org/pdf/1002.2858) — Massimo Franceschet, arXiv 1002.2858, about 2010. Brin and Page's 1998 score, the random surfer, damping 0.85 proposed by the inventors, uniqueness via Perron–Frobenius after teleportation (read November 4, 2026).
- Prior use with children: [Acting Like an Algorithm: Google PageRank Activity](https://www.teachengineering.org/activities/csm-2353-acting-algorithm-google-pagerank-activity) — TeachEngineering, grade 5 (4–6), about 30 minutes: groups stand for pages, a ball is thrown along yarn links chosen by a random draw, and pom-pom tallies are compared with PageRank (read November 4, 2026). Also [Teach Network Science to Teenagers](https://arxiv.org/pdf/1302.6567) — Heather A. Harrington, Mariano Beguerisse Díaz, M. Puck Rombach, Laura M. Keating, Mason A. Porter, about 2013: ages 13–16, "monkeys" clicking links at random, coin flips to choose edges, and a dead end that motivates teleportation (read November 4, 2026).

## A kid-friendly way in

Six chairs labelled A to F with string arrows on the floor between them: A to B and D; B to A and C; C to A; D to E and F; E to C; F to C. Every chair has one or two arrows, so a coin decides at a fork (each fork chair has a card saying which arrow is heads). One child walks; a partner puts a counter in the chair's cup at each visit. Prep: six labels, nine string arrows with tape, six cups, coin cards; about 15 minutes. Launch (2–3 minutes): before anyone walks, ask the room to vote on which chair will get the most visits; most will pick C (three arrows in). Demonstrate three steps with a coin.

## By band

- **K–1:** walk the room and drop counters; after the class has made many steps together, line up the cups and compare heights. Ask why E and F get so few.
- **2–3:** each pair walks 26 steps and records the visits; pool the class's tallies and compare with the vote; then change one arrow (make E and F point only at each other) and see the walker get trapped; add the die rule (on a 6, roll again and jump to that chair) and see the trap leak.
- **4–5:** find the exact long-run shares by sharing counters: start with 13 counters split 4, 2, 3, 2, 1, 1 and check that one round of "split your counters among your arrows" gives back the same numbers; explain why C's three arrows still leave it behind A. Compare with a rotor version (Week 91 cards), which hits the shares exactly every 13 steps.

## Checked facts

Computed in `check_networks_counting_2.py`, `check_week_152()`:

- Bryan–Leise web: 12/31, 4/31, 9/31, 6/31; with jump 0.15: 0.368, 0.142, 0.288, 0.202; page 3 has the most links in (3) and ranks second;
- six-chair room: arrows in 2, 1, 3, 1, 1, 1; long-run shares 4/13, 2/13, 3/13, 2/13, 1/13, 1/13, so 26 steps expect 8, 4, 6, 4, 2, 2; loops of length 2 and 3, so the walk does not alternate;
- with the die rule (jump with chance 1/6): 0.288, 0.148, 0.238, 0.148, 0.089, 0.089;
- trapped room (E and F point only at each other) with the die rule: E and F together hold 0.693 of the visits;
- rotor walk on the room, forks alternating and starting at A: every block of 13 steps gives exactly 4, 2, 3, 2, 1, 1.

Cited, not computed: Perron–Frobenius, the ergodic theorem, Brin and Page's damping value.

## Nearest existing themes

Week 91 (rotor routing) is the deterministic twin: here coins choose, there cards alternate, and the plan's rotor check shows the same shares appear. Week 20 (averaging) and atlas AP-01 study harmonic functions, a walk's chance of reaching a shore; this week asks a different question, where the walker spends its time in the long run, on a network with no shores. Week 131 (coupon collector) and Week 44 (urns) use repeated chance but not networks. New here: stationary distributions, ranking by them, and why a random jump is needed on real webs.

## App connection

Chance and machines, or Maps and networks: a "walker" family where the child builds or edits arrows among a few rooms, presses run, and watches visit bars grow; puzzles ask "add one arrow so that room D becomes most visited", "which room will win?" before running, or "build a trap". The rotor-routing family could share the board.

## Open questions

- How many steps a class needs before the cups clearly rank A first: 26 steps per pair is noisy, so pooling is essential; a pilot should count how many steps fit in ten minutes.
- Whether string on the floor survives walking; tape lines may be safer.
- Whether the counter-sharing check for grades 4–5 is clear without fractions, since 13 counters split evenly at every fork.
