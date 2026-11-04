# Week 178 (draft plan): Bidding for turns

**Strand:** games (Games and choices). **Deep-math field:** combinatorial game theory (Richman games, bidding games, random-turn games). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Take any two-player game where players move a token toward winning positions, but instead of taking turns, both secretly bid chips for the right to move; the higher bidder pays their bid to the other player and moves. Lazarus, Loeb, Propp and Ullman ("Richman games", 1995) proved that for games on finite graphs with real-number bids and the winner paying the loser, each position v has a critical share R(v), the Richman cost: a player holding more than that share of all the money wins with best play, and a player holding less loses. R satisfies a simple averaging rule: R(v) is the average of the best next position for one player and the best next position for the other. The surprise is Richman's theorem, in their Section 3: R(v) equals the probability that the opponent wins the random-turn version of the same game, where a fair coin decides who moves each time. So money and luck are exchangeable: on a race where you need 1 step and your opponent needs 3, you win the coin-flip race 7/8 of the time, and you need only 1/8 of the money to win the bidding race for sure. In tic-tac-toe with bidding, where the bid winner places their own mark and a draw counts as a loss for X, X needs a share of 133/256, a little over half. Real chips are whole numbers. Develin and Payne ("Discrete bidding games", 2010) add a tie-breaking advantage (here a star) whose holder may take a tied bid, passing the star, or give it away and keep the star; in every race checked here each position is then won by exactly one player, and as chip totals grow the discrete game behaves more and more like Richman's (their Theorems 3.10 and 3.12; some convergence questions remain open, their Problems 3.15 and 3.16). On a two-step race with 5 chips each, the star decides: its holder wins. Proved: the threshold theorem, the averaging rule and R = 1 − P for finite game graphs, and Develin and Payne's convergence results. Checked here: R = 1 − P on every race up to 5 steps each, the tic-tac-toe value 133/256, and the discrete race results quoted below. Open: the convergence questions above; for large games such as bidding Hex, practical play relies on heuristics (Payne and Robeva's program estimates cell importance by random filling, as the Berkeley handout describes).

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Richman games](https://arxiv.org/abs/math/9502222). A. J. Lazarus, D. E. Loeb, J. G. Propp and D. Ullman, arXiv math/9502222, 1995. Abstract; the full text (read at [ar5iv](https://ar5iv.arxiv.org/html/math/9502222)) gives the definition R(v) = (R⁺(v) + R⁻(v))/2, the critical ratio theorem, coin-toss tie-breaking, and Section 3's result that R(v) is the probability of winning the coin-toss game (read November 4, 2026).
- [Discrete bidding games](https://ar5iv.arxiv.org/html/0801.0579). Mike Develin and Sam Payne, arXiv 0801.0579 (accepted 2010). Whole-chip bidding with the tie-breaking advantage, a sample bidding tic-tac-toe game with four chips each, the Richman threshold 133/256 for tic-tac-toe, and convergence to Richman's theory for large chip totals (read November 4, 2026).
- Prior use with students: [Bidding Games](https://mathcircle.berkeley.edu/sites/default/files/archivedocs/2014_2015/lectures/1415lecturespdf/Adv%20-%202015.01.27.pdf). Aaron Kleinman, Berkeley Math Circle advanced session, January 27, 2015 (date from the file name). Bidding tic-tac-toe as the opening example, Richman cost functions, R(v) = 1 − P(v) for random-turn games, random-turn and bidding Hex (read November 4, 2026). This is a high-school-level circle; no K–5 use was found (searched NRICH, JRMF and circle handouts for bidding tic-tac-toe and bidding races).

## A kid-friendly way in

The flag race. Each player has a pawn on their own short track (2 or 3 squares to a flag) and a pile of chips. Every turn both players hide some of their chips in a fist (zero is allowed), open together, and the bigger fist pays its chips to the other player and steps one square. Equal fists: the player holding the star chooses either to step (paying their chips and handing over the star) or to let the other step (and be paid). First to the flag wins. Later, the same bidding runs tic-tac-toe: the bid winner places their own mark. Prep: printed tracks, pawns, 20 chips per pair (beans or counters), a star token, a coin for a random-turn round, tic-tac-toe grids: about 15 minutes. Launch (2 to 3 minutes): two adults play one race with 5 chips each on 2-square tracks, showing a hidden bid, a payment, a step and one tie with the star; then the room plays.

## By band

- **K–1:** the flag race on 2-square tracks with 5 chips each, then with unequal tracks (1 square against 3). Questions are spoken: who won, how many chips did you pay, would you rather have more chips or a shorter track? Children notice that spending everything early hands the chips to the opponent.
- **2–3:** the question "With 2 squares each and 10 chips between us, how many chips do I need to be sure to win?" Explore splits (4 and 6, 5 and 5 with or without the star) and find that 5 chips with the star wins and 5 without loses. Then bidding tic-tac-toe with 4 chips each, as in Develin and Payne's sample game.
- **4–5:** compare money with luck. Play the coin-flip race (heads: you step) and find its winning chances by working back from the flags (1 against 3 squares: 7/8). Then the deeper question: the share of chips you need to be sure to win the bidding race is the opponent's coin-flip chance, 1/8. Explain the averaging rule on the race grid and test it with real chips (1 square against 3 with 10 chips: 1 chip is enough).

## Checked facts

Computed in `check_games_3.py`, `check_week_178()`:

- on every race with up to 5 steps each, Richman share = 1 − coin-flip chance; one step against 1, 2, 3, 4 steps needs 1/2, 1/4, 1/8, 1/16; 2 against 3 needs 5/16; equal races need 1/2;
- bidding tic-tac-toe (draws count as a loss for X) needs 133/256;
- whole chips with the star (10 chips in all): in the 2-against-2 race, 5 chips win with the star and 6 are needed without; with 8 chips in all and 3 squares each, 4 chips win only with the star; 1 against 3 squares: 1 chip wins, with or without the star; 2 against 3 squares: 3 chips (Richman's 5/16 of 10 is 3.125);
- every race position with 6, 8 or 10 chips and up to 3 squares each is won by exactly one player.

Cited, not computed: the general theorems of both papers.

## Nearest existing themes

Week 136 (sealed-bid auctions, draft) uses hidden bids for a prize; Week 7 and Week 8 are perfect-information games solved backward; the "Hex" scouting draft and Week 147's pairing strategies are positional games without bidding; Week 24 and Week 60 use chances computed backward. New here: control of the turn as the thing being bought, a theorem that turns a money threshold into a probability (Richman's theorem), and a discrete version where a single tie-breaking token decides close games. The coin-flip race is a small Week 60-style backward table; the link between that table and the bidding is the new idea.

## App connection

Games and choices. A "Bid to move" family: two tracks, chip piles and a hidden bid slider against a robot that bids optimally. Example puzzles: "You have 3 chips, the robot has 7, you need 1 square and it needs 3: win"; "Find the fewest chips that beat the robot on this race"; "Play bidding tic-tac-toe with 4 chips each and the star". Fit B: needs the exact discrete solver from the check script (small state spaces) and a bid animation.

## Open questions

- Hidden fists work for 5 chips; do larger piles need a screen and a written bid?
- The star rule (take the tie and pass the star, or give it and keep the star) is the hardest rule to explain; rehearse it with an adult pair before a page is written.
- Whether 4–5 can follow the averaging argument, or only test it; the guide should keep the proof as a discretionary conversation.
- Bidding tic-tac-toe with 4 chips each: solve it exactly before claiming who should win from the start.
