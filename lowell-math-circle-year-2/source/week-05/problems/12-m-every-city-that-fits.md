+++
id = "w05.m-every-city-that-fits"
title = "Every city that fits, then one more number"
grades = ["2-3"]
route = "first"
page = "new"
+++

## prompt
More than one city fits the numbers around this grid. Find every city that fits. Then write one more number around the grid so that only one of your cities fits.

## figure
close(gap(0.2) + pic(D.city(3, INCH, clues=P23_MANY)) + gap(0.4)
      + pic(place([D.city(3, 1.4) for _ in range(6)], 3, 5.8, 5.4)))
