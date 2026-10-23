+++
id = "w23.45-test-record"
title = "A failing start or a complete record"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "Bars (1,2), (2,3) fail 2,3,1 and 3,2,1 (and 3,3,1 among the repeats); bars (1,3), (1,2), (2,3) sort every order, so the evidence must be one counterexample or all six starts."
+++

## prompt @3.1
For each machine, decide whether it sorts every order of 1, 2, 3. Give a failing start or a complete test record. Decide whether either machine can fail with 1, 1, 3 or 1, 3, 3.

## figure
network(3,[(1,2),(2,3)],y=6.1,gap=1.3)
+ network(3,[(1,3),(1,2),(2,3)],y=13,gap=1.3)
