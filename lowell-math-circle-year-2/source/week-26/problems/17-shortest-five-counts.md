+++
id = "w26.shortest-five-counts"
title = "Shortest boundary for 12, 13, 17, 20 and 21 tiles"
grades = ["4-5"]
route = ["first", "return"]
kernel = 'The least boundaries for 12, 13, 17, 20 and 21 tiles are 14, 16, 18, 18 and 20, each certified by the greatest area for the previous even boundary.'
+++

## prompt
Find the shortest possible boundary for shapes with 12, 13, 17, 20, and 21 tiles. Explain why each of your shapes has the shortest possible boundary.

## figure
u_shortest_five_grids()

## key
\emph{Print guide, p. 16.} The exact answers are \textbf{14, 16, 18, 18, 20}. Construction row lengths are (4,4,4), (4,4,4,1), (4,4,4,4,1), (5,5,5,5), and (5,5,5,5,1). Every row/column is contiguous, so its perimeter is twice its row-plus-column span.

\textbf{Lower-bound certificates:} boundary 12 holds at most 9 tiles, excluding it for $n = 12$. Boundary 14 holds at most 12, excluding it for $n = 13$. Boundary 16 holds at most 16, excluding it for $n = 17$ and $n = 20$. Boundary 18 holds at most 20, excluding it for $n = 21$. Because boundaries are even, each construction at the next even value is optimal. Bounds for smaller perimeters are no larger, so excluding the preceding even value excludes all smaller ones.
