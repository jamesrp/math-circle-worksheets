# Week 133 (draft plan): Better in both, worse together

**Strand:** chance, with inference (app region "Chance and machines"). **Deep-math field:** probability, weighted averages, statistics and causal reasoning. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

Simpson's paradox (named for E. H. Simpson, 1951; earlier noticed by Yule, 1903): it is possible to have a/b > c/d and e/f > g/h, yet (a + e)/(b + f) < (c + g)/(d + h). In bag language: bag A1 gives red more often than bag B1, bag A2 gives red more often than bag B2, but when the A bags are poured together and the B bags are poured together, the merged B bag gives red more often. The reason is a fact about weighted averages: a merged bag's red chance always lies between the chances of its two parts (the mediant property), and it sits closer to the part that holds more counters. If A's counters are mostly in its weak bag and B's are mostly in its strong bag, the merged order flips. This also says exactly when it cannot happen: if A1 and B1 hold the same number of counters, and A2 and B2 do too (or more generally if A and B split their counters between the two groups in the same proportion), being better in both groups forces being better merged. With every bag holding both colours, the smallest reversal uses 19 counters (an exhaustive check over bags of up to 5 counters each). Real cases: in a 1986 kidney-stone study open surgery succeeded in 273 of 350 cases and a keyhole method in 289 of 350, yet the widely quoted split by stone size has open surgery ahead for both small and large stones, because it was used far more on the harder large stones. Which comparison to trust is not a question of arithmetic: Pearl's causal analysis says it depends on how the grouping variable relates to the choice and the outcome. Children can discover the reversal by drawing from bags, build their own reversals, and in grades 4–5 explain why equal-sized pairs can never reverse.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Simpson's Paradox (Stanford Encyclopedia of Philosophy, Summer 2006 edition)](https://plato.stanford.edu/archives/sum2006/entries/paradox-simpson/). Gary Malinas and John Bigelow. The fraction statement of the reversal, Simpson (1951), Yule (1903), Cohen and Nagel's 1934 tuberculosis example, a hiring example modelled on the Berkeley admissions case (Bickel et al. 1975), and unequal group sizes as the driver (read November 3, 2026).
- [Understanding Simpson's Paradox](https://ftp.cs.ucla.edu/pub/stat_ser/r414.pdf). Judea Pearl, UCLA technical report R-414, December 2013, marked forthcoming in The American Statistician (2014). Reversal under conditioning, the "sure-thing" result, and why causal structure decides which table to use (read November 3, 2026).
- [Comparison of treatment of renal calculi by open surgery, percutaneous nephrolithotomy, and extracorporeal shockwave lithotripsy](https://www.bmj.com/content/292/6524/879). C. R. Charig, D. R. Webb, S. R. Payne, J. E. Wickham, BMJ 292:879, 1986. Overall success 273/350 (78%) for open surgery and 289/350 (83%) for percutaneous nephrolithotomy; the page read does not show the split by stone size (read November 3, 2026).
- Prior use with children: [Probability Paradox](https://bpb-us-e2.wpmucdn.com/sites.wustl.edu/dist/b/4012/files/2023/02/20170924-probability-paradox.pdf). Chang Liu, Washington University Math Circle, September 24, 2017; a Simpson's paradox section using the 1973 Berkeley admissions data, alongside the birthday problem and Monty Hall (read November 3, 2026). No K–5 bag-based version was found (searched NRICH and math circle pages for Simpson's paradox with marbles or bags).

## A kid-friendly way in

Materials per table: four labelled paper bags and 20 counters: Pair 1, bag A1 holds 1 red, bag B1 holds 8 red and 1 blue; Pair 2, bag A2 holds 1 red and 8 blue, bag B2 holds 1 blue. Two empty bags marked "all of A" and "all of B". For 4–5 a gentler set of 19 counters: A1 2 red 1 blue, B1 3 red 2 blue, A2 2 red 5 blue, B2 1 red 3 blue. A bowl of spare counters for building. Prep: fill bags, about 15 minutes. Launch (3 minutes): "Red wins a sticker." Hold up A1 and B1, tip each onto a tray so everyone sees the contents, and take a class vote on which bag to draw from; draw once from each and put the counters back. Then do the same for Pair 2.

Suggested hour: 0–5 launch; 5–20 tables choose in each pair and test by drawing; 20–30 pour A1 and A2 into "all of A", B1 and B2 into "all of B", and choose again; 30–50 band questions; 50–60 share invented reversals.

## By band

- **K–1:** Choose the better bag in each pair by looking (one bag is all red, one bag has no red). Pour the A bags together and the B bags together, tip them out, and choose again. Line up reds against blues in rows to see which merged bag has more red.
- **2–3:** Explain to a partner how A can win both pairs but lose after pouring. Then use the spare counters to build your own set of four bags where the same thing happens; test a classmate.
- **4–5:** Use the gentler set, where the comparisons need care (2/3 against 3/5, 2/7 against 1/4). Find the merged chances, then try to build a reversal where A1 and B1 hold the same number of counters and A2 and B2 do too. Explain why it never works. For a closing discussion, the kidney-stone totals and what extra information a doctor would want.

## Checked facts

- `check_week_133()`: main set: A wins both pairs (1 > 8/9 and 1/9 > 0), but merged A is 2 red 8 blue (1/5) and merged B is 8 red 2 blue (4/5); 20 counters in all.
- `check_week_133()`: gentler set: 2/3 > 3/5 and 2/7 > 1/4, but merged A 4/10 = 2/5 < merged B 4/9; 19 counters.
- `check_week_133()`: exhaustive check over all bags of 1 to 5 counters: every merged chance lies between its parts; no reversal has equal sizes within both pairs, or the same split of A and B between the pairs; with both colours in every bag the fewest counters for a reversal is 19.
- `check_week_133()`: kidney-stone totals 273/350 and 289/350 (78% and 83%, read on the BMJ page). The often-quoted split 81/87 and 192/263 (open) against 234/270 and 55/80 (keyhole) sums to those totals and reverses; the split itself was not read in the paper.

## Nearest existing themes

Atlas AP-02 and Week 45 (The visible side) show that a clue's meaning depends on how it was produced; Weeks 94 (Calibration lab) and 95 (Count the unseen) are inference weeks; Week 42 uses draws from one bag. None merges groups. New here: aggregation reversal, the mediant property of weighted averages, a sharp condition (equal group sizes) under which reversal is impossible, and a first look at why data need a causal story. The fraction comparisons give 4–5 children real practice comparing unlike fractions.

## App connection

Region "Chance and machines", possible family "Two shops": two pairs of jars of red and blue marbles, with a pour button that merges each side's jars. Puzzle 1: "Move counters between A's jars (keeping A better in each pair) until merged A loses." Puzzle 2: "Make the A jars and B jars the same sizes and try to make a reversal" (impossible; the board can confirm after a set number of tries, and an explanation card follows). An existing bag-drawing family from Weeks 42 to 45 could carry the jars.

## Open questions

- Is a one-counter bag (A1) and a no-red bag (B2) too obviously a trick? A pilot should see whether children feel cheated or intrigued, and whether the gentler set is usable below grade 4.
- K–1 choice by looking needs no drawing at all; decide whether drawing adds anything for them.
- The medical example needs careful framing; a simpler real example (school sports or games data the group makes itself) may land better.
- Confirm the kidney-stone subgroup counts in the full paper before any guide quotes them.
