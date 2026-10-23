+++
id = "w49.three-stations"
title = "Four stations and three"
grades = ["K-1", "2-3", "4-5"]
route = "return"
kernel = "(1,0,0,0) on four stations reaches zero in 4 moves, but (1,0,0) on three stations cycles forever: the number of stations changes what can happen."
+++

## prompt @0 [K-1]
Try both starts with the same gap rule. Stop at all zeros or when the whole ring repeats.

## prompt @0
Use the gap rule on both rings. Keep going until the whole ring repeats or becomes all zeros. Does the number of stations change what can happen?

## figure
ring(30,45,[1,0,0,0],28,6)+ring(127,45,[1,0,0],28,6)+three_station_mats()
