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
| 2 | Switches and lamps | original verdict revise; both musts fixed October 23 without altering the approved catalog pages: blank boards with 22 mm lamps and two-sided counters (physically unrehearsed), and a theorem-first adult guide keyed to compact P1–P10 with checked answers, the one-light decision and the invented-puzzle test; should 3 (stale links) fixed; shoulds 4–8 deferred | [card](week-02.md), [math check](week-02-math.md) |
| 5 | Tower cities (visibility clues) | original verdict revise; the must-fix (the guide's 4–5 Problem 5 entry on the 204 cities no puzzle can single out) fixed October 23, with should-fixes 2–3 (pointing across the folder, the facts in section 1), coulds 4–6 and the README link of 9; could 7, the student-page could 8 and the redesign note of 9 deferred, student packets unchanged | [card](week-05.md), [math check](week-05-math.md) |
| 8 | Rook race and Nim | keep | [card](week-08.md), [math check](week-08-math.md) |
| 9 | Bouncing paths | original verdict revise; the must-fix (the guide's walking rule and K–1 hints) fixed October 23, with should-fixes 2–4 and coulds 7–9; the student-page coulds 5–6 and the second run's launch fold deferred, student packets unchanged | [card](week-09.md), [math check](week-09-math.md) |
| 10 | Bridges (Euler walks) | keep | [card](week-10.md), [math check](week-10-math.md) |
| 11 | Chip firing with a sink | keep | [card](week-11.md), [math check](week-11-math.md) |
| 12 | Catalan bijections (noncrossing pairings, paths and trees) | original verdict revise; the must (K–1 Problem 4 duplicate hint) and guide shoulds 2, 5 and 6 (return-visit line, 20 cm strings measured but unrehearsed, K–1 timing order) fixed October 23; shoulds 3–4 (student frames) deferred, student packets unchanged | [card](week-12.md), [math check](week-12-math.md) |
| 15 | Nearest-site regions | keep | [card](week-15.md), [math check](week-15-math.md) |
| 3 | Shuffle machines (permutations as arrow mats) | keep | [card](week-03.md), [math check](week-03-math.md) |
| 4 | Stars and secret wheels | original verdict revise; the must-fix (the 4–5 Problem 12 dents) fixed October 23, with should-fixes 2–3, the guide part of 4, coulds 5–7 and the README link of 9; the 2–3 Problem 5 wording (fix 4), could 8 and the redesign note of 9 deferred, student packets unchanged | [card](week-04.md), [math check](week-04-math.md) |
| 6 | Code breaking (guess my block, the counter code game) | original verdict revise; the must-fix (the 2–3 Problem 11 key) fixed October 23, with should-fixes 2, 3, 5 and 6 and coulds 7, 8 and 10; the K–1 Problem 6 wording (should 4) and coulds 9, 11–13 deferred, student packets unchanged | [card](week-06.md), [math check](week-06-math.md) |
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
| 23 | Sorting networks | original verdict revise; the must (a print-and-cut mat, cards and bars) fixed October 23 with a four-sheet table kit, `week-23-materials.pdf`, and a guide preparation section that names it and counts cutting; shoulds 2–9 and coulds deferred, student packets unchanged, kit physically unrehearsed | [card](week-23.md), [math check](week-23-math.md) |
| 24 | Nontransitive dice and decks | keep | [card](week-24.md), [math check](week-24-math.md) |
| 25 | Row and column shadows | original verdict revise; the must (Grades 2–3 Problem 4 lower-bound hint) and guide shoulds 2 and 8 (one-picture launch, 24 counters) fixed October 23; student-page shoulds 3–7 and 9 deferred, student packets unchanged | [card](week-25.md), [math check](week-25-math.md) |
| 26 | Same area, different boundaries (polyomino perimeter) | original verdict revise; the must's guide part (accept both hole answers with their corner conventions) and should 2 (K–1 extension) fixed October 23; the must's student wording for 4–5 P2 and should 3 deferred to a problem-file conversion, student packets unchanged | [card](week-26.md), [math check](week-26-math.md) |
| 27 | Stable matching | original verdict revise; the must (tokens, strips, links and markers nothing supplied) fixed October 23 with a nine-page table kit, `week-27-materials.pdf`, that prints every case's strips ready to cut, and should 2 (a launch profile printed in no packet); shoulds 3–7 and coulds deferred, student packets unchanged, kit physically unrehearsed | [card](week-27.md), [math check](week-27-math.md) |
| 28 | Single-vertex flat folding | original verdict revise; the must (nothing printed the disks, wedges, tabs or cards) fixed October 23 with a 15-page kit, physically unrehearsed, and guide pp. 1–2 (with should 2, the recording demonstration); shoulds 3–6 (student pages) deferred, student packets unchanged | [card](week-28.md), [math check](week-28-math.md) |
| 29 | Two-length builders (the last gap, ab − a − b) | original verdict revise; the must (K–1 Problem 6 key: 7, 9, 11) and guide shoulds 4, 5 (guide part), 6 and 10 (1 cm scale, 6-rods, 4/6 gaps, timing) fixed October 23; student-page shoulds 2, 3, 7–9, 11, 12 and the printable rod sheet deferred, student packets unchanged | [card](week-29.md), [math check](week-29-math.md) |
| 30 | Two-pan weight kits (balanced ternary) | keep | [card](week-30.md), [math check](week-30-math.md) |
| 31 | Hidden orchard (lattice visibility) | original verdict revise; the must (moved-viewer example) and guide should 6 (launch marks, timing) fixed October 23; student-page shoulds 2–5 deferred, student packets unchanged | [card](week-31.md), [math check](week-31-math.md) |
| 32 | Squares inside rectangles (Euclid by squares) | keep | [card](week-32.md), [math check](week-32-math.md) |
| 33 | Prime-length necklaces | keep | [card](week-33.md), [math check](week-33-math.md) |
| 34 | Hidden turns (distinguishing colourings) | keep | [card](week-34.md), [math check](week-34-math.md) |
| 35 | Footprint borders (frieze symmetry) | original verdict revise; the must (footprint pieces in four forms) fixed October 23 with a one-page card kit, `week-35-materials.pdf` (12 A and 12 mirror-A cards of 29 × 26 mm per group), and the anchor part of should 5 (recipe positions are card centres); the rest of should 5, shoulds 2–4 and 6–7 and coulds deferred, student packets unchanged, kit physically unrehearsed | [card](week-35.md), [math check](week-35-math.md) |
| 36 | Making threes (nine-tile SET) | keep | [card](week-36.md), [math check](week-36-math.md) |
| 37 | Mirror twins (tetrahedron chirality) | original verdict revise; both musts fixed October 23: the guide (pp. 1, 3, 4) accepts "A must go on A, and all three turns about A fail" as complete, and a 3-page kit (90 mm card net, letter caps A, A, B, B, C, C, D, pose mat; physically unrehearsed); guide shoulds 5–6 taken; shoulds 3–4 (student pages) deferred, student packets unchanged | [card](week-37.md), [math check](week-37-math.md) |
| 38 | Seams and cuts (Möbius band) | keep | [card](week-38.md), [math check](week-38-math.md) |
| 39 | Road detours (path reduction) | revise: K–1 Problem 7 has two readings, and the key tells the adult that the natural one is wrong, so an adult may correct a right answer | [card](week-39.md), [math check](week-39-math.md) |
| 40 | Loop colour certificates (knot tricolouring) | keep | [card](week-40.md), [math check](week-40-math.md) |
| 41 | Torus portals and lifts | keep | [card](week-41.md), [math check](week-41-math.md) |
| 42 | Fair results from a bag (von Neumann's fair coin) | keep | [card](week-42.md), [math check](week-42-math.md) |
| 43 | Shuffling picture cards (fair shuffles) | original verdict revise; the must (K–1 Problem 2's crossed-out cards, now printed as the card drawn first, and the guide key) and K–1 shoulds 4–5 (no chance wording, larger Problem 3 records) fixed October 23 in the new problem files, with could 14's typo; shoulds 2, 3, 6–8 and the other coulds deferred, Grades 2–3 and 4–5 packets unchanged | [card](week-43.md), [math check](week-43-math.md) |
| 44 | The bag that copies (Pólya's urn) | keep | [card](week-44.md), [math check](week-44-math.md) |
| 45 | The visible side (conditioning on a clue) | keep | [card](week-45.md), [math check](week-45-math.md) |
| 46 | Two boards forget their starts (coupling) | keep | [card](week-46.md), [math check](week-46-math.md) |
| 47 | Gentle-step landscapes (extending clues, lowest and highest landscapes) | keep | [card](week-47.md), [math check](week-47-math.md) |
| 48 | Inside and outside covers | keep | [card](week-48.md), [math check](week-48-math.md) |
| 49 | Four towers and differences (Ducci rings) | keep | [card](week-49.md), [math check](week-49-math.md) |
| 50 | Staircases and lengths | keep | [card](week-50.md), [math check](week-50-math.md) |
| 51 | Honest measurement ranges | revise; the first must (strips with lengths, count and construction) fixed October 23 with a one-page strip kit, `week-51-materials.pdf`, and a guide without sleeves; the second must (K–1 Problem 4 wording) is a student-page change left for a problem-file conversion, with shoulds 3–8 and coulds deferred; student packets unchanged, kit physically unrehearsed | [card](week-51.md), [math check](week-51-math.md) |
| 52 | Hinged frames and braces | revise: the K–1 route is three problems the guide finishes by minute 30, and Problem 13's "Yes" rests on a one-brace-per-cell rule no upper page states | [card](week-52.md), [math check](week-52-math.md) |
| 53 | Cheapest connected networks | revise: two price labels on page 8 sit on the wrong link, and the K–1 route is one page long | [card](week-53.md), [math check](week-53-math.md) |
| 54 | Partitions and rebuilding (Euler's odd and distinct parts) | keep | [card](week-54.md), [math check](week-54-math.md) |
| 55 | Sumsets (fewest and most totals) | keep | [card](week-55.md), [math check](week-55-math.md) |
| 56 | Corners of a solid (Euler's formula and angular defect) | revise: the K–1 table gets only the p. 3 fans and a fallback that repeats them, though the outline promised work with the closed solids | [card](week-56.md), [math check](week-56-math.md) |
| 57 | Lattice area (Pick's theorem) | keep | [card](week-57.md), [math check](week-57-math.md) |
| 58 | Fair division | keep | [card](week-58.md), [math check](week-58-math.md) |
| 59 | Constant-width shapes | keep | [card](week-59.md), [math check](week-59-math.md) |
| 60 | Take it or pass (optimal stopping) | keep | [card](week-60.md), [math check](week-60-math.md) |
| 61 | Geometry on a sphere (Girard's theorem) | keep | [card](week-61.md), [math check](week-61-math.md) |
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
| 79 | Numbered-ball detectives (the Ross–Littlewood paradox) | original verdict revise; sole must (guide hint scope) fixed October 17; remaining proposals deferred, student packet unchanged | [card](week-79.md), [math check](week-79-math.md) |
| 80 | Midnight laboratory (the Thomson lamp) | keep | [card](week-80.md), [math check](week-80-math.md) |
| 81 | Buckets of Fish (Hamkins's remove-and-refill game) | keep | [card](week-81.md), [math check](week-81-math.md) |
| 82 | Endless class lines (ordinal addition) | keep | [card](week-82.md), [math check](week-82-math.md) |
| 83 | Hackenbush balances | keep | [card](week-83.md), [math check](week-83-math.md) |
| 84 | Public knowledge | revise: Problem 3's "the same three replies" can also be read as which replies appear, under which the right answer is no, and the guide's key gives only yes | [card](week-84.md), [math check](week-84-math.md) |
| 85 | Drawing machines (pantographs) | revise: the whole hour runs on a hand-built pantograph, and nothing names what to build it from (strips, pivots, anchor pin, pencil mounts); both card runs agree | [card](week-85.md), [math check](week-85-math.md) |
| 87 | Voting and agendas | keep | [card](week-87.md), [math check](week-87-math.md) |
| 88 | Packing and kissing circles | keep | [card](week-88.md), [math check](week-88-math.md) |
| 89 | Growing shapes and totals | keep | [card](week-89.md), [math check](week-89-math.md) |
| 90 | Sliding number arrays (jeu de taquin) | keep | [card](week-90.md), [math check](week-90-math.md) |
| 91 | Rotor-router machines | keep | [card](week-91.md), [math check](week-91-math.md) |
| 92 | Fold-and-stretch predictions | keep | [card](week-92.md), [math check](week-92-math.md) |
| 93 | Squaring a rectangle | keep | [card](week-93.md), [math check](week-93-math.md) |
| 96 | Prime bags and divisor builders | keep | [card](week-96.md), [math check](week-96-math.md) |

## Calibration

The format was calibrated on Weeks 1, 2 and 15, which children have used, with the September version of Week 1 as a negative control. In the final round all four verdicts matched what the organizer saw. See [calibration.md](calibration.md) for the rounds, the changes and the limits.

## Changes

- 2026-10-05: first version, calibrated on Weeks 1, 2 and 15. `MATH.md` asks for scripts that run from their committed copy in `checks/`.
