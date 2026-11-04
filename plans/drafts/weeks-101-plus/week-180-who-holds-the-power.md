# Week 180 (draft plan): Who holds the power?

**Strand:** games (Games and choices). **Deep-math field:** cooperative game theory and social choice (weighted voting, power indices). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In a weighted vote each voter holds some number of votes and a proposal passes when the yes votes reach a quota, written [quota: weights]. Votes are not power. A voter's power is measured by how often they can change the result. The Banzhaf index (reintroduced by John Banzhaf in 1965 to argue that weighted voting did not work) counts, over all winning groups, how often a voter is critical: the group wins with them and loses without them. The Shapley–Shubik index (1954) lines the voters up in every order and counts how often each voter is the pivot whose arrival first reaches the quota; it is the Shapley value of the voting game, so Week 179's arrival-order average reappears. Both indices give the same striking facts. A voter can hold votes and have no power at all (a dummy): in Nassau County's board [16: 9, 9, 7, 3, 1, 1] a proposal passes exactly when two of the three largest members agree, so the members with 3, 1 and 1 votes never change anything, and the member with 7 votes has exactly as much power as each member with 9. In the 1958 European Economic Community Council [12: 4, 4, 4, 2, 2, 1] Luxembourg's single vote was a dummy under both indices (Mayer 2018 argues that other rules and the Benelux alliance gave it influence anyway). Very unequal weights can mean equal power: in [51: 49, 48, 3] any two of the three win, so each has a third of the power. Moving the quota or one vote changes everything: with weights 3, 2, 1, 1 the 2-vote voter is no stronger than a 1-vote voter when the quota is 4 and exactly as strong as the 3-vote voter when it is 6; moving one vote from the largest voter to the second, [8: 5, 3, 1, 1, 1] to [8: 4, 4, 1, 1, 1], turns the three small voters into dummies. Within one vote, more weight never means less power (checked here for small cases; it holds in general because a heavier voter can replace a lighter one in any group). Proved: the definitions and the general facts above; that the Shapley–Shubik index is the Shapley value. Checked here: every count and index quoted, and for all four-voter weight lists from 1 to 4 and all majority quotas, that both indices agree on who is a dummy and that heavier voters are never weaker. A modelling choice, not a theorem: which index is "right" depends on what one assumes about how coalitions form, and the two can give different shares (for [4: 2, 1, 1, 1], Banzhaf gives 2/5 and 1/5 each, Shapley–Shubik 1/2 and 1/6 each).

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Researchers in voting](https://mathbooks.unl.edu/Contemporary/sec-10-1-researchers-voting.html). M. Homp, A. Seideman, S. Gravelle and A. Hayes, *Contemporary Mathematics*, University of Nebraska–Lincoln open text. Banzhaf's 1965 reintroduction of the power measure to show weighted voting did not work; the Nassau County system [16: 9, 9, 7, 3, 1, 1] (read November 4, 2026).
- [Luxembourg in the Early Days of the EEC: Null Player or Not?](https://www.mdpi.com/2073-4336/9/2/29). Alexander Mayer, *Games* 9(2), article 29, 2018. Weights 4, 4, 4, 2, 2, 1 out of 17 with quota 12; standard indices, Shapley–Shubik and Penrose–Banzhaf, give Luxembourg zero power; the paper's argument that it was not a null player in practice (read November 4, 2026).
- [Weighted voting](https://mathematics-democracy-institute.org/wp-content/uploads/2020/11/weighted-voting.pdf). Stanley Chang, Wellesley College, for the Institute of Mathematics and Democracy, November 3, 2020. Notation, critical voters, the Banzhaf index, and the 1958 EEC with Luxembourg as a dummy (read November 4, 2026).
- Prior use with children: [Power Indices](https://sites.google.com/wellesley.edu/math-politics-modules/power-indices). Math and Politics Teaching Modules, Wellesley College (R. Balachandran, A. Belluck, G. Brittingham, A. Smith), aligned to a grade 7 standard. Dictators and dummies ([10: 7, 6, 2]), Banzhaf by critical voters, Shapley–Shubik over 120 orders for [15: 9, 6, 3, 3, 3] (45%, 20%, 11.67% each), and a Banzhaf paradox comparing [8: 5, 3, 1, 1, 1] with [8: 4, 4, 1, 1, 1] (read November 4, 2026).

## A kid-friendly way in

The cube tower vote. Each child at a table holds a stack of cubes (their votes) and a yes/no card; a tape line on a wall card marks the quota height. A proposal ("the class pet is a frog") passes when the yes children's cubes, snapped into one tower, reach the line. The game is to find out who can change the result: make every possible team of yes voters, build its tower, and for each passing team ask, "If you left, would it still pass?" A child who is never needed gets a "never needed" sticker. Prep: snap cubes, yes/no cards, quota cards with lines at several heights, team-record sheets with names as pictures: about 15 minutes. Launch (2 to 3 minutes): three adults hold 4, 3 and 2 cubes with the line at 5; the room sees that any two adults' towers reach the line and no single tower does, and the question is "Who is most powerful?"

## By band

- **K–1:** three voters with 4, 3 and 2 cubes and the line at 5: build every pair's tower and find that any two win, so all three are equally needed although their stacks differ. Then the line at 6, where the 4-cube voter is needed every time. Spoken questions only; teams recorded with picture cards.
- **2–3:** four voters with 3, 2, 1 and 1 cubes; move the line from 4 to 7 and, for each line, count how often each voter is critical. Discover that the 2-cube voter can be as weak as a 1-cube voter (line 4) or as strong as the 3-cube voter (line 6), and that at line 7 everyone is equal. Then hunt for a voter with cubes and no power.
- **4–5:** the Nassau County board: show that the 3, 1 and 1 members are dummies and the 7 equals each 9, with an argument rather than a full list (every passing team contains two of the big three). Then the arrival-order index: line voters up in all orders and find the pivot, connecting to Week 179. Discuss the EEC and whether "zero power" in the formula is the whole story.

## Checked facts

Computed in `check_games_3.py`, `check_week_180()`:

- Nassau [16: 9, 9, 7, 3, 1, 1]: Banzhaf counts 16, 16, 16, 0, 0, 0 and Shapley–Shubik 1/3, 1/3, 1/3, 0, 0, 0;
- EEC 1958 [12: 4, 4, 4, 2, 2, 1]: Banzhaf counts 10, 10, 10, 6, 6, 0 and Shapley–Shubik 7/30, 7/30, 7/30, 3/20, 3/20, 0;
- [51: 49, 48, 3] and [5: 4, 3, 2]: equal power; [6: 4, 3, 2]: counts 3, 1, 1;
- weights 3, 2, 1, 1: quota 4 gives counts 6, 2, 2, 2 (Shapley–Shubik 1/2, 1/6, 1/6, 1/6); quota 5 gives 5, 3, 1, 1; quota 6 gives 3, 3, 1, 1 (5/12, 5/12, 1/12, 1/12); quota 7 gives 1, 1, 1, 1;
- [8: 5, 3, 1, 1, 1] counts 9, 7, 1, 1, 1 against [8: 4, 4, 1, 1, 1] counts 8, 8, 0, 0, 0; the Wellesley examples [10: 7, 6, 2] (counts 2, 2, 0) and [15: 9, 6, 3, 3, 3] (54/120, 24/120, 14/120 each);
- [4: 2, 1, 1, 1]: Banzhaf shares 2/5, 1/5, 1/5, 1/5 against Shapley–Shubik 1/2, 1/6, 1/6, 1/6;
- for all weight lists 1 to 4 with four voters and every quota above half, the two indices agree on dummies and heavier voters are never weaker.

Cited, not computed: the history (Banzhaf 1965, Shapley and Shubik 1954, the Nassau and EEC rules).

## Nearest existing themes

Week 87 (voting and agendas) is about majority cycles and agenda order with one vote each, a different question. Week 58 shares fairness language. The scouted "Locks and keys" (set aside) also asks which groups can act, through subsets. Week 179 (draft) supplies the arrival-order average. New here: weights against power, dummies, critical voters as the measure, and the surprise that the quota matters as much as the weights. Some care with framing: the real cases are political, so the pages should use class or club decisions and keep the history in the guide.

## App connection

Games and choices. A "Council" family: voters as stacks, a draggable quota line, and a team builder that lights up critical voters. Example puzzles: "Give these four voters weights so that one of them has votes but no power"; "Move the line so the smallest voter is as strong as the largest"; "Find weights for 3 voters so all have equal power but nobody has the same number of votes". Fit A: small exact enumeration.

## Open questions

- Listing all teams for four voters (15 nonempty teams) is bookkeeping-heavy for 2–3; a printed team chart with tick boxes may be needed.
- Whether K–1 grasps "needed" as "if you leave, it fails" through acting it out (one child steps away and the tower is rebuilt).
- Which index to teach first: the critical-voter count is more concrete, the arrival order links to Week 179; pilot one.
- Keep the Nassau story factual and brief; check the wording of any political example with James.
