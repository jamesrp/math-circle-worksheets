# Independent mathematical review: Weeks 66–75

Review date: 2026-10-06. Reviewer worked independently from `topics.json`, then inspected exact writer instances. This is a mathematical audit, not a student packet or facilitator guide. All ten kernel claims are correct with the assumptions below. Sources were checked against the actual documents; see `sources.md` for attribution limits.

Run `python3 verify_kernels.py` using only Python's standard library. It regenerates `kernel-check-results.json`. The exhaustive searches below are depth-bounded searches in the actual infinite state graphs, not searches on arbitrarily clipped boards. They have no coordinate boundary. Universal conclusions rest on the proofs here, not on finite experiments.

## 66. Lamplighter streets — PASS

A state is `(p,L)`, with integer walker position `p` and finite set `L` of lit lamps. One flip affects only the current lamp. Each target lamp must be flipped an odd number of times, so at least `|L|` flips are necessary. Other flips cannot improve a shortest solution. Every route must visit all target lamps and finish at `p`. Conversely, any such walk can flip each required lamp exactly once.

Let `l=min({0} union L)` and `r=max({0} union L)`. The exact distance from the all-off origin is

`|L| + min(-l + (r-l) + |p-r|, r + (r-l) + |p-l|)`.

A walk must encounter the two extremes in one order or the other; those two orders give the displayed lower bounds. Visiting the extremes in that order attains each bound and passes all intervening lamps. This also handles no lit lamps and targets wholly on one side of zero.

For `L={-1,0,1}`, `p=0`, three flips and four steps are both necessary and attainable: distance 7. Changing `p` to either `-1` or `1` leaves distance 6; flipping the origin lamp off also leaves distance 6. Thus this is a strict local maximum of distance **from the original state**, not an obstruction to moving toward some other goal.

Independent check: BFS verified the formula on all 4,167 states at distance at most 12.

## 67. Meeting on shortest roads — PASS

For graph vertices `a,b`, the interval `I(a,b)` consists of `p` satisfying `d(a,p)+d(p,b)=d(a,b)`. In a unit rectangular grid without deleted roads, shortest-path distance is Manhattan distance. Equality holds precisely when **each** coordinate of `p` is between the corresponding coordinates of `a,b`. For three scalar coordinates, the intersection of their three pairwise intervals is exactly their median. Taking coordinates separately proves existence and uniqueness of the common grid vertex.

The homes `(0,0),(4,1),(1,4)` therefore meet at `(1,1)`. A shortest route for a pair can be deliberately chosen through the meeting point. The point need not lie on every possible shortest route. Minimizing the sum of distances agrees here, but the definition and problem should retain all three pairwise interval conditions; on arbitrary graphs a sum minimizer need not be a common interval point.

In a tree, the unique simple paths form a tripod, possibly with a zero-length arm. Its center is the unique common point of all three pairwise paths. For a triangle graph, each pair's shortest path is its edge, and the three vertex-intervals have empty intersection. On the cube with edge/Hamming distance, each coordinate must be the majority bit: `000,110,101` have median `100`.

Independent checks cover 2,925 grid triples with repetition, all 120 cube triples with repetition, 1,540 tree triples, and the 3-cycle counterexample.

## 68. How many ways out — PASS, infinite patterns essential

An end tracks an unbounded component as finite regions are removed. An equivalent test for the finite-versus-infinite counts used here is to take the supremum of the numbers of infinite complementary components over finite vertex deletions. Vertices and their incident edges are removed, not an ambiguous shaded area.

Any finite deletion from the two-way line lies in `[-N,N]`. Outside that interval there are at most its two tails; deleting one vertex attains two infinite components. The two-way infinite ladder similarly has at most a left and a right infinite component outside a finite-width block. Deleting a complete rung separates those two tails, so it has two ends. Deleting only one ladder vertex need not disconnect it.

Any finite deletion from the square grid lies in `[-N,N]^2`. The grid outside a slightly larger box is connected: move each outside point to the surrounding square boundary while staying outside the smaller box, then travel around that boundary. Every infinite component must reach this connected exterior, so exactly one infinite component remains. Finite enclosed pockets do not count.

In a 3-regular tree, deleting the center leaves three infinite branches. Deleting the radius-`r` vertex ball leaves `3*2^r` infinite branches: there are that many outward edges from its boundary, and no two branches reconnect without making a cycle. These counts are unbounded, proving infinitely many ends. More precisely the set of individual ends is uncountable; the worksheet need only claim infinitely many, not identify it with a count of exits in a finite picture.

Independent checks verify finite-window component counts 3,6,12,24,48; a grid with an isolated center and a connected exterior; and both ladder deletions. The explicit continuation rule and argument above are what justify conclusions about infinity.

## 69. Thin and fat road triangles — PASS

A geodesic triangle includes a chosen shortest path for each pair; its vertices do not determine it when shortest routes are nonunique. In a tree, the three paths form a tripod, and every point of any side belongs to another side. Thus every tree triangle is 0-thin.

For `A=(0,0), B=(n,0), C=(n,n)`, choose the bottom and right sides for `AB,BC`, and left then top for `AC`. Their lengths are `n,n,2n`, the Manhattan distances of their endpoints, so all are geodesics. The corner `(0,n)` has distance `n` to the bottom/right union: to `(x,0)` the distance is `x+n`, and to `(n,y)` it is `n+|n-y|`. Equality is attainable. Every other side point is within `n` of the other sides, so this particular triangle's thinness is exactly `n`.

As `n` is arbitrary, no uniform finite thinness bound works for all grid triangles. This does not say every grid triangle is fat. Distances are measured along **any** roads of the full grid, including interior roads, not just around the chosen triangle boundary. The same lower bound applies if edges are treated continuously as unit segments.

Independent checks verify the exact thinness for `n=1,...,12` and 1,540 tree triangles.

## 70. Four shields in a portal room — PASS, minimum proved

Model the room as `R^2 / (4Z)^2`, with translation identification of opposite edges. Straight trajectories are continuous projected Euclidean segments, not walks on a grid. Shields are points, not discs; neither endpoint is an allowed shield.

Lift a trajectory from `S=(0,0)` to `T=(2,2)` to a segment ending at `(2+4m,2+4n)`. Its halfway point is `(1+2m,1+2n)`, one of `(1,1),(1,3),(3,1),(3,3)` modulo 4. Hence these four shields block all segments. If a long segment would hit the target earlier, apply the same midpoint argument to the segment ending at its first hit. One must not treat a midpoint after a first hit as successful interception.

For necessity, consider the four lifted displacements `(2,2),(2,-2),(-2,2),(-2,-2)`. Each first reaches the target at its endpoint. For an interior time, each coordinate is strictly in one of the two open half-circles `(0,2)` or `(2,4)` modulo 4, according to its sign. Their four sign combinations put these four trajectory interiors in disjoint open quadrants. A point shield can therefore block at most one of them; at least four are needed. The midpoint construction attains the minimum.

Independent checks cover 3,721 lift midpoints and exact open-segment intersection tests for every pair of the four indispensable trajectories, including translated lifts.

## 71. Can you hear the room — PASS, label and reflection conventions matter

Assume distinct consistent side labels, equal-angle billiard reflection, and no corner collision during an observed segment. Let `A` be the bottom side of a rectangle and `B` an adjacent vertical side. Immediately after an `A` collision the vertical velocity points upward. Reflection at `B` changes only horizontal velocity. The ray cannot next hit `A`; it must first reach the top or another side. Thus `ABA` is impossible for every positive rectangular aspect ratio.

An exact non-corner witness in a unit-side 60-degree rhombus has vertices `(0,0),(1,0),(3/2,sqrt(3)/2),(1/2,sqrt(3)/2)`. Label the bottom side `A` and the sloping side through the origin `B`. Start at `(11/16,sqrt(3)/16)` toward `(1/2,0)`. The three hits are

`A: (1/2,0), B: (1/8,sqrt(3)/8), A: (1/2,0)`.

At the first `A`, flip the vertical component. The resulting direction is perpendicular to `B`, so reflection there reverses it and returns to the same non-corner `A` point. All segments lie in the rhombus. Returning to the same hit point is permitted. If one insists on complete nonsingular bi-infinite trajectories, perturb the finite witness slightly within the open set preserving these three hits and avoid the countable exceptional vertex-hit directions.

For a rectangle, the linear stretch `(x,y)->(alpha*x,beta*y)`, with positive factors and corresponding labels, commutes with flipping either velocity component. It maps each straight segment to a straight segment and preserves the reflection law at all horizontal/vertical sides. Its inverse does the same. Consequently all such rectangles have the same full bounce language/spectrum, despite different lengths and directions. This stretch argument does not apply to arbitrary non-right-angled rooms.

A witnessed impossible-in-one-candidate word can exclude that candidate. Failed trial-and-error cannot establish impossibility. Finite words are not generally a unique room identifier.

Independent checks use exact rational rectangle ray tracing on 1,068 corner-free examples and the rhombus reflection calculation. Another 132 rays that hit a corner within the tested segment were explicitly excluded.

## 72. A robot that remembers area — PASS, matrix versus exponential height

Use the state law `(x,y,z)(a,b,c)=(x+a,y+b,z+c+x*b)`. It is ordinary multiplication of matrices with rows `(1,x,z),(0,1,y),(0,0,1)`, so it is associative. Right multiplication by the E/W/N/S generators gives exactly the printed rules. The inverse is `(-x,-y,-z+x*y)`. Central states `(0,0,z)` commute with everything.

For any axis-aligned path, the counter increment is the signed sum `sum x*delta_y`, or the line integral of `x dy`. For a closed simple lattice loop, vertical boundary pieces contribute one signed unit per enclosed unit square; interior contributions cancel. The result is signed area, positive counterclockwise and negative clockwise. More generally self-crossing or retraced loops record algebraic area with multiplicity; they do not record the unsigned area of a union of regions. Translating a closed loop by `a` horizontally adds `a*sum delta_y=0`, so its memory is unchanged.

`ENWS` leaves `(0,0,1)` while its reverse traversal `NESW` leaves `(0,0,-1)`. This extra coordinate makes motion noncommutative. The six two-E/two-N words have counters `4,3,2,2,1,0` in the order in `topics.json`.

For an **open** path from the origin to `(x,y)`, `z` is not in general its signed area relative to the straight closing chord. That area is `z−xy/2`. The Duchin–Mooney source uses this exponential/symmetric height, whereas the worksheet uses the upper-right matrix entry. For example `EENN` has worksheet memory 4 and symmetric height 2. The distinction disappears on loops. Never import the source's height formula unchanged into this worksheet.

Independent checks cover all 21,845 words of length at most 7, including 441 closed words, and 19,683 associativity triples.

## 73. The gentlest stretch — PASS under named-side constraint

Let `R=[0,4]x[0,1]` and `Q=[0,2]x[0,2]` with Euclidean distance. The permitted maps are homeomorphisms carrying each named side to the corresponding named side. Choose points `(x,0),(x,1)` on the two horizontal boundaries. They are distance 1 apart. Their images are on opposite horizontal square boundaries, so are at least distance 2 apart. Every legal map therefore has worst pairwise stretch at least 2. A non-Lipschitz map has infinite worst stretch and does not evade the bound.

The map `F(x,y)=(x/2,2y)` is a legal homeomorphism. For every displacement `(u,v)`, its squared image length is `u^2/4+4v^2 <= 4(u^2+v^2)`. Thus its worst stretch is at most 2; vertical pairs attain 2. The optimum is exactly 2.

Pin or ruler tests over finitely many pairs establish only a lower bound on a chosen map's all-pairs maximum. A general proposed map needs a whole-sheet rule before an upper bound can be proved. This is a one-sided Lipschitz optimization; do not call the number 2 a Teichmüller distance or confuse it with a logarithmic or quasiconformal normalization. Side correspondence is an essential hypothesis.

Independent checks verify the squared bound on 351 exact sampled pairs. The universal proof is the inequality and boundary argument above. The particular elementary optimization is authored here, not attributed to the 2005 talk.


### Exact fan-map extension in the Week 73 draft

The old center is `(2,1/2)` in the 4-by-1 rectangle; its new location is `O'=(u,v)` strictly inside the 2-by-2 square. Map each center-to-side triangle affinely to its corresponding triangle. The four maps agree along shared edges. Both sets of four nondegenerate triangles partition their rectangles, so the glued map is a side-preserving homeomorphism. Putting O on the boundary would invalidate this argument; the draft now explicitly excludes edges.

All ten original five-pin pairs have stretch at most2, whatever the interior location of O'. The old vertical corner pairs attain2. Each old center-to-corner distance is `sqrt(17)/2`, while any new center-to-corner distance is at most `sqrt(8)`, giving ratio less than2. Horizontal and diagonal corner pairs also give smaller ratios. Thus the initial five-pin score is exactly2 everywhere, and genuinely cannot distinguish the good map from bad ones.

Let M,N be the midpoints of the bottom and top sides. Their old distances to O are both1/2, and their images are `(1,0),(1,2)`. Passing the two additional O–M and O–N tests requires `|(u,v)−(1,0)|<=1` and `|(u,v)−(1,2)|<=1`. The two closed unit disks are tangent only at `(1,1)`, so every off-center fan fails one of these tests. Equivalently, adding the two squared inequalities yields `(u−1)^2+(v−1)^2<=0`. The centered fan is the globally optimal linear map already proved above.

For a general target rectangle of width W and height H, the same opposite-side argument gives lower bound `max(W/4,H)`; the diagonal linear map attains it. Thus the draft's 6-by-2 and2-by-3 targets have optimum2 and3. Exactly1.5 is attained when positive W,H satisfy `W<=6`, `H<=1.5`, and at least one equality holds. For instance6-by-1 and3-by-1.5 work.

## 74. Doubling elevators — PASS on the full stated toy graph

Vertices are `(x,h)` for integer `x` and nonnegative integer `h`; horizontal moves add or subtract `2^h`, while vertical moves change only `h`. All cost one. This is an exponential-shortcut model related to `BS(1,2)`, not its full Cayley graph. In particular, negative levels and their dyadic coordinates are absent.

If a ground-to-ground route with at most `N` moves reaches maximum height `H`, it uses at least `2H` vertical moves. Each of its at most `N−2H` horizontal moves has absolute size at most `2^H`, so its absolute net displacement is at most `(N−2H)2^H`. This uses the triangle inequality and includes left moves, extra vertical excursions and intermediate-level moves. Necessarily `0<=H<=floor(N/2)`.

For `N=7`, the bounds at `H=0,1,2,3` are 7,10,12,8. All are below 16. The eight-move route `UURRRRDD` attains 16, so eight is optimal. Another is `UUURRDDD`.

More generally, the largest rightward coordinate attainable within budget `N` is exactly the maximum of `(N−2H)2^H`: the upper bound just proved is attained by climbing to `H`, spending all remaining nonvertical moves rightward there, and descending. In the draft's budgets 4,5,6,7,8 the answers are 4,6,8,12,16.

**New draft instance x=23.** The route `UUURRRDDDL` reaches 24 at ground then steps left: ten moves. To rule out at most nine, the general bound leaves only `H=3` (all other heights allow at most 20). There can then be at most three horizontal moves. Odd final coordinate needs an odd-sized horizontal move, which only level 0 supplies; hence their displacement is at most `8+8+1=17`, a contradiction.

If left moves are forbidden, reaching 23 with maximum height `H` requires at least `floor(23/2^H)+popcount(23 mod 2^H)` horizontal moves. This is the minimum number of coins of denominations `1,2,...,2^H`: combining any two smaller equal coins never increases count, and yields the unique binary remainder. Adding `2H` gives 23,14,11,11,12 for `H=0,...,4`; higher heights cannot improve 11 because they already require at least ten vertical moves plus horizontal motion, and a size-32 right move cannot occur in a no-left trip to 23. Eleven is attained at height2 or3. Thus left moves genuinely help for this destination.

Independent unbounded BFS through depth12 visits 4,785 states and confirms the budget bounds. The printed window includes `(24,3)` and states continuation beyond the page; it is not a movement restriction.

## 75. Twists on a cylinder — PASS, relative endpoints essential

Write the annulus as `(R/Z)x[0,1]`. For integer `n`, `T_n(theta,t)=(theta+n*t,t)` is a homeomorphism with inverse `T_-n`. It fixes both boundary circles **pointwise**, because adding `n` at the upper boundary is zero modulo 1. Composing maps gives `T_a T_b=T_(a+b)`.

A joining arc is proper and simple: its endpoints are on the two different rims and its interior remains in the open annulus. Fix the same endpoint on each rim for both arcs. A lift starting at `(0,0)` ends at `(a,1)` for an integer winding `a`. Isotopies keep the endpoints fixed. Reversing a twist subtracts winding; freely rotating a marked rim would change this problem.

The minimum number of **interior** intersections of arcs of winding `a,b` is `max(|a−b|−1,0)`. Upper bound: straight lifts `(a*t,t)` and `(b*t,t)` intersect after projection when `(a−b)t` is integral. For `a!=b` and `0<t<1`, this happens exactly `|a−b|−1` times. When the windings agree, move one representative a small amount sideways, vanishing at the endpoints, to make their interiors disjoint.

For the lower bound, straighten one arc to winding zero by a boundary-fixing annular homeomorphism (cut along that proper simple arc to obtain a disk/rectangle, then reglue). Its lifts are the vertical barriers at all integer horizontal coordinates. The other lifted arc joins `(0,0)` to `(d,1)`, where `d=b−a`. Its horizontal coordinate must attain every integer strictly between 0 and `d`. At each such time it crosses a lift of the first arc. Its simplicity ensures the resulting projected interior intersection points are distinct. Therefore at least `|d|−1` intersections are necessary when `|d|>=2`; the other cases have lower bound zero.

This is a minimum over representatives, not the number of crossings in an arbitrary drawing. Shared endpoints are excluded; overlapped strands are not a transverse minimal-position drawing. Changing either endpoint changes the count. The strands stay on the surface: lifting yarn into three-dimensional space to pass over another strand is outside the model. A rigid paper cylinder is a strand-routing model, not a literal deforming Dehn twist.

Independent checks enumerate straight-representative crossings for winding pairs from −8 to8 and check twist composition and boundary fixing with rational angles/heights. Davis Problem 111 supplies related torus shear imagery; the annular fixed-endpoint formula is an independently proved extension, not a quoted result there.

## Exact draft-instance audit

See `draft-instance-review.md` and `verify_draft_instances.py` for problem-by-problem answers and SHA-256 fingerprints of the versions inspected. Kernel certification is complete. Final-version matching and page-layout/physical rehearsal checks remain separate responsibilities.
