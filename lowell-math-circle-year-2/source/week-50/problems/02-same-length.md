+++
id = "w50.same-length"
title = "A one-step and a two-step staircase"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "Regrouping the right pieces and the up pieces shows the two lengths are equal."
+++

## prompt [K-1]
Follow both staircases with string. Compare the two pieces of string.

## prompt
Compare the lengths of these two staircases. Find their exact lengths using the width and height.

## figure
diagram(42, [(stairs(1), 'line width=1.8pt'), ([(0,0),(0,60),(80,60),(80,120),(160,120)], 'dashed,line width=1.4pt')])

## text @9,184 [K-1]
Circle: same length / solid longer / dashed longer

## text @9,184
Solid: \rule{20mm}{.3pt} mm     Dashed: \rule{20mm}{.3pt} mm

## figure
calibration()
