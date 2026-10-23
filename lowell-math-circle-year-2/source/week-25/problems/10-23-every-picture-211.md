+++
id = "w25.23-every-picture-211"
title = "Every picture with row and column counts 2, 1, 1"
grades = ["2-3"]
route = "first"
kernel = "Row A chooses two of three columns, and each choice leaves 1, 2 or 2 ways below: 1 + 2 + 2 = 5 pictures."
+++

## prompt @27
Find and draw every different picture with these counts. How can you be sure your list is complete?

## figure
m_211_grids()

## key
\emph{Print guide, p. 9.} \textbf{Answer:} exactly five. Six recording grids are available; the unused grid is intentional space, not evidence of a sixth solution.

Row A occupies exactly two of three columns, so it has exactly three possible patterns. If A uses columns 2 and 3, the remaining column counts are 2, 0, 0; both B and C must use column 1. This gives one picture.

If A uses 1 and 3, the remaining counts are 1, 1, 0. B and C each need one counter, so they use columns 1 and 2 in either order. This gives two pictures. If A uses 1 and 2, the remaining counts are 1, 0, 1, giving two more in the same way. These cases are disjoint and exhaust row A, so there are 1 + 2 + 2 = 5.
