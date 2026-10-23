+++
id = "w26.shortest-seven-ten-thirteen"
title = "Shortest boundary with 7, 10 and 13 tiles, two ways"
grades = ["4-5"]
route = "first"
page = "same"
kernel = 'A boundary of $2s$ holds at most $\lfloor s/2\rfloor\lceil s/2\rceil$ tiles, so 7, 10 and 13 tiles need at least 12, 14 and 16, and compact shapes reach them.'
+++

## prompt @66
Find the shortest boundary you can with 7, 10, and 13 tiles. For each number, find two different shapes reaching your best length, if you can.

## figure
u_shortest_grids()

## key
\emph{Print guide, p. 13.} \textbf{Exact minima:} 7 gives 12, 10 gives 14, 13 gives 16. Each figure has every row and every column in one interval, so $P = 2(r + c)$.

At boundary 10, the biggest possible area is $2 \times 3 = 6$, so 7 needs at least 12. At boundary 12, the biggest area is $3 \times 3 = 9$, so 10 needs at least 14. At boundary 14, the biggest area is $3 \times 4 = 12$, so 13 needs at least 16. The diagrams attain these next even lengths.
