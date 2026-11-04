# Week 171 (draft plan): Shared birthdays

**Strand:** chance (app region "Chance and machines"). **Deep-math field:** probability, counting pairs, the pigeonhole principle. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

If n people have birthdays that are independent and equally likely to fall on any of d days, the chance that all n are different is d(d − 1)(d − 2)…(d − n + 1)/dⁿ, so the chance of at least one shared day is one minus that product (proved; a count of ordered lists). For d = 365 the chance passes one half first at n = 23 (50.7%; 22 people give 47.6%); a group of 11 already has about a 14% chance, 30 people 71%, and 57 people 99%. The intuition that fails is "someone shares my birthday": that needs 253 other people for an even chance, while a group of 23 contains C(23, 2) = 253 pairs, each matching with chance 1/365. Treating the pairs as nearly independent gives 1 − e^(−253/365) ≈ 0.50, and in general about √(2d ln 2) ≈ 1.18√d people give an even chance, so the threshold grows like the square root of the calendar, not like the calendar. The pigeonhole principle is the certain end: d + 1 people always share. Variants are also exact counts: three people sharing a day needs 88 people for an even chance (McKinney 1966), and a birthday on the same or an adjacent day needs only 14 (Abramson and Moser 1970), both reported by Diaconis and Mosteller (1989) and recomputed here. The model's assumptions (no leap day, no twins, equal days) matter only a little: uneven day frequencies make matches more likely, not less; this plan checks that only for real month lengths in the month-only version. The problem is usually credited to Harold Davenport (around 1927, unpublished), with the first published version by Richard von Mises in 1939. With a 12-day "calendar" (a 12-sided die, or months only) the same arithmetic gives a 43% chance with 4 people, 62% with 5, and certainty with 13; with a 6-sided die, 44% with 3 people and 72% with 4. Children can discover that matches come far sooner than they expect, that the number of pairs grows much faster than the group, and, in grades 4–5, why the chance that everyone differs is a product of shrinking fractions.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Methods for Studying Coincidences](https://www.stat.berkeley.edu/users/aldous/157/Papers/diaconis_mosteller.pdf). Persi Diaconis and Frederick Mosteller, Journal of the American Statistical Association 84 (1989). The 23-person even chance, the approximation of about 1.2√c people for c categories, 88 people for a triple (McKinney 1966), 14 for birthdays within a day (Abramson and Moser 1970), and the remark that unequal probabilities can be handled (read November 4, 2026).
- [Birthday problem](https://en.wikipedia.org/wiki/Birthday_problem). Wikipedia, as a secondary pointer only: the Davenport and von Mises history, the n(n − 1)/2 pairs heuristic, √(2d ln 2), and the statement that uneven birthday distributions raise the chance of a match (read November 4, 2026).
- Prior use with children: [Probability Paradox](https://bpb-us-e2.wpmucdn.com/sites.wustl.edu/dist/b/4012/files/2023/02/20170924-probability-paradox.pdf). Chang Liu, Washington University Math Circle, September 24, 2017; asks whether to bet that two people in the class share a birthday and how large a class must be for an even chance (read November 4, 2026). Also [Same Number!](https://nrich.maths.org/7221), NRICH, ages 14–16: everyone picks a number from 1 to 225 and duplicates turn up surprisingly often, with the birthday problem as the extension (read November 4, 2026), and the [MSTE birthday simulation](https://mste.illinois.edu/activity/birthday/), University of Illinois, which simulates classes of 1 to 60 (read November 4, 2026). No K–5 version with dice or small calendars was found (searched NRICH and circle pages for birthday and same-number activities).

## A kid-friendly way in

Never use children's real birthdays, in records or aloud; every "birthday" is rolled. Materials per group of four or five: one 12-sided die (or a bag of 12 month cards drawn with replacement), a printed "calendar" of 12 boxes, five counters in five colours (one per pretend guest), and a class tally chart with two columns, "a shared box" and "all different". For K–1, a 6-sided die and a 6-box calendar. Prep: print calendars and the chart, about 10 minutes; d12 dice are cheap but must be bought ahead.

Launch (3 minutes): five volunteers each roll the d12 and place their counter in that box of the board calendar. Before the fifth roll, ask: "Will two counters share a box?" Mark the class chart. Then tables run their own "parties" and add a mark per party.

## By band

- **K–1:** Teddy parties: roll a die for each of four teddies and put each teddy's counter on the 6-box calendar. Does any box get two? Drop a cube in the "shared" or "all different" cup and compare the towers after many parties. Then three teddies, then two.
- **2–3:** On the 12-box calendar, how many guests does a party need before a shared box happens more often than not? Groups test parties of 3, 4, 5 and 6 guests and pool their marks. Why are 13 guests always enough?
- **4–5:** Count the pairs in a party of 5 (10) and of 23 (253). Then the exact route: the second guest misses the first with chance 11/12, the third misses both with chance 10/12, and so on; multiply (fraction strips or a calculator) to find that 5 guests all differ only 38% of the time. Extensions: how many rolls of a d12 until the first repeat, on average (about 5)? How does that compare with Week 131's wait to see every face (about 37 for twelve faces, much longer)? How many people would you need for one of them to share *your* box on a 365-day calendar?

## Checked facts

- `check_week_171()`: 365 days: 22 people 0.4757, 23 people 0.5073, 11 people 0.1411, 30 people 0.7063, 57 people 0.9901; C(23, 2) = 253 and 1 − e^(−253/365) ≈ 0.500; √(2·365·ln 2) ≈ 22.49; someone sharing your day among 22 others ≈ 0.0586, and 253 others are the first count above one half.
- `check_week_171()`: 12-box calendar: 4 guests 0.4271, 5 guests 0.6181 (= 1 − 95040/248832), 13 guests certain; 6-box calendar: 1/6, 4/9 and 13/18 for 2, 3 and 4 guests, 7 certain; real month lengths raise the 5-guest chance slightly (by under one percentage point).
- `check_week_171()`: a triple needs 88 people (87 fall short); same-or-adjacent day needs 14 (13 fall short), on a circular 365-day year.
- `check_week_171()`: expected rolls to the first repeat: 3.77 (d6), 5.04 (d12), 24.6 (365 days, near √(πd/2) ≈ 23.9); a class running 30 five-guest parties sees a majority of shared boxes with chance about 87%; a seeded simulation of 20,000 parties agrees with 0.618.

## Nearest existing themes

Week 42 (Fair results from a bag) and Week 44 (The bag that copies) draw repeatedly from bags but ask about fairness and urn composition. Week 95 (Count the unseen) uses overlaps between two catches to estimate a population; a 4–5 extension here (guess how many sides a hidden die has from when the first repeat arrives) is the same idea in a different form, so it should be scheduled after Week 95 or left as a return visit. Draft 131 (collecting every sticker) is the natural contrast: the first repeat comes after about √d draws, collecting everything takes about d ln d. Atlas AP-08 uses pigeonhole in a different setting. New here: counting pairs as the reason, the square-root threshold, and pigeonhole as the certain end of a chance question.

## App connection

Region "Chance and machines", possible family "Party machine": guests arrive and the machine rolls each a box on a calendar of d boxes; the child sets the number of guests and the calendar size. Puzzle 1: "Choose the smallest party on a 12-box calendar where a shared box happens more often than not; the machine throws 200 parties to score your choice." Puzzle 2: "A hidden die keeps rolling until a repeat; from five runs, guess whether it has 6, 12 or 20 sides." A tally-and-pool family from Week 42 or Week 95, if one exists, could carry the simulation.

## Open questions

- Privacy: confirm with the organizer that no real birthdays are used anywhere, including in a launch story; the plan rolls all birthdays.
- Whether a class's pooled tallies separate 4 guests (43%) from 5 guests (62%) clearly enough; about 30 parties per size are needed, which may take most of the hour.
- Whether 2–3 children can manage the "always enough with 13" pigeonhole argument in words.
- d12 dice availability, or whether month cards drawn with replacement are an acceptable substitute (replacement must be enforced).
