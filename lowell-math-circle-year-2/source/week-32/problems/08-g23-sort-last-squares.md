+++
id = "w32.g23-sort-last-squares"
title = "Last squares of 7, 8 and 9 by 6, and a prediction for 6 by 10"
grades = ["2-3"]
route = "return"
kernel = "7, 8 and 9 by 6 end with squares of side 1, 2 and 3; 6 by 10 ends with 2, breaking the pattern, because the last side is a common divisor."
+++

## prompt @0
Try the biggest-square rule on these rectangles and sort them by the side length of their last square. Predict the last square for a 6 by 10 rectangle and explain your prediction.

## figure
gridrect(.5,3.5,7,6)+gridrect(10,3.5,8,6)+gridrect(.5,12.5,9,6)+ruled(21,3)
