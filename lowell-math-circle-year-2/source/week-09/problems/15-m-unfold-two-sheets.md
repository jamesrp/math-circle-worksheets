+++
id = "w09.m-unfold-two-sheets"
title = "A straight line on a sheet of tables, folded"
grades = ["2-3"]
route = "return"
page = "new"
+++

## prompt
With a ruler and a dark marker, draw a straight line from the dot to the opposite corner of each sheet. How many thick lines inside the sheet does each line cross? Then cut out the tables each line passes through, keeping them in one piece. Fold them on the thick lines until they are the size of one table with the dot in front. Hold them up to the light, and copy the path you see onto the small table beside the sheet.

## figure
vspace(0.1) + row([sheet(3, 2, 2, 3, 0.5), table(2, 3, 0.5, label=lab(2, 3))], gap=0.8)
+ vspace(0.3) + row([sheet(3, 1, 1, 3, 0.5), table(1, 3, 0.5, label=lab(1, 3))], gap=0.8)
