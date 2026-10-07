# Week 70: mathematical verification

## 70. Four shields in a portal room — PASS, minimum proved

Model the room as `R^2 / (4Z)^2`, with translation identification of opposite edges. Straight trajectories are continuous projected Euclidean segments, not walks on a grid. Shields are points, not discs; neither endpoint is an allowed shield.

Lift a trajectory from `S=(0,0)` to `T=(2,2)` to a segment ending at `(2+4m,2+4n)`. Its halfway point is `(1+2m,1+2n)`, one of `(1,1),(1,3),(3,1),(3,3)` modulo 4. Hence these four shields block all segments. If a long segment would hit the target earlier, apply the same midpoint argument to the segment ending at its first hit. One must not treat a midpoint after a first hit as successful interception.

For necessity, consider the four lifted displacements `(2,2),(2,-2),(-2,2),(-2,-2)`. Each first reaches the target at its endpoint. For an interior time, each coordinate is strictly in one of the two open half-circles `(0,2)` or `(2,4)` modulo 4, according to its sign. Their four sign combinations put these four trajectory interiors in disjoint open quadrants. A point shield can therefore block at most one of them; at least four are needed. The midpoint construction attains the minimum.

Independent checks cover 3,721 lift midpoints and exact open-segment intersection tests for every pair of the four indispensable trajectories, including translated lifts.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
