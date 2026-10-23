+++
id = "w26.most-tiles"
title = "Most tiles inside a given boundary"
grades = ["4-5"]
route = ["first", "return"]
kernel = 'Boundary $2s$ allows $r + c \le s$ and so at most $\lfloor s/2\rfloor\lceil s/2\rceil$ tiles: 9, 12, 16 and 20 for boundaries 12, 14, 16 and 18.'
+++

## prompt
For each boundary length shown, find the greatest number of tiles a shape can have. Explain why no shape with that boundary length can contain more tiles.

## figure
u_most_tiles_grids()

## key
\emph{Print guide, p. 16.} The exact answers are \textbf{9, 12, 16, 20}. For boundary 12, 14, 16 or 18, the sum $r + c$ cannot exceed 6, 7, 8 or 9. For each sum, the balanced dimension pair gives the largest product (page 3). A smaller sum cannot give more area: increasing one positive dimension increases its product. The displayed rectangles reach the bounds with exactly the requested boundary.
