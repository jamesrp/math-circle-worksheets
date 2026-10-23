+++
id = "w26.eight-tile-records"
title = "Shortest and longest eight-tile shapes, two of each"
grades = ["2-3"]
route = "first"
page = "same"
kernel = 'Eight tiles have shortest boundary 12 (the 2-by-4 rectangle or the 3-by-3 square missing a corner) and longest $2 \cdot 8 + 2 = 18$ (any shape with exactly 7 shared sides).'
+++

## prompt @66
Use eight tiles to make a shape with the shortest boundary you can and one with the longest boundary you can. Find a different shape reaching each of those lengths. Draw all four shapes and record their boundary lengths.

## figure
m_eight_tile_grids()

## key
\emph{Print guide, p. 8.} \textbf{Exact answer:} minimum 12, maximum 18. The 2-by-4 rectangle and 3-by-3 square missing a corner are different shapes, because their bounding boxes are different even after turning. The two long-boundary examples are also different.

For a short boundary, $P$ at most 10 forces $r + c$ at most 5, whose largest possible box is 2 by 3, holding 6 tiles. Eight tiles therefore need $P$ at least 12, and both compact figures attain it. For the maximum, connectivity requires at least 7 shared sides; $32 - 2 \times 7 = 18$. Both long examples have exactly 7 shared sides.
