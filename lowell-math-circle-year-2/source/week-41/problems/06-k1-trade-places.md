+++
id = "w41.k1-trade-places"
title = "Can two pawns trade places?"
grades = ["K-1"]
route = "return"
kernel = "Two pawns given the same steps keep the same offset, so pawns on H and E can never trade places."
+++

## prompt @27
Put one pawn on H and one on E. Give both pawns the same arrow steps; can you make them trade places?

## figure
tile(18,71,180,True,True,True,15)

## key
No. Every shared arrow sequence translates both pawns equally. The pawn initially at E remains one cell to the right of the pawn initially at H, including across portals. If H moved to E, that translation is one cell right, so E would move to D, not H.
