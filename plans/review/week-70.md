# Week 70: Four shields in a portal room

**Verdict: keep.** The theorem is real and both halves are within children's reach, and every printed answer checks. No must remains. A thin first problem, a cramped map and counters that hide the tested point are should items.

Reviewed October 10, 2026 by Claude, with the math check in [week-70-math.md](week-70-math.md). Packets: week-70-students.pdf, GGT70-S-v1, 4 pages, one shared Grades 4–5 packet. Adult guide: week-70-facilitator.pdf, GGT70-FAC-v1, 3 pages. Companions noticed but not reviewed: none exist. Status: unpiloted prototype awaiting organizer review; an earlier review and revision are in plans/ggt-prototypes-66-75/week-70/.

## The mathematics

The 4×4 room with opposite edges glued by translation is a flat torus. S is the corner and T=(2,2) the centre. Shields at the halfway points (1,1), (1,3), (3,1), (3,3) stop every straight shot from S to T, because the segment to the first T copy (2+4m, 2+4n) has its midpoint at odd coordinates. Three never suffice, because the four corner-to-centre shots share no interior point. This is the Lelièvre–Monteil–Weiss blocking lemma in one room, with a construction and a reason it cannot be beaten; a mathematician would enjoy it. P1 carries the lower bound, P2 the unfolding and first-T rule, P3 the conjecture by testing, and P4 the proof.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Matching bounds. The map's shots alone force the unique four-shield answer, so testing leads to the conjecture. |
| Problems | adequate | P2–P4 are substantial and well ordered. P1's minimum of 4 is visible at a glance. |
| Student pages | adequate | Header, footer and labels are right, with no slop or hints. Page 2 has one narrating paragraph, and the maps are drawn at 7 mm per unit. |
| Concreteness | adequate | A ruler on the map enforces straightness and a partner tests shields. Shield copies exist only on paper; opaque counters cover the point. The 5-minute launch is right. |
| Correctness | strong | math.md finds no errors; I agree and confirmed the forcing shots. |
| Adult guide | adequate | Theorem-first with limits, a drawing-level proof, hints, a first route and rehearsal flags. No extension; 10 minutes for P1. |
| Age fit, K–1 | no route | Not offered ("No K–1 route is implied"). This is a recorded design choice. |
| Age fit, grades 2–3 | no route | Not offered either. Those tables need another week's material that hour. |
| Age fit, grades 4–5 | adequate | Predictions: P3 asks a child to juggle two scales, sixteen room copies and the first-T rule; P4 suits the quickest fifth grader with adult talk. Ordered pairs (p.2) are a grade-5 skill. |

## Keep

- The order of the problems: disjoint short shots, then unfolding with a first-T trap, then a test-and-move game, then the open question "Could three shields ever stop every shot?"
- P2's targets (2,6), (6,2), (6,6), (10,6): a top wrap, a side wrap, an earlier T, and a three-crossing shot.
- P3's partner as tester. The shots to (2,6), (6,2) and (6,−2) each meet the diagonals at one point, and (10,2) then forces (1,1). So the map has exactly one four-shield answer.
- The p.1 non-task example, with P=(1,2), the start (3,1) and the seam at (4,1.5). It reveals no solution shield.
- The guide's overview, limits and hint ladder.

## Fix

1. **should**, p.1 Problem 1. Four boards each hold one corner-to-centre shot. The shots meet only at T, so the minimum is settled in a minute. "Swap jobs for a new arrangement" pads the task, and the guide budgets 10 minutes. Draw the four arrows in one room, delete the swap sentence and allow 3 minutes. For a five-minute problem, also draw the folded shots to (2,6) and (6,2) in that room. The minimum stays 4, and (1,3) and (3,1) become forced.
2. **should**, p.2 Problem 2. "Each large square below is another copy of the same room. Every T is the same target. The bold square is the room shown below the map." This unnumbered paragraph narrates the diagram. Put its first two sentences in the p.1 rules and delete it.
3. **should**, pp.2–3 maps. At 0.70 cm per unit a child must draw shield crosses in every room copy a line crosses and judge exact passes; the small room is at 1.05 cm, so positions are recounted, not traced. The bottom third of each page is blank. On p.3 enlarge the map to the text width at the room's scale and drop the small room, so shields go in the bold room. On p.2, enlarge the map into the blank space.
4. **should**, the p.1 rule "A counter marks the point at its center" and the guide's materials. An opaque counter hides the line where it must be checked, as the guide itself warns. Use pencil crosses or clear centre-dot counters. Add a tracing-paper square at map scale that carries the crosses and slides from copy to copy, so the material enforces the repeat rule.
5. **should**, guide. There is no extension after P4. A verified one: shots that return to S, with no T. The halfway points (2,0), (0,2), (2,2) block all of them, and the disjoint shots (4,0), (0,4), (4,4) show that three are needed.
6. **could**, p.1: "A shot stops only if its line passes through that point" seems to contradict the first-T rule. Say "A shield stops a shot only if…".
7. **could**, p.1: in the right example, the "start" label overlaps the arrow.
8. **could**, p.2: "crosses a portal" uses a word the rules never define. Say "an X or Y edge".
9. **could**, p.2: letter the four aimed T copies for children who cannot read ordered pairs.
10. **could**, source: math.md is right that `check70()` in verify_kernels.py tests aimed midpoints, not first hits. Reduce each target by the gcd first.
11. **could**: fix 1's one-room puzzle would make a 2–3 route if the week is used for the whole circle.

## Overlaps

Week 41 (Torus portals and lifts) has the same room, portal rule and lift map, but a different theorem: winding pairs classify loops. Week 70 is a natural 4–5 return visit to that theme, and neither should absorb the other. Week 31 (Hidden orchard) gives the first-lattice-point fact behind the (6,6) case. Weeks 9 and 71 unfold billiard rooms; they share the representation but ask a different question.

## App fit

Proposed row: | 70 | Portal shields | Place point shields in a wraparound room so no straight shot from S reaches T; test on an unfolded map | Four halfway points block every shot; four corner-to-centre shots share no point, so three never suffice | No (shares Week 41's portal board) | B | Tap to place shields; the app fires an escaping shot until none is left; four disjoint shots certify "fewest" | M |

The child taps snapped crosses into a portal room beside a live unrolled view (Week 41's engine). The app plays the partner, firing an escaping shot drawn in both views up to its first T. The solve is that no shot escapes. The "fewest" certificate is the four disjoint diagonal shots. With four shields the check is finite: the diagonals plus the shots to (2,6), (6,2), (6,−2) and (10,2) refute every set except the midpoints, which the theorem certifies.

Avoid shield slots that give the count away, discs, near-miss hit tests and predict-the-path tasks.

Groups, drawn from P1–P3, with P4's three-shield question as the "can't" star:
- Easy: the fewest shields for a few drawn shots.
- Medium: all shots.
- Hard: shots back to S, which need three shields.

**Decision, October 10, 2026.** Not ported in the October 10, 2026 round: the port rests on Week 41's portal board, which the app does not have yet.

## Classroom evidence

None reported.
