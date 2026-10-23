+++
id = "w09.u-unfold-2-by-3"
title = "Unfold the 2 by 3 table"
grades = ["4-5"]
route = "first"
page = "new"
+++

## prompt
With a ruler and a dark marker, draw a straight line on the big sheet from the dot, crossing each square from corner to corner. Stop when the line first reaches another point where two thick lines cross. How many thick lines did it cross before it reached that point? Then cut out the tables the line passes through, keeping them in one piece. Fold them on the thick lines until they are the size of the 2 by 3 table with the dot in front. Hold them up to the light, and copy the path you see onto the small 2 by 3 table.

## figure
vspace(0.15) + row([sheet(4, 3, 2, 3, 0.5), table(2, 3, 0.5, label=lab(2, 3))], gap=1.0)
