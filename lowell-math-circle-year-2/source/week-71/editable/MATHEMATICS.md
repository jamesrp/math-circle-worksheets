# Week 71: mathematical verification

## 71. Can you hear the room — PASS, label and reflection conventions matter

Assume distinct consistent side labels, equal-angle billiard reflection, and no corner collision during an observed segment. Let `A` be the bottom side of a rectangle and `B` an adjacent vertical side. Immediately after an `A` collision the vertical velocity points upward. Reflection at `B` changes only horizontal velocity. The ray cannot next hit `A`; it must first reach the top or another side. Thus `ABA` is impossible for every positive rectangular aspect ratio.

An exact non-corner witness in a unit-side 60-degree rhombus has vertices `(0,0),(1,0),(3/2,sqrt(3)/2),(1/2,sqrt(3)/2)`. Label the bottom side `A` and the sloping side through the origin `B`. Start at `(11/16,sqrt(3)/16)` toward `(1/2,0)`. The three hits are

`A: (1/2,0), B: (1/8,sqrt(3)/8), A: (1/2,0)`.

At the first `A`, flip the vertical component. The resulting direction is perpendicular to `B`, so reflection there reverses it and returns to the same non-corner `A` point. All segments lie in the rhombus. Returning to the same hit point is permitted. If one insists on complete nonsingular bi-infinite trajectories, perturb the finite witness slightly within the open set preserving these three hits and avoid the countable exceptional vertex-hit directions.

For a rectangle, the linear stretch `(x,y)->(alpha*x,beta*y)`, with positive factors and corresponding labels, commutes with flipping either velocity component. It maps each straight segment to a straight segment and preserves the reflection law at all horizontal/vertical sides. Its inverse does the same. Consequently all such rectangles have the same full bounce language/spectrum, despite different lengths and directions. This stretch argument does not apply to arbitrary non-right-angled rooms.

A witnessed impossible-in-one-candidate word can exclude that candidate. Failed trial-and-error cannot establish impossibility. Finite words are not generally a unique room identifier.

Independent checks use exact rational rectangle ray tracing on 1,068 corner-free examples and the rhombus reflection calculation. Another 132 rays that hit a corner within the tested segment were explicitly excluded.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
