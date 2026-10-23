+++
id = "w05.u-every-city-that-fits"
title = "Every city that fits two 4s, then one more number"
grades = ["4-5"]
route = "first"
page = "new"
+++

## prompt
More than one city fits the numbers around this grid. Find every city that fits. Then write one more number around the grid so that only one of your cities fits.

## figure
close(gap(0.2) + pic(D.city(4, 1.7, clues=TWO_FOURS)) + gap(0.3)
      + pic(place([D.city(4, 1.0) for _ in range(6)], 3, 5.8, 5.0)))
