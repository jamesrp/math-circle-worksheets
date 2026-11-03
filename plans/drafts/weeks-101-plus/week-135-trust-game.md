# Week 135 (draft plan): The trust game

**Strand:** games (Games and choices). **Deep-math field:** game theory (dominance, Nash equilibrium, repeated games). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In the prisoner's dilemma two players secretly choose "share" or "keep". With Axelrod's payoffs, both sharing earn 3 each, both keeping 1 each, and a keeper facing a sharer earns 5 while the sharer earns 0 (in general T > R > P > S, here 5 > 3 > 1 > 0). Whatever the other does, keeping earns more, so keeping dominates and (keep, keep) is the only equilibrium (no player gains by changing alone), although both players prefer (share, share): what is best for each is worse for both. Repetition changes this only when nobody knows which round is last. If the number of rounds is known, backward induction (keep in the last round, so keep in the one before, and so on) gives keeping in every round. If after each round the game continues with chance w, then "copycat" (tit for tat: share first, then copy the partner's last move) paired with copycat is an equilibrium once w is large enough; checking the two standard ways to exploit a copycat (keep forever, or alternate keep and share) gives the threshold w ≥ 2/3 for these payoffs, so a die that ends the game on a 6 (w = 5/6) is enough and a coin (w = 1/2) is not. Robert Axelrod's computer tournaments, which led to his 1981 *Science* paper with William Hamilton (the second tournament had over 60 entries), were won both times by tit for tat, the simplest entry. Two cautions are proved or checked, not opinions: tit for tat never outscores its partner in a single match (it trails by at most 5 = T − S), so it wins tournaments by doing well with everyone rather than by beating anyone; and no strategy is best in every field, since the winner depends on who else plays. Proved: dominance, the unique one-round equilibrium, backward induction for a known end. Checked here: the payoff facts, the threshold 2/3, the never-outscores fact for every partner up to 8 rounds, and two class-sized tournaments. Open in a sense: there is no single best strategy, and which one wins is an empirical question about the field.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Prisoner's Dilemma](https://plato.stanford.edu/entries/prisoner-dilemma/). Steven Kuhn, *Stanford Encyclopedia of Philosophy*, first published 1997, revised October 24, 2025. Dominance and the unique equilibrium, backward induction for a known number of rounds, continuation probability ("shadow of the future"), tit for tat as an equilibrium with itself when that shadow is large, Axelrod's tournaments, and that no strategy is best against every field (read November 3, 2026).
- [The Evolution of Cooperation: citation classic](https://websites.umich.edu/~axe/research/Software/CC/ECHome/ECCitationClassic.html). Robert Axelrod, University of Michigan. The two tournaments, tit for tat's wins, and the 1981 *Science* paper with William Hamilton (read November 3, 2026).
- [Repeated games](https://vknight.org/gt/2025/10/13/repeated-games.html). Course blog post, October 2025; the site's code credit names Vince Knight. A classroom tournament of student-written strategies, strategies as rules mapping history to moves (read November 3, 2026).
- Prior use with children: [Prisoner's Dilemma Math Circle Activity](https://maitiennn.github.io/Prisoner_s_Dilemma_Math_Circle_Activity.pdf). T. Truong, UF Math Circle, February 2025; level not stated. A sibling story, dominating strategy and Nash equilibrium, ten-round tables for always-silent and tit-for-tat (read November 3, 2026).

## A kid-friendly way in

The bean game. Each child has a green "share" card and a red "keep" card; partners choose behind their hands and reveal together; the bank pays in beans (3 and 3, 1 and 1, or 5 to the keeper and 0 to the sharer), shown on a picture chart. After each round a die is rolled and a 6 ends the game, so nobody knows the last round. Later, children choose or write a strategy on a card (always share, always keep, copycat, grudger, forgiving copycat, or their own rule) and adults run a class round robin with the cards. Prep: beans, two cards per child, payout chart, dice, strategy cards, about 20 minutes. Launch (2 to 3 minutes): two adults play three rounds in front of the class with the bank paying out beans, then ask "Which card would you play if you knew your partner will share?"

## By band

- **K–1:** play the bean game with a partner and count beans after each game. Then pick a picture strategy card (a smiling hand that always shares, a closed fist, a mirror for copycat) and watch two cards play each other with an adult moving beans. Questions are spoken: who got more, and did they both get a lot?
- **2–3:** one-round thinking: if your partner shares, which card earns more? If they keep? Discover that keeping is always better for you, yet two keepers end poorer than two sharers. Then repeated play with the die, and writing a strategy rule in one sentence.
- **4–5:** the class tournament: predict, then run, a round robin of written strategies over 10 rounds; explain why copycat can never beat its partner but can still top the table; change the field (add three always-keepers) and see the ranking change. Discuss what happens if everyone knows the game lasts exactly 10 rounds (round 10, then round 9, …), and why the die matters.

## Checked facts

Computed in `check_symmetry_games.py`, `check_week_135()`:

- keeping earns more against either card; (keep, keep) is the only pair where neither player gains by switching; 3 + 3 > 5 + 0, so steady sharing beats taking turns exploiting;
- copycat never scores more than its partner in a match, and trails by at most 5, for every partner sequence up to 8 rounds;
- a 10-round round robin (each pair once) of always share, always keep, copycat, grudger, forgiving copycat (keeps only after two keeps in a row) and keep-then-copy scores 117, 106, 124, 112, 125, 112: forgiving copycat wins by one point;
- in a field of three always-keepers, one copycat and one always-sharer, each keeper scores 84, copycat 57, always share 30;
- the continuation threshold max((T − R)/(T − P), (T − R)/(R − S)) is 2/3; copycat against copycat beats both deviations at w = 5/6, 3/4 and 2/3 and loses to one of them at 1/2 and 3/5.

Cited, not computed: backward induction for a known end, tit for tat being an equilibrium with itself, Axelrod's tournament results.

## Nearest existing themes

Atlas AP-23 (three travellers on two roads) already shows that a state where nobody wants to move alone need not be best for the group, which is the one-round lesson here; AP-22 is a zero-sum secret-choice game with a mixed-strategy value; the scouting draft "Hidden armies" is a zero-sum simultaneous game; Week 87 (voting) and Week 58 (fair division) are social-choice cousins. New here: a non-zero-sum game, dominance, and the way repetition with an unknown end makes cooperation stable, plus strategies written as rules and tested in a tournament. Honest overlap: the one-round dilemma alone would duplicate AP-23's moral; the repeated game and the tournament are what justify a week.

## App connection

Games and choices. A "Trust tournament" family: the child builds a strategy from blocks (first move; what to do after the partner shares; after the partner keeps) and runs it against a set of robot strategies. Example puzzles: "Build a rule that scores at least 25 against Copycat in 10 rounds"; "Build a rule that beats Always Keep's score in this field"; "Add one robot so that Copycat no longer wins". Fit B: a small rule builder and a simulator, with checks by replay.

## Open questions

- Social fit: some children take "keep" as betrayal; rotate partners, keep the stakes as beans returned to the bank, and say so in the launch.
- Is the die ending clear to K–1, or should K–1 play a fixed short game?
- The tournament by hand is slow; the guide needs a fast scoring sheet, or adults precompute pairings for the strategies children choose.
- Whether 4–5 can follow the backward-induction argument in conversation; it is a discretionary follow-up.
