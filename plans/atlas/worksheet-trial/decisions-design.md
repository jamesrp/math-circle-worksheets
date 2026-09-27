# Four decision and probability worksheet designs

Fixed sample: AP-23, AP-21, AP-01, AP-29. Three student pages each; facilitator material is separate. Original atlas records are preserved.

**Status:** exact checks passed; independent design review completed; maker and independent PDF reviews are recorded separately; not classroom-piloted.

The literal student copy, figures and complete solutions are in `decisions-data.json`. This Markdown is a readable rendering. `decisions-checks.py` independently enumerates/solves the finite instances.

## Print and teaching contract

Use 11.5–12 pt student body text and substantial workspaces. Do not put staged hints, completed code trees, graph edges or correct values on the student pages before the questions intended to elicit them. Cards can remain on the sheet; cutting is optional. Completing all pages is optional.

The educational design follows Week 1’s objects → representation → certificate → variation progression and the book-based `plans/lesson-format-source-notes.md`, particularly reducing copying and allowing different stopping points. These are design inferences, not classroom results.

## AP-23 — The route everyone wants

Can every traveler be sensible and the group still do worse?

**Assessment:** Strong worksheet candidate after replacing the original tie-based toy by a sharper instance. The six-state tie variation is a genuine dynamics question, not just another total-cost table.

**Arc:** Play with named travelers → compress eight named states into four crowds → compare directed personal improvements with group cost → change one number and obtain a six-state loop.

- **entry:** Count to three, add costs up to 15, move one named counter at a time. An adult can read the rules.
- **satisfying core:** Compare a traveler’s current cost with that same traveler’s cost after joining the other route; distinguish personal improvement from total improvement.
- **extension:** Trace a directed state graph; no algebra or calculus.
- **honest limit:** A drawing of four occupancies suffices because travelers have identical cost rules. Different personal rules would require remembering who is where.

**Materials/prep:** Three differently colored counters (R, G, B); the route mat on page 1; pencil. Optional cost counters. No scissors required. About 5 minutes.

**Suggested hour:** 0–8 move counters freely and practice charging costs; 8–22 search for stable arrangements; 22–35 explain the inefficient stable state; 35–40 stand in the two routes; 40–55 choose the tie variation; 55–60 explain one distinction. Pages are choices, not a completion quota.

### Student page 1: 1. Choose your road

Three travelers R, G and B each choose one road. On the QUICK road, each traveler pays 1 if alone, 3 if there are two, or 5 if there are three. On the STEADY road, each always pays 4. Lower is better. All travel at the same time; these are costs, not a race.

**23.1** Try at least three arrangements. For each, record who is on QUICK, each traveler’s cost, and the group’s total. Which arrangement would you choose as the group’s planner?

*Workspace/figure:* Route mat about 6.5 × 2 in; three trial rows with columns QUICK names | R cost | G cost | B cost | total.

**23.2** Now be one traveler. Move only your counter, and only when YOUR new cost is strictly smaller. Recalculate QUICK after you join or leave! Keep moving until nobody can improve. Can you find a stopped arrangement with a different number on QUICK?

*Workspace/figure:* A four-row crowd table: number on QUICK 0, 1, 2, 3; cost for each QUICK traveler; cost for each STEADY traveler; stopped? Leave answers blank; use a dash when a road is empty.

**23.3** Complete the crowd map. Draw an arrow when one traveler can move to a neighboring box and strictly improve. Circle every box where play can stop.

*Workspace/figure:* Four large boxes in a horizontal line labeled only 0 on QUICK, 1, 2, 3. Draw no arrows in advance.


### Student page 2: 2. What changes when G switches?

Keep the same costs: QUICK 1 / 3 / 5 per traveler; STEADY 4. A stopped arrangement is called stable: nobody can lower their own cost by moving alone.

**23.4** Start with R alone on QUICK, and G and B on STEADY. G switches to QUICK. Show the before-and-after costs. Who benefits? Who is worse off? What happens to the total?

*Workspace/figure:* Two large before/after route pictures; blank R/G/B cost labels and a total box under each. 3 explanation lines.

**23.5** Find the cheapest total and prove no arrangement is cheaper. Then explain why the travelers do not stay there under the strict-improvement rule. Your proof should cover every possible crowd, not just three examples.

*Workspace/figure:* Four total-cost boxes aligned with crowds 0, 1, 2, 3; 5 lines or a drawing area.

**23.6** The travelers are at a stable arrangement. Can one traveler’s move lower the GROUP’s total even though that traveler refuses to make it? Draw one such move and label every changed cost. What did “stable” fail to guarantee?

*Workspace/figure:* Blank paired route mats and 4 explanation lines.


### Student page 3: 3. When “just as good” is good enough

Change STEADY’s cost to 3. QUICK still costs 1 / 3 / 5. First keep the strict-improvement rule. Then try this NEW rule: a traveler may move whenever the new cost is no larger, including a tie.

**23.7** Under the strict rule, which crowd sizes are stable now? Under the new tie rule, can play continue forever? Act out an example.

*Workspace/figure:* Mini crowd ladder and 3 record lines.

**23.8** A box lists exactly the travelers on QUICK; everyone else is on STEADY. Join two boxes when ONE traveler can switch between them at unchanged personal cost. Put an arrow in each allowed direction. Find a loop visiting all six boxes once before returning.

*Workspace/figure:* Six blank-edge state boxes around a hexagon in this order: R, RG, G, GB, B, RB. No edges printed.

**23.9** Label each box with the group’s total cost. Around your loop, does the total always decrease? Explain how each moving traveler can avoid doing worse while the group sometimes does worse.

*Workspace/figure:* Total-cost blank beside each of the six boxes; 5 explanation lines.

### Separate facilitator material

**Solutions to every prompt**

**23.1:** Any three arrangements are legitimate experiments. By QUICK occupancy n=0, 1, 2, 3, group totals are 12, 9, 10, 15. The planner chooses exactly one on QUICK; the named traveler is arbitrary.

**23.2:** For n=0 all pay 4 and a mover can get 1; n=1 QUICK pays 1, STEADY pays 4, and a STEADY traveler can join QUICK for 3; n=2 QUICK pays 3, STEADY pays 4, and neither type improves by switching (3→4 or 4→5); n=3 all pay 5 and any one can move to STEADY for 4. Only n=2 is stable. Emphasize that joining QUICK changes its cost.

**23.3:** Arrows 0→1, 1→2, 3→2. No other strict-improvement arrows. Exactly one stable crowd size, n=2; three named stable arrangements. Compressing names is valid here because the rules treat all travelers identically. Every legal strict sequence stops after at most two moves.

**23.4:** Before: R=1, G=4, B=4, total 9. After: R=3, G=3, B=4, total 10. G improves by 1, R worsens by 2, B is unchanged. The group loses 1 overall. G imposes a crowding cost on R that G does not pay.

**23.5:** Enumerate all four occupancies:12, 9, 10, 15. Exactly one on QUICK is the minimum 9. This covers every named arrangement because names do not affect costs. It is unstable: either STEADY traveler can lower their own cost 4→3 by joining QUICK, raising the total 9→10.

**23.6:** At n=2, one QUICK traveler may move to STEADY. That traveler’s cost rises 3→4, the remaining QUICK traveler improves 3→1, and the other STEADY traveler stays 4. Total 10→9. Individual stability guarantees only the absence of a personally profitable one-person move; it does not guarantee the least group total.

**23.7:** With STEADY 3: n=0 has a strict move 3→1; n=1 has no strict move because joining QUICK costs 3, a tie; n=2 has no strict move because leaving QUICK costs 3, a tie; n=3 has a strict move 5→3. Thus n=1 and 2 are stable under strict moves. With ties allowed, a traveler may alternate between QUICK and STEADY while one other remains on QUICK, producing endless play. No simultaneous moves are needed.

**23.8:** The only edges are R↔RG↔G↔GB↔B↔RB↔R. A move adds or removes one name, switching between one and two QUICK travelers. The mover pays 3 on either road. Opposite pairs such as R and GB change three names and are illegal. The printed cyclic order offers one valid six-state tour; students may traverse it either way or begin anywhere.

**23.9:** Singleton boxes total 1+3+3=7; two-name boxes total 3+3+3=9. The six-state loop alternates 7, 9, 7, 9, 7, 9. The moving traveler stays at 3; the other QUICK traveler changes 1↔3. The group need not improve when the mover alone does not worsen.

**Staged hints — offer only after exploration**

1. (23.2–23.3) Cover everyone except the traveler about to move. What does that traveler pay after the move, including their own arrival?
2. (23.5) Forget the names briefly. How many travelers could QUICK have?
3. (23.8) Compare R with RG. Which one person moved? What did that person pay before and after?

**stop:** Stop after 23.5 with a checked stable arrangement, a cheaper group arrangement and an explanation of the conflict. The six-state loop is an extension, not an obligatory second lesson.

**adult math:** An exact finite atomic congestion game. The base is stronger than the atlas instance because the inefficient equilibrium has no indifferent escape: the efficient pattern is strictly unstable. In the base, a congestion potential has values 12, 9, 8, 9 across crowds 0, 1, 2, 3 and decreases at each strict personal improvement; total cost has different values. The worksheet does not need this theorem or name.

**prior use:** The current route worksheets study edge traversal. Week 1 studies undirected tiling flips. This asks who bears a move’s cost and contrasts strict versus weak improvement. The six-state shape is not claimed novel by itself.

**source note:** Adapted mathematical framework from the AP-23 source below; all numerical games, graph prompts and solutions here are new independently checked instances. No claim of a classroom pilot.

**Source trail**

- Giacomo Bonanno, Game Theory, Section 1.6: Nash equilibrium; finite congestion instance checked directly. https://arxiv.org/pdf/1512.06808 (named source scope inspected; displayed finite result proved directly here)

**Programmatic figure specification**

```json
{
  "route_mat": {
    "quick": "Two branches from HOME to PARK; QUICK upper road, STEADY lower road. Distinct grayscale line styles, not color-dependent. Put cost badge QUICK: 1 person→1 each; 2→3 each; 3→5 each. STEADY:4 each. Use broad empty roads for physical counters.",
    "tokens": [
      "R",
      "G",
      "B"
    ]
  },
  "crowd_ladder": {
    "nodes": [
      0,
      1,
      2,
      3
    ],
    "student_edges": true,
    "solution_directed_edges": [
      [
        0,
        1
      ],
      [
        1,
        2
      ],
      [
        3,
        2
      ]
    ]
  },
  "externality_pair": {
    "before": {
      "QUICK": [
        "R"
      ],
      "STEADY": [
        "G",
        "B"
      ]
    },
    "after": {
      "QUICK": [
        "R",
        "G"
      ],
      "STEADY": [
        "B"
      ]
    },
    "student_costs_blank": true
  },
  "tie_hexagon": {
    "cyclic_order": [
      "R",
      "RG",
      "G",
      "GB",
      "B",
      "RB"
    ],
    "student_edges": true,
    "solution_edges": "Adjacent nodes in the displayed cyclic order, in both directions. No diagonals."
  }
}
```

## AP-21 — The robot’s five-day battery

A good plan—and a way to prove it is best

**Assessment:** Strong for children who enjoy planning. The original three-day counterexample was too slight. Five offers, converging histories, a compact backward certificate and a changed ending produce real substance without a 30-cell arithmetic drill.

**Arc:** Choose a plan → defeat two tempting local rules → notice histories that share a future → certify a global maximum by reusing a small set of subproblems → change the last offer and revise the plan.

- **entry:** Count and spend up to 5 battery tokens; add rewards up to 18. Read a five-day order, with oral help if desired.
- **satisfying core:** Keep a fixed resource budget and justify an upper bound by cases.
- **extension:** Reason backward about best possible future scores; no algebra or calculus.
- **honest limit:** All offers are visible in advance. This is not a strategy for an unknown future. The future depends on day and battery, while total score also includes points already earned.

**Materials/prep:** Five battery counters, about 20 reward counters or a written score, and five printed offer cards. Cross off each day as it passes. Scissors optional: cards can remain on the sheet. About 7 minutes.

**Suggested hour:** 0–10 act out a couple of plans; 10–25 improve them; 25–35 compare the two histories; 35–40 swap planner/robot roles; 40–55 use the backward certificate or changed ending; 55–60 explain why the bound covers all choices.

### Student page 1: 1. Spend now or save?

The robot begins day 1 with 5 battery tokens and 0 points. Each day it may take that day’s job once, paying the battery cost and earning the points, or skip it. Spent battery never returns. No recharge. All five jobs are known now.

**21.1** Act out three different plans. Record the days you take, battery spent and points earned. What is your best score? Can your partner beat it?

*Workspace/figure:* Five big offer cards; three plan rows; a 5-token battery parking strip.

**21.2** A robot says, “Take each job when it comes, whenever I have enough battery.” Another says, “Choose the job with the biggest point reward first, then fit in what else I can.” Try both suggestions. Can you do better than either?

*Workspace/figure:* Two labeled robot proposal boxes with blank selected days / battery / score; 4 lines for an improved plan.

**21.3** Your best plan is a construction. What would convince someone that NO plan earns more? Keep your current best below; we will build a certificate on the next pages.

*Workspace/figure:* Large best-plan box and 3 lines. Do not request a full proof yet.


### Student page 2: 2. Two different pasts, one future

The five jobs stay visible. We are just about to begin day 3.

**21.4** Robot X took day 1 and skipped day 2. Robot Y skipped day 1 and took day 2. Fill in their battery and points. Which remaining jobs would you recommend to X? To Y? Explain what can be shared and what cannot.

*Workspace/figure:* Two timeline strips through days 1–2 with TAKE/SKIP already indicated. Blank current battery and score; common remaining-job strip for days 3, 4, 5.

**21.5** Make a help card for any robot beginning day 4. Only days 4 and 5 remain. Find the largest EXTRA score for each battery amount 0, 1, 2, 3, 4, 5. Explain why the answer stops rising.

*Workspace/figure:* Small 6-column table headed battery 0, 1, 2, 3, 4, 5; blank extra-score row and optional take-day row; 4 explanation lines.

**21.6** A robot starts day 3 with 3 battery. Compare taking day 3 with skipping it. Use your help card instead of listing every complete five-day story. Does the robot’s earlier score change the best recommendation?

*Workspace/figure:* Two branches: TAKE day 3 / SKIP day 3. Blank immediate score, battery before day 4, best later score and sum; 4 lines.


### Student page 3: 3. A proof that works backward

“Best extra score” means only points from the named day onward. Once a help card is proved, anyone with that day and battery can use it. Job cards: day 1 costs 2/pays 5; day 2 costs 2/pays 6; day 3 costs 3/pays 9; day 4 costs 1/pays 4; day 5 costs 2/pays 8.

**21.7** Complete these three day 3 help cards by comparing TAKE with SKIP. Battery 1: __. Battery 3: __. Battery 5: __. Use the day 4 card you already made. Show both possibilities whenever taking is legal.

*Workspace/figure:* Three branching boxes, each with battery amount supplied; blank take value, skip value and best.

**21.8** Certify your best score. Work through decision boxes (a)–(c) in order, comparing TAKE with SKIP. Then use box (d) to trace a plan that reaches the bound.

*Workspace/figure:* Four spacious compare boxes: (a)day 2, battery 3; (b)day 2, battery 5; (c)day 1, battery 5; (d)trace chosen days. Reference arrows point from 21.7 battery 1/3/5 to the two day 2 boxes, then to day 1.

**21.9** Change only day 5’s reward from 8 points to 3. Find a new best plan. Is there more than one? What part of your old reasoning must be updated? This is an optional fresh investigation: do not assume the old plan stays best.

*Workspace/figure:* Changed day 5 card and two blank plan rows; a 3-row proof table headed day 3 taken / day 3 skipped, day 2 taken / day 3 and day 2 skipped.

### Separate facilitator material

**Solutions to every prompt**

**21.1:** Many feasible plans. Unique optimum is days 2, 4, 5: battery 2+1+2=5, points 6+4+8=18. Let students find it before offering structural hints.

**21.2:** Chronological take-when-possible chooses days 1, 2, 4, spends 5, earns 5+6+4=15. Highest reward first chooses day 3 (9 points, cost 3), then day 5 (8, cost 2), earning 17. Days 2, 4, 5 earn 18. The second rule here chooses among all visible offers, then schedules selected offers on their proper days. Neither counterexample says every greedy rule always fails.

**21.3:** Accept an explicitly feasible candidate and an honest distinction between finding a plan and excluding better plans. Possible future proof ideas: list all feasible subsets, split into take/skip cases, or develop reusable best-future cards. A guessed maximum is not yet a certificate.

**21.4:** X: battery 3, earned 5. Y: battery 3, earned 6. Both should skip day 3 and take days 4, 5 for 12 more points. Final totals 17 and 18. They share the best future decisions and extra score because day and battery coincide. They do not share the points already earned. An earlier score is an additive constant in the future optimization, so it does not change the maximizing continuation.

**21.5:** For battery 0, 1, 2, 3, 4, 5, best extra scores are 0, 4, 8, 12, 12, 12. With 0 take none; with 1 take day 4; with 2 take day 5; with 3+ take both. Rewards are positive and each remaining job is available at most once. More than 3 battery buys no new job; the maximum remains 12.

**21.6:** Take day 3: gain 9 now, no battery remains, extra total 9. Skip: retain 3 for days 4, 5, whose proved value is 12. Skip is better. Earlier earned points add equally to both alternatives, so they cannot change this comparison.

**21.7:** Before day 3, battery 1: cannot take cost 3, so value 4 from day 4 card. Battery 3: max(9+0, 12)=12. Battery 5: max(9+8, 12)=17. The 8 is day 4 value with 2 battery, achieved by skipping day 4 and taking day 5. This is why one must track battery as well as day.

**21.8:** (a)Day 2, battery 3: take gives 6+V(day 3, 1)=10, skip givesV(day 3, 3)=12, so value 12. (b)Day 2, battery 5: take 6+V(day 3, 3)=18, skipV(day 3, 5)=17, so value 18. (c)Day 1, battery 5: take 5+V(day 2, 3)=17, skipV(day 2, 5)=18, so value 18. (d)Trace skip 1, take 2, skip 3, take 4, take 5. At each card the take/skip split exhausts all legal possibilities, and the later values have already been proved. Therefore 18 is both an upper bound and achieved, not just the largest tried plan.

**21.9:** There are exactly two optimal plans, days 2, 3 and days 1, 2, 4, each worth 15. With day 3 taken, remaining battery 2 can add at most 6 (day 2 beats day 1=5, day 4=4, day 5=3), giving at most 15. If day 3 skipped and day 2 taken, there are 3 battery left for days 1, 4, 5: day 1+day 4 gives 9, larger than day 4+day 5=7, so total at most 15. If both day 3 and day 2 skipped, all of days 1, 4, 5 fit at cost 5 and pay 12. These cases cover every plan. The day 4 help-card row changes to 0, 4, 4, 7, 7, 7; the affected later-to-earlier cards must be recomputed. Full changed value rows are in decisions-checks-results.json. It is legitimate to ignore the old table and give the three-case certificate instead.

**Staged hints — offer only after exploration**

1. (21.1–21.3) Try a plan that skips day 1. A maximum needs both a plan and a reason no better plan can exist.
2. (21.4) Put earned points in a separate pile. Which objects can affect what jobs the robot is still able to take?
3. (21.7–21.8) Every plan either takes today’s job or skips it. If it takes the job, what exact day and battery will it have next?

**stop:** A feasible 18-point plan plus a convincing take/skip upper bound is a complete investigation. The changed ending can be a separate revisit. Do not turn the six-state certificate into a mandatory full 30-cell table.

**adult math:** A deterministic finite-horizon dynamic program; the worksheet creates common subproblems before naming a backward method. V(d, e)=max(V(d+1, e), reward_d+V(d+1, e−cost_d)) over legal actions. The proof is backward induction. Converging histories motivate state sufficiency and, in forward search, dominance by larger earned score.

**prior use:** Weeks 7–8 use backward winning states in adversarial games. This task uses a resource state, accumulated reward and optimization against constraints, with no opponent. These are related proof habits but different questions.

**source note:** Source framework from AP-21. The five-job instance, all state cards and changed-ending classification were checked independently by exhaustive subset enumeration for every day/battery state.

**Source trail**

- Jeffrey Chasnov, Mathematical Biology, Chapter 7.3: dynamic programming located; this finite resource recurrence is self-contained. https://www.math.hkust.edu.hk/~machas/mathematical-biology.pdf (dynamic-programming chapter located in authored contents; this finite decision recurrence has a complete independent proof)

**Programmatic figure specification**

```json
{
  "offer_cards": {
    "days": [
      1,
      2,
      3,
      4,
      5
    ],
    "battery_cost": [
      2,
      2,
      3,
      1,
      2
    ],
    "points": [
      5,
      6,
      9,
      4,
      8
    ],
    "labels": [
      "A",
      "B",
      "C",
      "D",
      "E"
    ],
    "dimensions": "Five equal-width cards with large day, battery icons plus numeral, reward-star icons plus numeral. Do not draw18 tiny stars; numbers suffice."
  },
  "converging_histories": {
    "X": {
      "day1": "take",
      "day2": "skip"
    },
    "Y": {
      "day1": "skip",
      "day2": "take"
    },
    "merge_state": {
      "before_day": 3,
      "energy": 3
    },
    "earned_scores_blank": true
  },
  "backward_certificate": {
    "states": [
      [
        3,
        1
      ],
      [
        3,
        3
      ],
      [
        3,
        5
      ],
      [
        2,
        3
      ],
      [
        2,
        5
      ],
      [
        1,
        5
      ]
    ],
    "meaning": "[day,battery]",
    "blank_answers": true,
    "dependencies": {
      "2,3": {
        "take": "6 + V(3,1)",
        "skip": "V(3,3)"
      },
      "2,5": {
        "take": "6 + V(3,3)",
        "skip": "V(3,5)"
      },
      "1,5": {
        "take": "5 + V(2,3)",
        "skip": "V(2,5)"
      }
    },
    "student_notation": "Use words “6 now + best from day3 with1 battery”; symbolic V is facilitator-only."
  }
}
```

## AP-01 — A fair price for a wandering token

Chance heights—and a shortcut that changes less than you expect

**Assessment:** Worth making, but the honest complete version needs halves/quarters and first-step reasoning. Playing with a coin alone is only an entry. The ferry variation earns its third page by separating path duration from endpoint chance.

**Arc:** Follow unpredictable paths → price a known endpoint reward → derive a local balance rule → force the whole height map → redesign the transitions while preserving the same endpoint chances.

- **entry:** Move a counter one step and follow heads/tails. Counting trials is optional.
- **satisfying core:** Halves and quarters; average two quantities, or use equal height gaps and a balance argument. Distinguish a trial from an exact probability.
- **extension:** Multiply fractions for the optional almost-sure stopping argument; limits are an adult extension. No calculus required.
- **honest limit:** A few trials do not prove the probabilities. Expected reward and average-of-neighbors need explanation; do not call this a complete probability lesson for a child who is only following the moves.

**Materials/prep:** A coin, a counter, pencil, and optionally stacking cubes for chance heights. Use a fair coin model: each toss has independent half-chances. A physical coin is an implementation, not a proof of fairness. About 5 minutes.

**Suggested hour:** 0–8 explore paths; 8–15 record at most 4 completed trials; 15–35 build and justify the height map; 35–40 walk the track physically; 40–55 try the ferry; 55–60 compare exact evidence and experiment.

### Student page 1: 1. Which shore?

Use a fair coin with independent tosses. Choose a start at 1, 2 or 3 on the track 0–1–2–3–4. Heads moves one step right; tails one step left. Stop at shore 0 or shore 4. Reaching 4 wins 4 prize counters; reaching 0 wins none. There is no prize for a long walk.

**01.1** Try the walk from two different starting places. Record at most four finished trips. Before more tossing, predict: which start gives the best chance of reaching 4? Can any of those starts guarantee a win?

*Workspace/figure:* Large 0–4 track; four rows for start / a short path or toss record / finishing shore. Stop recording after 4 trials.

**01.2** Imagine buying a token already standing at 1, 2 or 3. A fair price equals its average eventual prize over many independent games. Guess a fair price for each start. Record a reason, not just a fraction from your four trips.

*Workspace/figure:* Three price tags under positions 1, 2, 3; endpoint tags 0 and 4 filled; 5 lines for prediction.

**01.3** Two students disagree: “Start 2 must win because it is in the middle.” “Start 2 wins about half the time because left and right paths can be paired.” Which argument makes sense? Explain what you think happens.

*Workspace/figure:* 4 lines and a blank mirrored-path sketch area.


### Student page 2: 2. Build a chance skyline

The endpoints have prices 0 and 4. At any interior place, one fair toss sends the token to one of two neighbors. Use that first toss to reason about the price HERE before you know the whole path.

**01.4** If the two possible next places have prices a and b, what fair price should HERE have? Explain with two equally likely possibilities. Use words, a balance drawing or an equation.

*Workspace/figure:* Empty split-arrow diagram from HERE to two boxes a and b.5 lines.

**01.5** Choose heights at 1, 2, 3 so every interior height balances its two neighboring heights. Draw your skyline. Then try changing just one height. Can a different skyline still satisfy every balance?

*Workspace/figure:* Large coordinate grid with x labels 0, 1, 2, 3, 4 and height labels 0, 1, 2, 3, 4; endpoint dots(0, 0), (4, 4) only. Three blank price boxes.

**01.6** Give a reason that forces your heights. What does “middle height equals the average of its neighbors” say about the two gaps beside it? Finally turn your prices into chances of winning 4 counters.

*Workspace/figure:* Four blank adjacent-gap labels and chance boxes at 1, 2, 3; 5 lines. Do not preprint equal gaps or the diagonal line.


### Student page 3: 3. A ferry at the middle dock

Change only the move from 2. At 2, heads now ferries the token straight to 4; tails ferries it straight to 0. From 1 and 3, keep the old one-step rule. The coin is still fair and independent. Stop at either shore as before.

**01.7** Before playing, predict which starting places have a changed chance of winning. Draw new fair prices on the ferry map. Check the first-step balance at EVERY interior place, including the ferry dock.

*Workspace/figure:* A fresh 0–4 map with explicit directed arrows 1→0/2, 2→0/4, 3→2/4; blank interior price tags.

**01.8** What changed: the possible paths, the winning chances, or both? Does having a shorter route to a shore automatically mean a better chance of reaching 4? Give evidence from this game.

*Workspace/figure:* 4–5 lines. Optional two trial rows only; do not suggest trials prove equality.

**01.9** Design a fair shortcut on 0–1–2–3–4–5–6. Keep prize 6 at the right shore and 0 at the left. Ordinary one-step moves have prices 0, 1, 2, 3, 4, 5, 6. Change the TWO destinations from one interior place so its old price still balances them. Show your arrows and explain. Both destinations must differ from the starting place.

*Workspace/figure:* Large blank 0–6 board with endpoint shore labels. Space for a changed start and H/T destinations, plus 4 lines.

### Separate facilitator material

**Solutions to every prompt**

**01.1:** Valid records follow H:right, T:left and stop on first reaching a shore. Higher starts have larger exact winning chances:1/4, 1/2, 3/4. No interior start guarantees a win; an appropriate finite run of tails reaches 0 with positive probability. Any trial pattern, including four identical results, is acceptable experimental evidence and does not refute the exact probabilities.

**01.2:** Predictions are provisional here. Exact fair prices later are 1, 2, 3 for starts 1, 2, 3. Avoid grading guesses by proximity. Ask whether the reason distinguishes an endpoint prize from the number of tosses.

**01.3:** The pairing argument is valid: reflect a path across the middle and interchange heads/tails to exchange its two endpoint outcomes while preserving probability. It does not make an individual path win. A full claim of half each also uses eventual arrival with probability 1; the elementary first-step map below independently gives the winning probability. The first statement confuses symmetry with certainty.

**01.4:** Fair price is(a+b)/2: there are two equally likely next situations, so expected future prize averages their values. Integer-price balance can be written 2×HERE=a+b, avoiding fraction notation initially. If p_i is the eventual winning probability, the same conditioning gives p_i=(p_left+p_right)/2. The existence of a well-defined eventual hitting event makes this equation legitimate, not an inference from simulation.

**01.5:** Heights 0, 1, 2, 3, 4 balance every interior place. No other skyline with these endpoint heights works. Changing one interior height while freezing the others breaks at least that point’s balance. To exclude coordinated changes as well, use 01.6, not just this perturbation test.

**01.6:** If 2 b=a+c, thenb−a=c−b: the two adjacent gaps agree. Applying this at 1, 2, 3 forces all four gaps equal. Their total is 4, so each gap is 1. Thus prices 1, 2, 3 are uniquely forced. The prize is 4 on a win and 0 otherwise, so price=4×winning chance: chances 1/4, 1/2, 3/4. The proof is a local-to-global uniqueness argument, not curve-fitting.

**01.7:** The prices remain 0, 1, 2, 3, 4. At 1:(0+2)/2=1; at 2:(0+4)/2=2; at 3:(2+4)/2=3. Since the ferry dock terminates immediately at a shore on its next toss, its price 2 is directly fixed. The prices at 1 and 3 then follow directly; these equations have no alternate solution. All three winning chances are unchanged.

**01.8:** Paths and duration changed; winning chances did not. From 2 the ferry ends after exactly one toss, whereas an ordinary walk from 2 cannot reach a shore before two tosses. Yet both give chance 1/2 of winning. With the ferry, no game from an interior start lasts more than two tosses. Original games can be arbitrarily long, though terminate with probability 1. Faster arrival is not by itself a higher chance of the right endpoint.

**01.9:** If a changed start is i and destinations are a, b, old prices stay balanced exactly whena+b=2 i, with 0≤a, b≤6 and a, b≠i. Valid new choices include start 2→0/4, start 3→0/6 or 1/5, start 4→2/6. Starts 1 and 5 have no distinct-destination longer jump within the board; their only unordered pair is 0/2 or 4/6. Swapping H/T labels makes the same average. A completed answer must state both destinations, not just the favorable jump. For the single modified site, eventual absorption still holds: from any site, repeatedly choosing a rightward destination reaches 6 in at most 6 moves, probability at least 1/64 per independent block. The unchanged linear prices satisfy the first-step system uniquely. For elementary learners, validating the local balance is the intended stopping point; claiming a general stopping theorem is unnecessary.

**Staged hints — offer only after exploration**

1. (01.4) Imagine many tokens, half arriving at one neighbor and half at the other. What is their average value?
2. (01.5–01.6) A balanced middle height has the same rise from its left neighbor as to its right neighbor. Follow that condition across the whole track.
3. (01.7–01.9) A shortcut replaces the two possible next prices. Check their average, not how far the token travels.

**stop:** A justified 0, 1, 2, 3, 4 price skyline and the quarter/half/three-quarter chances. A younger child who only plays has explored the object but has not completed this argument; record that distinction honestly.

**adult math:** Discrete harmonic functions and a finite Dirichlet problem. The linear solution arises from equal first differences. Almost-sure absorption in the ordinary walk: a block of 3 all-heads tosses reaches 4 from any interior state, with probability 1/8; survival afterk independent blocks is at most(7/8)^k→0. Finite first-step equations already suffice to derive the probability of the eventual winning event; absorption additionally guarantees the two shore events exhaust outcomes up to probability 0. Expected toss counts, not required on student pages: ordinary(0, 3, 4, 3, 0), ferry(0, 3/2, 1, 3/2, 0).

**prior use:** Week 1’s extension samples an ongoing tiling-flip walk and asks about visit frequencies/return times. This has absorbing shores, exact hitting probabilities, an affine harmonic function and a changed transition preserving the boundary chances. Do not count mere coin-tossing as novelty.

**source note:** Source framework from AP-01. Ferry, price representation and shortcut design are independently checked adaptations. Prices are imaginary prize counters, not financial guidance.

**Source trail**

- Grinstead and Snell, Introduction to Probability, Chapters 4 and 12.2. https://math.dartmouth.edu/~prob/prob/prob.pdf (relevant exposition inspected; finite instance independently derived below)

**Programmatic figure specification**

```json
{
  "ordinary_walk": {
    "positions": [
      0,
      1,
      2,
      3,
      4
    ],
    "endpoint_reward": [
      0,
      4
    ],
    "arrows": "One-step arrows, heads right/tails left; endpoints absorbing. Use clear arrowheads, no arrows leaving shores."
  },
  "first_step": {
    "source": "HERE",
    "destinations": [
      "a",
      "b"
    ],
    "probabilities": [
      "half",
      "half"
    ]
  },
  "chance_skyline": {
    "x_range": [
      0,
      4
    ],
    "y_range": [
      0,
      4
    ],
    "grid_step": 1,
    "printed_points": [
      [
        0,
        0
      ],
      [
        4,
        4
      ]
    ],
    "student_points": true
  },
  "ferry_walk": {
    "outgoing": {
      "1": {
        "T": 0,
        "H": 2
      },
      "2": {
        "T": 0,
        "H": 4
      },
      "3": {
        "T": 2,
        "H": 4
      }
    },
    "route_arcs": "Draw ferry arcs above the track to the shores; ordinary one-step arrows below it to avoid ambiguous crossings."
  },
  "design_shortcut": {
    "positions": [
      0,
      1,
      2,
      3,
      4,
      5,
      6
    ],
    "student_arrows": true,
    "valid_changed_destination_examples": {
      "2": [
        [
          0,
          4
        ]
      ],
      "3": [
        [
          0,
          6
        ],
        [
          1,
          5
        ]
      ],
      "4": [
        [
          2,
          6
        ]
      ]
    }
  }
}
```

## AP-29 — Send it with fewer bits

Short names, missing spaces, and two rival trees

**Assessment:** Very strong worksheet candidate. It has physical message strips, a real ambiguity, freely designed codes, a finite optimality certificate and a frequency change that reverses the winning tree.

**Arc:** Send real concatenated messages → see what missing separators can break → build a leaf code → justify optimal labeling and classify shapes → change frequencies and make the old best lose.

- **entry:** Match four symbols, read 0/1 strings left to right and count bits. An adult can read instructions.
- **satisfying core:** Repeated addition for weighted length, branching diagrams, and explaining why an example works for every concatenation.
- **extension:** Classify full binary trees with four leaves and compare costs; no probability or logarithms needed.
- **honest limit:** Optimality is proved among binary prefix codes, not all conceivable communication schemes. No free spaces, timing gaps, punctuation or hidden lengths are allowed.

**Materials/prep:** Four distinct simple icons (A=triangle, B=circle, C=square, D=star), message strip ABACABDA, pencil, and optional movable icon labels. A paper divider can hide the sender’s original message. About 8 minutes.

**Suggested hour:** 0–10 send short strings with the fixed-length code; 10–20 discover ambiguity; 20–35 design a shorter prefix code; 35–40 walk left/right tree branches; 40–55 prove optimality or change frequencies; 55–60 decode a partner’s test string.

### Student page 1: 1. No spaces allowed

A sender uses only 0 and 1. The receiver sees one long string, with no spaces, pauses or punctuation. Our four pictures are A△, B○, C□ and D☆. The day’s message strip is A B A C A B D A. Spaces on this picture strip are for the sender only.

**29.1** First use A=00, B=01, C=10, D=11. Send the strip to a partner. The receiver marks the boundaries and restores the pictures. How many bits did you send?

*Workspace/figure:* Eight picture tiles ABACABDA, 16 empty bit boxes with no preprinted group dividers, and a receiver picture row.

**29.2** A sender proposes A=0, B=01, C=10, D=11. Can the string 010 mean two different picture messages? Show both readings. What went wrong?

*Workspace/figure:* One 010 strip printed twice; ample room for cut marks and decoded pictures.4 explanation lines.

**29.3** Build a shorter reliable code for the original eight-picture strip. Use a branching tree: each left edge sends 0, each right edge sends 1, and put each picture at a LEAF, where that path ends. A picture may not sit partway along another picture’s path. Try to beat 16 bits.

*Workspace/figure:* Large blank rooted tree workspace (root only), four blank code boxes and a total-bit box. Do not supply the 1, 2, 3, 3 tree yet.


### Student page 2: 2. How do you know it is best?

Use the original counts: A appears 4 times, B 2 times, C 1 time and D 1 time. A picture’s code length is its number of edges from the root. A tree is full when every branching point has two children.

**29.4** Look at a tree with a one-child branching point. Can removing that unnecessary step ever make any message longer or confuse two leaves? Explain why a best tree can be full.

*Workspace/figure:* A small illustrative tree with root→single child→two leaves; second branch-free shortened version left blank.4 lines.

**29.5** Find the full binary tree shapes with exactly four leaves. Ignore left/right mirror flips. At the root, how many leaves can go on each side? Draw the possibilities; then decide which leaf should get each picture.

*Workspace/figure:* Two generous blank tree frames, each with only a root and two short branches. Label prompts: root split __ + __. No completed tree shapes printed.

**29.6** Compute the best total bits for each shape. Explain why moving a more frequent picture to a shorter path cannot hurt. Use that fact and your shape list to prove that your best code cannot be beaten by a prefix code.

*Workspace/figure:* Two weighted-total record rows; 5–6 proof lines. Counts 4, 2, 1, 1 printed as movable-looking icon chips; no finished code supplied.


### Student page 3: 3. A new day, a different best tree

Keep four pictures and binary prefix codes. Only the frequencies change.

**29.7** New message strip: A B C D A B C D. Which of your two tree shapes wins now? Could yesterday’s shortest-total code be worse today? Show the bit totals.

*Workspace/figure:* Eight icon tilesABCDABCD; balanced-shape and long-branch-shape cost boxes; 4 lines.

**29.8** Invent a SIX-picture strip using every picture at least once, for which the two tree shapes have the SAME best total length. Show your strip, a best code of each shape and both totals.

*Workspace/figure:* Six empty icon slots; two code tables A/B/C/D with blank codewords; total boxes.

**29.9** Trade codes and invent a difficult test message for your partner. Send only the bits. The receiver must decode it without guessing. Explain why stopping at a leaf and returning to the root always works for your code.

*Workspace/figure:* One long blank bit strip, receiver picture row, and 4 explanation lines. Offer any message length; this is a verification game, not a new optimization problem.

### Separate facilitator material

**Solutions to every prompt**

**29.1:** ABACABDA encodes as 00|01|00|10|00|01|11|00, transmitted 0001001000011100:16 bits. Because all words have length 2, pairwise decoding is unambiguous. The printed icon message includes fourA, twoB, oneC, oneD.

**29.2:** 010=0|10 gives AC, while 010=01|0 gives BA. This specific complete proposed code is genuinely ambiguous. A is a prefix of B, and a greedy stop at 0 can prevent decoding 01 asB. Do not generalize that every non-prefix code must be ambiguous; the worksheet restricts to leaf/prefix codes to guarantee immediate decoding.

**29.3:** One successful code isA=0, B=10, C=110, D=111, using 14 bits. The original strip encodes 0|10|0|110|0|10|111|0, transmitted 01001100101110. Many mirrored codes and a C/D swap work equally well. A valid code must give four distinct nonempty leaf words with no word a prefix of another. An impressive bit total achieved with hidden delimiters is not valid.

**29.4:** Suppress a node with exactly one child by bypassing that edge/subtree step; every descendant code shortens by 1, other code lengths do not increase, and the leaf relation still gives a prefix code. All frequencies are positive, so the total strictly decreases. Root-unary steps can also be removed. Therefore a shortest prefix tree has no unary internal nodes. The tiny picture illustrates the operation; it does not claim there are only two messages in the main problem.

**29.5:** At the root the positive leaf counts split 1+3 or 2+2, up to exchanging sides. A two-leaf full tree is a fork. A three-leaf full tree splits 1+2. Thus the only four-leaf depth patterns are 1, 2, 3, 3 and 2, 2, 2, 2. Planar mirror variations add codes but not new length shapes. Best skew labeling putsA at depth 1, B at 2, C/D at 3; balanced labeling is arbitrary.

**29.6:** Balanced total 2(4+2+1+1)=16. Skew total 4×1+2×2+1×3+1×3=14. Exchange proof: if a frequent picture has a longer path than a less frequent one, swapping them saves one bit per extra occurrence per exchanged depth step, and cannot increase cost. For example, weights 4 and 1 at depths 3 and 1 cost 13; swapped cost 7. Sorting larger counts toward shorter depths minimizes each shape. Removing unary steps and classifying both full shapes exhausts all prefix-code possibilities, so 14 is optimal among binary prefix codes.

**29.7:** All counts are 2. Balanced total 8×2=16. Skew total 2(1+2+3+3)=18. The balanced tree wins; yesterday’s skew winner now loses. A rarer message can be longer in a code designed to minimize total length, so one cannot optimize by asking only for the longest codeword.

**29.8:** Use frequencies 2, 2, 1, 1, for example ABACBD. A balanced code costs 6×2=12. A skew code placing one doubled picture at depth 1 and the other at 2 costs 2×1+2×2+1×3+1×3=12. All placements of the two doubled labels in the first two depths tie. With six total messages and all four present, the only frequency multisets are 3, 1, 1, 1 (skew 11 vs balanced 12) and 2, 2, 1, 1 (tie 12); hence this also characterizes all possible successful frequency multisets.

**29.9:** Any correctly decoded partner message using a verified prefix tree is acceptable. Starting at the root, each bit chooses exactly one edge. A symbol is emitted only at a leaf, so no longer codeword could share that entire word as a proper prefix. Return to the root and repeat. Induction over symbols shows every concatenation decodes uniquely. A partial final word or traversal off the tree flags an invalid/incomplete transmission; it is not an alternate valid decoding.

**Staged hints — offer only after exploration**

1. (29.2) Try a cut after the first bit. Then try a cut after the second.
2. (29.3) The four pictures are not equally common. Try giving the most common one a single-edge leaf, and put the other three under the other branch.
3. (29.5–29.6) Count leaves on the two sides of the root. For labels, compare the cost before and after swapping a frequent deep picture with a rare shallow one.

**stop:** A working 14-bit prefix code and either its decoding explanation or its complete two-shape optimality proof. The frequency reversal and six-message tie are worthwhile extensions, not filler.

**adult math:** Finite lossless source coding; weighted external path length; tree reduction and exchange arguments. This is a complete small optimality proof without giving Huffman’s algorithm as a recipe. The general continuation asks why two least-frequent symbols can be placed as deepest siblings and merged recursively. Entropy/logarithms are unnecessary for this finite task.

**prior use:** Week 6’s code-query trees optimize questions to identify an object. Here one sends a sequence with no boundaries, and weighted communication cost is the objective. Both use trees; the constraints and the proof are different.

**source note:** AP-29’s Shannon source supplies the code framework and the classical 4, 2, 1, 1 example. The sender/receiver script, ambiguous strip, classification prompts and changed-frequency challenges are instructional adaptations, checked directly.

**Source trail**

- Claude Shannon, A Mathematical Theory of Communication, Part I, PDF p. 18: code 0,10,110,111 and weighted average length. https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf (relevant source framework inspected; finite example explicitly proved below)

**Programmatic figure specification**

```json
{
  "message_strip": {
    "message": "ABACABDA",
    "symbols": {
      "A": "triangle",
      "B": "circle",
      "C": "square",
      "D": "five-point star"
    },
    "render": "Draw vector icons and include letters; do not rely on unsupported Unicode glyphs or color alone. Baseline code00/01/10/11 printed in a small legend."
  },
  "empty_code_tree": {
    "root": [
      0.5,
      0.95
    ],
    "student_tree": true,
    "edge_rule": {
      "left": 0,
      "right": 1
    }
  },
  "unary_tree": {
    "edges": [
      [
        "root",
        "u"
      ],
      [
        "u",
        "A"
      ],
      [
        "u",
        "B"
      ]
    ],
    "labels": "root→u edge0, u→A edge0,u→B edge1. It is a two-message illustration, not the four-message answer. Suppress root’s unary step; A=0,B=1 replaces00,01."
  },
  "two_tree_frames": {
    "solution_depths": [
      [
        2,
        2,
        2,
        2
      ],
      [
        1,
        2,
        3,
        3
      ]
    ],
    "student_shapes_blank": true
  }
}
```
