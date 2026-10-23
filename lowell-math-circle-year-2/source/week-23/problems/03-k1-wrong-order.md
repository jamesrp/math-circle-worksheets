+++
id = "w23.k1-wrong-order"
title = "Starts that beat a machine"
grades = ["K-1"]
route = "first"
# Card should 4, October 23, 2026: Problem 1's six starts are printed under each machine to circle,
# in the same order (123, 132, 213, 231, 312, 321 from left to right).
kernel = "Bars (1,2), (2,3), (1,2) sort every start; bars (1,2), (1,2), (2,3) repeat a comparison and fail 2,3,1 and 3,2,1."
+++

## prompt
For each machine, circle every start that finishes in the wrong order.

## figure
network(3,[(1,2),(2,3),(1,2)],y=3.4,gap=1.3)
+ start_grid(ORDERS3,[1.8,4.8,7.8,10.8,13.8,16.8],[8.0])
+ network(3,[(1,2),(1,2),(2,3)],y=13.6,gap=1.3)
+ start_grid(ORDERS3,[1.8,4.8,7.8,10.8,13.8,16.8],[18.2])
