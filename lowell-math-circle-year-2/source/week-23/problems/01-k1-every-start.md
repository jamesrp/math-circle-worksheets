+++
id = "w23.k1-every-start"
title = "Which starts does the two-bar machine sort?"
grades = ["K-1"]
route = "first"
page = "same"
kernel = "A fixed machine can sort some starts and not others: bars (1,2) then (2,3) sort four of the six orders of three cards and fail 2,3,1 and 3,2,1."
+++

## prompt @3.7
Try every start. Circle the starts that finish in order.

## figure
network(3,[(1,2),(2,3)],y=6.0,gap=1.45,bar_xs=[6.5,11.7])
+ start_grid(ORDERS3,[3.3,9.3,15.3],[12.4,18.0])
