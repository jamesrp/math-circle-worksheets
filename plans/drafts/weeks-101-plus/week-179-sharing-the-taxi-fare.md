# Week 179 (draft plan): Sharing the taxi fare

**Strand:** games (Games and choices). **Deep-math field:** cooperative game theory (the Shapley value, cost sharing, axioms). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Friends share one taxi along a road from school; the fare is set by the farthest stop. How should they split it? In 1953 Lloyd Shapley answered a general version for any cooperative game, where each group of players has a value (here, the fare the group would pay riding alone together): there is exactly one way to split the total that satisfies four conditions, now called efficiency (the shares add up to the whole fare), symmetry (two friends who change every group's fare in the same way pay the same), the null player rule (someone who never changes any fare pays nothing) and additivity (the shares for two separate costs add). That rule, the Shapley value, has a concrete description: line the players up in every possible order, let each newcomer pay the extra fare their arrival adds, and average over all orders. For the taxi, and for Littlechild and Owen's airport problem (1973; planes of different sizes sharing a runway built for the largest), the average has a still simpler form: cut the road at every stop and split each stretch equally among the riders still in the taxi. Friends at 3, 5 and 6 blocks pay 1, 2 and 3; at 6, 12 and 42 they pay 2, 5 and 35. For airport and taxi games the Shapley shares also lie in the core: no group of friends pays more in total than its own taxi would cost (a theorem for these concave games). Other natural rules break a condition: an equal split charges a friend who never rides (stop 0) a share, breaking the null player rule, and can charge a near neighbour more than their own ride (friends at 1, 5 and 6 splitting 6 equally pay 2 each, but a ride to 1 costs 1); paying in proportion to distance satisfies the core here but gives different shares (9/7, 15/7, 18/7 for 3, 5, 6); "the first one in pays for the first stretch" depends on an arbitrary order. Proved: Shapley's uniqueness theorem; the sequential rule equals the Shapley value for airport games (Littlechild and Owen); the core property for these games. Checked here: every share quoted, the 6-order average, the core checks and the failures of the alternatives. A choice, not a theorem: whether these four conditions are the right meaning of "fair" is for the children to argue about.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Shapley, Lloyd S.](https://www.informs.org/About-INFORMS/History-and-Traditions/Biographical-Profiles/Shapley-Lloyd-S.). INFORMS biographical profile. The 1953 Shapley value as a fair distribution of payoffs in n-person games, "a splendid example of the use of the axiom method"; the 1954 power-index paper with Shubik; the 2012 Nobel prize shared with Alvin Roth (read November 4, 2026).
- [The Shapley value for airport and irrigation games](https://mpra.ub.uni-muenchen.de/30031/1/MPRA_paper_30031.pdf). J. Márkus, M. Pintér and A. Radványi, MPRA Paper 30031, 2011. The airport cost game (cost of the largest plane in a coalition), Shapley's axiomatization on these games, Littlechild and Owen's (1973) result that the sequential equal contributions rule is the Shapley value, and that the Shapley value lies in the core (read November 4, 2026).
- [Fair Ride Allocation on a Line](https://arxiv.org/pdf/2007.08045). Y. Amano, A. Igarashi, Y. Kawase, K. Makino and H. Ono, arXiv 2007.08045. Taxis whose cost is the farthest drop-off, built on the airport game; the example of riders to 12, 24, 36 and 40 paying 3, 7, 13 and 17 (read November 4, 2026).
- [Chapter 16: Cooperative games](https://vknight.org/Year_3_game_theory_course/Content/Chapter_16_Cooperative_games/). Vincent Knight, third-year game theory course page. The taxi game with stand-alone costs 6, 12 and 42, the predecessor-set definition over orderings, the four properties with a unique payoff vector, and the split 2, 5, 35 (read November 4, 2026).
- Prior use with children: none found. Searched NRICH, JRMF and math circle pages for taxi-fare sharing, the airport problem and the Shapley value; only university course material turned up.

## A kid-friendly way in

The taxi strip. A paper road of 6 to 9 squares runs from school; each friend puts a house card on their stop, and a toy taxi drives out with everyone aboard. The fare is one cube per square driven, laid on the road as the taxi passes, so the fare is visibly the road to the farthest house. Children then decide who pays which cubes, first by arguing, then by testing their rule on new stops. A second game lines up the friends in arrival order: each new friend pays the extra cubes their stop adds. Prep: printed road strips, house cards, a toy car, 30 cubes per table, six arrival-order cards per table: about 15 minutes. Launch (2 to 3 minutes): an adult drives three friends to stops 3, 5 and 6, lays six cubes, and asks the room "Who should pay what?", collecting two or three different answers without judging them.

## By band

- **K–1:** stops 3, 5 and 6. Everyone rides the first 3 squares, so those 3 cubes are shared one each; two friends ride the next 2 squares, one cube each; the last friend pays the last cube alone. Children hand out cubes square by square and count what each paid (1, 2, 3). Then stops 6, 8, 9 (2, 3, 4).
- **2–3:** compare rules on several trips: equal split, pay by distance, "each stretch shared by its riders", and pay-as-you-arrive in one order. Which rules ever make someone pay more than their own taxi would cost? Which change if the friends line up differently? Discover that the stretch rule treats friends at the same stop equally and never overcharges.
- **4–5:** play all six arrival orders for three friends and average each friend's extra cubes; find that the average matches the stretch rule (the far friend pays 6, 6, 3, 1, 1, 1 in the six orders, averaging 3). Explain why with a picture of the road, then meet Shapley's four conditions and test which rules break which.

## Checked facts

Computed in `check_games_3.py`, `check_week_179()`:

- the Shapley value by all orders equals the stretch rule and adds to the fare for stops (3, 5, 6) → (1, 2, 3), (6, 8, 9) → (2, 3, 4), (6, 12, 42) → (2, 5, 35) and (12, 24, 36, 40) → (3, 7, 13, 17), each in the core;
- symmetry and the null player rule on stops (4, 4, 7, 0): 4/3, 4/3, 13/3 and 0; an equal split of stops (0, 3, 5, 6) charges the friend at 0 a share of 3/2;
- the far friend's arrival costs in the six orders for (3, 5, 6) are 1, 1, 1, 3, 6, 6, averaging 3;
- equal split for stops (1, 5, 6) charges 2 to a friend whose own ride costs 1, so it leaves the core; the Shapley shares there are 1/3, 7/3, 10/3;
- splitting by distance for (3, 5, 6) gives 9/7, 15/7, 18/7, in the core but not the Shapley shares; nearest-first arrival gives 3, 2, 1.

Cited, not computed: Shapley's uniqueness theorem, Littlechild and Owen's identification, and the core theorem for airport games.

## Nearest existing themes

Week 58 (fair division) splits goods by envy-freeness and proportionality, and Week 27 (stable pairings) is Gale and Shapley's matching, a different Shapley theorem. New here: cooperative games, where groups have values and the question is how to share a joint cost; the axiomatic method (state the fairness conditions, then prove only one rule meets them); averaging over all arrival orders; and the core. Week 180 (power indices) uses the same arrival-order average for voting, so the two weeks make a natural pair.

## App connection

Games and choices. A "Taxi fares" family: houses dragged onto a road, a taxi animation laying fare coins, and a splitter where the child assigns coins to riders; checks flag anyone paying more than their own ride or two neighbours treated differently. Example puzzles: "Split the fare so nobody pays more than riding alone"; "Find the stops where equal split is unfair"; "Average the six arrival orders". Fit A: exact arithmetic on small trips.

## Open questions

- K–1 shares of a stretch must divide evenly; choose stops so every stretch has as many cubes as riders (or a multiple), as in 3, 5, 6.
- Is "fair" a productive argument for 2–3, or does it stall? The guide needs a short script that turns opinions into testable rules.
- The additivity condition is abstract; decide whether 4–5 meet it at all or only the other three.
- A two-trip or round-trip story could make additivity concrete; untested.
