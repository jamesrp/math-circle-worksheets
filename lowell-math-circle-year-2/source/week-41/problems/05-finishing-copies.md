+++
id = "w41.finishing-copies"
title = "Name the finishing copy"
grades = ["4-5"]
route = "first"
kernel = "Each R adds a third of a copy to the first coordinate and each U a third to the second; the finishing copy is the net count over three."
+++

## prompt @27
Start at H in copy (0,0). Find the finishing copy for each trip.

## figure
trip_list(['RRRUUU','UUURRR','RRLL','RRRUUULLLDDD'],45,93,11)+tiled(18,75,60,True)

## key
In printed order, RRRUUU and UUURRR both finish in (1,1); RRLL and RRRUUULLLDDD both finish in (0,0). Each full copy is three small-cell steps, not one. Add right-minus-left and up-minus-down steps, then divide both by three for a home-returning route. The copy labels on the map give the coordinates.
