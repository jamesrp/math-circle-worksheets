+++
id = "w50.two-staircases"
title = "Two different staircases"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"             # shares page 1 with the staircase rule
scale = "actual"          # string and ruler work on a 160 x 120 mm board
kernel = "Every right-and-up path from S to F has length width + height = 280 mm."
+++

## prompt @73
Make two different staircases from S to F. Use string to compare their lengths.

## figure
diagram(104, diag=False)

## key
Any two different right/up routes between the printed endpoints work. For example, right 160 then up 120, and up 60, right 80, up 60, right 80. Each is 280 mm. Small differences in measured strings are measurement error, not a counterexample to the segment-total proof.
