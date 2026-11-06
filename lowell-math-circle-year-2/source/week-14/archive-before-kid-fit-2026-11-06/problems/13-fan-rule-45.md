+++
id = "w14.fan-rule-45"
title = "A rule for the fewest flips to a fan"
grades = ["4-5"]
route = "return"
kernel = "The fewest flips to the fan at A is $n-3-d_A$: each flip adds at most one A diagonal, and a flip that adds one always exists in a convex polygon."
+++

## prompt
Find a rule for the fewest flips needed to turn any filling into a fan at A. Explain why your rule works for every starting filling and every number of corners, when all corners point outward.

## figure
polygon(8,4.25,4.35,4.8,3.6,labels='letters')

## key
For a convex $n$-gon, let $d_A$ be the number of \emph{interior diagonals} in the starting filling incident to A. The minimum number of flips to the A fan is
\[
\boxed{n-3-d_A}.
\]
Do not count the two boundary sides at A. For a triangle, $n-3=d_A=0$, so the formula includes the zero-move case. Lower bound. Every filling has $n-3$ diagonals. An A fan has all of them incident to A. One flip adds at most one new A diagonal, so at least $n-3-d_A$ flips are necessary. Why that bound can always be attained. Look at the union of all triangles touching A. If it is not the whole polygon, part of its boundary is an interior diagonal $uw$, with triangle $Auw$ on one side and a triangle $uwx$ on the other. Their union is a convex quadrilateral. Flip $uw$ to $Ax$. The old edge is not incident to A, and the new one is. The union of triangles at A grows, and the number of A diagonals rises by exactly one. Repeat until every diagonal meets A. There are exactly $n-3-d_A$ increases. What constitutes an explanation. ``I always add an A line'' is a useful strategy but incomplete unless the child explains why such a flip exists whenever some A lines are missing. The boundary-of-the-shaded-region argument supplies that missing step. The lower bound and construction have different jobs, and both are needed for an exact minimum. Why convexity matters. In a nonconvex polygon, the union of two triangles need not be a convex quadrilateral; its other diagonal may leave the polygon. The guide's always-available flip argument is only for the strictly convex printed polygons.

## hints
First shade every triangle touching A on one concrete drawing. Ask where the shaded region could expand by changing one line. Once the child can do it twice, ask what would have to be true for the same move to be available again.
