# Week 77: Persistent holes

**Verdict: keep.** No must: every answer checks, every board matches its text, and the guide is theorem-first and complete. The should items are a Problem 3 that repeats Problem 2, one overview sentence, a hand-made kit and the launch.

Reviewed October 10, 2026 by Claude, with the math check in [week-77-math.md](week-77-math.md). Packets: week-77-students.pdf (F77-45-v1, 5 pp., one shared Grades 4–5 packet, Problems 1–6). Adult guide: week-77-facilitator.pdf (F77-FAC-v1, 4 pp.). Companions noticed but not reviewed: none exist. Status: unpiloted prototype awaiting organizer review; guide p. 2: "Physical rehearsal and classroom piloting have not been performed." I agree with both math.md findings and rate them should (fix 2) and could (fix 6).

## The mathematics

Small planar triangle boards grow by edges and filled triangles. A saved loop is gone exactly when some filled triangles cancel its edges in pairs (mod 2). So a gone loop never returns (P5); equal hole counts at every stage do not fix when a loop dies (P2–P3); and different loops can be equivalent on one board yet separable on a fresh one, as their required-tile sets are nested or not (P6). This is persistent homology over F2 in miniature, and a mathematician would enjoy P6.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Cycles modulo boundaries, irreversible deaths, counts that do not determine history, homologous cycles separated on a smaller complex. |
| Problems | adequate | P1, P2, P6 substantial; P5 a real "explain why". P3 repeats P2 (fix 1); P4 is a light four-case check. The order carries the development. |
| Student pages | adequate | Spec header and footer; no headings, hints or encouragement. P1's 219 words are needed conventions and the required worked XYZ visual. Faults: fixes 3, 6. |
| Concreteness | adequate | Strips, tiles and a partner enforce legal builds; stage lists hold the schedule. The "gone" test is a token procedure the tiles do not enforce; kit and launch: fixes 4, 5. |
| Correctness | strong | math.md: 93 checks pass, every guide table matches. I re-derived P6's L1 as the boundary of ABO + CDO + DAO, and both orders. |
| Adult guide | adequate | Theorem-first overview with limits, exact tables, ordered hints, timings, fallback, proofs. Fixes 2, 4. |
| Age fit, K–1 | no route | By design: "This packet supplies no route or print allocation for those eight children" (guide p. 1). |
| Age fit, grades 2–3 | no route | Same. |
| Age fit, grades 4–5 | adequate | No arithmetic. The load is keeping board, stage, saved list, test tokens and hole count apart (a prediction); the referee, organizer and stage lists help. P6 is for the quickest. |

## Keep

- p. 1: only test tokens change, never the saved list or board; the partner check that a tile needs all three edges; the XYZ example; P1 tested in separate builds.
- p. 2: the printed stage list; "Explain why you have all of them."
- p. 3: the counts question, the point of the packet.
- p. 4: P4's tied stage; P5 as printed.
- p. 5: P6's two parts, with "or explain why it is impossible."
- Guide: the overview, all four tables, the P5 proof, the P6 necessity argument, the fallback.

## Fix

1. **should**, 4–5, p. 3, P3: "Make one build where the first loop is gone at 5, and another where it first disappears at 8." P2 already has both with equal counts (guide p. 3, rows 3–4), so P3 takes a minute and its question answers itself. Replace that sentence with "Whichever dashed edge comes first, can the first loop be gone at stage 5? Can it on the square in Problem 2?" and the last with "Every build on these two boards has 0, 1, 2, 1, 0 holes after stages 0, 2, 4, 5, 8. Can those counts alone tell you when the first loop disappears?" Relabel the answer areas "AB first", "DE first", "Square". Guide answer: yes here; on the square only with AC first, since DA first saves the outer rim, which needs both tiles (P1).
2. **should**, guide p. 1 (math.md item 1): "Two triangles meeting at a single vertex can instead lose their older loop first" implies the square cannot, but P2 row 3 does. Use math.md's wording: "When R closes first (DA before AC), either one-tile filling leaves R nonzero; both kill it. When a triangle rim closes first, on the square or on two triangles meeting at a vertex, filling that triangle first kills the older loop."
3. **should**, 4–5, p. 2: "Every allowed schedule has 0, 1, 2, 1, 0 holes after stages 0, 2, 4, 5, 8." P2 never asks about holes. Delete it; move "Count each enclosed, unfilled region as one hole." into P3 before its counts sentence.
4. **should**, guide pp. 1–2: the organizer hand-labels 44 tokens and 8 stage cards and traces 17 tiles, and nothing ties a tile to its three test tokens but the child's reading (the shape of Week 2's paper-rule failure; a prediction here). Add a print-and-cut sheet: tokens, stage cards, and tiles at board scale with each edge name printed along its side.
5. **should**, K–1 and 2–3, guide p. 2: "5–8: short whole-group demonstration; only the target trio continues", with p. 1's 1.8 cm XYZ triangle, too small for a group. Eight children watch what they will not use. Make it the 4–5 table's launch after the session's shared one. A later 2–3 route: P1–P2 with tiles, asking "is every triangle inside covered?" (a prediction).
6. **could**, p. 3 (math.md item 2): A, C, E and B, C, D are collinear, so the board prints as two crossing lines. Bend at C: D = (11.6, 1.2), E = (11.6, 7.0).
7. **could**, guide: say that on these planar boards a loop is gone exactly when every triangle inside it is tiled, so survival needs no search over tile choices.
8. **could**, p. 4, P5: "survive again" → "come back".

## Overlaps

Week 2's bonus Problem 1C finds the same square's three do-nothing sets, P, Q and R. Week 77 adds filled faces and time, so it is the sequel; cite it in the guide. Weeks 39 (reduced walks), 56 (V − E + F), 41 and 75 (winding) treat loops otherwise. None has filled faces or a growing board. No merge.

## App fit

Fit B, size M. Proposed row: | 77 | Persistent holes | Add edges and tiles on a schedule; save a loop; test whether filled tiles cancel it | Loops modulo filled boundaries, mod 2; gone loops never return; counts don't fix which loop dies | No (Lantern Wires toggles mod 2) | B | Tap tiles to cancel a lit loop; schedule pieces to hit a target death stage or order | M |

A triangle fills only when its edges are present. Tapping a filled tile toggles its three edges on the lit saved loop; the solve is a dark loop, and "can't" often has a certificate: a lit edge that only unfilled tiles touch. Schedule goals (P2, P6) check by replay; nested tile sets certify that a pair cannot die in both orders. Pitfalls: four schedules invite guessing, so use strips of four to six triangles or a ring with a permanent hole; leave out P3's question and P5 (predict-and-explain) and any "3 of 4" counter. Draw on P1, P2, P6.

**Decision, October 10, 2026.** Port, in Wave 9, as a loop group in Lantern Wires, which already toggles mod 2: tapping a filled triangle toggles its three edges on the lit loop, the solve is a dark loop, and "can't" is certified by a lit edge that only unfilled tiles touch. Boards are strips or rings with a permanent hole, so whether a loop can be cancelled is a real question. Schedule goals (a target death stage or order, checked by replay) are the Hard puzzles. No counters and no predict-and-explain screens. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported. Unpiloted prototype awaiting organizer review.
