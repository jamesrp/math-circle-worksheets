+++
id = "w05.u-three-numbers-no-4"
title = "Three numbers, none a 4, one city"
grades = ["4-5"]
route = "return"
page = "new"
+++

## prompt
Make a puzzle with only three numbers around the grid, none of them a 4, that has exactly one city.

## figure
close(gap(0.2) + pic(place([D.city(4, 1.2, boxes=True) for _ in range(2)], 2, 9.0, 0)))
