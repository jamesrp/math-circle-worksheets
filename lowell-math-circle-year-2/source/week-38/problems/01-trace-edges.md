+++
id = "w38.trace-edges"
title = "Trace every edge of A and B"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "A strip joined matching (A) has two boundary circles; joined with a half-turn (B) it has one."
+++

## prompt @124 [K-1]
Trace every edge of A and B. Give each separate closed edge its own color.

## prompt @124 [2-3]
Trace all the edges of A and B. How many separate closed edges does each band have?

## prompt @124 [4-5]
Trace all the edges of A and B. Show on each flat recipe where each separate closed edge goes through the seam.

## figure
strip(26,162,163,30,False,name='A')+strip(26,210,163,30,True,name='B')+lab(103,253,'A: ____________       B: ____________',12)
