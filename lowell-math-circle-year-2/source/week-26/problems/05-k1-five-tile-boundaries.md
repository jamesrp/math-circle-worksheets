+++
id = "w26.k1-five-tile-boundaries"
title = "Which boundaries five tiles can make"
grades = ["K-1"]
route = "return"
kernel = 'Every boundary is even, because each shared side hides two edges, and boundary 8 holds at most four tiles, so five tiles make only 10 and 12.'
+++

## prompt
Which of these boundary lengths can you make with five tiles? Make each one you can, and tell your adult why the others will not work.

## figure
k1_five_tile_grids()

## key
\emph{Print guide, p. 6.} Among 8, 9, 10, 11, 12, 13, only 10 and 12 work.

Boundary 8 would force a box holding at most 4 tiles (page 5), so it is too short. Odd lengths 9, 11 and 13 are impossible because starting from 4 sides per tile, every shared side removes two. Thus every boundary is even. The two drawings attain the remaining candidates. Equivalently, every occupied row contributes an even number of vertical boundary edges and every occupied column an even number of horizontal edges.
