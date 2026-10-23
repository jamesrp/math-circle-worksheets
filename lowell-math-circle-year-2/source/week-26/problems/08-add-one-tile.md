+++
id = "w26.add-one-tile"
title = "Every boundary change from adding one tile"
grades = ["2-3"]
route = "first"
kernel = 'A new tile beside $k$ old tiles changes the boundary by $4 - 2k$, so the four starts allow \{+2\}, \{0, +2\}, \{$-2$, +2\} and \{$-4$, +2\}.'
+++

## prompt
Add one tile to each shape. Find every different change you can make to its boundary length.

## figure
m_add_one_tile()

## key
\emph{Print guide, p. 9.} For +2 in every start, attach a tile beyond the left end of the top row. The resulting boundaries are 14, 14, 14 and 18 in reading order. Each start allows at most two changes and the row only one, so at least one recording box per start stays blank.

An addition touching $k$ old neighbors changes $P$ by $4 - 2k$. The row has no empty position touching two of its cells. The stair has empty positions touching one or two cells, but none touching three. In the U, its central gap touches three; all other available positions touch only one (there is no two-neighbor position). In the frame, the center touches four and every exterior position touches one. This accounts for every empty side-neighbor position, so the complete change sets are \{+2\}, \{0,+2\}, \{$-2$,+2\}, \{$-4$,+2\}.

The frame has outer boundary 12 and inner boundary 4, totaling 16. Filling the hole removes its 4 inner edges, giving 12. Counting only the outside would give a wrong starting value and obscure the intended phenomenon.
