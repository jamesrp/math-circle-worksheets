+++
id = "w41.replay-copies"
title = "Replay trips on the repeated map"
grades = ["2-3"]
route = "return"
kernel = "Replaying on the repeated map shows which copy a trip finishes in: RRLL returns to the original copy, RRRUUU does not."
+++

## prompt @27
Replay each trip on these copies, starting at the original H. Mark the copy where each trip finishes.

## figure
trip_list(['RRR','UUU','RRRUUU','RRLL'],49,90,12)+tiled(18,75,60)

## key
The starting H is in the original copy. RRR: one copy right, (1,0). UUU: one copy up, (0,1). RRRUUU: one copy right and up, (1,1). RRLL: original copy, (0,0).

Each route finishes at H on the portal map. The first three do not finish in the original copy. For RRLL, the route crosses into the right copy and comes back; count the signed displacement, not just whether another copy was visited.
