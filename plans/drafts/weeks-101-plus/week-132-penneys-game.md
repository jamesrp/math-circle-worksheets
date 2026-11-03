# Week 132 (draft plan): Coin-pattern races

**Strand:** chance, with games (app region "Chance and machines"). **Deep-math field:** probability, patterns in random sequences, nontransitivity. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Penney's game (Walter Penney, 1969; popularised by Martin Gardner, 1974): each player names a pattern of three coin results, a fair coin is flipped until one pattern appears, and that player wins. Whatever the first player picks, the second can pick a pattern that wins more than half the time, so "beats" runs in cycles and no pattern is best. The reply rule for length 3: flip the first player's middle letter, put it in front, and drop their last letter (against HHH choose THH). The winning chances are 7/8 against HHH and TTT, 3/4 against HHT and TTH, and 2/3 against the other four. A four-pattern cycle: THH beats HHT (3/4), HHT beats HTT (2/3), HTT beats TTH (3/4), TTH beats THH (2/3). The 7/8 has a one-line proof children can follow: HHH can only come first if the first three flips are HHH, because otherwise the first HHH has a T just before it, and that T with the next two H's already made THH. Separately, patterns differ in how long they take to appear on their own: HHT, HTT, THH and TTH average 8 flips, HTH and THT 10, HHH and TTT 14, because a pattern that overlaps itself wastes progress when it fails. Conway's "leading numbers" turn self-overlaps and cross-overlaps into binary numbers that give both the waiting times (twice the self-overlap number) and the exact odds of any race; Conway stated the algorithm without proof, and proofs were given later (Miller 2019 gives one by a no-arbitrage betting argument). Waiting time and racing are different questions: for length 3 the pattern with the shorter wait never loses a race, but for length 4 THTH (average wait 20) beats HTHH (average wait 18) with chance 9/14. Children can discover by playing that the second player has an edge, find replies for every pattern, and explain the 7/8 case.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Penney's Game Odds From No-Arbitrage](https://arxiv.org/pdf/1904.09888). Joshua B. Miller, arXiv 1904.09888, version of November 5, 2025, accepted in Theory and Decision. A proof of Conway's leading-number odds formula, the second mover's advantage, a pattern's expected waiting time equal to its gross betting return (following Li 1980), and the history (Penney 1969, Gardner 1974) (read November 3, 2026).
- [Pattern matching probabilities and paradoxes as a new variation on Penney's coin game](https://blogsarchive.sites.haverford.edu/mathproblemsolving/files/2011/06/Penney-Ante.pdf). Yutaka Nishiyama, Osaka University of Economics, April 2010. The reply rule for length 3, a table of best replies (THH against HHH at 7:1, HHT against HTH at 2:1), all 64 pairings by Conway's algorithm, and a card-deck version (read November 3, 2026).
- [Penney's Game: Winning and Waiting](https://digitaleditions.sheridan.com/article/Penney%E2%80%99s+Game%3A+Winning+and+Waiting/4372753/766255/article.html). Robert Vallin, Math Horizons 30(2), November 2022. Waiting times 14, 10 and 8 and the distinction between waiting and winning (read November 3, 2026).
- Prior use with children: [Coin Tossing Games](https://nrich.maths.org/512). NRICH, set by Susan Pitts for a 1997 NRICH Maths Club video-conference, ages 14–16: race HH against TH, then find a counter for every triple (read November 3, 2026). No K–5 circle handout was found (searched math circle, JRMF and elementary classroom pages for Penney's game).

## A kid-friendly way in

Materials per pair: a coin (or a cup with one red and one blue counter to shake and pour, if coins roll away), a printed "flip track" of 30 boxes, red and blue crayons, eight pattern cards (HHH … TTT, drawn as red/blue dots for non-readers), and a tally sheet. Prep: print tracks and cut cards, about 15 minutes. Launch (3 minutes): two children each hold a two-flip card, red-red and blue-red; the facilitator flips and colours the track box by box until one card's pattern shows up in neighbouring boxes; repeat once, and show that a win is checked by sliding the card along the track.

Suggested hour: 0–5 launch; 5–25 two-flip races in pairs, then three-flip races where one child picks first; 25–45 hunt for replies; 45–60 share a reply for each card and explain one.

## By band

- **K–1:** Race red-red against blue-red with coloured boxes. Play ten races and stack a cube for each win. Does one card keep winning? Then swap cards.
- **2–3:** One child picks a three-flip card, the other picks a reply after seeing it. Find a reply card that beats each of the eight cards more often than not, and fill in a class chart of who beat whom. Is there a card that nothing beats?
- **4–5:** Explain why THH beats HHH unless the first three flips are HHH, and why that gives 7 of 8. Then a different question: how many flips on average until HHT appears alone, and until HTH? Use the class tracks to compare, and decide whether the faster-to-appear pattern must win a race.

## Checked facts

- `check_week_132()`: Conway's leading-number formula agrees with an exact Markov-chain calculation (fractions) for all 56 ordered pairs of three-flip patterns.
- `check_week_132()`: waiting times 14 (HHH, TTT), 10 (HTH, THT), 8 (the other four), each equal to twice the self-overlap number.
- `check_week_132()`: the reply rule gives the best reply for every pattern, with chances 7/8 (THH against HHH), 3/4 (THH against HHT), 2/3 (HHT against HTH and against HTT), and symmetric values with H and T swapped; the four-cycle THH > HHT > HTT > TTH > THH holds with 3/4, 2/3, 3/4, 2/3.
- `check_week_132()`: two-flip races: TH beats HH with chance 3/4, HT against HH is even; HH takes 6 flips on average, HT takes 4.
- `check_week_132()`: no three-flip pair has the longer-wait pattern winning; THTH (wait 20) beats HTHH (wait 18) with chance 9/14.
- `check_week_132()`: a seeded run of 20,000 races of THH against HHH gives THH within 0.01 of 7/8.

## Nearest existing themes

Week 24 (Three random decks) is the closest: nontransitive "beats" with three decks whose cycle is found by listing the 9 equally likely card pairs. Here the chances come from a process in time (a growing coin sequence) rather than a single draw, the reply depends on the opponent's pattern, and overlaps of a pattern with itself are the mechanism. Week 87 (Voting and agendas) has majority cycles. Atlas AP-01 uses coin tosses to move a token. New here: waiting times for patterns, self-overlap, and the gap between "appears sooner on average" and "wins the race" (seen at length 4).

## App connection

Region "Chance and machines", possible family "Pattern race": a coin machine fills a track while two pattern flags wait; the child picks a reply flag after seeing the rival's and the machine races them 100 times. Puzzle 1: "Pick a flag that beats HHT in most races." Puzzle 2: "Arrange four flags in a circle so each beats the next." A family built for Week 24's decks could share the "who beats whom" chart.

## Open questions

- Pace: three-flip races last about 5 to 8 flips each; are ten races per pair enough for the 2/3 edges to show up, or should tables pool results?
- Recording: the coloured track is the single record; check that K–1 children can spot a two-box pattern on it without adult help.
- Whether 2–3 children read H/T letters or need colour-only cards throughout.
- The length-4 example is for adults and strong 4–5 groups; a reviewer should decide whether it belongs in a guide extension.
