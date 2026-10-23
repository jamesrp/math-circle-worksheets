# Week 93: Squaring a rectangle

**Verdict: keep.** No must: every answer and diagram checks, each problem has its board, and the guide opens with the theorems. The fixes add concrete cases of the missing square and the trap, trim p. 3's method lines, settle two wordings, and repair the guide's notation and K–1 gap.

Reviewed October 23, 2026 by Claude, with math.md. Packet: week-93-students.pdf (W93-S-v2, 5 pp.: pp. 1–4 Grades 3–5, p. 5 Grades 4–5, ready for general reasoning). Adult guide: week-93-facilitator.pdf (5 pp.). Companions noticed but not reviewed: band views (Grades 2–3 slice pp. 1–4, menu) and the guide's return visits. Status: unpiloted; cutting, card fit and timing unrehearsed. Written October 17 through the worksheet workflow. No K–1 packet, by design.

## The mathematics

A rectangle a by b, a < b, becomes m = (a + b)/2 by h = ab/m, with the same area. The average-side square holds the rectangle plus one square of side (b − a)/2, so h < √A < m: each new pair traps the equal-area square's side inside the old one. The gap more than halves each move, so the trap narrows past any tolerance, yet an unequal rectangle never becomes a square, even at area 36. It is Newton's square-root method with a picture proof of the mean inequality; a mathematician would enjoy it. P2 and P6 carry the missing square, P3–P5 the trap, P7 the limit.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | An invariant area, a picture proof, nested certificates, a limit never reached. |
| Problems | adequate | P3's cases contrast well; P6–P7 are real proofs. P2's two cases share short side 2 (fix 1); the trap has no concrete case before P3 (fix 2). On pp. 1–4 children make only single moves. |
| Student pages | adequate | Headers, footers, numbering and board sizes are right; a worked visual precedes the move. P. 3 has activity talk, method and a P3 answer (fix 3); two wordings read two ways (fixes 4, 5). |
| Concreteness | adequate | Tiles and cuts enforce area and fit in P1–P2, after a tile launch. From P3 the move is paper arithmetic, checked only by the printed area. |
| Correctness | strong | The math check confirms every answer and finds three minor items. I agree with all three. |
| Adult guide | strong | Theorem-first with assumptions, limits and a band map; exact prep sizes; every solution reasoned. Notation clash (fix 6), no K–1 route (fix 7). |
| Age fit, K–1 | weak | "No K–1 packet is forced" (guide p. 1), and nothing says what that table does. |
| Age fit, grades 2–3 | adequate | P1–P2 and P3's 2 by 6 suit third graders. Prediction: 18 ÷ 9/2 and P4–P5's fractions and decimals need a calculator or adult. |
| Age fit, grades 4–5 | strong | P3–P5 work with a calculator; P6 is a drawable proof; P7's no-square half follows from P6. |

## Keep

- P. 3's worked visual: 1 by 3, then 1 + 3 halved to 2, then 2 by 3/2, area 3.
- P2's four boards at 15 mm per unit with matching letters; area forces each hole's size.
- P3's cases and number lines. In 2 by 6 and 2 by 10 a nearest pair (2 and 3; 2 and 10/3) misses the side, so "the closest numbers" fails and a child must use one rectangle's pair.
- P4's shuffled exact cards and "Show why that square's side cannot lie outside your range."
- P5's "Could either decimal be the exact side length?"
- P6–P7 on a readiness page; P7 separates approaching the square from reaching it.
- The guide's overview, the area-36 return visit, and pacing that leaves P4–P7 for later.

## Fix

1. **should**, p. 2, P2. Both rectangles have short side 2 (holes of side 2 and 1), so "half the long side minus 1" fits as well as "half the difference", yet P6 asks for the extra area in general. Add C: 5 by 1 into 3 by 3 (hole 2; 9 − 5 = 4), at 15 mm per unit in the empty lower third.
2. **should**, p. 1, P1. P3 asks for the "tightest guaranteed range for the side of a square", but no earlier task traps a square's side. Prediction, shared by the workflow's critic: adults will explain it at every table. Add to P1: "How long would the side of a square made from 24 tiles be?" The tiles answer it: 4 by 4 leaves 8, 5 by 5 needs 25.
3. **should**, p. 3. Delete "We are making the rectangle closer to a square and trying to trap the square's side length." Replace "Keep side lengths exact: 20 ÷ 6 = 10/3. Use fractions as labels; a calculator estimate can help place them. Check any proposed decimal bound by squaring it." with "Write side lengths as exact fractions." The old lines give P3's hardest new side and two methods; P5 already asks for area checks. Move the advice to the guide's hints.
4. **should**, p. 2, P2: "Can you leave exactly one square uncovered" can mean one grid square, which makes A impossible (16 − 12 = 4). Use the math check's "Can the uncovered part be a single square, of any size, in each case? Find its side length."
5. **should**, p. 1, P1: "Use 24 square tiles" allows rectangles from some tiles, such as 4 by 4, making the last question trivial. Write "Use all 24 square tiles to make each different rectangle you can."
6. **should**, guide pp. 1 and 4: d is b − a in the overview and (b − a)/2 in P6–P7, so under the first, P7's d²/m is four times too big. Rename the overview's gap g = b − a (g_new, g/2ⁿ).
7. **should**, guide p. 1. Name a K–1 route: P1 with 12 tiles and P2's cuts, adult reading, or another week's K–1 packet.
8. **could**, guide p. 2: say P2's squares have the average side, so their hole is why the move shortens the other side.
9. **could**, guide launch: rebuild 2 by 6 tiles as 3 by 4, so the first move is seen with tiles.
10. **could**, guide P4: hold "How much narrower does each range get?" (widths 4, 1, 1/14, 1/2716).
11. **could**, p. 5: drop "Diagrams not to scale"; 7 by 3 and 5 by 5 are in proportion.
12. **could**, guide p. 5: cut the production notes (workflow stages, atlas exclusions, rebuild claims).

Fixed October 23, 2026 (W93-S-v3, after the problem-file conversion): shoulds 1–7 and coulds 8–12; Problem 1's added question reads "How long would the side of a square with the area of 24 tiles be?", and fix 9's tile rebuild is a Problem 3 hint rather than part of the launch, so the launch does not show Problem 3's first answer; see `source/week-93/README.md`.

## Overlaps

Week 48 traps an area between cell counts and Week 51 carries ranges through sums; here a transformation narrows a range while keeping an area. Week 26's balanced rectangles touch P1; Week 32 cuts rectangles toward gcd. Atlas GA-28 and AP-06 do bisection and tangent Newton; comparing bisection's halving would make a return visit. No merge.

## App fit

Not in themes.md yet. I propose Fit B, size S, as a group beside Week 32's grid cuts in Tile gardens.

- **Missing square.** A grid rectangle and its average-side square. The child cuts along grid lines and drags and turns pieces into the square; the app checks containment, no overlap and one uncovered square. Vary the short side (6 by 2, 5 by 1, 7 by 3, 10 by 4) so the hole's rule shows. Harder goals name the hole's place within a piece budget; one piece never fits, so two is best for a corner hole. Verify other "fewest" claims by search.
- **Reverse move,** a short set: which 12-tile rectangle reshapes to 3 by 4? Sides with sum 8 and product 12.
- Avoid a reshape button that plays the convergence, P4's ordering and decimal squaring. P7 stays on paper. Draw on P2 and P6.

## Classroom evidence

None reported. Not yet taught.
