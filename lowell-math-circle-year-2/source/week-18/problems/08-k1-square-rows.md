+++
id = "w18.k1-square-rows"
title = "Every square row that works with a given triangle row"
grades = ["K-1"]
route = "return"
kernel = "A square row works exactly when it differs from the triangle row in at least three of the four places: the opposite row and its four one-change neighbours, five for every triangle row."
+++

## prompt
For each triangle row, find every square row that always works. Use more paper if needed.

## figure
''.join(keyed(3.4,y,'triangle',bits)+keyed(3.4,y+2.8,'square','----')+keyed(3.4,y+5.45,'square','----') for y,bits in [(3.2,'0011'),(13.0,'0100')])
