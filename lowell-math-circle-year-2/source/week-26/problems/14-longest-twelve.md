+++
id = "w26.longest-twelve"
title = "Longest twelve-tile boundary: blocks and holes"
grades = ["4-5"]
route = "return"
kernel = 'Twelve tiles have boundary at most 26, reached exactly when there are 11 shared sides (a tree); a 2-by-2 block makes a cycle, but with tiles touching at a corner closing the gap, as the page says, a tree can enclose a hole.'
+++

## prompt
What is the longest possible boundary of a twelve-tile shape? Explain why no shape can have a longer boundary. Draw three shapes reaching that length, none of them a straight row. Can such a shape contain a 2-by-2 block? Can it have a hole? Two tiles that touch at a corner leave no gap between them.

## figure
u_longest_grids()

## key
\emph{Print guide, p. 14.} \textbf{Exact answer:} maximum 26. All three examples attain it, with twelve tiles and eleven shared sides. None is a straight row. The connection bound gives $P$ at most $48 - 22 = 26$, so no longer boundary is possible.

A 2-by-2 block: no. A hole: yes, sealed at a corner.

A 2-by-2 block creates a four-edge cycle in the tile-adjacency graph. Removing one edge from a cycle leaves its vertices connected, so any connected graph with such a cycle has at least $n$ edges rather than $n - 1$. Its perimeter is at most $2n$, below the maximum. This rules out the block.

In the third drawing, the empty center cell has a tile on each of its four sides, and the empty upper-left corner cell is outside. Where those two empty cells meet diagonally, two tiles meet at a corner and close the passage, so in the union of closed squares the center is a hole. Four of the 26 exposed edges surround it; the outer boundary contributes 22.

This corner contact adds no shared side, so the shape is still a tree: ``tree adjacency implies no holes'' is false once two tiles meeting at a corner close a gap, and the student page says they do. A child who answers no is usually thinking of a hole closed by full sides. That argument is right for such a hole: it needs a ring of side-joined tiles, a cycle, which forces at least $n$ shared sides. Point to the page's sentence about corners and ask whether the ring can be left open at one corner.
