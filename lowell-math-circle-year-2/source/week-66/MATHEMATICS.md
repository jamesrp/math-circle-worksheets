# Week 66: mathematical verification

## 66. Lamplighter streets — PASS

A state is `(p,L)`, with integer walker position `p` and finite set `L` of lit lamps. One flip affects only the current lamp. Each target lamp must be flipped an odd number of times, so at least `|L|` flips are necessary. Other flips cannot improve a shortest solution. Every route must visit all target lamps and finish at `p`. Conversely, any such walk can flip each required lamp exactly once.

Let `l=min({0} union L)` and `r=max({0} union L)`. The exact distance from the all-off origin is

`|L| + min(-l + (r-l) + |p-r|, r + (r-l) + |p-l|)`.

A walk must encounter the two extremes in one order or the other; those two orders give the displayed lower bounds. Visiting the extremes in that order attains each bound and passes all intervening lamps. This also handles no lit lamps and targets wholly on one side of zero.

For `L={-1,0,1}`, `p=0`, three flips and four steps are both necessary and attainable: distance 7. Changing `p` to either `-1` or `1` leaves distance 6; flipping the origin lamp off also leaves distance 6. Thus this is a strict local maximum of distance **from the original state**, not an obstruction to moving toward some other goal.

Independent check: BFS verified the formula on all 4,167 states at distance at most 12.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
