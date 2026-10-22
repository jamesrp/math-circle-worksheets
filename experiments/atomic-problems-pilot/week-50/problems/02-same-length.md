+++
id = "w50.same-length"
title = "A one-step and a two-step staircase"
grades = ["K-1", "2-3", "4-5"]
route = "first"
scale = "actual"
kernel = "Regrouping horizontal and vertical pieces proves the two lengths equal."
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

## key
Both solid and dashed routes are \textbf{280 mm}. Solid: 160+120. Dashed: 60+80+60+80. K-1 should circle ``same length.'' The two paths need not look equally direct for their horizontal and vertical totals to agree.
