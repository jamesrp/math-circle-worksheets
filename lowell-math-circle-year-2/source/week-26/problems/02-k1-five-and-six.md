+++
id = "w26.k1-five-and-six"
title = "Shortest and longest with 5 and 6 tiles"
grades = ["K-1"]
route = "first"
kernel = 'With 5 and 6 tiles the shortest boundary is 10, since boundary 8 fits only a 2-by-2 box, and the longest is $2n + 2$: 12 and 14.'
+++

## prompt
Make a shortest-boundary shape and a longest-boundary shape with 5 tiles. Do the same with 6 tiles.

## figure
k1_extreme_grids([5,5,6,6],11,7)

## key
\emph{Print guide, p. 5.} \textbf{Exact extrema:} 5 tiles give 10 and 12; 6 give 10 and 14; 7 give 12 and 16; 8 give 12 and 18. These are witnesses, not lists of every optimizer.

\textbf{Longest:} the connection argument on page 3 gives $2n + 2$. The rows shown meet that bound. Children can start with 4 sides on one tile and add 2 exposed sides for each new tile in a row.

\textbf{Shortest for 5 or 6:} boundary 8 or less would allow $r + c$ at most 4. The largest rectangle with that sum is 2 by 2, holding only 4 tiles. Thus at least 10 sides are needed, and the diagrams attain 10.
