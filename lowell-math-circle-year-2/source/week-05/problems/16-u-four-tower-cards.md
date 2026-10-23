+++
id = "w05.u-four-tower-cards"
title = "Rows of four for eight cards"
grades = ["4-5"]
route = "first"
+++

## prompt
Use towers of 1, 2, 3, and 4 cubes. For each card, find a row that shows the left number from the left end and the right number from the right end, and write the heights of the row on the card. If no row can, explain why.

## figure
close(gap(0.2) + pic(place([D.row_record(4, sq=1.1, left=a, right=b, frame=True) for a, b in U_CARDS4], 2, 9.0, 2.05)), gap(3.0))
