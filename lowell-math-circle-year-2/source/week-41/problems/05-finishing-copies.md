+++
id = "w41.finishing-copies"
title = "Name the finishing copy"
grades = ["4-5"]
route = "first"
kernel = "Each R adds a third of a copy to the first coordinate and each U a third to the second; the finishing copy is the net count over three."
+++

## prompt @27
The original copy is (0,0). A full copy is three small-cell steps wide. One copy right adds 1 to the first number; one copy up adds 1 to the second. Find the finishing copy for each trip from H.

## figure
trip_list(['RRRUUU','UUURRR','RRLL','RRRUUULLLDDD'],51,93,11)+tiled(18,75,60,True)

## key
In printed order, RRRUUU and UUURRR both finish in (1,1); RRLL and RRRUUULLLDDD both finish in (0,0). Each full copy is three small-cell steps, not one. Add right-minus-left and up-minus-down steps, then divide both by three for a home-returning route.
