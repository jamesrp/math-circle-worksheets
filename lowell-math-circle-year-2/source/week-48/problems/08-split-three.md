+++
id = "w48.split-three"
title = "Spend three splits on the trapezoid"
grades = ["4-5"]
route = "return"
kernel = "A split removes at most its own cell's uncertainty, so the best three splits on the trapezoid are the cells whose children all become whole or outside."
+++

## figure
legend()

## prompt @43
Split exactly three big squares into four small squares each. Choose the three that most reduce the gap between your inside count and your cover.

## figure
shape(33,76,4,'trap')+blanks(207,True)
