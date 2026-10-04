> Historical v2 plan, preserved before the September 27 classroom-guidance revision. See the [current version](../week-07-redesign.md) and [revision record](../fall-weeks-02-10-classroom-guidance-review.md). Preparation is not evidence of classroom use.

# Week 7: A strategy against every reply

Prepared September 19, 2026. Replaces the earlier depth of F07, retaining the common hands-on theme. Grade bands are entry points. The one-page grades 6–7 extra is optional.

## The mathematical work

Backward induction, recursive W/L classification, modular losing sets, finite-state eventual periodicity, and Sprague–Grundy labels for sums of games.

| Entry level | Investigation |
| --- | --- |
| K–1 · F07-K-v2 | Use both reply branches to prove a trap of three, then maintain groups of three across pairs of turns. |
| 2–3 · F07-M-v2 | Classify 1/3/4 positions by all legal options, refute greedy play, and find multiple winning moves. |
| 4–5 · F07-U-v2 | Prove losing remainders 0,2 modulo 7, compare 1/3/5 parity, and explain why finite subtraction rules force eventual repetition. |
| Extra 6–7 · F07-X-v2 | Compute mex labels and prove two piles lose exactly when their labels agree, exposing the information lost by W/L alone. |

## Prerequisites and preparation

K–1: count/remove 1 or 2, alternate turns; no reading; check both replies. Middle: physical subtraction/counts to 14, adult reading available; one winning move versus all losing options. Upper: subtraction to 28 and grouping by 7; general proof and finite-memory argument. Extra: small labels and smallest-missing operation; no XOR prerequisite.

25 counters per group, distinct move cards 1-or-2 / 1,3,4 / 1,3,5, pencils and numbered charts. Two mats for extra two-pile play. For the finite-memory reserve, bring a straight paper strip and a movable paper frame (or two folded scraps) that exposes four consecutive chart entries; no special printing is needed. Preparation: about 10 minutes.

Current roster: K,K,1 / 3,3,3 / 5. Print three K–1 packets (two pages each), three middle (two each), one upper (three): 15 student sheets; add one extra if needed. Facilitator prints separately. US Letter, single-sided, 100%; grids are workspaces rather than calibrated physical templates.

## Default 60-minute flow, adjusted to the children

0–10: Free handling, sorting, and grouping of counters before adding game rules.

10–15: Brief launch: play 1-or-2 from three counters without giving a strategy. Check legality including the last move. Older groups then receive their different move cards. Zero is losing for the next player; taking the last wins.

15–35: K plays 4,5,3 and checks both replies; middle plays 5,6,7 under 1/3/4, then reasons from smaller piles; upper classifies enough positions to conjecture the repeat. More chart entries are optional after the structure is clear.

35–40: Movement/reset. Keep charts and move cards ready for the return.

40–55: Continue play and defend one claim, or take an optional proof continuation below. Use groups of seven for the upper remainder argument. Save rule changes, four-label memory, and the extra for children ready for a new question.

55–60: Share one strategy and its reason, then tidy.

| Group | Satisfying stopping point | Optional proof continuation |
| --- | --- | --- |
| K–1 | Demonstrate both replies that make a pile of three a trap. | Group counters in threes and explain why the response strategy works from every multiple of three. |
| 2–3 | Defend W/L labels through seven using one move for W and all moves for L. | Refute greedy play at eight and find both winning moves at ten, explaining why they work. |
| 4–5 | Conjecture losing remainders 0,2 and defend selected labels with legal moves. | Prove both remainder obligations and termination; if already proved, use the paper four-cell window to explain eventual repetition. |

One adult stays primarily with K,K,1. The organizer starts the upper investigation, checks middle play, and returns for a strategy explanation. While waiting, middle children play two opposing sides with a rotating checker, and the upper child tests a disputed label or slides the paper frame. Choose one proof conversation at a time; a complete chart is not a prerequisite for it.

**Hints:** Try smaller piles. State whose turn a W/L label describes. One legal arrow into L proves W; all options leading to W prove L. Marks come from reasoning, not who happened to win. Group counters and chart cells in sevens before introducing remainders.

The facilitator packet gives exact checked solutions, prompts, and optional reasoning. Children can point, build, dictate, or draw.

## Checked mathematics and boundaries

For 1/3/4, losing sizes are 7k and 7k+2. No allowed move connects these remainders; remainders 1,3,4,5,6 subtract 1,1,4,3,4 to reach them, legally even in the first block. For 1/3/5, every move changes parity and every odd pile takes 1 to even, so evens lose. Four W/L labels determine the next for 1/3/4; among 17 windows two agree and force equal futures. This proves eventual repetition, not necessarily repetition from zero. Extra labels 0–10 are 0,1,0,1,2,3,2,0,1,0,1. A move destroys label equality; from unequal labels the larger can move to the smaller by mex. Thus two piles lose exactly at equality. (1,1) loses, (1,4) wins; (1,3),(4,6) lose; (5,6) wins by taking 1 from 5.

Run **python3 plans/verify-week-07.py**. Computation verifies finite instances; the facilitator supplies explanatory proofs of general claims.

## Sources and lineage

- Downloaded JRMF *Countdown Teaching Guide*, PDF pp. 1–2: play and questions; pp. 4–5: W/L recursion; p. 8 challenge 4 explicitly introduces 1/3/4.
- Ferguson, [UCLA Math 167 Game Theory course](https://www.math.ucla.edu/~tom/GameTheory.html), textbook Part I §1.3–1.4 (P/N and subtraction), §3.2 (Sprague–Grundy), §4.2 (sums).
- Shenxing Zhang, [*On the linearity of the periods of subtraction games*](https://zhangshenxing.github.io/publications/Zhang2024tcs%20On%20the%20linearity%20of%20the%20periods%20of%20subtraction%20games.pdf), *Theoretical Computer Science* 985 (2024), §1, Lemma 1.1, Conjectures 1.2–1.3 and Theorem 1.4. It studies period/preperiod behavior as a new move varies and proves predicted behavior for specified families. Classroom periodicity is elementary, not the family classification. No assertion that all conjectures remain open today.

**Teaching lessons actually read:** *Math Circle by the Bay*, preface printed pp. ix–x/PDF pp. 10–11 recommends manipulatives, varying pace, extras, practice explaining, and themes at different depths. JRMF pages above provide physical launches and explanation prompts. Staffing, timetable, and new proof scaffolds are our adaptations. See [lesson-format source notes](../lesson-format-source-notes.md).

## Returning children and records

Lowell Handout 2.3 and 3.1–3.3 used 1-through-3 and 1-through-5. Handout 3.1 incorrectly labels 5 losing after identifying a move to losing 4. Do not retain that error. JRMF already contains 1/3/4; it is not our invention. Reserve misère play, more move sets, and three-pile XOR for later years.

Status: **prepared, not taught**. Record exact instances, claims proved, hints, and extra branches in the shared use log. Untouched reserves remain available. [Print/source index](../../lowell-math-circle-year-2/source/week-07/README.md) and [review](../../lowell-math-circle-year-2/source/week-07/REVIEW.md).
