# Week 6: How many tests does a secret need?

Revised September 27, 2026, applying the adopted Week 1 classroom guidance. Grade bands are entry points. All v3 revisions and their optional multi-page extras are **unpiloted**. The Week 1 observations are evidence about that session, not observations of Week 6.

## The mathematical work

Adaptive decision trees, minimax query selection, indistinguishability lower bounds, Hamming distance, and resolving sets of hypercubes.

| Entry level | Investigation |
| --- | --- |
| K–1 · F06-K-v3 | Eliminate candidates physically, make all branches of a two-position decision tree, and show why one test is insufficient. |
| 2–3 · F06-M-v3 | Build a three-test identification method and show why no two-test method always works, using an unavoidable three-secret branch. |
| 4–5 · F06-U-v3 | Prove four tests suffice and three cannot for four binary positions, using symmetries and adversarial score partitions. |
| Extra 6–7 · F06-X-v3 | Decode five-bit words from four fixed probes in a published research construction; prove all 32 signatures differ using pair sums. |

## Prerequisites and preparation

K–1: match positions and count 0–2, no independent reading; exclude inconsistent examples. Middle: counts to 3 and ±1 score changes; complete finite cases. Upper: counts to 4 and casework; worst-case reasoning and symmetry. Extra: bits, small sums, variables or placeholder counters; distinguish fixed from adaptive queries.

Two counter types, symbols or R/B labels for accessibility, three folded-paper screens, pencil records, position strips. Use 12 counters of each type for the K and middle groups, and 16 of each type for the upper group so all six candidate rows and a test can remain visible. Reuse test counters after recording. Preparation: about 10 minutes.

Current roster: K,K,1 / 3,3,3 / 5. **Start with page 1 for each child: seven student sheets.** Keep remaining pages as continuation masters and copy the next stage only when useful; preserve earlier records beside later tasks. Complete packet lengths are K–1 3, middle 3, upper 4, optional extra 3, facilitator 6 pages. Printing all core packets for the roster would use 22 sheets, but that is not the default session print plan. US Letter, single-sided, 100%; grids are recording spaces rather than calibrated physical templates.

## Concrete work before each new representation

- K–1: score visible secrets and play, filter four concrete candidate rows, compare an unhelpful repeated test with a separating test, then build and replay a tree.
- Grades 2–3: score and play first, compare four contrasting secrets under the baseline method, recover a hidden secret, then test a difficult three-candidate branch and a concrete color-renaming operation.
- Grades 4–5: record play and single-position score changes, try four complete baseline signatures, recover a hidden secret, then sort six candidates and test the triple/quartet obstructions. Every-query symmetry proofs remain adult-supported follow-ups.
- Extra: score visible words and two hidden games, isolate all four two-bit contributions, decode the original example, build all four ambiguous-pair-count cases, and return to the hidden records. The general proof and hypercube language follow successful decoding.

Give one page at a time and choose a continuation by demonstrated readiness. Proof questions and hints remain in the facilitator guide, including complete arguments supporting the finite checks. Each student page now uses only the common header/footer and numbered problems with essential rules, next actions, diagrams, and recording space.

## Default 60-minute flow, adjusted to the children

0–10: Free handling, copying, and matching of counter strings before adding feedback rules.

10–15: Brief launch: keep RBR visible and score RRR→2, BRB→0, RBR→3. Hide it only after feedback is understood. Feedback is total correct positions, not which positions or right-color/wrong-place information.

15–35: K plays and builds four candidate rows; middle explores the three-test baseline method; upper develops and explains its four-test method. Keep tests and scores visible.

35–40: Movement/reset. Preserve candidate rows and records for the return.

40–55: Continue the current method or choose an adult-supported lower-bound proof below. The upper comparison/proof continuation and extra are reserves. Stop repetitive table calculations once the child explains the score structure.

55–60: Share one method and why it works, then tidy.

| Group | Satisfying stopping point | Optional proof continuation |
| --- | --- | --- |
| K–1 | Build all branches of a method identifying a two-place secret within two tests. | For any first test, construct two secrets that both score one, showing one test cannot always suffice. |
| 2–3 | Explain and test the three-query baseline method, including how it recovers the last place. | Explain the one-B triple and at most two scores, then rename colors coordinate by coordinate to cover every first query and establish optimality. |
| 4–5 | Explain why the baseline and three single-place flips identify every four-place secret. | Sort the adversarial branches, prove the triple and four-candidate obstructions separately, and use symmetry to cover all queries. |

One adult stays primarily with K,K,1. The organizer alternates middle and upper proof conversations; give the other group a concrete next attempt, such as testing a partner's secret or sorting candidate cards. Preserve two opposing sides and rotate a checker in each triplet. Do not start both older groups' lower-bound proofs at once. A proved upper bound is a complete worthwhile outcome; record RRR-first obstruction separately if the middle symmetry discussion is not reached.

**Hints:** Keep candidate rows and every score visible. Change one place while holding the others at baseline. For lower bounds, be the difficult but consistent setter. Queries need not be possible secrets. The upper final pages are a proof reserve, not a required completion target.

The facilitator packet gives exact checked solutions, prompts, and optional reasoning. Children can point, build, dictate, or draw.

## Checked mathematics and boundaries

Exact worst-case identification costs are 2,3,4 for two,three,four binary places. Baseline plus n−1 single-place flips identifies any n-bit string in n tests. At n=3, a baseline score-2 branch has three one-B candidates on which every next test has at most two outcomes. At n=4, score 2 leaves six two-B candidates: second queries with one/three Bs leave a hard triple, two Bs leaves four candidates with at most three final scores, zero/four gives no information. In both the middle and upper proofs, coordinatewise color renaming covers every first query: BRB becomes RRR by swapping R/B at places 1 and 3 in every secret and query, preserving every match. The upper triple BBRR/BRBR/BRRB has a fixed first B and one moving B, so a final query gives at most two scores on it; this is separate from the four-candidate, at-most-three-scores obstruction. Extra probes 00000,00011,00101,01001 reveal three pair sums and the total number of ones, distinguishing all 32 secrets; scores 2,2,2,0 decode 10110. Identification and submission are explicitly different: naming a determined secret is free here; the original game may require an extra turn.

Run **python3 plans/verify-week-06.py**. Computation verifies finite instances; the facilitator supplies explanatory proofs of general claims.

## Sources and lineage

- Downloaded JRMF *Crack the Code*, PDF pp. 2–4: binary exact-position rules and n+1 submitted-guess challenge.
- Cáceres et al., [*On the Metric Dimension of Cartesian Products of Graphs*](https://users.monash.edu.au/~davidwo/papers/MetricDimension-arXiv.pdf), 2005 manuscript/published 2007, §2/PDF p. 3: exact four extra-page landmarks; §6/PDF p. 8: static exact-position Mastermind and resolving sets. Pair-sum decoding is our explanation.
- Knuth, *The Computer as Master Mind* (1976–77), linked from [his author page](https://cs.stanford.edu/~knuth/fg.html): commercial six-color/four-place five-guess method uses additional feedback and is not a bound for our rules. Its minimax idea is related.
- Undergraduate topics: decision-tree algorithms, adversarial lower bounds, graph distance, and Hamming geometry. Printed small optima have complete direct proofs.

**Teaching lessons actually read:** *Math Circle by the Bay*, preface printed pp. ix–x/PDF pp. 10–11 recommends manipulatives, varying pace, extras, practice explaining, and themes at different depths. JRMF pages above provide physical launches and explanation prompts. Staffing, timetable, and new proof scaffolds are our adaptations. See [lesson-format source notes](lesson-format-source-notes.md).

## Returning children and records

JRMF binary rules remain; old fixed histories are replaced by methods and exact bounds. Related Week 3 identification deepens through an ordered-string score model, adaptive queries, adversarial bounds, and hypercube geometry. Save more colors, noisy feedback, coin weighing, and average-case strategy for later.

Status: **v3 prepared, unpiloted; no Week 6 classroom observations supplied**. Record exact instances, claims proved, hints, and extra branches in the shared use log. Untouched reserves remain available. [Print/source index](../lowell-math-circle-year-2/source/week-06/README.md) and [review](../lowell-math-circle-year-2/source/week-06/REVIEW.md).

## Review after first use

Record the exact problems attempted, examples built, claims explained, prompts needing repeated adult rescue, time spent recording versus acting, and what children wanted to continue. Distinguish observations from hypotheses and proposed changes. A completed chart is not evidence that its general argument was established; prepared reserves remain unused until recorded otherwise. See the [Week 1 classroom review](week-01-classroom-review.md) for the actual observations behind this revision.

Source distinction: *Math Circle by the Bay*, printed pp. ix–x supports flexible pace, manipulatives, and explanations; Rozhkovskaya, Lessons 3, 7, and 8, “At the lesson,” supports attempts before tables, checking legal actions, and adjusting recording. Our exact added examples, worksheet format, and common launch respond to the organizer's guidance.
