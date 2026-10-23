+++
id = "w23.k1-build-three"
title = "Build a three-card sorter"
grades = ["K-1"]
route = "first"
kernel = "Three bars, such as (1,2), (2,3), (1,2), sort every order of three cards; no two-bar machine does."
+++

## prompt
Build a machine that sorts these three cards from every start. Use as few bars as you can.

## figure
bank([1,2,3],x=6,y=3,dots=True)
+ network(3,[],y=6.0,gap=1.8)
+ network(3,[],y=15.0,gap=1.8)
