# Week 32: Squares inside rectangles

**Verdict: revise.** The mathematics and the problems are right. One must: Grades 2–3 Problem 6 asks for three rectangles on a 12 × 12 grid that no valid answer fits.

Reviewed October 10, 2026 by Claude. Packets: week-32-k-1.pdf (F32-K-v2, 5 pp.), week-32-grades-2-3.pdf (F32-23-v2, 5 pp.), week-32-grades-4-5.pdf (F32-45-v2, 5 pp.). Adult guide: week-32-facilitator.pdf (5 pp.; p. 5 is the October 4 route note). Companions noticed but not reviewed: week-32-bonus.pdf ("Square recipes encore", W32-BON-v1, 3 pp.) and its guide. Status: unpiloted.

## The mathematics

Cut the largest square from one end of a whole-number rectangle and repeat on what is left. Cutting a×b to (a−b)×b keeps the same common divisors, and the sides shrink, so the last square has side gcd(a, b): the largest square whose identical copies tile the original. This is Euclid's algorithm as a dissection, and 4–5 P6 adds its extremal side: in range only 13×8, a Fibonacci rectangle, reaches five sizes. A mathematician would enjoy it. K–1 P4–P5, 2–3 P3–P6 and 4–5 P2–P6 carry it.

## Ratings

| | Rating | Evidence |
|---|---|---|
| Mathematics | strong | Invariant, termination and the equal-tile theorem are reached by drawing; 4–5 P6 is a real extremal search. |
| Problems | strong | Each has two or three boards and a real question. Every band goes from the rule to equal tilings to the connection to a construction or search. Rectangles recur on purpose: 2–3 P3 reuses P1's 10×6 and P2's 12×8. |
| Student pages | adequate | Clean: header, footer, rules once, no titles, hints or encouragement; 1 cm grids with close labels. Two grids are too small (Fix 1); 4–5 P6 asks for ties that don't exist (Fix 2). |
| Concreteness | adequate | The grid keeps edges on lines, and a wrong-sized square leaves a visible non-rectangle. Nothing enforces "largest"; pieces exist only for K–1 P5. The launch (guide p. 2) shows the 5×2 cut to everyone first. |
| Correctness | adequate | Every answer and key checks (math.md; I recomputed every sequence and the 49-cell table). Faults: Fixes 1, 2 and 5. |
| Adult guide | adequate | Precise theorem-first overview with honest limits (greedy is not minimal; sizes are not pieces). It never says why 13×8 wins. |
| Age fit, K–1 | adequate | Short read-aloud problems, counting to 12, drawing on 1 cm cells. P1–P3 ask one compare question three times. Kindergartners' drawing accuracy is a prediction. |
| Age fit, grades 2–3 | strong | Multiplication facts and subtraction suffice; P5's abstract question follows nine rectangles. |
| Age fit, grades 4–5 | strong | Factors, subtraction and casework; P4–P5 proofs suit the organizer's table; P6 can be pooled. |

## Keep

- The shared rule and the 5×2 example: input, one shaded cut, labelled remainder, on a non-task rectangle.
- K–1 P4 (equal squares on P1's 6×4) and P5 (four 3×3 squares make only 3×12 and 6×6, ending at 3 and 6).
- 2–3 P4's trap: 7×6, 8×6, 9×6 end at 1, 2, 3, but 6 by 10, P1's rectangle turned, ends at 2.
- 2–3 P5's open "How is … related …?" and P6's inverse construction.
- 4–5 P4's single cut with both divisor lists, P5's proof, P6's bounded search.
- The guide's overview and limits, its K–1 table, 49-cell table and remainder recurrence.

## Fix

1. **must**, Grades 2–3 p. 5, P6: "Make three rectangles with different first squares and the same last square of side 3," over one 12 × 12 grid. Every valid trio contains 12×9 and 9×6, the only 9-first and 6-first rectangles: 162 cells on a 144-cell grid. A child who draws them cannot finish on the page, and may call the task impossible (prediction). I disagree with math.md's 12 × 15 fix: it holds a trio only with 3×3 or 6×3 beside 9×6, not the guide's own key (12×3, 9×6, 12×9: 198 cells > 180). Fix: give P6 its own page with a 12-wide, 18-tall grid at 1 cm, which holds every valid trio stacked. The same fault, milder because cutouts carry the task, is K–1 p. 5 P5: 3×12 and 6×6 cannot share the 12 × 8 grid, and guide p. 5 offers drawing instead of cutouts. Change `p.workgrid(1,9,12,8)` to `p.workgrid(1,9,12,9)`.
2. **should**, Grades 4–5 p. 5, P6: "Find every rectangle that ties." 13×8 is the unique winner (guide p. 4), so the page presupposes a tie. Fix: "Is any other rectangle as good? Explain how you know."
3. **should**, guide pp. 1 and 4: nothing says why 13×8 wins. Add: each size is at least the sum of the next two and the last appears at least twice, so five sizes need sides of at least 8 and 13; in range only 13×8 qualifies (8×6 and 8×7 give two sizes), and six sizes need a short side of 13. Children can follow this instead of 49 cases.
4. **should**, K–1 P1–P4, materials: the outline's reusable square pieces are supplied only for P5, and each rectangle has one board, so K P4's failed 3×3 and 4×4 trials on 6×4 pile up on it. Prediction, untested. Fix: a card cut sheet per pair of 1 cm-cell squares, sides 6, 5, 4, 4, 3, 3, 2, 2, 1, 1, 1, which covers P1–P3.
5. **could**, guide p. 1: "12 cutouts for the current KK1 group" against p. 5's sixteen; or cut the four printed squares from K–1 p. 5.
6. **could**, guide p. 2: the timeline runs 0–60 with twelve minutes of sharing; context.md allows 35–40 minutes of table work.
7. **could**, guide p. 2: say what children "cover a small grid rectangle" with at the launch.
8. **could**, K–1 p. 2, P2: "Predict" has no basis yet; P3's "Will they end with the same size square?" is enough.
9. **could**, Grades 2–3 p. 4, P4: the boards already sit in order 1, 2, 3, so "sort them" does nothing; print 9×6 first.
10. **could**, Grades 4–5 p. 5, P6: swap one blank grid for a 7 × 7 record table for the pooled search.

## Overlaps

gcd also closes Weeks 4 (stars), 9 (bouncing paths), 29 (two rod lengths) and 31 (visible lattice points), each through a different object. Only Week 32 makes the subtraction invariant the thing children cut, and proves the equal-tile theorem. No merge. Week 9, where doubled rectangles also behave alike, is the nearest relative.

## App fit

Fit B, size S–M, with a changed idea. "Tap to cut squares on a grid" has the child execute a forced rule: only the outcome is in question, the predict mode children enjoyed least. The plan's fold into Spring-water Jugs covers the subtraction; jugs lack the tiling. Port the choices on the shared square grid, or as a square-piece mode in Tile Gardens:
- Design: drag a rectangle's corner until the rule's cuts hit a target (first square 9, last 3; five sizes in the smallest rectangle). The app runs the rule as the check; Fix 3's bound certifies "smallest".
- Fewest squares (bonus P1–P3): beat the rule's six squares on 6×5; fill it with only 2s and 3s while 5×5 and 7×5 fail. Use only boards whose "can't" has an area or edge-fit argument, as the bonus guide gives.

Pitfalls: long forced cut sequences; confusing sizes with pieces; showing the gcd before the child commits. Draw on 4–5 P6, 2–3 P6, K–1 P5 and bonus P1–P4.

## Classroom evidence

None reported. The source README and guide say unpiloted. The October 4 revision only added the guide's route note.
