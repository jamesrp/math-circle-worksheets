# Week 207 (draft plan): Random walks home

**Strand:** chance (app region "Chance and machines"). **Deep-math field:** random walks, recurrence and transience, expected values that are infinite. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A walker starts at home and moves one step at a time in a random direction, each direction equally likely. Pólya's theorem (Mathematische Annalen 84, 1921): on a line or a flat square grid the walker returns home with probability 1 (the walk is recurrent, and then it returns infinitely often), but on the three-dimensional cubic grid it returns with probability only about 0.3405 and otherwise wanders off for good (transient); in higher dimensions the chance is smaller still (0.1932 in four). On the line the details are exact. After 2n coin flips the walker is home with chance u(n) = C(2n, n)/4ⁿ; the first return happens at flip 2n with chance 1/2, 1/8, 1/16, 5/128, … (the first-return paths are counted by twice the Catalan numbers, as in Week 12), and the chance of no return yet by flip 2n is exactly u(n), which shrinks like 1/√(πn) but never reaches 0 in finite time: about 82% are home within 20 flips and 92% within 100. Yet the average time to return is infinite. A child-sized proof uses the road of Week 91 and atlas AP-01: after the first step (say to 1), on the road 0 … m the walker reaches 0 before m with chance 1 − 1/m, which tends to 1 (so return is certain), but the average length of that trip is 1·(m − 1) flips, which grows without bound, so the return time cannot have a finite average. A grid version children can walk: flip two coins, one for east or west and one for north or south, and move diagonally; this is two independent line walks, so the chance of being home at time 2n is u(n)², whose sum diverges like (1/π) ln n, so the walk is recurrent. With three coins (a corner-to-corner walk in 3D) the chance is u(n)³, whose sum converges, and the walker returns with probability about 0.282 (computed here); the usual one-axis-at-a-time cubic walk gives Pólya's 0.3405. The reason in one line: the expected number of visits home is Σ P(home at time 2n), and the walk is recurrent exactly when that sum is infinite. Proved: all of the above. Children can discover that walkers always seem to get home on a line but some take a very long time, that the class average keeps changing as more walks are added (a sign of an infinite mean), and in grades 4–5 why the road argument forces return.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [Pólya's Random Walk Theorem](https://ar5iv.arxiv.org/html/1301.3916). Jonathan Novak (MIT), arXiv 1301.3916. Statement: simple random walk on ℤᵈ is recurrent for d = 1, 2 and transient for d ≥ 3, citing Pólya, Math. Ann. 84 (1921), 149–160 (read November 4, 2026).
- [Pólya's Random Walk Constants](https://mathworld.wolfram.com/PolyasRandomWalkConstants.html). MathWorld (Wolfram Research). p(1) = p(2) = 1; p(3) = 0.3405373…; p(4) = 0.193202 and further values; Watson's 1939 closed form (read November 4, 2026).
- [First passage notes, Math 135A](https://www.math.ucdavis.edu/%7Etracy/courses/math135A/UsefullCourseMaterial/firstPassage.pdf). University of California, Davis course material (no author named on the page). For the fair walk, the first visit to +1 is certain but its expected waiting time is infinite (read November 4, 2026).
- Prior use with children: [Random Walks](https://mathcircle.berkeley.edu/sites/default/files/archivedocs/2013_2014/lecture/1314lecturespdf/BMC-Advanced%20May%206th,%202014.pdf). Paul Zeitz, Berkeley Math Circle, May 6, 2014. Warm-ups on line walks and a problem asking for the chance of returning to the origin in d dimensions (read November 4, 2026).
- Prior use with children: [Random Walk II](https://tasks.illustrativemathematics.org/content-standards/tasks/664). Illustrative Mathematics (a high school task). Coin flips move a person left or right on a number line; flip a real coin first, then ask which positions are possible (read November 4, 2026). No K–5 activity on returning home was found.

## A kid-friendly way in

Materials: a floor number line from −10 to 10 in masking tape (or printed strips per pair), a coin per child, a token, a class chart of "flips until home", and for 4–5 a floor or table grid with two coins of different colours. Prep: tape lines and make the chart, about 20 minutes. Launch (3 minutes): one child stands on 0; heads is a step right, tails a step left; the class counts flips until the child is back on 0. Ask: will every walker get home? How long will it take?

Suggested hour: 0–5 launch; 5–25 pairs walk the line, each walk recorded as a sticker on the "flips until home" chart (stop a walk at 40 flips and mark it "still out"); 25–45 band questions; 45–60 compare the chart's average after 10, 20, 30 walks.

## By band

- **K–1:** Walk the floor line by coin flips until home, several times; put a sticker on the chart for each walk. Did everyone get home? Who took longest?
- **2–3:** What is the fewest flips to get home? Can you ever be home after an odd number of flips? List all ways to be home after 4 flips and count the ones that did not come home earlier. Then work out the class average of the chart and see how it changes when one more long walk arrives.
- **4–5:** Use the road from Week 91: from 1, the walker reaches 0 before 10 with chance 9/10 and before 100 with chance 99/100. What does that say about getting home? Then the two-coin grid walk: is the walker still sure to get home? What changes with three coins (a stack of tables or a printed 3D picture)?

## Checked facts

- `check_week_207()`: first-return chances 1/2, 1/8, 1/16, 5/128, 7/256; for every n < 40, the chance of no return by flip 2n equals C(2n, n)/4ⁿ; home within 20 flips with chance 1 − 184756/1048576 ≈ 0.824, within 100 about 0.920.
- `check_week_207()`: first-return paths number 2, 2, 4, 10, 28 (twice the Catalan numbers), and each has chance 2^(−2n).
- `check_week_207()`: the capped average of the return time, E[min(T, 2N)], is about 7.05, 22.54, 71.36, 225.67 for N = 10, 100, 1000, 10000, within 1.3% of 4√(N/π), so it grows without limit.
- `check_week_207()`: on the road 0 … m, the chance s/m and the duration s(m − s) satisfy the one-step averaging equations for every m ≤ 10.
- `check_week_207()`: the two-coin sums Σ u(n)² grow by about (ln 100)/π between n = 1000 and 100000; the three-coin walk returns with chance 0.28223; the six-direction cubic walk's return chance, recomputed from exact return chances up to 400 steps plus a tail estimate, is 0.3405.
- `check_week_207()`: a seeded run of 2000 walks of 20 flips gets about 82% home.

## Nearest existing themes

Week 91 (Rotor-router machines) has the absorbing road 0 … m, whose exit chance s/m is gambler's ruin, and atlas AP-01 computes the same fair prices; this week uses that result as a lemma and asks a new question, return on an endless line. Week 46 (Two boards forget their starts) is a random walk on the corners of a cube that forgets its start; draft 152 walks a network and compares visit counts (stationary distributions), and draft 173 computes the average length of Snakes and Ladders. Week 44 (The bag that copies) is Pólya's urn, a different theorem of the same mathematician. Week 12 (Catalan bijections) counts the up-down paths that make first returns. What is new: recurrence versus transience, the role of dimension, and an average that is infinite even though return is certain.

## App connection

Region "Chance and machines", possible family "Walk home": the child sets the walker's world (line, flat grid, layered 3D grid), presses Go and watches many walkers at once, with a running tally of "home" and "still out" and a histogram of return times. Puzzle 1: "Predict: will this walker be home within 20 flips? Bet on yes or no over 50 walks." Puzzle 2: "On the road from 1, how long must the road be for the walker to reach 0 first 99 times in 100?" The existing "Flip switches" family (Week 91) already has the road.

## Open questions

- Long walks: some line walks take hundreds of flips; the 40-flip cap must be explained, and "still out" walks must not be dropped from the average.
- Is the infinite-average idea visible from one class chart, or only from the app's large simulations?
- The 3D walk has no comfortable physical version; perhaps adult demonstration only.
- Age fit of the road argument for grades 4–5 without having done Week 91.
