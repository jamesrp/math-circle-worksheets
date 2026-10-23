+++
id = "w38.explain-cut"
title = "Explain the cut with U and L"
grades = ["K-1", "2-3", "4-5"]
route = "return"
kernel = "The seam sends the halves U and L to themselves on A (two pieces) and swaps them on B (one piece)."
+++

## prompt @27 [K-1]
Trace every edge of each cut piece. Can two dots be on the same piece but on different closed edges?

## prompt @27 [2-3]
Use the U and L marks to explain why the cuts made that many pieces. On each cut result, can two edge dots lie on the same piece but on different closed edges?

## prompt @27 [4-5]
Use U and L to explain the connected pieces after the cuts. Explain separately the number of boundary components on each piece.

## figure
strip(23,82,173,30,False,True,'A')+strip(23,137,173,30,True,True,'B')+blank(16,188,180,60)
