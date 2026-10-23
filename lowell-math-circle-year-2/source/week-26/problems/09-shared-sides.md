+++
id = "w26.shared-sides"
title = "Shared sides and a rule for the boundary"
grades = ["2-3"]
route = ["first", "return"]
kernel = 'Each shared side hides two tile edges, so the boundary is $4n - 2e$: ten tiles with 9 to 13 shared sides have boundaries 22 down to 14.'
+++

## prompt
A shared side is where two tiles meet. Use ten tiles to make shapes with 9, 10, 11, 12, and 13 shared sides. Find a rule that gives the boundary length from the number of tiles and the number of shared sides.

## figure
m_shared_side_grids()

## key
\emph{Print guide, p. 10.} Each figure has ten tiles. The two-row examples have row lengths (8,2), (7,3), (6,4) and (5,5), all left-aligned. Their shared sides are, respectively, $7 + 1 + 2 = 10$; $6 + 2 + 3 = 11$; $5 + 3 + 4 = 12$; and $4 + 4 + 5 = 13$. These sums count within each row, then between rows. The row of ten has 9 meetings.

\textbf{Rule:} four times the tile count, minus twice the shared-side count. In symbols, $P = 4n - 2e$. The proof is the two hidden contributions at each meeting (page 3). This identity includes inner hole edges and allows shapes with holes.
