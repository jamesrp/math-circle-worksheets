# Week 68: mathematical verification

## 68. How many ways out — PASS, infinite patterns essential

An end tracks an unbounded component as finite regions are removed. An equivalent test for the finite-versus-infinite counts used here is to take the supremum of the numbers of infinite complementary components over finite vertex deletions. Vertices and their incident edges are removed, not an ambiguous shaded area.

Any finite deletion from the two-way line lies in `[-N,N]`. Outside that interval there are at most its two tails; deleting one vertex attains two infinite components. The two-way infinite ladder similarly has at most a left and a right infinite component outside a finite-width block. Deleting a complete rung separates those two tails, so it has two ends. Deleting only one ladder vertex need not disconnect it.

Any finite deletion from the square grid lies in `[-N,N]^2`. The grid outside a slightly larger box is connected: move each outside point to the surrounding square boundary while staying outside the smaller box, then travel around that boundary. Every infinite component must reach this connected exterior, so exactly one infinite component remains. Finite enclosed pockets do not count.

In a 3-regular tree, deleting the center leaves three infinite branches. Deleting the radius-`r` vertex ball leaves `3*2^r` infinite branches: there are that many outward edges from its boundary, and no two branches reconnect without making a cycle. These counts are unbounded, proving infinitely many ends. More precisely the set of individual ends is uncountable; the worksheet need only claim infinitely many, not identify it with a count of exits in a finite picture.

Independent checks verify finite-window component counts 3,6,12,24,48; a grid with an isolated center and a connected exterior; and both ladder deletions. The explicit continuation rule and argument above are what justify conclusions about infinity.



These universal arguments are separate from finite code checks. The packaged independent checker covers the kernel and recorded student instances; the guide checker additionally checks its own printed answers. Physical and classroom readiness remain untested.
