# Week 86: Pursuit and escape

**Verdict: keep.** No must. Every board, answer and proof checks, and the guide opens with the theorems. The fixes are a K–1 route, two key sentences, trees that add nothing to the paths, and a printed fold lemma.

Reviewed October 23, 2026 by Claude, with math.md. Packets: week-86-shared.pdf (W86-S-v1, Grades 2–5, 4 pp., P1–P4), week-86-upper.pdf (W86-U-v1, Grades 4–5, 6 pp., P1–P6; P1 repeats shared P1), week-86-materials.pdf (3 pp.). Adult guide: week-86-facilitator.pdf (6 pp.). Companions noticed but not reviewed: none. Status: unpiloted, and no organizer review is recorded. There is no K–1 packet, by design. I agree with both math.md items and rate both should. The keep depends on fix 2 being a should. A second card run from the same inputs ([checks/week-86/card-second-run.md](checks/week-86/card-second-run.md)) rated the missing K–1 route a must and the verdict revise. Reconciled October 23 as keep: the week claims no K–1 coverage ("There is no independent K–1 edition", guide p. 1; the source plans decline K–1 packets for these families), which the Week 76, 81, 87, 96 and 97 cards rate should. The Week 52, 53, 56 and 63 musts concern weeks whose outlines offered a K–1 route that the pages left thin. Both runs agree on the math items and rate them should.

## The mathematics

Cops and robbers on a map, with visible moves, stays allowed and the cop first. Every tree is cop-win: once C's dot is removed, R's piece shrinks with each cop step. Bare rings of four or more dots are robber-win, because R stays out of C's reach; the triangle is not. A fold removes a dot whose reach lies inside a neighbour's and keeps the winner, so a map is cop-win exactly when it folds to one dot (Nowakowski–Winkler, Quilliot). A mathematician would enjoy it. Shared P1–P4 set trees against rings; upper P2–P6 add edits, design, folds and two cops.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A classification theorem reached through play. The path trap and the square's opposite-dot reply are proofs children can play out. |
| Problems | strong | The order carries it: paths, trees, triangle against square, odd and even rings, then edits, design, folds and two cops. One thin rung (fix 4). |
| Student pages | adequate | Spec header, footer and numbering. Dots are 22 mm for 18 mm counters, rings are regular, and worked visuals come before the game and before folds. Upper p. 4 prints the fold lemma (fix 5). |
| Concreteness | strong | The opponent enforces the rules and the tile holds the turn. Covers hide deleted dots beside an unchanged original. The guide has a whole-group launch on a non-task graph. |
| Correctness | strong | math.md checks all 29 boards and every proof. My solver (card_spot.py) agrees on P1, the trees, the rings and all ten E5 chord pairs. Fixes 2–3 are guide sentences. |
| Adult guide | strong | Theorem-first, with assumptions, limits, a band map and experiment kept apart from explanation. Every problem keyed with reasons; both fold proofs; the two-cop blocker. |
| Age fit, K–1 | weak | No route: "Select a familiar activity for K–1" (guide p. 2). |
| Age fit, grades 2–3 | adequate | No reading for the child, and counting only to three. Prediction: P3–P4's "plan that works against every reply" needs the table's mathematician. |
| Age fit, grades 4–5 | strong | Edits, design and folds give real arguments, and the rotating referee suits a trio. |

## Keep

- p. 1's rules and the three-panel w, x, y, z example (C moves, R stays, tiles C, R, C).
- P1's "fewest C turns"; P3's triangle against square in one question; P4's odd and even rings.
- Upper P2's "as few roads as possible" and "A crossing is not a new dot".
- Upper P3's "all six dots and at least six roads", which forces a cycle into the cop-win map, on hexagons with no three dots in line.
- Upper p. 4's fold rule with staying included, the boxed reach sets, and F1/F2 as original and working copies.
- Upper P5's common start at a, and P6's every-ring question.
- The guide's "Merely saying the distance decreases is insufficient" and its projection proof for one chord.

## Fix

1. **should**, K–1, guide p. 2. There is no route, and the K–1 table watches a launch for a game it won't play. It is a should, as on the Week 76, 81 and 87 cards, because the family plan records "a full separate K–1 packet is not planned". Fix: run the launch, P5 aloud ("Where should C start?") with the parent turning the tile, then R3 against R4 ("On which ring can R get away?"). That K–1 keeps the turns is a prediction.
2. **should**, guide p. 3, shared P4: "“Opposite” is not an adequate general rule on an odd ring." On odd rings, staying on either dot across from C is never caught (math.md item 1). It is not a must: the paragraph's own rule, two sentences earlier, accepts that plan, and the likely intent (an odd ring has no single opposite dot) is true. Use math.md's replacement.
3. **should**, guide p. 4, upper P2: "A different pair of chords is acceptable if its claimed strategy is valid". All five crossing pairs (such as a–c with b–d) lose, and the key gives the adult nothing to check a lucky pair against. Add math.md's two sentences (item 2).
4. **should**, shared p. 2, P2. Both trees have centre c at radius 2, like P5. Under the guide's plan, walk toward R, R never gets from one branch into another on either tree, from any start (card_arms.py, every reply). P1's answer settles both trees in two cop moves, against the guide's 12–20 minutes (a prediction). Fix: lengthen T1's branch to c–f–g–h and add "On T1, C starts at h". R can then run out of the branch into the row ahead of C.
5. **should**, upper p. 4: "Try shrinking a map without changing who can force a win." This states as fact the lemma whose shadow proof the guide calls "an additional readiness gate" (p. 4), and it answers P4's "What does this suggest about the chasing game?" in advance. Delete it.
6. **could**, shared P4: cut "A long game is a test;".
7. **could**, guide p. 2: drop the "compact locators" sentence (there are none), and call the tile "Both cops", as printed.
8. **could**, upper P2 and P3: use one wording for crossings ("not a new dot" or "not junctions").
9. **could**, upper p. 3: D1's label d sits 0.4 mm above "D2: R can escape forever"; move the heading down.
10. **could**, move labels that sit on roads (T1 f, g; T2 c; R6 and Q6 b, f; F1 a) beside their dots.
11. **could**, materials pp. 1–2: change the header to "Grades 4–5".
12. **could**, guide p. 5: add the outline's one-minute two-cop demonstration before upper P5.
13. **could**, guide p. 3: name upper P2 as the next problem for a pair that finishes shared P4.

Fixed October 23, 2026: shoulds 1–5 and coulds 6–13 in the problem files, materials and guide (the second run's "Who can always win the chasing game on F1, and on F2?" ends upper P4, and its cover sentences are cut to one); see source/week-86/README.md.

## Overlaps

Week 67 uses a tree's unique paths for a meeting dot, here for a sure capture. Week 69 also sets trees against rings, and the square's reply is the Week 1 encore's copying strategy. No other theme has a pursuit game. No merge.

## App fit

Not in themes.md. I propose this row: | 86 | Pursuit and escape | Move a cop and a robber one road at a time; add roads; design maps; fold dots; two cops | Trees are cop-win; bare rings of four or more dots are robber-win; a map is cop-win exactly when it folds to one dot; two cops catch on any ring | No | B | Catch a perfect robber within a target; Can't by answering every cop move; fold to a dot | M |

The child taps C's moves on the graph board and the app plays a perfect R. Solves:
- Catch R within a target: 2 turns on P5, 3 on P7, or from h on fix 4's tree. The app's R, staying on the far end, certifies "best".
- Rings: Can't, then play R against every cop move (Pebble Duel's every-reply groups); escape is certified when the positions close up.
- Add the fewest roads, then catch. The crossing pentagon pairs are the trap.
- Fold by tapping v, then u; an illegal fold shows the dot u misses. Fold to one dot, or That's all when stuck.
- Two cops on rings of 6 and 8.

Pitfalls: never accept a turn count as escape; R must play perfectly; don't highlight reach sets or safe dots; no predict-who-wins screens. Draw on shared P1–P4 and upper P2 and P4–P6.

## Classroom evidence

None reported. Counter fit, the turn tiles and the fold covers are physically untested (source README). The index says "Nothing is marked taught or organizer-promoted."
