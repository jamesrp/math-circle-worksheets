+++
id = "w23.45-thresholds"
title = "Thresholds: numbers to 0s and 1s"
grades = ["4-5"]
route = "first"
kernel = "Replacing values by 0 (at most t) or 1 (larger than t) commutes with every bar, because min and max commute with an increasing map; a row with k different values gives k + 1 different 0-1 rows (4, 5 and 2 here)."
+++

## figure
threshold_example(r'Example: choose $t=4$. Keep each card in its position.', 'Input', '0--1 row', r'At most 4 $\to$ 0\\Larger than 4 $\to$ 1')

## prompt @4.0
Choose a number $t$. Replace a value by 0 when it is at most $t$, and by 1 when it is larger than $t$. For each start, find every different row of 0s and 1s that choosing $t$ can produce.

## figure
bank([-2,8,5,8],x=.72,y=7.0,size=1.12,step=1.42) + line(0,7.0+2.3)
+ bank([6,2,9,4],x=.72,y=11.0,size=1.12,step=1.42) + line(0,11.0+2.3)
+ bank([4,4,4,4],x=.72,y=15.0,size=1.12,step=1.42) + line(0,15.0+2.3)

## text @0,19.1
Can replacing values before a bar ever give different final 0s and 1s from replacing them after the bar? Explain for any two values and any $t$.
