+++
id = "w26.k1-seven-and-eight"
title = "Shortest and longest with 7 and 8 tiles"
grades = ["K-1"]
route = "first"
kernel = 'With 7 and 8 tiles the shortest boundary is 12, since boundary 10 fits only a 2-by-3 box, and the longest is $2n + 2$: 16 and 18.'
+++

## prompt
Make a shortest-boundary shape and a longest-boundary shape with 7 tiles. Do the same with 8 tiles.

## figure
k1_extreme_grids([7,7,8,8],10,8)

## key
\emph{Print guide, p. 5.} \textbf{Exact extrema:} 5 tiles give 10 and 12; 6 give 10 and 14; 7 give 12 and 16; 8 give 12 and 18. These are witnesses, not lists of every optimizer. In particular, the seven-tile minimum is a 2-by-4 rectangle with one corner missing.

\textbf{Longest:} the connection argument on page 3 gives $2n + 2$. The rows shown meet that bound.

\textbf{Shortest for 7 or 8:} boundary 10 or less would allow $r + c$ at most 5. The best such box is 2 by 3, holding only 6 tiles. At least 12 sides are needed, and the diagrams attain 12. Odd boundary lengths are excluded by paired shared-edge cancellations.
