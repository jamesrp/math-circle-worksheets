# Week 176 (draft plan): Hide and seek with unequal prizes

**Strand:** games (Games and choices). **Deep-math field:** game theory (zero-sum games, mixed strategies, the minimax theorem). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In a two-player zero-sum game with finitely many choices, where both choose secretly and at the same time, von Neumann's minimax theorem (1928, "Zur Theorie der Gesellschaftsspiele") says there is a number v, the value of the game, and a random mixture for each player such that the first player's mixture earns at least v on average against anything the second player does, and the second player's mixture holds the first to at most v against anything. The two mixtures together are a certificate: neither player can do better. Without randomness there is usually a gap. In "hide the bean", the seeker scores 1 for finding the bean under the red cup, 2 under the blue cup and 0 for a miss; the best any fixed choice guarantees the seeker is 0, and the best any fixed hiding place caps the seeker at 1, but with mixtures both meet at 2/3: the hider should use the cheaper red cup 2/3 of the time (a die, red on 1 to 4), and so should the seeker. In general, with prizes a and b, the hider uses the red cup with chance b/(a + b) and the value is ab/(a + b). The odds are exact and unequal, and they come from making the opponent's two options equally good, not from making one's own options equally likely. Two games look fair and are not. In the Princeton Friends School "Professor Swindle" game (two heads pay Louie 9, two tails pay 1, a mismatch pays the professor 5), both sides should play heads 3/10 of the time and the professor wins 4/5 of a cent per round; in odds-and-evens Morra (each shows 1 or 2 fingers and the total goes to Evens if even, to Odds if odd), both should show one finger 7/12 of the time (a 12-card deck with 7 "one" cards) and Odds wins 1/12 of a point per round, although fifty-fifty play by both gives exactly 0. The other half of the story is why randomness is needed: a predictable player can be exploited. At Bell Labs in the 1950s, Claude Shannon's "mind-reading machine" (a 1953 memorandum) and David Hagelbarger's SEER (described in 1956) played matching pennies against people and could predict an untrained player's heads and tails; against a hider who uses a die, no prediction rule does better than half. Proved: the minimax theorem and the formulas above. Checked here: every value, mixture and certificate quoted, and that each of the 16 rules that guess from the last two moves finds a die-driven bean exactly half the time. Observed, not proved: that people are predictable (the machines' records are reported, not reproduced here). Limits: the theorem is for zero-sum games; Week 135's trust game is not zero-sum and needs Nash's equilibrium instead.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Zur Theorie der Gesellschaftsspiele](https://historyofinformation.com/detail.php?id=601). Jeremy Norman's History of Information. Von Neumann's 1928 paper in *Mathematische Annalen* 100, 295–300, which "propounded the minimax theorem" (read November 4, 2026).
- [Blast it like Beckham?](https://plus.maths.org/blast-it-beckham). John Haigh, *Plus* magazine, September 2002. Penalty kicks as a zero-sum game: both sides should randomise with unequal odds (aim left 56.25%, dive left 68.75%), and a predictable shooter or an off-balance mix is punished (read November 4, 2026).
- [CS 6783 Lecture 1: A bit of fun](https://www.cs.cornell.edu/courses/cs6783/2025fa/lec1.pdf). Cornell machine learning theory course notes, fall 2025 (no author named on the page). Matching pennies as a prediction game; the Bell Labs "mind reader" machines could predict the heads and tails of an untrained human, Shannon's using only 8 states (read November 4, 2026).
- [On Hagelbarger's and Shannon's matching pennies playing machines](https://magazines.ulbsibiu.ro/ijasitels/index.php/IJASITELS/article/view/49). M. Breazu, D. Volovici, D. Morariu and R. G. Cretulescu, 2020. SEER (1956) and Shannon's mind-reading machine (Bell Labs memorandum, March 18, 1953), re-implemented and compared; the abstract does not give human win rates (read November 4, 2026).
- Prior use with children: [Two Games with Pennies](https://www.princetonfriendsschool.org/editoruploads/files/Problem%20of%20the%20Week/2006/Two%20Games%20with%20Pennies.pdf). Problem of the Week sheet dated October 30, 2006, on the Princeton Friends School site; level not stated, with an extension for algebra students. Students play Professor Swindle's matching game (9, 1, −5), decide whether it is fair, and graph the payoff lines (read November 4, 2026). The atlas family AP-22 is this repository's closest prior plan.

## A kid-friendly way in

Hide the bean. A pair has two upside-down cups (red and blue), one bean, a folder as a screen and a cube bank. The hider hides the bean behind the folder, the seeker points, and the cups are lifted: a find under red earns the seeker 1 cube, under blue 2 cubes, a miss nothing. After a few rounds the pair swaps roles, and each child keeps a "hiding record" strip of R and B stickers. Then the adult brings out a die and a 12-card deck as randomisers for children who want them. Prep: cups (two colours), beans, folders, cubes, dice, a 12-card deck per pair (7 cards marked 1 and 5 marked 2), sticker strips: about 15 minutes. Launch (2 to 3 minutes): two adults play five rounds where the hider always uses blue; the room sees the seeker catch on, and the question is "What should the hider do instead?"

## By band

- **K–1:** play hide the bean and swap roles; notice that always hiding in the same cup gets caught, and that the blue cup is the dangerous one. Count cubes after ten rounds. A die rule ("red on 1, 2, 3, 4") is offered as a way to keep the seeker guessing; children compare it with their own hiding.
- **2–3:** the question "How often should the hider use red?" Children try fixed recipes (always red; red and blue taking turns; a die with red on 1 to 3; red on 1 to 4) against a seeker who knows the recipe but not the next roll, and pool cube totals. Then the Professor Swindle game with counters: is it fair?
- **4–5:** explain why red 2/3 of the time is the hider's best recipe (make the seeker's two guesses equally good: 1 × red share = 2 × blue share) and why the seeker's matching recipe proves nobody can do better. Find the recipe for other prizes, then Morra: show that fifty-fifty looks fair, find the 7/12 deck, and explain who wins in the long run. A mind-reader round: an adult predicts each child's "random" hiding with a written rule based on the last two moves, then tries the same rule against a die.

## Checked facts

Computed in `check_games_3.py`, `check_week_176()`:

- hide the bean (1 and 2): mixtures 2/3 and 2/3, value 2/3, certificate checked; pure play guarantees only 0 and caps at 1; prizes 1 and 3 give 3/4; the formula b/(a + b) and ab/(a + b) for all prizes 1 to 6;
- Professor Swindle (9, 1, −5): both play heads 3/10, value −4/5 for Louie; fifty-fifty play by both gives 0; against the professor's 3/10 every Louie mix averages −4/5;
- Morra (2, −3, −3, 4 to Evens): both show one finger 7/12, value −1/12 for Evens; fifty-fifty gives 0; against Odds's 7/12 every Evens mix loses exactly 1/12;
- each of the 16 last-two-moves guessing rules finds a die-driven bean exactly half the time (all sequences of length 8), and "guess the opposite of last time" catches an alternating hider every time.

Cited, not computed: the minimax theorem, the penalty-kick numbers, the history of the machines and their success against people.

## Nearest existing themes

Atlas AP-22 is the closest: a secret-choice game with a bag of one U and two D slips whose value 2/3 is certified by both bags. Its numbers are exactly hide the bean's, so that game alone would duplicate it; this plan should be built as AP-22's week, not beside it. Week 24's return visit already has concealed deck choice with a uniform mixture as the unique best (a symmetric game), and the scouted "Hidden armies" (Colonel Blotto) shows that no plan is safe. Week 42 makes fair coins from bags; Week 135 is a non-zero-sum game; the "Who beat whom" scouting draft uses rock-paper-scissors only to decide games. New here: unequal exact odds as the answer, games that look fair and are not (Professor Swindle, Morra), the certificate as a proof, and the experiment that people are predictable while a die is not.

## App connection

Games and choices. A "Hide and seek" family: the child sets a hiding recipe (a spinner with adjustable red and blue slices) and plays 100 fast rounds against robot seekers, one of which learns patterns. Example puzzles: "Set a spinner that earns at least 2/3 against every seeker"; "This game looks fair. Find who wins in the long run and by how much"; "Beat the pattern robot by hand for 20 rounds, then with the spinner". Fit B: a simulator and a small exact solver for 2 × 2 games.

## Open questions

- Is AP-22 to be developed as this week, or does the library want only one of them? The Professor Swindle and Morra games would also fit an AP-22 return visit.
- Whether K–1 children can follow a die recipe without peeking at the seeker's habits; does the folder keep the hiding secret enough?
- Morra's 12-card deck needs reshuffling every round; is that practical, or should 4–5 use a 12-section spinner?
- A real mind-reader round needs a rule an adult can apply fast; draft and rehearse it.
