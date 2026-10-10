# Week 74: Doubling elevators

**Verdict: keep.** The mathematics is real, every answer and diagram checks, and the pages meet the spec. The fixes are one guide sentence, a stride aid and a plan for the other tables. None leaves anyone stuck.

Reviewed October 10, 2026 by Claude, with the math check in [week-74-math.md](week-74-math.md). Packets: week-74-students.pdf (GGT74-S-v1, one shared Grades 4–5 packet, 4 pp.). Adult guide: week-74-facilitator.pdf (GGT74-FAC-v1, 3 pp.). Companions noticed but not reviewed: none. Status: unpiloted prototype awaiting organizer review. Independently reviewed (plans/ggt-prototypes-66-75/week-74/). Marker and partner handling unrehearsed.

## The mathematics

The board is a graph on (x, h) with h ≥ 0. At level h a stride moves 2^h, and every move costs one. It is the part of BS(1,2) where strides double going up. A trip of at most N moves that tops out at level H spends 2H moves climbing and descending. Each remaining move goes at most 2^H, so the trip ends at most (N − 2H)2^H from 0. The bound is attained, so 16 needs 8 moves. A second idea is that a step back can strictly win: 23 takes 10 moves via 24, against 11 without left moves, by a binary coin count. A mathematician would enjoy both. P2–P4 carry the bound, P5 the saving.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | An attained all-routes bound and a signed-binary saving. |
| Problems | strong | The order runs: find routes (P1), find ties (P2), budgets 4–8 (P3), prove impossibility (P4), compare left moves (P5). P1 is lightest but sets 3 (climbing does not pay) against 7 (it does). |
| Student pages | strong | Correct header and footer. Rules are stated once, with a non-task example (URD from 1). No hints, titles or slop; full boards on pp. 1, 2, 4. Only coulds remain. |
| Concreteness | adequate | The partner checks and writes one move word, but nothing enforces the stride. Dots are 5.84 mm apart, and a level-4 stride is 16 dots counted by eye. The launch is for one table. |
| Correctness | strong | math.md verifies every student answer, board and guide claim. My BFS agrees: reach is 4, 6, 8, 12, 16. Left moves strictly save at 23, 31, 39, 46, 47, 55, 62, 63 (up to 64). |
| Adult guide | strong | Theorem-first, with limits. It gives an honest rehearsal note, a launch, timings, hints and the 15, 23 and no-left proofs, plus a token version of the bound. |
| Age fit, K–1 | no route | Not claimed, as a recorded design choice. |
| Age fit, grades 2–3 | no route | Not claimed. P1–P3 need only letters and adding 1–16 under 25, so third graders might start with an adult (prediction). P4–P5 would be adult-run. |
| Age fit, grades 4–5 | strong (predicted) | Short reading, easy arithmetic, and one word kept by the partner. Abstraction rises late, in P4 and P5. The organizer is at this table. |

## Keep

- The board: every integer dot on every level, shared columns, "step" labels, the origin ring, and the −4 to 24 window, which holds every guide route including (24,3). Keep "The roads continue beyond this page".
- The URD example from coordinate 1 (input, intermediate, output), which gives away no task.
- One child moves while the partner checks and records one word. They swap after a trip.
- P2's open "two different trips tied". Exactly two exist, UURRRRDD and UUURRDDD, at different heights.
- P3's budgets. Budget 8 meets P2's 16.
- P4's "seven or fewer" and its demand to cover left moves and repeated level changes.
- P5's targets: 9 and 17 just past 8 and 16, 15 (an overshoot ties) and 23 (an overshoot wins). Keep the child's choice.
- The guide's overview, its "best found" versus "proved best" stop, the token argument and the proofs.

## Fix

1. **should**, guide p. 2, Problem 2: "Do not reject different routes just because they use intermediate heights; a valid shorter claim should be replayed." math.md (Finding 1, exhaustive to length 8) shows these are the only two eight-move trips. The sentence implies more exist, and the adult cannot tell children their list is complete. Use math.md's replacement. Equality in (8−2H)2^H ≥ 16 forces H = 2 or 3, exactly 2H vertical moves and every horizontal move rightward on top. Any other claimed route of eight or fewer moves has a replay error.
2. **should**, guide p. 1, Materials and Launch. The guide admits the rows do not enforce the stride. The partner counts up to 16 dots 5.84 mm apart. This is context.md's paper-only-rule risk, though here it is a prediction. Add a printable stride strip with ticks at 0.23, 0.46, 0.92, 1.84 and 3.68 in. Lay it along the row from the marker. Use it in the launch for one R from an odd coordinate on level 2.
3. **should**, guide p. 1, "Who this fits" and Launch. context.md has three tables, and AGENTS.md wants one whole-group demonstration first, but the packet serves one table. Add a paragraph naming what the K–1 and 2–3 tables do that hour and the shared demonstration. For example, the 2–3 table could do P1–P2 with targets up to 8. No new packet is needed.
4. **could**, boards pp. 1, 2, 4: only even coordinates are labelled, but every target is odd. Label every column in \scriptsize.
5. **could**, p. 3, P4: three answer lines over an empty bottom third. Extend them.
6. **could**, p. 1: "Move a pawn" conflicts with the guide's "very small pointed marker". Say "marker".
7. **could**, p. 3, P3: "Start at 0 on level 0." repeats the shared rule. Cut it.
8. **could**, guide overview: add that two more moves double the reach (4, 8, 16, 32), so the shortest trip to 2^k is 2k moves. This is the distortion it names.

## Overlaps

Week 66 (Lamplighter streets) is the nearest sibling. It also asks for shortest move words with lower bounds from unavoidable moves, but its group and theorem differ (dead ends, a decomposition). Keep both, and consider sharing a move-word board in the app. Week 30's signed-digit weights echo the 23 = 24 − 1 saving on a different object. No merge.

## App fit

Fit A, size S. themes.md has no row. Proposed: | 74 | Doubling elevators | Ride a marker up and down levels whose strides double; shortest trips, farthest reach in a budget, when a step back helps | Top level H costs 2H moves and allows strides ≤ 2^H, so reach ≤ (N − 2H)2^H; 16 needs 8; 23 needs a left step (10 vs 11) | No | A | Tap U/D/L/R on a scrolling level board; reach a target within par; certify "can't" level by level | S |.

The app enforces the stride and scrolls past the window. The solve is to reach (n, 0) within a BFS-checked par. Plume's count fits.

- **Easy:** 3, 7, 8.
- **Medium:** 9, 15, 17, and 16 with both ties.
- **Hard:** 23, 31, 47, 63, plus a locked-L variant at 23 (11 against 10).
- **Reverse:** farthest reach in N moves (P3).
- **"Can't":** 16 in 7 and 23 in 9. The certificate is P4's height table or the guide's tokens: two per level go to the climb, and the rest stretch at most 2^H.

Avoid four things:
- A "2 of 2" counter on the ties. The child should declare "done".
- Predict-the-landing tasks.
- Any par that has not been proved optimal.
- Calling the board the full BS(1,2) Cayley graph.

**Decision, October 10, 2026.** Ported as **Doubling elevators** ([app PR #29](https://github.com/jamesrp/small-math-adventure/pull/29), `docs/elevators/`): flags within the fewest moves, the step-back savings at 23, 47 and 63, and the farthest reach in 9 and 11 moves. The window is fixed rather than scrolling, and the "can't" certificate and locked-left variant wait. Satchel only; not deployed and not yet played by children.

## Classroom evidence

None reported.
