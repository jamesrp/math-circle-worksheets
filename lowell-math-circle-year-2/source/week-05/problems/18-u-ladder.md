+++
id = "w05.u-ladder"
title = "The ladder: six puzzles"
grades = ["4-5"]
route = "first"
page = "new"
+++

## prompt
Find the city that fits the numbers around each grid, and write its heights in the grid.

## figure
close(gap(0.3) + pic(place([D.city(4, 1.7, clues=c) for c in LADDER[:4]], 2, 9.4, 9.6)))

## text
\newpage

## figure
gap(0.3) + pic(place([D.city(4, 1.7, clues=c) for c in LADDER[4:]], 2, 9.4, 0))
