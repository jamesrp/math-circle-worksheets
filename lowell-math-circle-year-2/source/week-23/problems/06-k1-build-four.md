+++
id = "w23.k1-build-four"
title = "Build a four-card sorter"
grades = ["K-1"]
route = "return"          # a reserve
kernel = "Five bars, (1,2), (3,4), (1,3), (2,4), (2,3), sort every order of four cards; no four-bar machine does."
+++

## prompt
Build a machine that sorts these four cards from every start. Use as few bars as you can.

## figure
bank([1,2,3,4],x=4.9,y=3,dots=True)
+ network(4,[],y=6,gap=1.45)
+ network(4,[],y=15,gap=1.45)
