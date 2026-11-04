# Week 172 (draft plan): First digits

**Strand:** chance and number (app region "Chance and machines", or "Numbers"). **Deep-math field:** Benford's law, equidistribution, logarithms. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Benford's law says that in many collections of numbers the first (leftmost nonzero) digit is d with probability log₁₀(1 + 1/d): about 30.1% for 1, 17.6% for 2, down to 4.6% for 9. Simon Newcomb proposed it in 1881 from worn logarithm tables, and Frank Benford rediscovered it in 1938 from 20,229 numbers (river areas, baseball statistics, atomic weights). For a definite sequence the law can be a theorem. For the powers of 2 it holds exactly in the limit: 2ⁿ starts with d when the fractional part of n·log₁₀ 2 lies between log₁₀ d and log₁₀(d + 1), and because log₁₀ 2 is irrational these fractional parts are equidistributed (Weyl's equidistribution theorem, as Cai and coauthors apply it), so each digit gets its share. The digit-1 case has a proof children can follow: the numbers from 10^(k−1) up to 2·10^(k−1) form a "doubling interval", so exactly one power of 2 with k digits starts with 1, and since 8 < 10 < 16 each digit length holds 3 or 4 powers of 2; so among 2¹, …, 2^N exactly ⌊N log₁₀ 2⌋ start with 1 (301,029,995 of the first billion, as Cai and coauthors note), a share between 1/4 and 1/3 that tends to 0.30103. A second elementary fact explains why 1 wins: doubling moves first digits along a small map, 1 → 2 or 3, 2 → 4 or 5, 3 → 6 or 7, 4 → 8 or 9, and all of 5, 6, 7, 8, 9 → 1. For real data the law is not a theorem but an observation with partial explanations: a law of first digits that does not change when units change (scale invariance) or when the base changes must be Benford's (Hill, 1995, for base invariance), and mixing samples from many different distributions tends toward it (Hill, 1996). It fails for data confined to a narrow range (heights, phone numbers within one area, lottery numbers), and the whole numbers 1 to N never settle: the share starting with 1 swings from 11/99 at N = 99 to 111/199 at N = 199, between about 1/9 and 5/9. Fabricated data often has too few leading 1s, which is why auditors use the law as a screen (Nigrini's work, as reported by Hill). Children can discover that 1 is the most common first digit in doubling chains, that it is not a coincidence of the starting number, and, in grades 4–5, prove the "exactly one per digit length" fact.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The First Digit Phenomenon](<https://hill.math.gatech.edu/publications/PAPER PDFS/TheFirstDigitPhenomenonAmericanScientist1996.pdf>). T. P. Hill, American Scientist (feature article, 1998 per the PDF). Newcomb 1881 and Benford 1938, scale and base invariance, the random-samples explanation, Nigrini's fraud screening, and examples that fit (county populations, accounting data) and do not (telephone numbers, single bell curves) (read November 4, 2026).
- [Base-invariance implies Benford's law](https://www.ams.org/journals/proc/1995-123-03/S0002-9939-1995-1233974-8). Theodore P. Hill, Proceedings of the American Mathematical Society 123 (1995), 887–895. Every base-invariant distribution of significant digits is a mix of a point mass and the logarithmic (Benford) law (read November 4, 2026; abstract page). A broader survey is Berger and Hill, [A basic theory of Benford's Law](https://ftp.gwdg.de/pub/EMIS/journals/PS/viewarticlec281.html?id=175), Probability Surveys 8 (2011), 1–126, with open problems (read November 4, 2026; abstract page).
- [The Surprising Accuracy of Benford's Law in Mathematics](https://arxiv.org/pdf/1907.08894). Zhaodong Cai, Matthew Faust, A. J. Hildebrand, Junxian Li and Yuan Zhang, arXiv (about 2019). Powers of 2, Fibonacci numbers and factorials obey the law; exactly 301,029,995 of the first billion powers of 2 start with 1; Weyl's theorem applied to n·log₁₀ 2 (read November 4, 2026).
- [Probability of 2ⁿ Beginning with Digit 1](https://www.cut-the-knot.org/m/Probability/ProbabilitiesInPowersOf2.shtml). Cut-the-Knot. Two proofs that the share is log₁₀ 2: counting by digit lengths, and equidistribution of the mantissa (read November 4, 2026).
- Prior use with children: [Benford's Law](https://mathcircle.berkeley.edu/sites/default/files/handouts/2016/IntIIBenford%27sLaw2.pdf). Austin Shapiro, Berkeley Math Circle, September 6, 2016; powers of 3, a circular "wheel" number line for fractional parts, and which sequences obey the law (read November 4, 2026). No K–5 activity was found (searched NRICH and circle pages for Benford and first-digit tasks).

## A kid-friendly way in

Materials: a "first-digit chart" on the board with nine columns; dot stickers; a deck of about 40 printed number cards (the powers of 2 from 1 to 2³⁹ for one deck, and a contrast deck of numbers whose first digits are evenly spread, such as 40 random 3-digit numbers from a die-rolled table); calculators for grades 2–5 or paper for doubling by hand. Optional: one printed table of public data, such as county populations, chosen and checked by the facilitator beforehand (no personal data). Prep: print and cut two decks per table, about 20 minutes.

Launch (3 minutes): start at 3 and double out loud with the class: 3, 6, 12, 24, 48, 96, 192, 384, … Circle each leftmost digit and put a sticker in its column. Ask: "Which column will be tallest if we keep going?"

## By band

- **K–1:** Sort the powers-of-2 deck by the leftmost digit into nine piles (matching digit shapes is enough), then build a cube tower for each pile. Sort the contrast deck the same way. Which deck makes a staircase and which makes a flat row?
- **2–3:** Each child picks a start (any number from 1 to 9) and doubles at least 12 times with a calculator or by hand, adding a sticker for each first digit to the class chart. Does the start matter? Then: if a number starts with 5, 6, 7, 8 or 9, what can its double start with? Find all the arrows of the doubling map.
- **4–5:** List the powers of 2 with 1, 2, 3 and 4 digits. Why does exactly one in each group start with 1? Why can a group hold only 3 or 4 powers? What does that say about the share of 1s (between 1/4 and 1/3)? Extension: double every number in a list from 1 to 9; five answers start with 1, so equally common first digits do not survive a change of units. Optional: test the county table against the class chart.

## Checked facts

- `check_week_172()`: log₁₀(1 + 1/d) ≈ 0.30103, 0.17609, …, 0.04576, summing to 1; the first ten powers 2⁰…2⁹ start with 1, 2, 4, 8, 1, 3, 6, 1, 2, 5.
- `check_week_172()`: for every digit length up to 360 digits, exactly one power of 2 starts with 1 and the length holds 3 or 4 powers; among 2¹…2^N the count starting with 1 equals ⌊N log₁₀ 2⌋ for every N up to 3000, and gives 301,029,995 for N = 10⁹.
- `check_week_172()`: first digits of 2⁰…2⁹⁹ occur 30, 17, 13, 10, 7, 7, 6, 5, 5 times (Benford predicts 30.1, 17.6, 12.5, …); 3⁰…3⁹⁹ have 29 leading 1s and the first 100 Fibonacci numbers 30.
- `check_week_172()`: the whole numbers 1 to N: share of leading 1 is 11/19, 11/99, 111/199, 111/999, and 1111/1999 ≈ 0.556; doubling 1…9 gives five answers starting with 1; the doubling map 1 → {2, 3}, 2 → {4, 5}, 3 → {6, 7}, 4 → {8, 9}, 5–9 → {1}; the chain from 7 for ten terms has three leading 1s.

## Nearest existing themes

Week 74 (Doubling elevators) and Week 54 (halving and doubling in partitions) use powers of 2 but not their digits; atlas GA-34 marks doubling times. Draft 114 (Sunflower spirals) uses the same deep fact in another form: multiples of an irrational turn never line up and spread evenly round a circle, which is exactly why the fractional parts of n·log₁₀ 2 fill the "log wheel". A return visit could pair the two. New here: first digits, a logarithmic distribution, a provable statement about every digit length, and the boundary between a theorem (powers of 2) and an empirical law (real data).

## App connection

Region "Chance and machines" or "Numbers", possible family "Doubling meter": a number doubles each tick and its first digit lights one of nine lamps, which keep counts. Puzzle 1: "A number starts with 4. Which lamps can light next?" (8 or 9). Puzzle 2: "Choose a multiplier (×2, ×3, ×10) and predict which lamp will be brightest after 100 ticks" (×10 keeps one lamp forever, a good surprise). Puzzle 3: "Which of these two tables of numbers was made up?"

## Open questions

- The real-data table: which public table to print, and whether its first digits actually follow the law closely enough with 30 to 60 entries; this plan has not checked any real data set.
- Whether K–1 sorting by leftmost digit is meaningful for children who do not yet read multi-digit numbers (matching the first shape may be enough).
- Calculator use for 2–3: doubling by hand past 1000 may become arithmetic practice, which the circle avoids; a printed doubling ladder may be better.
- Whether to mention fraud detection to children at all, or keep it as an adult note.
