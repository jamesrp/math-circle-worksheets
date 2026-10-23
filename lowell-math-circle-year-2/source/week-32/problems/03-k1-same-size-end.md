+++
id = "w32.k1-same-size-end"
title = "Same last square? (9 by 6 and 10 by 6)"
grades = ["K-1"]
route = "first"
kernel = "Changing one side by one changes the last square: 9 by 6 ends with a 3 by 3, 10 by 6 with a 2 by 2."
+++

## prompt @0
Try the biggest-square rule on these rectangles. Will they end with the same size square?

## figure
gridrect(1,3,9,6)+gridrect(1,14,10,6)
