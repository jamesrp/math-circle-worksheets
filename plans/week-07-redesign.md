# Week 7: A strategy against every reply

Revised September 27, 2026, applying the adopted Week 1 classroom guidance. Grade bands are entry points. All v3 revisions and their optional multi-page extras are **unpiloted**. The Week 1 observations are evidence about that session, not observations of Week 7.

## The mathematical work

Backward induction, recursive W/L classification, modular losing sets, finite-state eventual periodicity, and Sprague–Grundy labels for sums of games.

| Entry level | Investigation |
| --- | --- |
| K–1 · F07-K-v3 | Use both reply branches to prove a trap of three, then maintain groups of three across pairs of turns. |
| 2–3 · F07-M-v3 | Classify 1/3/4 positions by all legal options, refute greedy play, and find multiple winning moves. |
| 4–5 · F07-U-v3 | Prove losing remainders 0,2 modulo 7, compare 1/3/5 parity, and explain why finite subtraction rules force eventual repetition. |
| Extra 6–7 · F07-X-v3 | Compute mex labels and prove two piles lose exactly when their labels agree, exposing the information lost by W/L alone. |

## Prerequisites and preparation

K–1: count/remove 1 or 2, alternate turns; no reading; check both replies. Middle: physical subtraction/counts to 14, adult reading available; one winning move versus all losing options. Upper: subtraction to 28 and grouping by 7; general proof and finite-memory argument. Extra: small labels and smallest-missing operation; no XOR prerequisite.

25 counters per group, distinct move cards 1-or-2 / 1,3,4 / 1,3,5, pencils and numbered charts. Two mats for extra two-pile play. For the finite-memory reserve, bring a straight paper strip and a movable paper frame (or two folded scraps) that exposes four consecutive chart entries; no special printing is needed. Preparation: about 10 minutes.

Current roster: K,K,1 / 3,3,3 / 5. **Start with page 1 for each child: seven student sheets.** Keep remaining pages as continuation masters and copy the next stage only when useful; preserve earlier records beside later tasks. Complete packet lengths are K–1 3, middle 3, upper 4, optional extra 3, facilitator 5 pages. Printing all core packets for the roster would use 22 sheets, but that is not the default session print plan. US Letter, single-sided, 100%; grids are recording spaces rather than calibrated physical templates.

## Concrete work before each new representation

- K–1: play and record several games from 4 and 5 before checking both replies from 3 and 6; then test first/second choices and grouped-counter replies through 12.
- Grades 2–3: play each of 5, 6, and 7 twice, list every move from 2 and 4, build a small W/L chart with all legal destinations, then compare every move from 8 and 10 and test a strategy card.
- Grades 4–5: play before classifying, record W with a concrete winning move, compare all moves from contrasting piles, group those same piles in sevens, then use a remainder table in a game. A rule change and actual four-cell window extensions each receive their own tasks.
- Extra: play contrasting two-pile positions before introducing g-labels; list legal destinations and reachable labels for every computed case; then test equalization and every reply from (4,6). The mex proof follows these checks.

Give one page at a time and choose a continuation by demonstrated readiness. Proof questions and hints remain in the facilitator guide, including complete arguments supporting the finite checks. Each student page now uses only the common header/footer and numbered problems with essential rules, next actions, diagrams, and recording space.

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

**Teaching lessons actually read:** *Math Circle by the Bay*, preface printed pp. ix–x/PDF pp. 10–11 recommends manipulatives, varying pace, extras, practice explaining, and themes at different depths. JRMF pages above provide physical launches and explanation prompts. Staffing, timetable, and new proof scaffolds are our adaptations. See [lesson-format source notes](lesson-format-source-notes.md).

## Returning children and records

Lowell Handout 2.3 and 3.1–3.3 used 1-through-3 and 1-through-5. Handout 3.1 incorrectly labels 5 losing after identifying a move to losing 4. Do not retain that error. JRMF already contains 1/3/4; it is not our invention. Reserve misère play, more move sets, and three-pile XOR for later years.

Status: **v3 prepared, unpiloted; no Week 7 classroom observations supplied**. Record exact instances, claims proved, hints, and extra branches in the shared use log. Untouched reserves remain available. [Print/source index](../lowell-math-circle-year-2/source/week-07/README.md) and [review](../lowell-math-circle-year-2/source/week-07/REVIEW.md).

## Review after first use

Record the exact problems attempted, examples built, claims explained, prompts needing repeated adult rescue, time spent recording versus acting, and what children wanted to continue. Distinguish observations from hypotheses and proposed changes. A completed chart is not evidence that its general argument was established; prepared reserves remain unused until recorded otherwise. See the [Week 1 classroom review](week-01-classroom-review.md) for the actual observations behind this revision.

Source distinction: *Math Circle by the Bay*, printed pp. ix–x supports flexible pace, manipulatives, and explanations; Rozhkovskaya, Lessons 3, 7, and 8, “At the lesson,” supports attempts before tables, checking legal actions, and adjusting recording. Our exact added examples, worksheet format, and common launch respond to the organizer's guidance.
