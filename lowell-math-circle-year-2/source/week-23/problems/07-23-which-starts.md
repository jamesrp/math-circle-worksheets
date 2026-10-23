+++
id = "w23.23-which-starts"
title = "Which starting orders does each machine sort?"
grades = ["2-3"]
route = "first"
page = "same"
kernel = "Bars (1,2), (2,3) fail 2,3,1 and 3,2,1; bars (2,3), (1,2) fail 3,1,2 and 3,2,1; bars (1,3), (1,2), (2,3) sort all six orders."
+++

## prompt @3.1
For each machine, find every starting order of 1, 2, 3 that it sorts. Which machines sort all starting orders?

## figure
network(3,[(1,2),(2,3)],y=6,gap=1.15)
+ network(3,[(2,3),(1,2)],y=12,gap=1.15)
+ network(3,[(1,3),(1,2),(2,3)],y=18,gap=1.15)
