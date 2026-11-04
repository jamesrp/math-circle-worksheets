# Week 177 (draft plan): Pirates share the gold

**Strand:** games (Games and choices). **Deep-math field:** game theory (backward induction, voting games, subgame-perfect equilibrium). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Pirates ranked by seniority must split G gold coins. The most senior pirate proposes a split; everyone, the proposer included, votes; if at least half vote yes the split happens (the proposer breaks ties), and otherwise the proposer walks the plank and the next pirate proposes. Each pirate wants first to survive, then as many coins as possible, and, all else equal, enjoys seeing someone walk the plank, so they vote yes only for strictly more than they would get later. Working backward gives a surprising, lopsided answer. One pirate keeps everything. Two pirates: the senior one votes yes and that is half, so they keep everything. Three: the proposer needs one more vote and buys the most junior pirate, who would get nothing in the two-pirate game, for one coin. With five pirates and 100 coins the proposer keeps 98 and gives one coin each to the third and fifth pirates in rank, who would get nothing if the proposer fell; a coin offered to the fourth pirate would be refused, because that pirate gets the same coin later and prefers a splash. For any number of pirates k up to 2G, the proposer keeps G − ⌊(k − 1)/2⌋ and gives single coins to every second pirate below. The rules matter: with a strict majority (the University of Waterloo handout's version), two pirates means the senior one always walks, so in a three-pirate game the middle pirate votes yes for nothing, and with five pirates the proposer must choose which of two pirates gets two coins, so the answer is no longer unique. With many pirates and few coins, Steve Omohundro's extension, described by Ian Stewart in *Scientific American* (May 1999), gives a pattern of powers of two: for more than 2G pirates, the proposer survives only when the number of pirates is 2G plus a power of 2 (so with 100 coins: 201, 202, 204, 208, 216, 232, 264, 328, 456), because the pirates who would die next vote yes for nothing. Proved: the backward-induction answers for k ≤ 2G (with the stated tie-breaking preferences). Checked here: the answers for 1 to 7 pirates with 10 gems, the general formula for every k ≤ 2G with G = 10 and 100, the strict-majority cases, and the counting recursion behind the power-of-two survivors. Cited, not proved here: the full many-pirate analysis, which needs extra care about which pirates can count on a coin; I could not read Stewart's article itself, only an account of it. Limits: the answer is about perfectly self-interested reasoners who know that everyone else reasons the same way; children (and adults) may well refuse an insulting single coin, and the session can discuss that gap without treating it as a mistake.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Pirate game](https://en.wikipedia.org/wiki/Pirate_game). Wikipedia (secondary pointer). The rules and priorities, the 98, 0, 1, 0, 1 answer and why the fourth pirate cannot be bought, and its summary of Omohundro's extension as described by Stewart in May 1999 (survivors up to 2G + M, M the largest power of 2 not above N − 2G; the 500-pirate example) (read November 4, 2026).
- [The Pirate Puzzle](https://sites.ualberta.ca/~esimmt/needachallenge/problems/piratePuzzle.html). Elaine Simmt, University of Alberta "Need a Challenge?" problems, 2009. The puzzle as posed for students, with majority-or-tie passing and the survive, gold, see-someone-overboard priorities; credits Ian Stewart (read November 4, 2026).
- [A Puzzle for Pirates (MAS project)](https://www.ai.rug.nl/mas/finishedprojects/2015/MatthiaZhenweiFrancesco/conclusion.html). Student project page, multi-agent systems course, 2015, on the University of Groningen AI site (authors named only in the address). With 100 coins, the surviving proposers above 200 are spaced 204, 208, 216, 232 because doomed pirates vote yes (read November 4, 2026).
- Prior use with children: [Game Theory, Solutions](https://cemc.uwaterloo.ca/sites/default/files/documents/2024/Junior7_8_20211124_Game_Theory_Soln.pdf). Grade 7/8 Math Circles handout on the University of Waterloo CEMC site, November 2021. Five pirates, 100 coins, a tie throws the proposer overboard; answer 97 for A, 1 to C, 2 to D or E; 6 and 7 pirates with a casting vote as exercises (read November 4, 2026).

## A kid-friendly way in

Act it out. Five children wear rank cards (Captain, First Mate, Bosun, Cook, Cabin Kid), a table is the deck and a paper strip at the edge is the plank; ten gold counters sit in a treasure tray. Start with the smallest ship: two pirates and ten coins, then three, then four, with one rule on a picture card: "Thumbs up only if you get more than you would after the captain walks." A "what happens next" strip under each ship, filled from the smallest ship up, is the record. Prep: rank cards, gold counters, a plank strip, a printed strip of ships with 1 to 6 places: about 15 minutes. Launch (2 to 3 minutes): two adults play the two-pirate ship: the senior adult proposes "all ten for me", votes yes, and that is half; the room sees the rule work, and the question is what happens when a third pirate joins.

## By band

- **K–1:** play ships of 2 and 3 pirates with coins and thumbs, with an adult reading the rule. Notice that in the 2-pirate ship the captain takes everything, and that in the 3-pirate ship one coin to the most junior pirate is enough. Count coins in each hand.
- **2–3:** the question "What is the captain's best split with 4 pirates? With 5?" worked from smaller ships, recorded on the ship strip. Discover the 1, 0, 1, 0 pattern and why giving a coin to the wrong pirate fails. Then change the rule to "more than half must say yes" and redo the small ships.
- **4–5:** explain why the pattern continues for any number of pirates up to twice the coins and how much the captain keeps; then the deeper question for few coins: with 1 coin, which captains survive (1, 2, 3, 4, 6, 10, 18, 34)? Explain why pirates who would walk the plank next vote yes for nothing, and find the doubling gaps.

## Checked facts

Computed in `check_games_3.py`, `check_week_177()`:

- ten gems, from most junior to captain: 2 pirates (0, 10); 3 (1, 0, 9); 4 (0, 1, 0, 9); 5 (1, 0, 1, 0, 8); 6 (0, 1, 0, 1, 0, 8); 7 (1, 0, 1, 0, 1, 0, 7); and five pirates with 100 coins give the captain 98 and coins to the third and fifth pirates;
- for every k ≤ 2G (G = 10 and 100) the captain keeps G − ⌊(k − 1)/2⌋ and the bribes alternate below the captain;
- strict majority: the 2-pirate captain walks; 3 pirates (0, 0, 10); 4 pirates (1, 1, 0, 8); 5 pirates have a tie among the cheapest voters, and the captain keeps 97, as in the Waterloo handout;
- the counting recursion (a captain survives when the pirates who would die, plus G bought votes, reach half) gives survivors 201, 202, 204, 208, 216, 232, 264, 328, 456 for G = 100, so with 500 pirates the top 44 walk; with G = 1 it gives 1, 2, 3, 4, 6, 10, 18, 34.

Cited, not computed: the full equilibrium analysis for more than 2G pirates (Stewart, via the Wikipedia summary).

## Nearest existing themes

Week 7 (take-away games) and Week 60 (take it or pass) teach working backward from the end, and atlas families with work-backward mechanisms share the move. Week 87 (voting and agendas) and Week 58 (fair division) share the setting of votes and splits. New here: backward induction in a game with many players, where the reasoning is about coalitions (whose vote is cheapest) rather than one opponent's replies; an answer that offends everyone's sense of fairness yet follows from the rules; the way one rule change (casting vote or strict majority) changes every answer; and the power-of-two pattern for large ships. No overlap with the Year 1 handouts was found.

## App connection

Games and choices. A "Pirate ship" family: the child is the captain, drags coins to crewmates, and the crew votes by the rule, with each pirate's "what I get if you walk" shown after the smaller ships are solved. Example puzzles: "Keep as many coins as you can with 5 pirates"; "Change the rule to strict majority and survive"; "With 1 coin and 10 pirates, who survives?". Fit A: discrete moves and an exact solver; it could share a backward-solving engine with Week 7's Pebble Duel.

## Open questions

- Social fit: children may be upset by a captain who keeps 98 or by a vote that sends someone overboard; use a gentle frame (the plank is a splash into a paddling pool) and rotate roles.
- The "enjoys a splash" tie-break is essential and easy to forget; does it need its own picture card?
- The many-pirate pattern should be checked against Stewart's article, or a full solver, before it reaches a page; only the counting recursion was checked here.
- Whether 2–3 can hold the ship strip as a record without adults doing the bookkeeping.
