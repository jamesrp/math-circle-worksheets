# Week 72: mathematical verification

## 72. A robot that remembers area — PASS, matrix versus exponential height

Use the state law `(x,y,z)(a,b,c)=(x+a,y+b,z+c+x*b)`. It is ordinary multiplication of matrices with rows `(1,x,z),(0,1,y),(0,0,1)`, so it is associative. Right multiplication by the E/W/N/S generators gives exactly the printed rules. The inverse is `(-x,-y,-z+x*y)`. Central states `(0,0,z)` commute with everything.

For any axis-aligned path, the counter increment is the signed sum `sum x*delta_y`, or the line integral of `x dy`. For a closed simple lattice loop, vertical boundary pieces contribute one signed unit per enclosed unit square; interior contributions cancel. The result is signed area, positive counterclockwise and negative clockwise. More generally self-crossing or retraced loops record algebraic area with multiplicity; they do not record the unsigned area of a union of regions. Translating a closed loop by `a` horizontally adds `a*sum delta_y=0`, so its memory is unchanged.

`ENWS` leaves `(0,0,1)` while its reverse traversal `NESW` leaves `(0,0,-1)`. This extra coordinate makes motion noncommutative. The six two-E/two-N words have counters `4,3,2,2,1,0` in the order in `topics.json`.

For an **open** path from the origin to `(x,y)`, `z` is not in general its signed area relative to the straight closing chord. That area is `z−xy/2`. The Duchin–Mooney source uses this exponential/symmetric height, whereas the worksheet uses the upper-right matrix entry. For example `EENN` has worksheet memory 4 and symmetric height 2. The distinction disappears on loops. Never import the source's height formula unchanged into this worksheet.

Independent checks cover all 21,845 words of length at most 7, including 441 closed words, and 19,683 associativity triples.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
