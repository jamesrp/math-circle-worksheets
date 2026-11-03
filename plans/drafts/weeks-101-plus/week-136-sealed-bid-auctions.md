# Week 136 (draft plan): Sealed-bid auctions

**Strand:** games (Games and choices). **Deep-math field:** game theory (mechanism design, auction theory). **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Each bidder has a private value for a prize (how many points it is worth to them) and writes a sealed bid; the highest bid wins. In a first-price auction the winner pays their own bid; in a second-price auction (William Vickrey, 1961) the winner pays the highest of the other bids. Vickrey's theorem: in a second-price auction, bidding exactly your value is a dominant strategy. The proof is a case check on the highest other bid B: if B is below your value, bidding your value wins and earns value − B, which no other bid beats; if B is above, bidding your value loses and earns 0, while any bid that wins would pay more than the prize is worth; your own bid only decides whether you win, never what you pay. In a first-price auction, bidding your value always earns 0, so bidders shade their bids; with n bidders whose values are independent and uniform on [0, 1], the equilibrium bid is (n − 1)/n of the value. Revenue equivalence: under standard assumptions (independent private values from a continuous distribution, the highest bidder wins, and the lowest possible type pays 0), both auctions give the seller the same expected revenue; for uniform values both equal (n − 1)/(n + 1). The design idea is what makes this worth a week: the rules of a game can be chosen so that honesty is each player's best plan. Proved: dominance in the second-price auction, the uniform equilibrium, revenue equivalence under its assumptions. Checked here: dominance for every whole-number value up to 10 and bid up to 12, with ties split by a coin, a small payoff table, the revenue formulas for 2 to 6 bidders, and that bidding half your value is a best reply against one rival who bids half. Limits: the assumptions matter, and real auctions with shared values or many items behave differently; this week uses values printed on cards and never real money.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Algorithmic Game Theory, Lecture 16](https://www.cs.jhu.edu/~mdinitz/classes/AGT/Spring2020/Lectures/lecture16.pdf). Michael Dinitz, Johns Hopkins course 601.436/636, March 31, 2020. Theorem 16.2.1 (truthful bidding is dominant in the second-price auction, by cases on the highest other bid) and why first-price bidders underbid (read November 3, 2026).
- [Order Statistics and Revenue Equivalence](https://cs.brown.edu/courses/csci1440/lectures/2025/revenue_equivalence.pdf). Brown University CSCI 1440/2440 course notes, January 29, 2025, no author named. The first-price equilibrium bid (n − 1)/n · v, expected revenue (n − 1)/(n + 1) for both auctions, and the assumptions of revenue equivalence (read November 3, 2026).
- [The Work of Milgrom and Wilson in the Theory and Practical Application of Auctions](https://hitelintezetiszemle.mnb.hu/en/fer-20-1-e1-biro-magyarkuti). Péter Biró and Gyula Magyarkuti, *Financial and Economic Review* 20 (1), 2021. Context for the 2020 economics prize and the reference for Vickrey, "Counterspeculation, auctions, and competitive sealed tenders", *Journal of Finance* 16 (1), 1961 (only the abstract and references were readable) (read November 3, 2026).
- Prior use with children: [Auction Lab](https://www.competitivekids.org/games/auction-lab). CKSTEM (Competitive Kids STEM Projects), grades 6 and up. Secret values, sealed bids, first-price and second-price rounds, and the lesson that truthful bidding is never beaten in a second-price auction (read November 3, 2026). Also [Auctions: The Science of Bidding](https://www.mathsisfun.com/sets/game-auction-theory.html), Math is Fun, a school-level explanation of second-price truthful bidding with a payoff table (read November 3, 2026). No K–5 auction activity was found.

## A kid-friendly way in

Secret value cards and sealed bids. The prize is a picture card ("a jar of beans"); each child draws a secret value card from 1 to 10 saying how many points the prize is worth to them. Bids are written on slips (K–1 build cube towers behind a folder). The winner scores value minus price; everyone else scores 0. Play pay-your-bid rounds and pay-the-next-highest rounds and keep a points tally. Prep: value cards, slips or cubes and folders, a tally sheet, about 15 minutes. Launch (2 to 3 minutes): an adult auction with three volunteers, values shown only to the audience; one volunteer who bid above their value wins and the class works out that they lost points.

## By band

- **K–1:** cube towers. The value card shows a tower picture; bid by building a tower behind a folder; the tallest wins. In "pay the next tower" rounds the winner snaps off as many cubes as the second-tallest tower from their value tower and keeps the rest as points. Questions are spoken: was winning good for you this time?
- **2–3:** play both kinds of rounds; then, for a value card of 7, fill in the points for bids of 5, 7 and 9 against a highest other bid of 4, 6 or 8 in the pay-the-next-highest auction, and look for the bid that is never worse. Does the same bid work when you pay your own bid?
- **4–5:** explain why bidding your value is never worse in the second-price auction, case by case on the highest other bid. First-price puzzle: one rival always bids half their value, and their value is equally likely to be anything from 0 to 10; what fraction of your value should you bid? (Half.) Discuss why a seller might expect the same income from both auctions, then compare class totals, knowing a few rounds are noisy.

## Checked facts

Computed in `check_symmetry_games.py`, `check_week_136()`:

- second price, values 0 to 10, bids 0 to 12, highest other bid 0 to 12, ties split: bidding your value is never worse than any other bid, and every other bid is strictly worse against some highest other bid;
- first price: bidding your value always earns 0; with value 8 against a highest other bid of 5, bidding 6 earns 2;
- the table for value 7 (bids 5, 7, 9 against 4, 6, 8): 3, 3, 3 / 0, 1, 1 / 0, 0, −1;
- for n = 2 to 6 uniform bidders, (n − 1)/n × n/(n + 1) = (n − 1)/(n + 1), so the two revenue formulas agree;
- against a rival bidding half a uniform value, bidding half your own value is the best reply (grid check).

Cited, not computed: the equilibrium bid (n − 1)/n · v and the general revenue equivalence theorem.

## Nearest existing themes

Week 58 (Fair division) also starts from private valuations; atlas AP-22 and AP-23 study equilibria; the scouting draft "Hidden armies" is a sealed simultaneous game; Week 87 (Voting and agendas) shows how rules change outcomes. New here: designing the rules so that honesty is a dominant strategy (mechanism design), and comparing two rule sets by the income they produce. It shares the "secret choice, simultaneous reveal" format with the Week 135 draft (trust game), so the two should not run back to back.

## App connection

Games and choices. A "Sealed bids" family: the child sees their value and short descriptions of robot bidders and chooses a bid; puzzles ask for a bid with a guarantee. Example puzzles: "Find a bid that never loses you points in a pay-the-next-highest auction, whatever the robots bid"; "Against Robbie, who bids half their value, which bid earns you the most on average?"; "Change one rule so that bidding your value is always safe". Fit B: simple validators by enumeration over robot bids.

## Open questions

- Value cards must stay clearly separate from real money and prizes; decide whether any physical prize changes hands at all (probably not).
- K–1 cube subtraction (value tower minus price tower) may need an adult at each table.
- Whether a classroom revenue comparison is worth doing, given how noisy a few rounds are; it could stay a facilitator demonstration.
