# Week 74: mathematical verification

## 74. Doubling elevators — PASS on the full stated toy graph

Vertices are `(x,h)` for integer `x` and nonnegative integer `h`; horizontal moves add or subtract `2^h`, while vertical moves change only `h`. All cost one. This is an exponential-shortcut model related to `BS(1,2)`, not its full Cayley graph. In particular, negative levels and their dyadic coordinates are absent.

If a ground-to-ground route with at most `N` moves reaches maximum height `H`, it uses at least `2H` vertical moves. Each of its at most `N−2H` horizontal moves has absolute size at most `2^H`, so its absolute net displacement is at most `(N−2H)2^H`. This uses the triangle inequality and includes left moves, extra vertical excursions and intermediate-level moves. Necessarily `0<=H<=floor(N/2)`.

For `N=7`, the bounds at `H=0,1,2,3` are 7,10,12,8. All are below 16. The eight-move route `UURRRRDD` attains 16, so eight is optimal. Another is `UUURRDDD`.

More generally, the largest rightward coordinate attainable within budget `N` is exactly the maximum of `(N−2H)2^H`: the upper bound just proved is attained by climbing to `H`, spending all remaining nonvertical moves rightward there, and descending. In the draft's budgets 4,5,6,7,8 the answers are 4,6,8,12,16.

**New draft instance x=23.** The route `UUURRRDDDL` reaches 24 at ground then steps left: ten moves. To rule out at most nine, the general bound leaves only `H=3` (all other heights allow at most 20). There can then be at most three horizontal moves. Odd final coordinate needs an odd-sized horizontal move, which only level 0 supplies; hence their displacement is at most `8+8+1=17`, a contradiction.

If left moves are forbidden, reaching 23 with maximum height `H` requires at least `floor(23/2^H)+popcount(23 mod 2^H)` horizontal moves. This is the minimum number of coins of denominations `1,2,...,2^H`: combining any two smaller equal coins never increases count, and yields the unique binary remainder. Adding `2H` gives 23,14,11,11,12 for `H=0,...,4`; higher heights cannot improve 11 because they already require at least ten vertical moves plus horizontal motion, and a size-32 right move cannot occur in a no-left trip to 23. Eleven is attained at height2 or3. Thus left moves genuinely help for this destination.

Independent unbounded BFS through depth12 visits 4,785 states and confirms the budget bounds. The printed window includes `(24,3)` and states continuation beyond the page; it is not a movement restriction.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
