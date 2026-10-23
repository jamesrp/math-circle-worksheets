+++
id = "w18.k1-square-rows"
title = "Every square row that works with a given triangle row"
grades = ["K-1"]
route = "return"
kernel = "A square row works exactly when it differs from the triangle row in at least three of the four places."
+++

## prompt
For each key, find every square row that always works. Use both kinds of counter in each row, and use more paper if needed.

## figure
''.join(keyed(3.4,y,'triangle',bits)+keyed(3.4,y+3.15,'square','----') for y,bits in [(3.4,'0011'),(14.25,'0100')])
