+++
id = "w50.narrower-strip"
title = "A narrower strip"
grades = ["4-5"]
route = "return"
scale = "actual"
kernel = "Closeness in position does not bring the length closer: an 8 mm strip still forces 280 mm."
+++

## prompt
Fit a staircase inside this narrower gray strip. Can the new staircase be shorter than the one you drew in the wider strip? Explain your answer.

## figure
diagram(45, corridor=8)

## text @10,184 w=174
The strip reaches 8 mm vertically above and below the diagonal, clipped by the rectangle.

## figure
calibration()

## key
For the $\pm8$ mm strip, start U7.5. Then use eight R20 pieces, with U15 between consecutive horizontal pieces, and finish U7.5. This reaches (160,120) and has maximum vertical gap \textbf{7.5 mm}. Its length is still \textbf{280 mm}, so it cannot be shorter than a route in the wider strip if both obey the same right/up rule. This is a finite witness; no infinite physical construction is required.
