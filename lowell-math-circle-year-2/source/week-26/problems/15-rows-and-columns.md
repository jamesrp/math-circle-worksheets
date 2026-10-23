+++
id = "w26.rows-and-columns"
title = "Rows, columns and boundary"
grades = ["4-5"]
route = ["first", "return"]
kernel = 'A shape spanning $r$ rows and $c$ columns has boundary at least $2(r + c)$, with equality exactly when every row and column is one run, so 4 rows and 5 columns force at least 18.'
+++

## prompt
Count the occupied rows, occupied columns, and boundary sides of each shape.

## figure
u_given_shapes()

## text @15,134 w=184 size=14
Make two twelve-tile shapes that each occupy 4 rows and 5 columns but have different boundary lengths. What is the least possible boundary length for a shape occupying 4 rows and 5 columns? Explain.

## figure
u_span_grids()

## key
\emph{Print guide, p. 15.} All three supplied shapes have twelve tiles. Their exact (rows, columns, boundary) triples, left to right, are \textbf{(2,6,16), (3,4,14), (4,5,18)}. The third has left-aligned row lengths 5, 3, 2, 2.

For the second construction, move the right tile from the bottom row of the first construction to the far right of the second row. Its rows become 5; 3 plus a separated tile; 2; 1. It remains connected through the full top row. Both examples use twelve tiles and exactly four rows and five columns.

Each of four occupied rows contributes at least two vertical boundary edges, for at least 8. Each of five occupied columns contributes at least two horizontal boundary edges, for at least 10. These count disjoint edge directions, so $P$ is at least 18. The first construction attains it. Its rows and columns are all contiguous, so it has exactly those mandatory boundary edges.

The second construction has an extra gap in its second row, producing two extra vertical boundary edges; its columns remain contiguous. Thus $P = 20$.
