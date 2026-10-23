# Week 69: mathematical verification

## 69. Thin and fat road triangles — PASS

A geodesic triangle includes a chosen shortest path for each pair; its vertices do not determine it when shortest routes are nonunique. In a tree, the three paths form a tripod, and every point of any side belongs to another side. Thus every tree triangle is 0-thin.

For `A=(0,0), B=(n,0), C=(n,n)`, choose the bottom and right sides for `AB,BC`, and left then top for `AC`. Their lengths are `n,n,2n`, the Manhattan distances of their endpoints, so all are geodesics. The corner `(0,n)` has distance `n` to the bottom/right union: to `(x,0)` the distance is `x+n`, and to `(n,y)` it is `n+|n-y|`. Equality is attainable. Every other side point is within `n` of the other sides, so this particular triangle's thinness is exactly `n`.

As `n` is arbitrary, no uniform finite thinness bound works for all grid triangles. This does not say every grid triangle is fat. Distances are measured along **any** roads of the full grid, including interior roads, not just around the chosen triangle boundary. The same lower bound applies if edges are treated continuously as unit segments.

Independent checks verify the exact thinness for `n=1,...,12` and 1,540 tree triangles.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
