+++
id = "w26.fewest-starting-tiles"
title = "Fewest starting tiles for each boundary change"
grades = ["2-3"]
route = "return"
kernel = 'A change of $4 - 2k$ needs $k$ tiles around an empty cell, all connected without it, so $+2$, $0$, $-2$ and $-4$ need at least 1, 3, 5 and 7 starting tiles.'
+++

## prompt
Add one tile to a shape so that its boundary changes by each amount shown. For each amount, use as few starting tiles as possible. Explain why fewer tiles cannot work.

## figure
m_change_grids()

## key
\emph{Print guide, p. 12.} \textbf{Exact minima:} 1, 3, 5 and 7 starting tiles. The starting perimeters are 4, 8, 12 and 16; after addition they are 6, 8, 10 and 12. The last start is a 3-by-3 frame missing its center and one corner. It is side-connected and valid; eight starting tiles are not necessary.

\textbf{+2 needs one neighbor.} A starting shape is nonempty, so one is the lower bound and the singleton works.

\textbf{0 needs two neighbors.} Any two side-neighbor cells of the same empty target are not side-adjacent to one another. Two starting tiles therefore cannot form a connected shape. Three arranged as an L do work.

\textbf{$-2$ needs three neighbors.} These three neighbor cells are pairwise nonadjacent. One additional cell other than the target can touch at most two of them: only a diagonal corner can touch two, and no allowed cell touches three. Thus four starting tiles cannot connect all three target neighbors. Five tiles in the U shown do work.

\textbf{$-4$ needs four neighbors.} Color the grid like a chessboard, with the empty target black. All four required neighbors are white. With at most six starting tiles there are at most two other tiles. A black connector other than the target touches at most two of the four required neighbors. If both extra tiles are black, they are not adjacent to one another and give at most four total shared sides. Six connected tiles need at least five. If at most one extra tile is black, at most two required neighbors can meet it; no other white required neighbor has a connection. Five or fewer starting tiles fail for the same reason. Seven in the pictured almost-frame work.
