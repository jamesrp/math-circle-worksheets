# Week 145 (draft plan): The fake coin and the balance

**Strand:** logic (Codes and logic), information. **Deep-math field:** search theory, information lower bounds, ternary. **Status:** draft plan, November 2026. No student pages, guide, review card or pilot.

## The deep idea

A pan balance gives one of three answers: left heavier, right heavier, or level. So k weighings, however cleverly chosen, end in at most 3^k different ways, and they can tell apart at most 3^k cases. With one coin known to be heavier, that bound is exact: N coins can be searched in k weighings exactly when N ≤ 3^k (split into three groups as equal as possible, weigh two of them; the answer names the group). So 9 coins need 2 weighings, 10 need 3, and the number of weighings is the base-3 logarithm rounded up. When the fake may be heavier or lighter there are 2N cases, and counting alone would allow 2N ≤ 3^k, that is 13 coins in 3 weighings. The truth is subtler. Theorem (Dyson, with Lyness, Mathematical Gazette, 1946): to name the fake and say whether it is heavy or light in k weighings, with no extra coins, is possible exactly when 3 ≤ N ≤ (3^k − 3)/2; so 12 coins in 3 weighings, 39 in 4, and only 3 in 2. Why not 13: the first weighing puts j coins on each pan; a tilt leaves 2j cases, so j ≤ 4, but then a level result leaves at least 5 coins (10 cases) for two weighings, more than 9. If you only need to name the coin, 13 coins can be done in 3 weighings, and with one extra coin known to be genuine, (3^k − 1)/2 coins can be named with their direction. Dyson's solutions can even be fixed in advance (non-adaptive), by labelling coins with ternary codes, which is the same balanced-ternary idea as Week 30. All of these small cases are checked here by an exhaustive search over weighing strategies. Proved: the 3^k bound and Dyson's theorem. Checked: every count quoted below. Children can discover splitting into three groups rather than two, the counting bound, and the surprise that a bound that fits (26 cases, 27 outcomes) can still fail because of how the first question must be asked.

## Sources

Every link was opened and read on the date given; nothing is cited from memory or from a search snippet.

- [A bounded partition approach to identifying one fake coin and its type](https://arxiv.org/html/2306.10733v1) — Takehiro Tokuda and Yoshimichi Watanabe, arXiv 2306.10733 (submitted June 2023) (read November 4, 2026). States Dyson's 1946 result: n coins can be solved in k weighings when 6 ≤ 2n ≤ 3^k − 3, and not when 2n > 3^k − 3; the variant with one extra genuine coin, solvable for 2m ≤ 3^k − 1; why 1 and 2 coins are unsolvable.
- [Weighing 12 coins](https://www.cut-the-knot.org/blue/weight3.shtml) — Alexander Bogomolny, Cut the Knot (read November 4, 2026). A balanced-ternary labelling solution for 12 coins credited to F. J. Dyson and R. C. Lyness, Math. Gazette 30, October 1946; 27 − 3 = 24 usable labels, paired into 12 coins.
- [Puzzles on Weighing Truth With a Balance Scale](https://www.quantamagazine.org/puzzles-on-weighing-truth-with-a-balance-scale-20220627/) — Pradeep Mutalik, Quanta Magazine, June 27, 2022 (read November 4, 2026). Eight coins with one light fake in two weighings, the 12-coin puzzle and the four-weighing question, as a general-audience framing.
- Prior use with children: [9 Weights](https://nrich.maths.org/5827) — NRICH, ages 11 to 14 (read November 4, 2026): nine weights in two weighings, 27 in three, whether ten can be done in two, and the heavier-or-lighter version. [Find the fake](https://nrich.maths.org/node/62247) — NRICH, ages 14 to 16 (read November 4, 2026): 12 coins, with a published solution from a primary school pupil using four weighings. No K–5 activity was found (searched "counterfeit coin balance activity kindergarten first grade math circle").

## A kid-friendly way in

A real pan balance (a classroom bucket balance) and identical opaque containers, such as film canisters or plastic eggs, each holding the same number of metal washers except one that holds an extra washer. Children take turns as the "faker" (who loads one container in secret) and the "detective", who must find the heavy one with as few weighings as possible; every weighing is recorded as a small picture (which containers on which pan, and which way it tipped). Prep: load 10 to 13 containers per table in two sets (heavy and light versions marked inside the lid), number them with stickers; about 25 minutes, mostly checking that the balance tips clearly. Launch (3 minutes): with three containers, ask the room which two to weigh, do it, and show that one weighing finds the heavy one from three, because "level" is also an answer.

## By band

- **K–1:** Three containers, then four, then nine: find the heavy one. Notice that level points to the one left off. Count weighings with cubes. No reading.
- **2–3:** What is the most containers you can always solve with 2 weighings? With 3? Tables pool results on a chart (3, 9, 27) and test whether 10 can be done in 2. Draw each strategy as a tree of pictures with three branches.
- **4–5:** The fake may be heavy or light, and the detective must also say which. Three containers in two weighings; then the 12 in 3 challenge. Explain why 13 cannot be done in 3 if you must say heavy or light (the first-weighing argument), and why it can if you only name the container. Counting cases (24 and 27) is the entry to the explanation.

## Checked facts

All in `check_logic_games_2.py`, function `check_week_145()`, by exhaustive search over adaptive weighing strategies with equal numbers of coins on each pan:
- One heavy coin: 3, 9, 27 coins in 1, 2, 3 weighings; 4, 10, 28 cannot be done.
- Heavier or lighter, naming direction: with 2 weighings only 3 coins; with 3 weighings exactly 3 to 12 coins. 13 fails although 2 × 13 = 26 ≤ 27.
- Naming the coin only, 3 weighings: 1 and 3 to 13 coins (2 coins never).
- With one extra genuine coin, naming direction: 1 to 4 coins in 2 weighings, 1 to 13 in 3, which is (3^k − 1)/2.
- Two yes-or-no answers separate 4 cases; two weighings separate 9.
- The first-weighing argument for 13: no number j of coins per pan keeps both 2j and 2(13 − 2j) at most 9; and (3^k − 3)/2 is 12 for k = 3 and 39 for k = 4.
- Cited, not computed: Dyson's general theorem for all k (Tokuda and Watanabe; Cut the Knot).

## Nearest existing themes

Week 6 (Code breaking) proves that k yes-or-no answers separate at most 2^k cases and finds a case where counting is too weak; Week 30 (Two-pan weight kits) proves that m weights in three positions give at most 3^m arrangements. The catalog's learning path (`catalog/path.toml`, return visit rv-6, Year 3) already plans "weighing with three outcomes" as a return visit to Weeks 6 and 18, so the heavy-coin core substantially duplicates a planned return visit. The distinct angle for a full week is the heavier-or-lighter problem: Dyson's (3^k − 3)/2, the 13-coin argument that beats counting, and the non-adaptive ternary labelling that ties back to Week 30. If the return visit is built first, this plan should shrink to its 4–5 extension.

## App connection

Codes and logic region, possible family "Balance detective": a row of identical coins, two pans, drag coins on and press Weigh; the app picks the fake adversarially (it answers so as to keep as many cases alive as possible), so children must find a strategy that works against any fake. Puzzles: "Find the heavy coin among 9 in 2 weighings"; "Is 10 possible in 2?"; "12 coins, heavy or light, 3 weighings". The adversary is the honest way to show a lower bound. Week 30's balance art can be shared.

## Open questions

- Material fit: does a classroom bucket balance tip clearly for one extra washer in ten? Rehearse with the actual containers; if not, use a heavier fake (two extra washers).
- Can 2–3 children record a strategy tree, or should an adult scribe the branches?
- Whether to fold the K–1 and 2–3 parts into the Week 6 return visit and keep only the heavy-or-light part here.
- How to keep containers from being identified by sound or feel (padding with cotton wool).
