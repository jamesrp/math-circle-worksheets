+++
id = "w41.visit-copies"
title = "Visit another copy and come home"
grades = ["2-3"]
route = "return"
kernel = "A trip can leave the original copy and return to it, visiting a copy above and a copy to the right on the way."
+++

## prompt @27
Make a trip that visits another copy and finishes at the original H. Can you make one that visits both a copy above and a copy to the right?

## figure
tiled(18,73,60)

## key
RRRLLL visits the right copy and returns to the original H. To visit a copy above and a copy to the right, use UUUDDDRRRLLL, or RRRUUULLLDDD. The latter passes through right, upper-right, and upper copies before returning to the original. Accept any legal route with zero net small-step displacement meeting the visit condition.
