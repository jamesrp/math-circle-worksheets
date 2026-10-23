+++
id = "w23.45-which-machine"
title = "Which machine sorts?"
grades = ["4-5"]
route = "first"
kernel = "Bars (1,2), (3,4), (1,3), (2,4), (2,3) sort every start; swapping the last two bars fails 0100 and 1000, so the 0-1 check settles both machines."
+++

## prompt
Decide which machine sorts every start made of numbers. Give an explanation covering all inputs, including repeated values.

## figure
network(4,[(1,2),(3,4),(1,3),(2,4),(2,3)],y=4,gap=1.3)
+ network(4,[(1,2),(3,4),(1,3),(2,3),(2,4)],y=13.1,gap=1.3)
