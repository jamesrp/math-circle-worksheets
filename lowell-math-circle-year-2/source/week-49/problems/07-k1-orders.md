+++
id = "w49.k1-orders"
title = "Orders of 0, 1, 2 and 4"
grades = ["K-1"]
route = "return"
kernel = "Of the 24 orders of 0, 1, 2 and 4 around the stations, eight last 7 moves and sixteen last 4: the order, not just the heights, decides the length."
+++

## prompt @0
Put 0, 1, 2, and 4 around the four stations. Find an order that lasts longer than the other orders you try.

## figure
ring(23,53,[0,1,2,4],42,9)+ring(123,53,[0,1,4,2],42,9)+moves_row(15,136,95,80)+moves_row(15,174,95,80)+moves_row(15,212,95,80)
