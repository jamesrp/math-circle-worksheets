+++
id = "w05.u-twin-cities"
title = "Two cities with the same sixteen numbers?"
grades = ["4-5"]
route = "return"
+++

## prompt
Can two different 4-by-4 cities have exactly the same sixteen numbers around them? If they can, find two. If not, explain why.

## figure
close(gap(0.2) + pic(place([D.city(4, 1.2, boxes=True) for _ in range(2)], 2, 9.0, 0)), gap(3.0))
