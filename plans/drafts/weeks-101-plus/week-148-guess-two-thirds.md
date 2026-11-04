# Week 148 (draft plan): Guess two-thirds of the average

**Strand:** games (Games and choices). **Deep-math field:** game theory, equilibria, iterated dominance. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Everyone secretly writes a number from 0 to 100; the winner is whoever is closest to two-thirds of the average. Two-thirds of an average of numbers up to 100 is at most 66.7, so a guess above 66.7 is never better and sometimes worse than 66.7 itself; cross those out. If everyone knows that everyone crosses them out, the average is at most 66.7 and the target at most 44.4; then 29.6, 19.8, and so on, shrinking by two-thirds each round (below 1 after 12 rounds). This iterated elimination leaves only 0, and everyone choosing 0 is the game's only Nash equilibrium for real-number guesses: an equilibrium is a choice for each player such that nobody gains by changing alone. With whole numbers, everyone choosing 0 is an equilibrium for any group, everyone choosing 1 is also one exactly when there are at least 4 players, and no other "everyone picks the same" choice is (checked here for groups of 2 to 15). The equilibrium assumes more than rationality: it needs everyone to know that everyone is rational, that everyone knows that, and so on (common knowledge). Real groups do not play 0. Rosemarie Nagel's experiments (American Economic Review, 1995; groups of 15 to 18, four rounds) had a first-round mean of 36.73 for p = 2/3 (target 24.49), with clusters near 33 and 22, read as one or two steps of reasoning from 50 (50 × 2/3 and 50 × (2/3)²); medians fell every round, for example 33, 29, 14, 10 in one session. Richard Thaler's 1997 Financial Times contest had a target of 12.61 and a winning entry of 13; a 2009 ChessBase contest with over 6,000 chess players averaged 32.2 (target 21.48); a Danish newspaper contest in 2005 with 19,196 entries averaged 33. Schoolchildren aged 9 to 11 (Hermes and Schunk, 114 children) reasoned about as deeply as adults, and perspective-taking predicted success. So the winning number depends on what the group believes about itself, and the equilibrium describes a limit that is reached only with repetition. Proved: dominance, the unique equilibrium for real numbers. Checked: the levels, the bounds and the whole-number equilibria. Observed, not proved: the experimental numbers. Children can discover that guesses fall round after round, explain why 67 or more is never wise, and argue about whether 0 is "right" when nobody else plays it.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Unraveling in Guessing Games: An Experimental Study](https://extranet.parisschoolofeconomics.eu/docs/guesnerie-roger/nagel95.pdf) — Rosemarie Nagel, American Economic Review 85(5), 1995 (read November 4, 2026). The game with p = 1/2, 2/3, 4/3; 15 to 18 subjects for four rounds; first-round mean 36.73 for p = 2/3; iterated best replies from 50; medians decreasing in every session with p < 1 (33, 29, 14, 10 in Session 4).
- [6000 chess players took part in our beauty contest](https://en.chessbase.com/post/6000-che-players-took-part-in-our-beauty-contest) — ChessBase with Christoph Bühren and Björn Frank, July 29, 2009 (read November 4, 2026). Average 32.215, target 21.48; Thaler's Financial Times contest of June 16, 1997 with target 12.61; Nagel's first-round target 24.49.
- [Keynes was right about markets – they are crazy](https://www.thenationalnews.com/business/keynes-was-right-about-markets-they-are-crazy-1.201592) — excerpt from Richard H. Thaler, *Misbehaving*, The National, 2016 (read November 4, 2026). The 1997 FT replication of Nagel's game; winning guess 13.
- [Guess 2/3 of the average](https://en.wikipedia.org/wiki/Guess_2/3_of_the_average) — Wikipedia, secondary pointer (read November 4, 2026). Ledoux's 1981 origin, the Politiken contest (19,196 entries, average 33), iterated elimination, the equilibrium at 0, and the whole-number case.
- Prior use with children: [If You Could Read My Mind: An Experimental Beauty-Contest Game with Children](https://swopec.hhs.se/nhheco/abs/nhheco2019_023.htm) — Henning Hermes and Daniel Schunk, NHH discussion paper 23/2019 (read November 4, 2026). 114 children aged 9 to 11; reasoning depth and learning comparable to adults; perspective-taking linked to success. No math-circle handout was found (searched "beauty contest game children experiment guess two-thirds average").

## A kid-friendly way in

Play it as a class, round after round, with small whiteboards. For K–1 the numbers are towers: each child secretly builds a tower of 0 to 10 cubes behind a folder; the towers are pooled and shared out equally (levelling them finds the average), the target is half a levelled tower, and the closest tower wins a point. For 2–3 and 4–5, whiteboards with 0 to 100, target two-thirds of the average, worked by an adult with a calculator and written on a class chart round by round. Prep: folders, cubes, whiteboards, a chart with rows for rounds; about 10 minutes. Launch (2 minutes): play one practice round with three volunteers using towers 2, 4 and 9 (they level to 5 each; half of 5 is between 2 and 3), so the room sees the levelling, the target and the winner, then everyone plays.

## By band

- **K–1:** Tower rounds with target "half of the level". Notice that the winning tower gets shorter each round; ask what tower you would build if everyone built 10. No reading.
- **2–3:** Three to five rounds of the 0–100 game; chart the average, target and winner. Then: is there a number that can never win? Why would anyone guess under 50?
- **4–5:** The crossing-out argument (66.7, 44.4, 29.6, ...) as a staircase picture, why it ends at 0, and the twist that 1 also works for whole numbers in groups of 4 or more. Discuss: if 0 is the "answer", why does it lose in real classes? Compare with published contests.

## Checked facts

All in `check_logic_games_2.py`, function `check_week_148()`:
- Reasoning levels from 50: 33.3, 22.2, 14.8, 9.9.
- Bounds after crossing out: 66.7, 44.4, 29.6, 19.8; 100 × (2/3)^11 > 1 > 100 × (2/3)^12.
- Nagel's mean 36.73 gives target 24.49; ChessBase's 32.215 gives 21.48; Thaler's target 12.61 means an average near 18.9.
- Whole numbers 0 to 100, groups of 2 to 15: all-0 is always an equilibrium; all-1 exactly when the group has 4 or more players; all-2, all-10, all-50 and others are not.
- Towers 0 to 10, target half the level: all-0 is the only all-the-same equilibrium for groups of 2 to 11.
- Practice round: towers 2, 4, 9 level to 5; half is 5/2; the tower of 2 wins alone.
- Cited, not computed: the experimental and contest figures above.

## Nearest existing themes

Week 84 (Public knowledge) is about what everyone knows that everyone knows; here common knowledge of rationality is what the equilibrium needs, and experiments show where it breaks. Draft 135 (Trust game) has a dominant choice and one equilibrium in one round; draft 136 (auctions) has truthful bidding as a best strategy; atlas AP-23 has travellers settling where nobody gains by switching. Week 20 (Averaging) and Week 87 (Voting) touch averages and group choices. New: iterated elimination of dominated choices, levels of reasoning, and the gap between equilibrium and play, studied with the class's own data.

## App connection

Games and choices region, possible family "Two-thirds town": the child picks a number against a crowd of app characters whose reasoning levels are visible (a level-0 guesser picks at random, a level-1 guesser plays 33, and so on); the target and winner appear after each round. Puzzles: "Against two level-1 players, what wins?"; "Which numbers can never win?"; "Five rounds against learners: how low does it go?". The app makes the levels explicit without a class.

## Open questions

- Fairness and feelings: a class game with one winner per round can upset younger children; points for "within 5 of the target" may help.
- Whether K–1 can follow levelling as an average; rehearse the share-out with 6 towers.
- How many rounds keep 2–3 engaged before guesses settle.
- Whether the plan should state the Nash equilibrium definition to 4–5 at all, or only "nobody wants to change alone".
