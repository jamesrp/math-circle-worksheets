+++
id = "w05.m-how-many-cities"
title = "How many 3-by-3 cities?"
grades = ["2-3"]
route = "return"
page = "new"
+++

## prompt
How many different 3-by-3 cities are there? Cities that are turned or flipped count as different. Write each city you find in a grid. Explain how you know you have found them all.

## figure
close(gap(0.3) + pic(place([D.city(3, 1.0) for _ in range(15)], 5, 3.65, 3.75)))
