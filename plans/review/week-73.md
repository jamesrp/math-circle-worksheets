# Week 73: The gentlest stretch

**Verdict: keep.** Every answer checks, the problems run from a pin test to a whole-sheet proof of a real optimum, and nothing leaves a child or adult stuck. The fixes are a contrasting target in Problem 5 and two guide additions.

Reviewed October 10, 2026 by Claude, with the math check in [week-73-math.md](week-73-math.md); the card's spot checks were by hand. Packet: week-73-students.pdf (GGT73-S-v1, 4 pp., one shared Grades 4–5 packet). Adult guide: week-73-facilitator.pdf (GGT73-FAC-v1, 3 pp.). Companions: none. Status: unpiloted prototype awaiting organizer review; dot, strip and ruler handling unrehearsed (source README, QA.md).

## The mathematics

Move a 4-by-1 sheet onto a 2-by-2 square, each named side onto its match, with no gaps, overlaps or tears. Every such map stretches some pair by at least 2, because the ends of a vertical unit segment land on opposite sides of the square; halving across and doubling up attains 2 for every pair. For a W-by-H target the answer is max(W/4, H). P1–P2 add a sampling trap: every five-pin score ties at 2, and only side-midpoint tests single out the centered fan, by two tangent unit disks. A mathematician would enjoy both. P1–P2 carry the experiment, P3–P4 the theorem, P5–P6 the generalization.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A two-sided optimum certified by a rule and an unavoidable pair, plus the gap between finite tests and a whole map. |
| Problems | adequate | P2, P3–P4 and P6 each hold well over five minutes; the order carries the development. P1 is flat by design. P5's two targets both turn on height (fix 2). |
| Student pages | strong | Right header and footer, rules once with a 2 cm → 3 cm example, a non-task PQR example before the fan rule, both figures at one 0.94 in unit, no slop. Coulds only. |
| Concreteness | adequate | Dots, strips and a partner hunting for the worst pair; midpoints are constructible. The guide's launch shows one placement and one test. Rulers miss a quarter-unit sideways offset (0.735 mm); the guide says so. P3–P6 live on paper. |
| Correctness | strong | Everything checks (math check). I rechecked P1's ratios, the 0.735 mm and max(W/4, H). |
| Adult guide | adequate | Theorem-first overview separating ruler results, the fan-family argument and the all-maps proof; materials, timing, first route, keys, hints. Fixes 1 and 3. |
| Age fit, K–1 | not offered | No route, by design (source README; guide p. 1). |
| Age fit, grades 2–3 | not offered | No route, by design (guide p. 1). P1 with a doubling strip would suit third graders (fix 9). |
| Age fit, grades 4–5 | adequate | P1–P2 need a ruler, halves and midpoints; P3–P6 are late proofs, reachable with the organizer at the table. Predictions: dividing measured lengths is past most fourth graders (fix 1); P2 asks for spokes, halfway dots and paired measurements at every placement. |

## Keep

- P1's flat game and the guide's "Do not announce that every placement ties". It sets up P2's twist.
- P2's roles (the partner places O, the hunter seeks a pair beating the original five dots) and "Which positions for O survive your tests?"
- P2's PQR example: a different triangle, the midpoint rule shown, nothing given away.
- One 0.94 in unit and quarter grid on pp. 1–2; p. 3's dotted lines with "Draw where the dotted lines go".
- P4's two questions, P5's "Rule and unavoidable pair" blank, P6's open invention.
- Guide: the three stages, "Accept an honest set of apparently surviving near-center positions", the double-then-compress argument, the complete P6 answer.

## Fix

1. **should**, guide p. 1, launch: nothing says how a child gets a stretch from two ruler readings, and the 1½ example implies dividing. P1–P2 only need "more than twice?". Add: mark the old length twice along a strip and see whether the new length is longer; demonstrate on A–D, which fits exactly twice.
2. **should**, p. 4, P5: both targets are decided by height (6 by 2: across 1½, up 2; 2 by 3: across ½, up 3), so no case shows width deciding. A child who concludes "the answer is the new height" would offer 8 by 1½ in P6, whose optimum is 2. Replace 2 by 3 with 8 by 1, drawn under its 4 by 1 at the same 0.6 in scale. Key: optimum 2, rule (2x, y), unavoidable pair the two bottom corners, 4 apart, which must land 8 apart. Then 6 by 2 and 8 by 1 share the answer 2 for different reasons.
3. **should**, guide p. 2, P1 and P3 keys: the packet's thread is never stated. Add to P1 that A–D is P4's lower bound for every legal rule, since corners must go to corners. Add a P3 hint: a P2 fan is already a rule for every point, and the centered fan is exactly (x/2, 2y).
4. **could**, pp. 1–3, the inner "right" and "left" labels sit 1.4–2.3 mm apart (math check item 1); move them to x = 4.2 and −0.2. A mirror misreading still has stretch 2.
5. **could**, P5 "a pair that no legal rule can stretch less": "a pair that every legal rule stretches at least that much".
6. **could**, P5: the partner only chooses; add "and tests your rule", as in P3.
7. **could**, p. 4, the first arrow nearly touches the 6 by 2 "left" label; end it at 4.9.
8. **could**, p. 2 caption "Example: M stays halfway from P to Q; N stays halfway from P to R." repeats the labels; delete it.
9. **could**, a Grades 2–3 entry: P1 with the doubling strip and a 4 by 1 → 8 by 2 target use only whole-number stretches.

I agree with the math check's one finding and rate it a could, since no answer changes.

## Overlaps

Week 47 (1-Lipschitz extension on a row) shares the idea, not the object. Week 75 keeps named boundaries under whole-surface maps but counts winding. Nothing else asks for a least worst stretch. No merge; Week 47 makes a good return-visit contrast.

## App fit

B, size M. Proposed row: | 73 | The gentlest stretch | Place O's image to make a fan map; hunt for the worst pair; write a whole-sheet rule; least worst stretch for new targets | Opposite sides force stretch at least 2; (x/2, 2y) attains it; max(W/4, H) in general; a few pins can't certify a map | No | B | Drag mesh points on a snap grid with sides enforced; the app shows the worst-stretched pair; meet the budget, then tap a pair no map can beat | M |

The app computes stretch exactly, so the 0.735 mm a ruler misses becomes a highlighted pair. The child drags the image of O, later several mesh points; boundary points slide only along their own side. The solve is "worst stretch at most the budget", checked exactly (on a convex sheet, the largest stretch of any triangle piece). The certificate for "best" is the map plus a tapped pair whose ends sit on opposite sides, as in route packing. Pitfalls: a live number invites dragging until it drops, so show the worst pair after each try; P1's five-pin game is flat, so don't port it as an optimization; the piece shortcut fails on non-convex shapes; "predict max(W/4, H)" is the prediction children enjoy less. Draw on P2's fan hunt, P3–P4, and P5 with fix 2's width-bound target.

**Decision, October 10, 2026.** Not ported in the October 10, 2026 round: dragging mesh points under an exact worst-stretch check is a large new mechanic, and each sheet has one answer, so the supply of puzzles is thin.

## Classroom evidence

None reported. An unpiloted prototype awaiting organizer review; material handling at print scale is unrehearsed.
