+++
id = "w23.45-swap-records"
title = "Swap records"
grades = ["4-5"]
route = "return"          # the guide offers Problems 6-7 (records and minima) instead of 3-5
kernel = "A swap/no-swap record fixes the rearrangement of distinct cards, so at most one start with that record finishes sorted; bars (1,2), (2,3) make four records and bars (1,2), (2,3), (1,2) make six."
+++

## figure
record_example('Example: compare the same two lanes twice.', 'swap S', 'stay N', 'Record: SN')

## prompt @4.0
Write S when two cards swap at a bar and N when they stay put, in order from left to right. For each machine, find every record made by orders of 1, 2, 3, and find every start that makes each record.

## figure
network(3,[(1,2),(2,3)],y=7.4,gap=1.15,bar_xs=[6.5,11.7])
+ network(3,[(1,2),(2,3),(1,2)],y=14.0,gap=1.15)

## text @0,21.0
Could a fixed machine sort two different starting orders of distinct cards while making the same swap/no-swap record? Explain.
