# Review cards

One card per theme says whether the theme is good enough to keep as it is, and what to do with it if not. A theme is ported to the app only after its card exists ([the plan](https://github.com/jamesrp/small-math-adventure/tree/main/docs/plan), Track C). Cards live here as `week-NN.md`, each with its correctness check as `week-NN-math.md`.

## What a card says

A card follows [TEMPLATE.md](TEMPLATE.md): a verdict, the mathematics in a few sentences, nine ratings with evidence, what to keep, a located fix list, overlaps with other themes, the app fit, and what children actually did.

The verdict follows from the fix list:

| Verdict | Means | Next |
|---|---|---|
| keep | No must-fix. | Port when its wave comes. Should and could items wait for whoever next touches the theme. |
| revise | The design is right; at least one must-fix needs doing. Should-fixes alone never make a revise. | Run the workflow's reviser stage with the card as its review. Ports need not wait. |
| rework | The problems themselves must be replaced to deliver the mathematics. If they can stay and the fix is in materials, boards, the launch or the guide, it is a revise. | A new outline and a full workflow run. |
| merge | Another theme covers the same object and theorem as well or better. | Fold the named parts into that theme. |

Severity: **must** means a child or adult would be stuck or misled as printed, or the organizer would have to delete do-not-list items by hand from most pages; **should** means usable but costly to the session; **could** is taste. Ratings are strong (at the bar of the approved Week 2 catalogs or above), adequate (usable as printed) or weak (cannot be used as intended).

## How to write one

1. Claim the card on [WORKBOARD.md](../../WORKBOARD.md).
2. Make a run folder outside the repository's tracked files, such as `tmp/review-runs/week-NN/`.
3. In a fresh agent: "Your instructions are in plans/review/MATH.md. Read it and follow it exactly. Week: NN. Run folder: <run folder>." It writes `math.md`.
4. In another fresh agent: the same with `plans/review/CARD.md`. It writes `card.md`, using `math.md`.
5. If the verdict hinges on one finding, or the card disagrees with the math check, run step 4 again in a fresh agent and reconcile the two cards.
6. Read the card against the packet before committing it: check every quote and number you keep, and add what children actually did under "Classroom evidence". Copy `card.md` to `week-NN.md`, `math.md` to `week-NN-math.md` and the math scripts with their outputs to `checks/week-NN/`. Add the card to the table below and mark the board line done.

Claude Code runs each stage as a subagent; Codex runs each as a separate `codex exec` or session. Keep `CARD.md`, `MATH.md` and `TEMPLATE.md` as a set, and log changes to them below.

## Cards

| Week | Theme | Verdict | Card |
|---|---|---|---|
| 1 | Tiling lab (pattern blocks) | keep | [card](week-01.md), [math check](week-01-math.md) |
| 2 | Switches and lamps | revise: a working board that enforces the pair rule, and an adult guide for the compact catalog | [card](week-02.md), [math check](week-02-math.md) |
| 15 | Nearest-site regions | keep | [card](week-15.md), [math check](week-15-math.md) |
| 13 | Route packing and bottlenecks | keep | [card](week-13.md), [math check](week-13-math.md) |
| 23 | Sorting networks | revise: a print-and-cut mat, cards and bars, which the guide specifies but nothing supplies | [card](week-23.md), [math check](week-23-math.md) |
| 53 | Cheapest connected networks | revise: two price labels on page 8 sit on the wrong link, and the K–1 route is one page long | [card](week-53.md), [math check](week-53-math.md) |

## Calibration

The format was calibrated on Weeks 1, 2 and 15, which children have used, with the September version of Week 1 as a negative control. In the final round all four verdicts matched what the organizer saw. See [calibration.md](calibration.md) for the rounds, the changes and the limits.

## Changes

- 2026-10-05: first version, calibrated on Weeks 1, 2 and 15. `MATH.md` asks for scripts that run from their committed copy in `checks/`.
