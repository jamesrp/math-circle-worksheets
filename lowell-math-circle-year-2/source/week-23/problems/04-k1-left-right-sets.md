+++
id = "w23.k1-left-right-sets"
title = "Sort one set, fail the other"
grades = ["K-1"]
route = "first"
kernel = "Bars (1,2), (2,3) sort every order of 0, 0, 1 but fail 1, 1, 0; bars (2,3), (1,2) sort every order of 0, 1, 1 but fail 1, 0, 0."
+++

## prompt
Build a machine that always sorts the left set but sometimes fails on the right set. Make another that always sorts the right set but sometimes fails on the left set.

## figure
bank([0,0,1],x=2.25,y=3.6,dots=True,step=1.7)
+ bank([0,1,1],x=12.25,y=3.6,dots=True,step=1.7)
+ network(3,[],y=7.0,gap=1.8)
+ network(3,[],y=15.8,gap=1.8)
