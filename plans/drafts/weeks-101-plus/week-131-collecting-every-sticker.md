# Week 131 (draft plan): Collecting every sticker

**Strand:** chance (app region "Chance and machines"). **Deep-math field:** probability, expectation, harmonic numbers. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

The coupon collector problem: if each draw gives one of n kinds, all equally likely and independent, the expected number of draws to see every kind is n(1 + 1/2 + … + 1/n) = n·H_n. The proof splits the wait into stages. When k kinds are already seen, each draw is new with chance (n − k)/n, and a wait for an event of chance p averages 1/p draws, so the stages average n/n, n/(n − 1), …, n/1, and expectations add. For a die this is 1 + 6/5 + 6/4 + 6/3 + 6/2 + 6/1 = 14.7 rolls. The stages grow: the last face alone averages 6 rolls, more than the first four faces together (5.7). Because H_n ≈ ln n + 0.577, the total grows like n ln n, so doubling the number of kinds slightly more than doubles the wait. The spread is wide: the variance is n²(1 + 1/4 + … + 1/n²) − n·H_n, about 39 for a die (standard deviation about 6.2), the median is 13 rolls, below the mean, and about one run in six needs more than 20 rolls. With unequal chances collecting is slower than with the same number of equally likely kinds (a die stickered 1, 1, 2, 3, 4, 5 averages 12.7 rolls for its five kinds, against 11.4 for a fair five-way spinner); this is checked here only for small cases; the general claim that equal chances always give the shortest expected wait is believed true but is not sourced in this plan. Children can discover that the last sticker is the slow one, that a whole class's runs vary a lot but average near 15, and, in grades 4–5, why each stage's average wait is 6 divided by the number of faces still missing.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Coupon Collector Problem](https://brilliant.org/wiki/coupon-collector-problem/). Brilliant wiki. E[X] = n·H_n by summing geometric stage waits, H_n ≈ ln n + γ, the exact variance n²Σ1/k² − n·H_n, worked examples (3 toys: 5.5) (read November 3, 2026).
- [How many times must you roll a die until each side has appeared?](https://blogs.sas.com/content/iml/2011/07/20/how-many-times-must-you-roll-a-die-until-each-side-has-appeared). Rick Wicklin, The DO Loop (SAS), July 20, 2011. The 14.7 stage sum for a die and a 20-trial experiment with a long right tail (median 10.5, mean 12.1 in that small sample) (read November 3, 2026).
- [Data Mining lecture notes L2 (birthday paradox and coupon collectors)](https://users.cs.utah.edu/~jeffp/teaching/cs5955/L2-B+C-notes.pdf). Jeff Phillips, University of Utah, Data Mining. The stage argument, n·H_n ≈ n ln n, and that with unequal chances the rarest kind dominates the wait (read November 3, 2026).
- Prior use with children: [The Cereal Box Problem, teacher page](https://mste.illinois.edu/reese/cereal/teacher.php). Quinn Baetz and George Reese, MSTE, University of Illinois; middle and high school, hands-on simulation with dice before any online simulation (read November 3, 2026). Also [Cereal Box Problem](https://projects.ias.edu/pcmi/hstp/resources/cerealbox/), Beverly Farahani, Park City Mathematics Institute, grades 9–12, six toys simulated with dice (read November 3, 2026). No K–5 circle handout was found (searched NRICH and math circle pages for dice, stickers and cereal-box collecting).

## A kid-friendly way in

Materials per child: one die, a "sticker card" with the six die faces drawn on it, six small stickers or counters, and a strip of squares to write rolls in (or a pile of linking cubes, one cube per roll). Class materials: a long number line from 6 to 40 on the board and sticky notes. Prep: print the cards and strips, about 15 minutes. Launch (3 minutes): one child rolls at the front; each new face gets a sticker on the card, each roll adds a cube to a tower, and a repeated face adds a cube but no sticker. Stop when the card is full and place the tower's height on the class number line.

Suggested hour: 0–5 launch; 5–25 everyone collects several times, adding a sticky note per run to the number line; 25–45 band questions; 45–60 look at the class plot together: where is the middle, how far do the long runs reach, which sticker took longest?

## By band

- **K–1:** Fill the sticker card, build a cube tower for the run, and stand the towers side by side. Which part of your run had the most "no new sticker" cubes? A coin (two stickers) and a three-colour spinner give short games to compare.
- **2–3:** On the roll strip, circle the rolls that gave a new face. Collect the gaps between circles from many runs: which gap is usually longest? Predict, then test: how many rolls to collect both sides of a coin, three colours, six faces?
- **4–5:** If only one face is missing, how many rolls do you expect to wait (a 1-in-6 chance)? Build the 14.7 total stage by stage and compare with the class average. Extension: a die stickered 1, 1, 2, 3, 4, 5 has only five kinds; is it faster or slower to collect than a five-colour spinner, and than a normal die?

## Checked facts

- `check_week_131()`: 6·H_6 = 147/10 = 14.7; stage averages 1, 6/5, 3/2, 2, 3, 6 with running totals 1, 2.2, 3.7, 5.7, 8.7, 14.7; the last stage (6) exceeds the first four together (5.7).
- `check_week_131()`: other sizes: two kinds 3, three kinds 5.5, four kinds 25/3 ≈ 8.33, ten kinds ≈ 29.29.
- `check_week_131()`: exact distribution for a die: the minimum six rolls has chance 720/6⁶ ≈ 1.5%; median 13; P(at most 10 rolls) ≈ 0.272; P(more than 20) ≈ 0.152; P(more than 25) ≈ 0.062; variance ≈ 38.99, standard deviation ≈ 6.24.
- `check_week_131()`: a seeded simulation of 2,000 runs averages within 0.4 of 14.7.
- `check_week_131()`: the 1, 1, 2, 3, 4, 5 die averages 127/10 = 12.7 rolls, more than a fair five-way spinner (137/12 ≈ 11.42) and less than a normal die (14.7); a coin weighted 1/3 against 2/3 takes 3.5 tosses against 3 for a fair coin.

## Nearest existing themes

Week 42 (Fair results from a bag) and Week 44 (The bag that copies) use repeated draws but ask about fairness and urn compositions, not waiting times. Week 60 (Take it or pass) rolls a stickered die one offer at a time and is about stopping rules and expected value; Week 95 (Count the unseen) estimates a hidden population from overlap. Atlas GA-12 compares the harmonic sum 1 + 1/2 + 1/3 + … with the halving sum; here the same harmonic numbers appear as a waiting time, which gives GA-12 a concrete chance story. Week 141 (book stacking) is a second physical home for harmonic numbers. New here: waiting times, expectation adding over stages, and a sharp contrast between mean, median and long tail.

## App connection

Region "Chance and machines", possible family "Sticker machine": a machine dispenses one of n stickers at random and a child's album fills. Puzzle 1: "Bet on how many dispenses this album needs; the machine runs 100 albums and scores your guess." Puzzle 2: "Design a machine (choose how many of each sticker it holds) that takes longest to fill a five-sticker album" or "that fills fastest". A running-tally simulation family, if one exists for Week 60 or Week 95, could carry it.

## Open questions

- Time: a run averages about 15 rolls, so a child can do four or five runs in 20 minutes; is the class plot dense enough to show the long tail?
- Bookkeeping: cube towers versus written strips for K–1; the strip with circled new faces is the one record that lets 2–3 find the gaps, but writing every roll may slow younger children.
- Whether to state the n ln n growth to 4–5 children or leave it as an adult note.
- The claim that equal chances minimise the expected wait is checked only for the small examples above; a reviewer may want a source before it appears in a guide.
