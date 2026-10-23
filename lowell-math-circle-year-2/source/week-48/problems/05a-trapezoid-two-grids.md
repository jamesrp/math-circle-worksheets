+++
id = "w48.trapezoid-two-grids"
title = "The trapezoid on both grids"
grades = ["2-3"]
route = "return"
kernel = "The trapezoid's bounds go from 4 and 16 on the big grid to 6 and 9 on the small grid, so its uncertain area falls from 12 to 3: splitting every square does not always halve the gap."
+++

## figure
legend()

## prompt @43
Trap this shape's area with big squares and then with small squares. Compare what happens to the area left uncertain with the triangle and the diamond.

## figure
shape(33,76,8,'trap')+two_grid_blanks(207)
