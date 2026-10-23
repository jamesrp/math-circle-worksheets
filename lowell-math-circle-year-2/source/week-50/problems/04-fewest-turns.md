+++
id = "w50.fewest-turns"
title = "Fewest turns inside the strip"
grades = ["K-1", "2-3", "4-5"]
route = ["first", "return"]   # first visits reach it when a pair finishes Problems 1-3
kernel = "Inside the 15 mm strip the fewest turns is 8: a horizontal piece spans at most 40 mm, and 20 mm at either end."
+++

## prompt [K-1]
Make a staircase inside the gray strip with as few turns as you can. Its pieces may follow the edge of the strip.

## prompt
Find the fewest turns possible for an S-to-F staircase inside the gray strip. Its pieces may follow the strip's boundary. Explain why fewer turns cannot work.

## figure
diagram(45, corridor=15)

## text @10,184 w=174 [2-3, 4-5]
The gray strip reaches 15 mm vertically above and below the dotted diagonal.

## figure
calibration()
