+++
id = "w49.orders"
title = "Which order lasts longest?"
grades = ["2-3"]
route = "return"
kernel = "Of the 24 orders of 0, 1, 2 and 4 around the stations, eight last 7 moves and sixteen last 4: the order, not just the heights, decides the length."
+++

## prompt @0
Try different orders of 0, 1, 2, and 4. Which order lasts longest? Two rings count as different here only when their A, B, C, D heights differ.

## figure
ring(25,48,[0,1,2,4],42,9)+ring(123,48,[0,1,4,2],42,9)
