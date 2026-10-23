+++
id = "w26.k1-six-tile-boundaries"
title = "Six tiles with 10, 12 and 14 boundary sides"
grades = ["K-1"]
route = "return"
kernel = 'Boundary 10 with six tiles forces the full 2-by-3 rectangle, so only 12 and 14 can be made in two different ways.'
+++

## prompt
Use six tiles to make shapes with 10, 12, and 14 boundary sides. Which numbers can you make in two different ways?

## figure
k1_six_tile_grids()

## key
\emph{Print guide, p. 6.} Exactly 12 and 14 have two different answers.

With six tiles, $P = 10$ occurs only for a 2-by-3 rectangle up to turns/flips. Indeed $P = 10$ implies $r + c$ at most 5. To hold 6 cells, dimensions must be 2 and 3 and every cell of that box must be filled. Therefore the second 10-side answer space cannot contain a different shape. The 12-side examples above have different bounding boxes (4 by 2 and 3 by 3); the two 14-side examples are a row and a bent row.
