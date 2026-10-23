+++
id = "w50.closer-staircase"
title = "A staircase closer to the diagonal"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "Staircases can come as close to the diagonal as you like, yet every one stays 280 mm long; the diagonal is 200 mm."
+++

## prompt [K-1]
Make a staircase inside the gray strip. Compare its length with this one using string.

## prompt
Make a staircase inside the gray strip. Compare the two staircase lengths with the diagonal's length.

## figure
diagram(45, [(stairs(4), 'line width=1.1pt')], corridor=15)

## text @10,184 w=174 [K-1]
The straight diagonal is 200 mm long.

## text @10,184 w=174
The straight diagonal is 200 mm long. The strip reaches 15 mm vertically above and below it.

## figure
calibration()
