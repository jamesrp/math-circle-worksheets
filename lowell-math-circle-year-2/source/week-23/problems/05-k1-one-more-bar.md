+++
id = "w23.k1-one-more-bar"
title = "One more bar"
grades = ["K-1"]
route = "return"          # the guide calls Problems 5-6 reserves
kernel = "Each two-bar machine becomes a sorter with exactly the right last bar: (1,2), (2,3) and (2,3) respectively."
+++

## prompt
Each machine needs one more bar at the right. Add it so that every start of the three cards finishes in order.

## figure
bank([1,2,3],x=6,y=3.25,dots=True)
+ network(3,[(1,2),(2,3)],y=6,gap=1.2,bar_xs=[5.0,9.0])
+ network(3,[(2,3),(1,2)],y=12,gap=1.2,bar_xs=[5.0,9.0])
+ network(3,[(1,3),(1,2)],y=18,gap=1.2,bar_xs=[5.0,9.0])
