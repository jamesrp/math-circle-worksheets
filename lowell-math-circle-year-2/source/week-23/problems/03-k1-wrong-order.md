+++
id = "w23.k1-wrong-order"
title = "Starts that beat a machine"
grades = ["K-1"]
route = "first"
kernel = "Bars (1,2), (2,3), (1,2) sort every start; bars (1,2), (1,2), (2,3) repeat a comparison and fail 2,3,1 and 3,2,1."
+++

## prompt
Use the three cards. Find every start that makes either machine finish in the wrong order.

## figure
bank([1,2,3],x=6.0,y=3.0,dots=True)
+ network(3,[(1,2),(2,3),(1,2)],y=6.0,gap=1.8)
+ network(3,[(1,2),(1,2),(2,3)],y=15.0,gap=1.8)
