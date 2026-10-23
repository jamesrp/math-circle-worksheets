+++
id = "w42.check-labeled"
title = "Check the rule on all sixteen labeled pairs"
grades = ["2-3"]
route = "first"
kernel = "RB and BR each fill 3 of the 16 boxes, so the mixed-pair rule is exactly fair."
+++

## prompt @0
The counters are marked R1, R2, R3, and B. Use all the equally likely labeled pairs to check your rule exactly.

## figure
labeled_pair_grid()

## key
With labeled counters R1, R2, R3, B, all 16 ordered pairs are equally likely. In the grid below, rows are first draws and columns second draws.

R1: RR, RR, RR, RB. R2: RR, RR, RR, RB. R3: RR, RR, RR, RB. B: BR, BR, BR, BB.

The three RB cells and three BR cells have equal total weight. Pair (Ri,B) with (B,Ri). There are three outcomes for either shape and ten skipped outcomes; among the six kept outcomes each shape occupies half.
