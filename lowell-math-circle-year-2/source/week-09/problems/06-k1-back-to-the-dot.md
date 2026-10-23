+++
id = "w09.k1-back-to-the-dot"
title = "Back to the dot?"
grades = ["K-1"]
route = "return"
page = "new"
+++

## prompt
Can you draw a table where the ball comes back to the dot and stops there?

## figure
row([icon_item("bl")]) + row([blank_grid(4, 4, 0.75), blank_grid(4, 4, 0.75)], gap=0.8)
+ vspace(0.15) + row([blank_grid(4, 4, 0.75), blank_grid(4, 4, 0.75)], gap=0.8)
