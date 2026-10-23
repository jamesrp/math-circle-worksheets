+++
id = "w42.check-labeled-45"
title = "Check the rule on the labeled pairs"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "RB and BR each come from 3 of the 16 labeled pairs."
+++

## prompt @13
Check your rule using every equally likely pair of the labeled counters R1, R2, R3, B. Do the shape chances match? Explain.

## figure
labeled_grid_lines()

## key
The four color classes have labeled sizes 9, 3, 3, 1. Reversal pairs each (Ri,B) with (B,Ri), giving equal shape probabilities 3/16 and conditional probabilities 1/2. Other rules fail Problem 2’s check: RR $\to$ square, the rest $\to$ circle gives 9 against 7.
