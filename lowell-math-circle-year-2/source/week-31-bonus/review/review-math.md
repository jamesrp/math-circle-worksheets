# Week 31 independent mathematical review

**Pass.** The shared Grades 2–5 packet checks out completely: all seven tasks and the input → addition → plotted-point example are mathematically valid. Every rendered page and the diagram coordinates were inspected. No located mathematical correction is required.

`independent-check.py` is a standalone executable, using integer cross products to enumerate exact on-segment blockers, triangle boundary and interior dots, and legal ordered direction insertions. It writes `checks.json` without using the writer's checker or answer notes.

| Page / problem | Requested outcome independently verified |
|---|---|
| 1 / 1 | At across coordinates 0–6, row 3 has classifications **1,1,B,1,1,B,1**, and row 6 has **1,1,1,0,0,1,1**. Exact enumeration of strictly intermediate dots agrees with the translated gcd criterion. Both lookouts remain fixed. |
| 1 / 2 | No row-4 target is hidden from both lookouts, however far across it lies. Hiding from (0,0) requires across even; hiding from (1,0) requires across−1 even. These cannot both hold. The period-4 exhaustive residue check is complete for the row. |
| 2 / 3 | A and D are empty, each area 1/2. B has no extra boundary dots but interior dots (1,1),(2,1), area 5/2. C has boundary extras (1,0),(0,1),(1,1), no interior dots, and area 2. These distinctions are verified with exact signed cross products, not rounded distances. |
| 2 / 4 | Yes. Triangle B itself is a valid witness: all three sides are primitive while two dots lie inside. The task permits an example and does not falsely infer emptiness from visible sides. |
| 3 / 5 | Three different empty shapes fit on the supplied 0–3 grids, for example {(0,0),(1,0),(0,1)}, {(0,0),(1,0),(2,1)}, and {(0,0),(1,1),(2,3)}. Their unordered squared side-length lists differ, so they are noncongruent. All have area 1/2. No empty lattice triangle can have larger area: Pick's theorem with I=0 and B=3 gives 1/2. Exact enumeration on the actual grids finds 124 empty triangles among 516 nondegenerate ones, all area 1/2. This census verifies available cases; it is not a proof of Pick's theorem. |
| 4 / worked example | The ordered inputs (2,1),(1,1) have determinant 1, add to (3,2), and the drawing plots exactly 3 across and 2 up. They can be neighbors in a legally grown row. |
| 4 / 6 | Both (4,3) and (3,4) are reachable in the same row: insert (1,1), then (2,1), (1,2), (3,2), (2,3), (4,3), (3,4), each between its actual neighbors. Eight blank cards accommodate the seven insertions. (4,2) is impossible: every current neighbor pair has determinant 1; a common factor in their sum would divide 1. |
| 4 / 7 | Every allowed target is reachable. All 23 positive coprime pairs with both coordinates ≤6 have explicit verified routes. A finite complete closure under legal insertions, rejecting only sums outside the box, produces each once plus the two axis boundaries. |

For the general reachability argument, write a target between determinant-one neighbors u,v as A u+B v with positive integer coefficients. After inserting u+v, the target's angular side determines whether the coefficients become A−B,B or A,B−A. The coefficient sum decreases; primitiveness forces eventual A=B=1. Thus choosing the interval that contains the target always reaches it in finitely many legal insertions. Arbitrary addition of visible directions would not preserve primitiveness; the printed requirement to add current neighboring cards is essential and sufficient.

The lookout markers, circled target rows, four triangle corner sets, three blank grids, and addition example agree with their tasks. Working grids use x=y=2 cm; the compact example uses equal x/y scaling as well. “Dot centers” and “exactly between” correctly exclude merely nearby points and both segment endpoints. Triangles are understood as nondegenerate lattice triangles with corners at dots. Physical thread precision, pegboard fit, and classroom rehearsal remain untested.
