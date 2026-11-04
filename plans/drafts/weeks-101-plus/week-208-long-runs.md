# Week 208 (draft plan): Long runs

**Strand:** chance (app region "Chance and machines"). **Deep-math field:** runs in random sequences, the log n law, testing randomness. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

In n flips of a fair coin, the longest run of one face (all heads or all tails in a row) is usually close to log₂ n, and its spread does not grow with n. For n = 100 (log₂ 100 ≈ 6.6) the exact distribution, computed here by counting, has mean 6.98 and most likely value 6; the longest run is 5, 6 or 7 with chance 0.657, at least 6 with chance 0.807, at least 8 with chance 0.315, and 4 or less with chance only 0.028. Counting heads only shifts everything down by about one (mean 5.99 for 100 flips). Schilling (College Mathematics Journal, 1990) derived recursions for the exact distribution, the heuristic "about log₂ n − 1 for head runs", and a standard deviation of about 1.87 that stays put as n grows; for 200 flips he gives an expected longest head run of about 7, about 8 for either face, and 4 to 10 as limits containing the longest head run with probability 95.3%, all of which the check script reproduces. The reason for the log law: a run of length k starts at a given place with chance about 2^(−k), so among n places one expects about n/2^k such starts, which is near 1 when k ≈ log₂ n. People inventing "random" lists switch faces too often and avoid long runs; Schilling reports that very few students simulating 200 tosses write any run longer than five, and Schilling's own classroom guesses classified real versus invented sequences correctly about 85% of the time, adapting an experiment of Révész. The detector is a statistical judgement, not a proof: a real sequence can have a short longest run (about 3% of 100-flip sequences have none longer than 4) and a careful faker can include long runs. A second fingerprint is the number of switches: in 100 flips the face changes 49.5 times on average, and invented lists tend to switch more often (a pattern NRICH's student responses also note), though no rate for this was found in a source. Proved: the exact distributions (by recursion) and the averages; the log n growth for every n is cited from Schilling rather than proved here. Children can discover that real lists contain surprisingly long runs, that invented lists can be spotted, and in grades 4–5 why longer lists have only slightly longer runs.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [The Longest Run of Heads](https://petermchale.github.io/Math175/lectures/L1%20The%20Longest%20Run%20of%20Heads.pdf). Mark F. Schilling, The College Mathematics Journal 21(3), May 1990, 196–207 (copy posted on a course page). The classroom exercise after Révész (85% correctly classified), "very few students who simulate 200 coin tosses list any runs longer than five", expected longest head run about 7 and either face about 8 for 200 tosses, 4 to 10 with probability 95.3%, standard deviation about 1.873, the log n law (read November 4, 2026).
- [Long Run Predictions](https://www.csun.edu/%7Ehcmth031/LongRunPredictions.pdf). Mark F. Schilling, Math Horizons 1(2), Spring 1994, 10–12. The rule R = log₂ n for the longest run of heads or tails, and the observation that people writing imitation sequences rarely include runs longer than four or five (read November 4, 2026).
- Prior use with children: [What Does Random Look Like?](https://nrich.maths.org/node/65079). NRICH, ages 11 to 14. Students write one invented and one real sequence of 20 flips on strips, a partner guesses which is real, and the class compares longest runs and how often a flip repeats the previous one (read November 4, 2026). No K–5 version was found (searches of NRICH and math-circle handouts for real versus invented coin flips).

## A kid-friendly way in

Materials per pair: two coins, two paper strips with 20 boxes (100 boxes for 4–5, as a 10 by 10 grid), red and blue crayons or two colours of snap cubes (for K–1), a "detective" envelope, and a class chart of longest runs. Prep: print strips and grids, about 15 minutes. Launch (3 minutes): the adult shows two 20-box strips on the board, one real and one invented the night before, and asks the room to vote which came from a coin; then reveals and points to the longest run in each. Everyone then makes one real and one invented strip in secret and swaps with another pair.

Suggested hour: 0–5 launch; 5–25 make real and invented strips and swap; 25–40 detectives explain their guesses, then collect every real strip's longest run on the class chart; 40–55 band questions; 55–60 compare the chart with the adult's prediction.

## By band

- **K–1:** Flip a coin 10 times and build a tower of red and blue cubes, a new cube each flip; then try to make a "pretend" tower without the coin. Which tower has the longest stretch of one colour? Put the real towers in a row and look for the tallest one-colour stretch.
- **2–3:** Make a real and an invented 20-flip strip and swap with another pair: can they tell which is real? What is the longest run in each real strip? Collect the class's results and look for the most common longest run.
- **4–5:** Flip 100 times in a 10 by 10 grid (pairs can share: 50 flips each). Predict the longest run before you look. Then compare with 20-flip strips: how much longer are the longest runs in 100 flips than in 20? Explain with "a run of 6 starts at a given place about 1 time in 64".

## Checked facts

- `check_week_208()`: 100 flips, longest run of one face: P(5 to 7) = 0.657, P(at most 4) = 0.0283, P(at least 6) = 0.807, P(at least 8) = 0.315, mean 6.98, mode 6; log₂ 100 ≈ 6.64. Heads only: mean 5.99.
- `check_week_208()`: 200 flips: longest head run averages 6.98 and either face 7.98; P(4 ≤ longest head run ≤ 10) = 0.953, matching Schilling's 95.3%.
- `check_week_208()`: 20 flips: a run of 4 or more with chance 0.768, of 5 or more with 0.458; 10 flips: a run of 3 or more with chance 846/1024 ≈ 0.826, of 4 or more 0.465.
- `check_week_208()`: 49.5 switches (50.5 runs) on average in 100 flips; a seeded simulation of 4000 sequences agrees with 0.657.
- The 85% detection rate and the statements about people's invented lists are cited from Schilling, not computed.

## Nearest existing themes

Draft 132 (Coin-pattern races, Penney's game) also studies patterns in coin sequences, through waiting times and self-overlap; the overlap is the setting, not the question. Here the object is the longest run in a fixed number of flips and its log n growth, plus the idea of testing whether data came from a coin. Draft 174 (Shrinking piles) has the same log₂ n growth for the maximum of waiting times, a natural cross-reference for 4–5. Atlas AP-03 runs an exact test by listing assignments, a cousin of "could chance alone produce this?". Week 24 (Three random decks) and Week 44 (The bag that copies) use other chance mechanisms. New here: what randomness looks like, a quantitative fingerprint of real data, and the surprise that long runs are normal.

## App connection

Region "Chance and machines", possible family "Real or fake?": the app shows two sequences of 100 coloured beads, one from a coin and one from a character who "tries to look random"; the child picks the real one and sees the longest runs and switch counts highlighted. Puzzle 1: "Make a fake 100-bead string that fools the detective" (the detective checks longest run and switches). Puzzle 2: "Flip until a run of 5 appears; how many flips did it take?" across many trials.

## Open questions

- Bookkeeping: 100 flips per child is long; pairs sharing 50 each, or a cup of 10 coins tipped ten times, may be better. Rehearse the cup method for fairness and recording speed.
- Do K–1 children produce "pretend" towers, or simply copy the real one? The pretend task may need an adult prompt.
- The detective rule fails sometimes by design; the guide must say so plainly so children do not conclude a real strip was "wrong".
- Is the NRICH 20-flip version (ages 11 to 14) too reading-heavy for 2–3 without adult recording?
