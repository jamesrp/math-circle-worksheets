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
| 1e | Pattern blocks II (the Week 1 encore) | keep | [card](week-01e.md), [math check](week-01e-math.md) |
| 2 | Switches and lamps | revise: a working board that enforces the pair rule, and an adult guide for the compact catalog | [card](week-02.md), [math check](week-02-math.md) |
| 12 | Catalan bijections (noncrossing pairings, paths and trees) | revise: the guide hint for K–1 Problem 4 says comparing the partners of one dot detects duplicates, so an adult may call a new pairing a repeat | [card](week-12.md), [math check](week-12-math.md) |
| 15 | Nearest-site regions | keep | [card](week-15.md), [math check](week-15-math.md) |
| 3 | Shuffle machines (permutations as arrow mats) | keep | [card](week-03.md), [math check](week-03-math.md) |
| 4 | Stars and secret wheels | revise: the adult guide puts the 4–5 times-table dents where the curve touches the circle, so an adult would correct a right drawing | [card](week-04.md), [math check](week-04-math.md) |
| 6 | Code breaking (guess my block, the counter code game) | revise: the guide's key for 2–3 Problem 11 says testing every place takes five tests, though YRRR, RYRR, RRYR, RRRY take four, so an adult may correct a right method | [card](week-06.md), [math check](week-06-math.md) |
| 7 | Take-away games | keep | [card](week-07.md), [math check](week-07-math.md) |
| 13 | Route packing and bottlenecks | keep | [card](week-13.md), [math check](week-13-math.md) |
| 14 | Polygon triangulations and flips | keep | [card](week-14.md), [math check](week-14-math.md) |
| 16 | Three-colour triangles (Sperner's lemma) | keep | [card](week-16.md), [math check](week-16-math.md) |
| 17 | Machine memory (fewest states) | keep | [card](week-17.md), [math check](week-17-math.md) |
| 18 | Error-correcting codebooks | keep | [card](week-18.md), [math check](week-18-math.md) |
| 19 | No card inside another (subset antichains) | keep | [card](week-19.md), [math check](week-19-math.md) |
| 20 | Averaging circles (the maximum principle) | keep | [card](week-20.md), [math check](week-20-math.md) |
| 21 | Shortest reflected paths | keep | [card](week-21.md), [math check](week-21-math.md) |
| 22 | Meeting regions (four-point convex partitions) | keep | [card](week-22.md), [math check](week-22-math.md) |
| 23 | Sorting networks | revise: a print-and-cut mat, cards and bars, which the guide specifies but nothing supplies | [card](week-23.md), [math check](week-23-math.md) |
| 24 | Nontransitive dice and decks | keep | [card](week-24.md), [math check](week-24-math.md) |
| 25 | Row and column shadows | revise: a guide hint calls the natural lower-bound proof wrong (two switches, because four cells must empty and a switch empties two) | [card](week-25.md), [math check](week-25-math.md) |
| 26 | Same area, different boundaries (polyomino perimeter) | revise: Grades 4–5 Problem 2 asks "Can it have a hole?" without saying whether a corner contact closes one, and the guide calls the "no" answer false, so an adult may correct a right answer | [card](week-26.md), [math check](week-26-math.md) |
| 29 | Two-length builders (the last gap, ab − a − b) | revise: the guide's K–1 Problem 6 key lists only 7 as a gap for 2- and 4-rods, though 9 and 11 fail too, so an adult may correct a right answer | [card](week-29.md), [math check](week-29-math.md) |
| 30 | Two-pan weight kits (balanced ternary) | keep | [card](week-30.md), [math check](week-30-math.md) |
| 31 | Hidden orchard (lattice visibility) | revise: the guide's optional extension gives (4,3) as a sight line that changes when O moves to (1,1), and it doesn't, so an adult may correct a right answer | [card](week-31.md), [math check](week-31-math.md) |
| 33 | Prime-length necklaces | keep | [card](week-33.md), [math check](week-33-math.md) |
| 34 | Hidden turns (distinguishing colourings) | keep | [card](week-34.md), [math check](week-34-math.md) |
| 36 | Making threes (nine-tile SET) | keep | [card](week-36.md), [math check](week-36-math.md) |
| 37 | Mirror twins (tetrahedron chirality) | revise: the guide says failed turns never prove impossibility, though "A must go on A, and all three turns about A fail" is complete, and nothing supplies the tetrahedron kit it specifies | [card](week-37.md), [math check](week-37-math.md) |
| 39 | Road detours (path reduction) | revise: K–1 Problem 7 has two readings, and the key tells the adult that the natural one is wrong, so an adult may correct a right answer | [card](week-39.md), [math check](week-39-math.md) |
| 41 | Torus portals and lifts | keep | [card](week-41.md), [math check](week-41-math.md) |
| 42 | Fair results from a bag (von Neumann's fair coin) | keep | [card](week-42.md), [math check](week-42-math.md) |
| 43 | Shuffling picture cards (fair shuffles) | revise: K–1 Problem 2's crossed-out cards and four rows fit "this card can't be first", while the key reads them as drawn first, so an adult may mark a right answer wrong | [card](week-43.md), [math check](week-43-math.md) |
| 44 | The bag that copies (Pólya's urn) | keep | [card](week-44.md), [math check](week-44-math.md) |
| 45 | The visible side (conditioning on a clue) | keep | [card](week-45.md), [math check](week-45-math.md) |
| 46 | Two boards forget their starts (coupling) | keep | [card](week-46.md), [math check](week-46-math.md) |
| 47 | Gentle-step landscapes (extending clues, lowest and highest landscapes) | keep | [card](week-47.md), [math check](week-47-math.md) |
| 48 | Inside and outside covers | keep | [card](week-48.md), [math check](week-48-math.md) |
| 49 | Four towers and differences (Ducci rings) | keep | [card](week-49.md), [math check](week-49-math.md) |
| 52 | Hinged frames and braces | revise: the K–1 route is three problems the guide finishes by minute 30, and Problem 13's "Yes" rests on a one-brace-per-cell rule no upper page states | [card](week-52.md), [math check](week-52-math.md) |
| 53 | Cheapest connected networks | revise: two price labels on page 8 sit on the wrong link, and the K–1 route is one page long | [card](week-53.md), [math check](week-53-math.md) |
| 54 | Partitions and rebuilding (Euler's odd and distinct parts) | keep | [card](week-54.md), [math check](week-54-math.md) |
| 55 | Sumsets (fewest and most totals) | keep | [card](week-55.md), [math check](week-55-math.md) |
| 60 | Take it or pass (optimal stopping) | keep | [card](week-60.md), [math check](week-60-math.md) |
| 62 | Conflict networks and scheduling | keep | [card](week-62.md), [math check](week-62-math.md) |
| 63 | Cards away from home (derangements) | revise: the K–1 table has no route after the launch, though placing and checking cards suits it | [card](week-63.md), [math check](week-63-math.md) |
| 64 | Straight paths on strange surfaces (a glued octagon, square-tiled surfaces) | keep | [card](week-64.md), [math check](week-64-math.md) |
| 65 | Hyperbolic octagon streets | keep | [card](week-65.md), [math check](week-65-math.md) |
| 66 | Lamplighter streets (the lamplighter group) | keep | [card](week-66.md), [math check](week-66-math.md) |
| 67 | Meeting on shortest roads (medians) | keep | [card](week-67.md), [math check](week-67-math.md) |
| 68 | How many ways out (ends of graphs) | keep | [card](week-68.md), [math check](week-68-math.md) |
| 69 | Thin and fat road triangles (hyperbolicity) | keep | [card](week-69.md), [math check](week-69-math.md) |
| 70 | Four shields in a portal room (the torus) | keep | [card](week-70.md), [math check](week-70-math.md) |
| 71 | Can you hear the room? (billiard words) | keep | [card](week-71.md), [math check](week-71-math.md) |
| 72 | A robot that remembers area (the Heisenberg group) | keep | [card](week-72.md), [math check](week-72-math.md) |
| 73 | The gentlest stretch (least stretch maps) | keep | [card](week-73.md), [math check](week-73-math.md) |
| 74 | Doubling elevators (BS(1, 2)) | keep | [card](week-74.md), [math check](week-74-math.md) |
| 75 | Twists on a cylinder (winding and Dehn twists) | revise: "crossings" on page 4 means seam crossings everywhere before, so children can minimise the wrong thing, and page 3 asks for twisted routes with no board that holds them | [card](week-75.md), [math check](week-75-math.md) |
| 76 | Substitution strips (Thue–Morse) | keep | [card](week-76.md), [math check](week-76-math.md) |
| 77 | Persistent holes | keep | [card](week-77.md), [math check](week-77-math.md) |
| 78 | Three-armed lines (tropical lines) | keep | [card](week-78.md), [math check](week-78-math.md) |

## Calibration

The format was calibrated on Weeks 1, 2 and 15, which children have used, with the September version of Week 1 as a negative control. In the final round all four verdicts matched what the organizer saw. See [calibration.md](calibration.md) for the rounds, the changes and the limits.

## Changes

- 2026-10-05: first version, calibrated on Weeks 1, 2 and 15. `MATH.md` asks for scripts that run from their committed copy in `checks/`.
