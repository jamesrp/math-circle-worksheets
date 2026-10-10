# Week 57: Area from dots (Pick's theorem)

**Verdict: keep.** There is no must. Every figure, key and proof step checks, and the problems carry Pick's theorem from cut-and-copy area to a full proof. The missing K–1 route is a should, as on the Week 54, 55 and 60 cards.

Reviewed October 10, 2026 by Claude, with the math check in [week-57-math.md](week-57-math.md). Packets: week-57-students.pdf (N57-S-final-v2, 10 pp.: pp. 1–6 Grades 3–5, P1–6; pp. 7–10 Grades 4–5, P7–10). Adult guide: week-57-facilitator.pdf (W57-FAC-v1, 10 pp.). Companions noticed but not reviewed: none exist. Status: unpiloted. It was written October 4 under the 52–63 routing, and guide p. 2 lists physical rehearsal as unperformed.

## The mathematics

The objects are simple lattice polygons, with I dots inside and B dots on the outline. Pick's theorem says area = I + B/2 − 1. Its engine is a seam lemma. Join two polygons along a full side with k dots: the k − 2 middle seam dots move from B to I, and the endpoints stay, so I + B/2 − 1 adds. Rectangles, triangles and ear removal finish the proof; each hole adds 1. A mathematician would enjoy it, especially P5's inverse: area 6 allows exactly six records, since B = 14 − 2I ≥ 4. P1–P3 carry area and records, P4–P5 the rule, P6–P8 the proof and P9–P10 the holes.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | A real theorem, a complete elementary proof, its inverse and the hole correction. P6 shows the seam lemma before P7 asks for it. |
| Problems | strong | Substantial throughout, with contrasting cases: rectangle and parallelogram (P1); an even-B L and an odd-B triangle (3, 5, 9/2) (P2); seams with k = 3 and 4 (P6); a triangle with no grid-line side and an inward corner (P8). Fix 2. |
| Student pages | adequate | Clean header, footer and rules, worked panels before first use, 20 mm boards. Fixes 4 and 5. |
| Concreteness | adequate | Squares, halves, cuts and copies certify area; circles and boxes hold the counts. Nothing enforces a legal outline or a count. The launch (guide p. 3) covers, marks and records one 2×2 square before the tables split. Fix 6. |
| Correctness | strong | math.md ran 284 checks with 0 failures. One overview limit is wrong (fix 3). |
| Adult guide | strong | Theorem-first p. 1 with limits; prep counts; a timed route; keys, hints and the full proof. Fixes 2 and 3. |
| Age fit, K–1 | weak | No pages. Guide p. 3 gives an oral option, then "resume an unfinished accepted Week 1 pattern-block task" (fix 1). |
| Age fit, grades 2–3 | adequate | Third graders fit P1–P3, P5 and P6 with an adult reading. Halves come in P2 (9/2) and in B/2. P4's rule is a reach the guide plans for ("Then read P5's supplied rule"). |
| Age fit, grades 4–5 | strong | The concrete start, then P5–P6 and holes. P7–P8 are gated across return visits. |

## Keep

- The p. 1 and p. 2 worked panels, on non-task shapes.
- P1's parallelogram, which returns as P6's slanted shape.
- P2's triangle: odd B and a half area before any rule.
- P3's two fixed-count shapes, which both have area 4 and set up P4.
- P5's inverse collection task. All six records fit its board.
- P6's question, "What changes when the seam disappears?"
- P8's test cases, which need proof steps 4 and 5.
- P9's ring (0, 24, 12), where the old rule gives 11.
- The guide's triangle bridge and hole proof.

## Fix

1. **should**, K–1, guide p. 3. After an oral option the table goes to Week 1. A route at their scale: join four paper squares edge to edge on a dot sheet and circle the outline dots. Every such shape has 10, except the 2×2 square, which has 8 and one inside dot. Five squares give 12, or 10 with an inside dot. I checked this by enumeration. Add it to the guide's K–1 paragraph: "Can you make a four-square shape with a different number?"
2. **should**, Grades 4–5, P7 (p. 7); guide p. 6. P5 prints Pick's rule as fact, so "each value is the area, and areas add" answers P7 in one line. P8 then proves Pick's rule from this result, which is circular. Add to guide p. 6: "Do not accept 'each value is the area'. P8 proves Pick's rule from this result, so explain it with the dots."
3. **should**, guide p. 1: "Point contacts, several shared sides, overlaps, pinches and closed seams do not satisfy this claim." A seam of consecutive sides does satisfy it; I agree with math.md item 1. The P8 pentagon (5, 12, 10) and its notch (0, 6, 2) share two sides and make the rectangle (6, 14, 12). A child may use this, and an adult may say it fails. It is a should, because P7 states one side and asking for a reason is fair. Use math.md's wording, here and in the student README.
4. **should**, Grades 3–5, P3 (p. 3). The two boards are about 17 mm apart, dot to dot, against 20 mm spacing, so they read as one 10-by-5 field. A shape drawn across the gap is off the lattice, and its area disagrees with its counts (a prediction). Stack the boards, since the lower half of the page is empty, or frame them.
5. **should**, Grades 4–5, P8 (p. 8): "Use the joining result and what you know about rectangles and triangles" is the method, and "These shapes can be test cases for your explanation" says what the pictures are for. Print: "Explain why Pick's rule works for every allowed polygon, including these two."
6. **should**, guide p. 2. 120 squares are measured and cut by hand ("about 45–75 minutes"). Add two printed pages of ruled 20 mm squares, half of them with diagonals.
7. **could**, p. 1: delete "Dots are 20 mm apart; print at 100%" and "Leave no holes until Problem 9".
8. **could**, P1, P2, P3 and P5 each repeat "pieces, cuts or copies"; say it once on p. 1.
9. **could**, P3: cut the opening question, which the next sentence answers.
10. **could**, guide p. 5: for (5, 4), give the triangle (0,0), (2,0), (1,6) before the slender parallelogram.
11. **could**, guide p. 10: cut the process residue ("Root REPUBLISHING.md was read and preserved…").

## Overlaps

Week 26 is the case of shapes built from squares. There B is the perimeter, so Pick gives P = 2n + 2 − 2I, which is Week 26's tree maximum at I = 0. Neither absorbs the other, but the guide should name the bridge. Week 31's bonus states Pick only in its guide and can point here. Weeks 48 and 14 complement this week.

## App fit

Fit B, size M, confirmed. A geoboard: the child taps dots to stretch a band, the app refuses crossings and touching, which paper cannot, and it lights outline and inside dots.

- **Solves:** two shapes with I = 2 and B = 6 (P3); every area-6 record, ending in a "That's all" claim the app checks (P5); area 6 with 4 outline dots, such as (0,0), (0,1), (1,3), (4,1); a cut that shows seam dots change colour (P6); one and two holes (P9–P10).
- **Certificates for "can't":** area 6 with I = 6 (B would be 2), or area 5 with B = 3 (I would be 4.5).
- **Pitfalls:** do not make predicting area from I and B the main puzzle. Hide one of area, I and B as the target, and check every target on the actual board by enumeration.

**Decision, October 10, 2026.** Port, in Wave 6 (grids), as a geoboard where the app refuses crossing or touching sides and lights outline and inside dots: two shapes with matching dot counts, every area-6 record with a checked "That's all", seams, and holes, with Pick-count impossibilities (area 6 with six inside dots) as the "can't" certificates. Predicting area from the dot counts is never the main puzzle. The missing K–1 route stays a should, as for Weeks 54, 55 and 60. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

None reported.
