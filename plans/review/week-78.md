# Week 78: Three-armed lines (tropical lines)

**Verdict: keep.** There is no must. Every answer is right, the problems lead to a real theorem and its dual, and the guide is at the bar.

Reviewed October 10, 2026 by Claude, with the math check in [week-78-math.md](week-78-math.md). A second, independent card reached the same verdict and the same should items; its one extra finding is merged into fix 2, and it rated fix 8 a should. Packet: week-78-students.pdf (F78-S-v1, 4 pp., one shared Grades 4–5 packet, Problems 1–7). Adult guide: week-78-facilitator.pdf (F78-FAC-v1, 4 pp.). Companions: none. Status: unpiloted prototype awaiting organizer review. Its stage records are in plans/frontier-prototypes-76-78/week-78/.

## The mathematics

A line is three closed rays from a junction, pointing east, north and southwest: the tie set of min(x−a, y−b, 0), a tropical line. Two lines always meet. They meet in exactly one point, unless their junctions share a row, a column or a rising diagonal; then they share a ray (P1–P3, P6). Dually, two points lie on exactly one line unless they are aligned in one of those ways; then the possible junctions fill a ray (P4, P5, P7). The proofs are pictures (the rectangle between junctions, then a half-turn). A mathematician would enjoy Euclid's first facts about lines holding with honest exceptions and no parallels. Children meet the min rule only in page 1's worked example.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Complete intersection and joining classifications for all real junctions, with ordinary set intersection throughout. |
| Problems | strong | Eight boards (P1, P2) separate crossing from overlap before P3. P4's unique lines contrast with P5's three aligned pairs before P7. P6's off-window pair tests the rule that arms continue. |
| Student pages | strong | Spec header and footer, no slop, equal-scale boards (check_diagrams.py) and a non-task worked example. There is one printed hint (fix 2). |
| Concreteness | adequate | The grid fixes the directions, a partner checks for turning, and the launch shows one legal translation. A movable shape is optional (fix 3); nothing makes the arms continue. |
| Correctness | strong | math.md finds every answer and proof correct, with one guide wording slip (fix 1). I agree. |
| Adult guide | strong | Theorem table, limits and discovery map on p. 1; launch, hour, ordered hints, full answer sets, p. 4 proofs. |
| Age fit, K–1 | none, by design | Guide p. 1: "this prototype supplies no K–1 or Grades 2–3 route" (fix 4). |
| Age fit, grades 2–3 | none, by design | As above. Prediction: P1, P2 and P4 ask only for drawing from labelled dots. |
| Age fit, grades 4–5 | strong | (x, y) appears only on p. 1 and in P6. Proofs come last, with the organizer. Prediction: fourth graders may need (x, y) explained at the launch. |

## Keep

- p. 1: the non-example with a larger tie (4, 4, 2), and the rules "moved without turning", "continue without end" and "Points between grid dots count too."
- P1: B chosen by the child on A = (4,4), and the fixed unequal rectangles (2,2)/(6,5) and (2,2)/(5,6).
- P2: one point, then north, east and southwest shared rays. In (2,2)/(6,6) the segment between the junctions is not shared. Keep "How many shared points does each pair have?"
- P3 straight after P2, worded openly. P4's "Can you find a second line" before P5. P6's (2,7)/(10,5), which meet at (10,7), off the board. P7 last.
- Guide: the p. 1 table, the launch ("Do not announce the intersection theorem"), the P1 menu, the p. 4 proofs.

## Fix

1. **should**, guide p. 3, Problem 3: the model child explanation says "If the junctions are on the same row, column or diagonal, the matching arms keep sharing forever." Junctions on a falling diagonal, such as (2,6) and (6,2), meet only at (6,6) (math.md finding 1). Not a must: the p. 1 table and the P6 and P7 answers say "rising", and "diagonal" here names only the arms' direction. Write "same row, column or rising diagonal".
2. **should**, p. 3, Problem 5: "Mark a whole stretch if every point on it works." That aligned targets allow a whole stretch of junctions is P5's discovery and half of P7's rule; this prints it. Cut it, and put "a stretch can be an answer" in the guide's P5 hints. Page 1's P1 does the same for lines: "Circle single shared points and trace shared stretches heavily" announces shared stretches before P2 finds them. Print "Mark everything each pair shares." (second card).
3. **should**, guide p. 1: "Optional: two tracing sheets per pair". Without a shape the child can slide, each trial junction in P4–P5 means drawing three new rays. P4's hint 1, "Can one unchanged shape touch both targets?", assumes such a shape. Make one traced three-arm shape per pair standard and use it in the launch; it fits every board. Prediction; nothing is rehearsed.
4. **should**, scope: the whole-group launch shows eight children an action they will not use. The prototypes admit a younger entry "only where children retain meaningful mathematical choices", and research.md's "Meaningful younger entry" gives one: slide the shape over one target, then two, and compare "one place for the junction" with "lots of places". Build it on enlarged P4–P5 boards. That K–1 keeps the orientation is a prediction. A should, as on Weeks 60 and 62, because the scope is recorded.
5. **could**, P2 and P4: no pair lies on a falling diagonal, so a "same diagonal" rule is never tested. Change (2,5)/(6,2) to (2,6)/(6,2) in both. P2 then meets only at (6,6), and P4's junction stays (2,2) (checked).
6. **could**, p. 2, Problem 3 has no grid while P7 has one. Add a blank 0–8 board.
7. **could**, p. 4, Problem 6 asks for a meeting point, an impossibility and a classification in five sentences. Give the rule its own number.
8. **could**, p. 1: no problem uses the min rule. Late, ask which line "compare x, y + 1 and 3" makes: junction (3, 2), checked, with no negative numbers.
9. **could**, Q off the line is an open circle on p. 1, but open circles are targets on p. 3. Mark Q with a cross.

## Overlaps

Week 15's boundaries are also ties of a minimum, with three-armed junctions, but its theorems are convexity and insertion, not incidence. Week 67's meeting of three homes is a different tripod. No merge.

## App fit

The table has no row. Fit B, size M. Proposed row: | 78 | Three-armed lines (tropical lines) | Draw translated three-arm lines; mark what two share; find the line through two points | Two lines always meet, in one point or a ray when junctions share a row, column or rising diagonal; two points fix one line unless so aligned | No | B | Drag junctions on a pannable grid; make two lines meet a given way; one line through given targets, with allowed-junction fans as the "can't" certificate | M |

The child drags junctions; the app draws arms past the window, rings a shared point and thickens a shared ray. It enforces what paper cannot: no turning, endless arms.

- **Through the targets.** Place one junction so the line passes through every target. Two unaligned targets fix it (P4). For aligned targets the child marks the ray of junctions and declares done, with no count shown (P5). Three targets can make it impossible: (2,2), (7,5), (6,6), because the first two force (5,5) (research.md, checked). The certificate is each target's fan of allowed junctions (west, south, northeast): the first two fans meet only at (5,5), and the third misses it.
- **Meet like this.** Given A, place B so the lines share exactly a marked point, or a ray from a marked start (P1).

Pitfalls: no "how will these meet?" prediction rounds, which children enjoy least, and no rotate handle. On Hard, snap to half-steps so that points between grid dots count. Draw on P1, P2, P4, P5 and P6's pair, and leave P3, P6's rule and P7 on paper.

**Decision, October 10, 2026.** Not ported in the October 10, 2026 round: with live feedback, placing one junction becomes sliding until the stars light, and the theorems live in noticing and explaining. The three-star "can't" claim is the solve to build if it is revisited.

## Classroom evidence

None reported. Guide p. 1: "Physical rehearsal and classroom piloting have not been performed."
