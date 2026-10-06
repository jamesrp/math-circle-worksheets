# Week 67: mathematical verification

## 67. Meeting on shortest roads — PASS

For graph vertices `a,b`, the interval `I(a,b)` consists of `p` satisfying `d(a,p)+d(p,b)=d(a,b)`. In a unit rectangular grid without deleted roads, shortest-path distance is Manhattan distance. Equality holds precisely when **each** coordinate of `p` is between the corresponding coordinates of `a,b`. For three scalar coordinates, the intersection of their three pairwise intervals is exactly their median. Taking coordinates separately proves existence and uniqueness of the common grid vertex.

The homes `(0,0),(4,1),(1,4)` therefore meet at `(1,1)`. A shortest route for a pair can be deliberately chosen through the meeting point. The point need not lie on every possible shortest route. Minimizing the sum of distances agrees here, but the definition and problem should retain all three pairwise interval conditions; on arbitrary graphs a sum minimizer need not be a common interval point.

In a tree, the unique simple paths form a tripod, possibly with a zero-length arm. Its center is the unique common point of all three pairwise paths. For a triangle graph, each pair's shortest path is its edge, and the three vertex-intervals have empty intersection. On the cube with edge/Hamming distance, each coordinate must be the majority bit: `000,110,101` have median `100`.

Independent checks cover 2,925 grid triples with repetition, all 120 cube triples with repetition, 1,540 tree triples, and the 3-cycle counterexample.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
