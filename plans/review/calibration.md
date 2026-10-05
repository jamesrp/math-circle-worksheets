# Calibrating the review cards

October 5, 2026. The plan says to calibrate the card on Weeks 1, 2 and 15 before the other sixty: a card that marks down a theme children enjoyed is miscalibrated. A card that waves through a packet children struggled with is miscalibrated too, so the test also used a negative control. This file records what the cards were compared against, what went wrong in each round, and what changed.

## What the cards had to match

| Case | Packet reviewed | What the organizer saw or decided | A calibrated card |
|---|---|---|---|
| Week 1 | Current F01-K-v4, F01-M-v3, F01-U-v3 | An earlier version was taught in September and went well overall; children loved handling the blocks. The organizer approved these revised packets on September 27. On October 4 the organizer counted Week 1 among the weeks tested with children and good. | keep |
| Week 1, old | The September classroom packets in `week-01/archive-classroom-2026-09/` | The organizer's report on that session ([week-01-classroom-review.md](../week-01-classroom-review.md)): starting different sheets at two tables needed too much adult management; the first 2–3 problem was too short; children could not tell what to do in the triangle continuation; the chevron idea was undersupported; the two-pink-triangle question did not land; the upper progression was compelling but its instructions and order needed work. The packets were revised in response. | revise, finding those problems |
| Week 2 | The compact and upper catalogs, F02-S-CAT-v2 and F02-S-CAT-UP-v1 | AGENTS.md names these catalogs as approved examples of the page format. `worksheet-workflow/context.md` records that a paper lamp session went poorly: the two-lamp rule lived only on paper, children changed just the lamp they wanted, and many could not tell what was asked. Children love the same puzzles in the app, where a tap flips both lamps. On October 4 the organizer counted Week 2 among the good weeks, and later explained that the activity is good, especially in the app, while paper was harder to enforce in a larger group. | Pages and mathematics at the bar; the paper-only rule found as the problem |
| Week 15 | F15-K-v1, F15-23-v1, F15-45-v1 | Judged good, reported October 4. Details came on October 5, after the runs: the organizer drew the maps by hand at home with three children, two dots and then a third added on top, without the printed packets and not in the circle. | keep |

## How the runs were set up

Each run was a fresh agent given only `CARD.md` and a short message naming the week and its files. The math check (`MATH.md`) ran once per week, in its own agent, and every card run reused that report. Runs read a frozen copy of the repository and were told not to open classroom records. Under "Classroom evidence" they wrote "Withheld for calibration."

Blindness was partial. `context.md` is part of the bar for every card, and it describes the Week 1 and Week 2 sessions; source READMEs mention the Week 1 revision. In round 1 the app plan, which every card reads for app fit, also said that Weeks 1, 2 and 15 had been taught and liked. From round 2 on, the runs read copies of the app plan and the work board with those statements removed, so Week 15 was fully blind from then on.

All runs used the same model family that wrote most of the packets.

## Round 1: the first prompt

| Case | Verdict | Against the evidence |
|---|---|---|
| Week 1 | revise | Too harsh. No must; ten should items (restated rules, a question it read as a hint, a guide without an overview) made the verdict. |
| Week 1, old | revise | Right. It found the thin first 2–3 problem, the unclear continuation (an undefined "fewest blocks" task) and the order and clarity problems in 4–5, and reworded the pink question. It missed the undersupported chevrons and the two-table launch. |
| Week 2 | revise | Right. Mathematics, problems and pages strong; concreteness weak because nothing enforces the two-lamp rule, which is the recorded failure. It also found that the compact catalog has no current adult guide. |
| Week 15 | keep | Right, but the app plan had told it the week was taught. |

The prompt allowed a revise for "a cluster of should items". An adversarial reviewer always finds a cluster, so that clause would mark down nearly every packet.

**Changes:** should items alone never make a revise; a missing adult guide, or a do-not-list item on most pages, counts as a must; "Problems" asks whether each idea gets several contrasting concrete cases, and "Concreteness" asks for one whole-group launch before the bands split (the two misses in the old Week 1); taught or approved choices were to be treated as deliberate; cards were capped at about 1,200 words.

## Round 2

| Case | Verdict | Against the evidence |
|---|---|---|
| Week 1 | keep | Right. Ten should items, none a must. |
| Week 1, old | keep | Too lenient. It found the do-not-list items on every page but rated them should, citing the new clause about taught pages. It also missed the undefined "fewest blocks" task this time. |
| Week 2 | rework | Same findings as round 1, but it read "a rule nothing enforces", an example in the rework definition, as calling for a new design. Its own fix kept every problem. |
| Week 15 | keep | Right, with the outcome hidden. |

**Changes:** a page's history (taught, approved, or older than a rule) never changes a finding's severity; only observed classroom results may change a rating. Rework now means the problems themselves must be replaced; when the problems can stay and the fix is in materials, boards, the launch or the guide, the verdict is revise. A Week 2 run with only the rework change returned revise, with the same two musts.

## Round 3: the final prompt

| Case | Verdict | Against the evidence |
|---|---|---|
| Week 1 | keep | Right. Nine should items and five coulds. Its first should is that the K–1 packet never asks whether a shape can be filled. |
| Week 1, old | revise | Right. Two musts: do-not-list items on all eleven pages, and a K–1 packet that only asks children to fill shapes. It found the thin first 2–3 problem, the unclear continuation (through the "Go further" and titled-heading items the organizer's revision removed) and the 4–5 order (the six cards give away the count). It raised the pink-triangle question only as unrehearsed, named the launch only in passing, and again missed the undersupported chevrons. |
| Week 2 | revise | Right. Two musts: no board on which children can turn a printed lamp off, with nothing to enforce the pair rule (the recorded failure), and no current adult guide for the compact catalog. |
| Week 15 | keep | Right, with the outcome hidden. Four should items, all wording or guide repairs. |

All four verdicts match. The committed cards are these round 3 cards, read against the packets, with the claims they keep checked and the classroom evidence added (see each card's status line).

One adjustment was made by hand. Ratings varied between runs: of the four Week 2 runs, two rated its problems strong and two adequate, and three rated its student pages strong. "Strong" is defined as the level of the Week 2 catalogs, so the committed Week 2 card rates both strong and keeps the round 3 findings behind the lower ratings (short compact problems, a missing board) as fix items.

## Limits

- One run per case per round, and findings vary between runs: the old Week 1's undefined task was found in round 1 and missed in round 2, and its undersupported chevrons were missed in all three. Verdicts were stable once the rules were sharp, but a card is one reviewer's read, and it will miss some of what children would show.
- The only negative control is one packet, on a theme whose mathematics is strong. The format has not yet been tested on a packet whose mathematics is thin; the first wave-1 cards should be read with that in mind.
- The evidence is the organizer's summaries, not per-problem observations. Week 15's is the weakest: a hand-drawn version of its core at home with three children. It shows the idea lands, not that the printed packets do, so Week 15 tests the card's leniency less than Weeks 1 and 2.
- Reviewer and writer are the same model family, as in the worksheet workflow.

## Process rules that came out of this

- Read a card against its packet before committing it.
- When a verdict hinges on one finding, or the card disagrees with the math check, run the card stage a second time and reconcile the two.
- Children's observed results go under "Classroom evidence" and outrank the reviewer's predictions.
