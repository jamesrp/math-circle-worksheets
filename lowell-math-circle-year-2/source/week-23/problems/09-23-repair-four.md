+++
id = "w23.23-repair-four"
title = "Repair a four-lane machine"
grades = ["2-3"]
route = "first"
kernel = "The first two four-bar machines are repaired only by a last bar (2,3); the third, with (1,4) and (2,3), cannot be repaired by one bar."
+++

## prompt
For each machine, add one bar at the right end so that it sorts every starting order of 1, 2, 3, 4. If one new bar cannot do it, explain why.

## figure
network(4,[(1,2),(3,4),(1,3),(2,4)],y=4.1,gap=1.1,bar_xs=[4.4,6.5,8.6,10.7])
+ network(4,[(1,3),(2,4),(1,2),(3,4)],y=10.7,gap=1.1,bar_xs=[4.4,6.5,8.6,10.7])
+ network(4,[(1,2),(3,4),(1,4),(2,3)],y=17.3,gap=1.1,bar_xs=[4.4,6.5,8.6,10.7])
