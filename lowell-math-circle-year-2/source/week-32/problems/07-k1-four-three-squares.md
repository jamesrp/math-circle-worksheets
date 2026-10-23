+++
id = "w32.k1-four-three-squares"
title = "Rectangles from four 3 by 3 squares"
grades = ["K-1"]
route = "return"
kernel = "Four 3 by 3 squares make 3 by 12 and 6 by 6; their last squares differ (3 and 6) although both are covered by 3 by 3 squares."
+++

## prompt @0
Find every rectangle you can make with four 3 by 3 squares, counting turns as the same shape. Will their last squares match under the biggest-square rule?

## figure
four_three_squares()+workgrid(1,9,12,8)+ruled(21,2)
