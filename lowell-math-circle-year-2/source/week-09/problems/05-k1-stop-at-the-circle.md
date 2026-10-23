+++
id = "w09.k1-stop-at-the-circle"
title = "Draw a table that stops at the circled corner"
grades = ["K-1"]
route = "return"
page = "new"
+++

## prompt
For each little picture, draw a table starting at the dot so that the ball stops at the corner with the circle.

## figure
stack([[icon_mid(t, 3 * 0.75), blank_grid(3, 3, 0.75), blank_grid(3, 3, 0.75)]
       for t in ("tl", "br", "tr")], row_gap=0.42, gaps=[[0.6, 0.7]] * 3)
