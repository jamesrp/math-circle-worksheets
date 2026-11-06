+++
id = "w49.longest-run"
title = "A start that lasts long"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "With heights 0 to 4 (or 0 to 5) the longest runs last 7 moves; searching for long runs is the experiment behind the termination theorem."
+++

## prompt @0 [K-1]
Choose heights from 0 to 4. Find a start that lasts as many moves as you can; count the move that makes all four towers 0.

## prompt @0
Choose starting heights from 0 to 5. Find a ring that lasts as many moves as you can. Count the move that first makes all four heights 0.

## figure
big_mats()+moves_row(20,176,97,85)+moves_row(20,213,97,85)
