# Week 15: Nearest-site regions

**Verdict: keep.** No must. The maps, their order and the inverse tasks deliver real Voronoi mathematics in all three bands and the answers check; the fixes are rule wording and guide repairs.

Reviewed October 5, 2026 by Claude, blind (calibration round 3), with the math check in [week-15-math.md](week-15-math.md); classroom evidence added afterwards. Packets: week-15-k-1.pdf (F15-K-v1), week-15-grades-2-3.pdf (F15-23-v1), week-15-grades-4-5.pdf (F15-45-v1), 8 pp each. Adult guide: week-15-facilitator.pdf (15 pp). Companions noticed but not reviewed: week-15-return-visit.pdf and its adult guide (farthest-site cells, taxi-distance ties, largest-clearance placement). Status: piloted at home, not yet in the circle. The organizer tried the core maps by hand with three children and judged it good (see Classroom evidence); the guide now says piloted at home, and the student pages are unchanged.

## The mathematics

Each dot owns the closed set of places nearest to it. Two dots split the plane along their perpendicular bisector, and a cell is the intersection of half-planes, so it is convex. A third dot can erase part of a bisector, and four dots on a circle meet at one point. Adding a dot only shrinks old cells, and reflecting a dot across each edge of a convex polygon makes that polygon its cell. A mathematician would enjoy this. The order runs P1–P2 (bisector, then the erased ray), P4–P6 (four-way tie, perturbation, insertion), then P7–P8 (placement and inverse). Grades 4–5 P6 and P8 add a minimum with a lower bound and an impossibility proved by convexity.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Bisectors, convexity, insertion, inverse construction, a four-way vertex. |
| Problems | strong | Each map takes minutes of comparing and drawing. Contrasts: equal against unequal collinear gaps (K–1 P3, 2–3 P3); the square against the perturbed square (2–3 P4/P5). |
| Student pages | adequate | Headers, footers, 5.8 in equal-scale maps and short problem statements meet spec. The opening rules on p. 1 of every band are stiff and carry an adult hypothesis (fix 1). |
| Concreteness | adequate | String settles any single comparison. A fold gives a bisector. The guide launch (p. 2) demonstrates one string comparison and A/B/AB recording. Drawing a whole region is pencil work that nothing enforces. |
| Correctness | strong | [week-15-math.md](week-15-math.md) finds every student answer right; my exact spot checks (2–3 P5, P7; 4–5 P3; cross margins) agree. |
| Adult guide | strong | Theorem-first overview on p. 1, exact keys with answer diagrams, a held hint per problem, sources cited. Small repairs in fixes 2–5. |
| Age fit, K–1 | adequate | P1, P4 (crosses), P5 and P8 suit an adult reading aloud. Prediction, untested by the pilot: the oblique boundaries in P2, P6 and P7 will need adult hands. |
| Age fit, grades 2–3 | strong | Little reading and no arithmetic. Straightedge drawing. The open placement in P7 and the corner target in P8 suit third graders. |
| Age fit, grades 4–5 | strong | Proof questions come after drawing. P6–P8 give the quickest children a minimum, an exact construction and an impossibility. |

## Keep

- The crosses in K–1 P1, K–1 P4 and 2–3 P1: each non-tie cross has a gap of at least 0.67 in between nearest and next distance, so string decides; ties are exact.
- K–1 P4's cross at (0,1): A and B tie there, but C is nearer. This is the K–1 entry to the erased bisector.
- 2–3 P4 and P5 as a pair: in the square AC meet only at the centre; moving one corner gives BD a 5/8-unit edge and AC nothing.
- The insertion diamond (K–1 P6, 2–3 P6, 4–5 P5) and its four three-way vertices.
- The inverse targets with unique answers: K–1 P8 strip, 2–3 P8 corner, 4–5 P7 triangle.
- 4–5 P6 (two dots, and one cannot work) and 4–5 P8 (R can't be taken, S can). Both have two-sided answers.
- The launch, which labels one place without revealing the line, and the guide's held hints.

## Fix

1. **should**, all bands, p. 1 rules. K–1: "Keep the dots fixed and in different places. Compare straight lengths to their centers." Printed dots can't move, so a child can't act on the first sentence; the second is hard to follow heard once. Replace the K–1 rules with: "A place belongs to the dot closest to it. Measure straight to the middle of each dot. If dots tie, the place belongs to all of them. The map goes on past the frame." In 2–3 and 4–5, change the first sentence to "Put new dots in empty places."
2. **should**, guide p. 2, flexible hour: "K–1: 2 or 3", then "K 5–6" or "K 7–8". The plan never reaches K–1 P4, the only K–1 page whose crosses show a third dot erasing part of the A/B line. Change it to "K–1: 2 or 3, then 4."
3. **should**, guide p. 1 and p. 3, inverse construction. The text says "reflect that site across each supporting edge line… gives exactly the polygon." It omits the condition that no other sites are present. I agree with math check item 1: existing sites add their own half-planes. Add "(with no other sites present)" in both places.
4. **should**, guide p. 4, K–1 P2 hint: "If folding is awkward, trace the dots on translucent paper first." The dots can't be seen through the printed sheet at a table. The traced fold takes four steps, which the parent volunteer would likely do alone (prediction). Lead with the string route instead: "Mark three tie places with string, then join them with the straightedge; check with a traced fold."
5. **could**, guide p. 13, 4–5 P4. The reasoning covers only the triple A, B, D (math check, item 2). I rate it could rather than should, because the conclusion is right and the adult at that table is the organizer. Use the math check's sentence.
6. **could**, 4–5 P3. "Can a straight segment… ever leave it?" A child can close it with "it's a triangle." Ask whether any dot's region could have a dent.
7. **could**, guide p. 1, "Across the bands" says K–1 "compares lengths… simple placements." K–1 P2–P7 divide whole sheets, so add that.
8. **could**, guide p. 2. Prepare for eleven children, not ten, and allow for the five-minute run before the launch.
9. **could**, K–1 P2: cut "so every place belongs to its nearest dot", which repeats the rule.

## Overlaps

Week 21 (reflected paths) uses the same reflection that builds inverse cells here; Week 22 (Radon) shares convexity; Week 28 shares folding. None has the nearest-site object or its theorems, so no merge. The return visit stays a companion.

## App fit

Change the row from C to B, size M. The app draws exact cells, removing the paper's hardest part. With sites on a half-unit lattice the arithmetic is exact. The child drags new dots to:

- make a target cell (strip, corner, triangle, square), within a dot budget;
- touch some regions and avoid another (2–3 P7);
- take a point while keeping others (4–5 P8).

Certificates: for "can't take R", the child draws a segment PQ through R. A "fewest dots" goal pairs the witness with a "can't with fewer" claim the app verifies on the lattice.

Pitfalls:

- Live cell shading lets a child wiggle each dot until its edge lines up. Hide the cells until "check", or require several edges from a small budget.
- Don't make it a "which dot owns this place" quiz. That is predicting, which children enjoyed less.
- Show ties explicitly; pan to show unbounded regions.

Draw on K–1 P8, 2–3 P7–P8 and 4–5 P5–P8.

**Decision, October 10, 2026.** Port, in Wave 6 (grids), as a new family of nearest-site cells with sites on a half-unit lattice so every edge is exact: make a target cell within a dot budget, touch some regions and avoid another, and take a point while keeping others, with the child's segment through R as the "can't" certificate and a checked "can't with fewer" beside each fewest-dots witness. Cells stay hidden until Check, and nothing asks which dot owns a place. Tracked in the app's [decisions.md](https://github.com/jamesrp/small-math-adventure/blob/main/docs/plan/decisions.md).

## Classroom evidence

- **At home, observed.** The organizer tried Week 15 at home with three children: the organizer's two and one other child. The printer was out of paper, so the maps were drawn by hand: two dots, A and B, first, then a third dot, C, added on top to compete with them. The organizer judged it good (reported October 4–5, 2026), which agrees with the verdict.
- **What that does not test.** It covers the opening idea of every band: the dividing line between two dots, then a third dot that takes part of it (K–1 P1, P2 and P4; 2–3 and 4–5 P1–P2). It did not use the printed packets, the launch, the hour or the three tables, and it has not been tried in the circle. The children's ages, and whether string or folds were used, are not recorded. So the ratings for student pages, concreteness and age fit are still this card's predictions, and none was changed. Record what the circle shows here; it outranks them.
