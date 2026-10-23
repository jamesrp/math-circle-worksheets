+++
id = "w05.m-four-puzzles"
title = "Four city puzzles (one has no city)"
grades = ["2-3"]
route = "first"
page = "new"
+++

## prompt
Find the city that fits the numbers around each grid, and write its heights in the grid. If no city fits, explain why.

## figure
close(gap(0.3) + pic(place([D.city(3, INCH, clues=c) for c in P23[:2]], 1, 0, 10.4)))

## text
\newpage

## figure
gap(0.3) + pic(place([D.city(3, INCH, clues=c) for c in P23[2:]], 1, 0, 10.4))
