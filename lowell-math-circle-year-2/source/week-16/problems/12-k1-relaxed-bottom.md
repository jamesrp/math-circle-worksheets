+++
id = "w16.k1-relaxed-bottom"
title = "When the bottom side allows Y"
grades = ["K-1"]
route = "return"
page = "new"
kernel = "Once the bottom side may use Y, fillings with no triangle with R, B and Y exist."
+++

## prompt
The bottom side now allows R, B, or Y. Find four different fillings with no little triangle that has R, B, and Y.

## figure
board(3,exception='whole',counter=True)+'\n\\vspace{0.2in}\n'+record_triangles()
