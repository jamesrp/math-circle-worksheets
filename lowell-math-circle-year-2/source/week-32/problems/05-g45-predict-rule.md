+++
id = "w32.g45-predict-rule"
title = "A rule for the last square (15 by 9 and 14 by 8)"
grades = ["4-5"]
route = "first"
kernel = "The last square's side is the greatest common divisor of the two sides: 3 for 15 by 9, 2 for 14 by 8."
+++

## prompt @0
Predict the last square in each rectangle, then test. Find a rule that predicts the last square from the two starting side lengths.

## figure
gridrect(1,3,15,9)+gridrect(1,15,14,8)
