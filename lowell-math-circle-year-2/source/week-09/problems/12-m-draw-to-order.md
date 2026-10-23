+++
id = "w09.m-draw-to-order"
title = "Draw a table for each outcome, or explain why none"
grades = ["2-3"]
route = "first"
page = "new"
+++

## prompt
On each grid, draw a table with its bottom left corner at the dot, so that the ball does what is written under the grid. If there is no such table, explain why.

## figure
vspace(0.1) + row([blank_grid(6, 6, 0.5, label=r"stops at the bottom right\\after 1 bounce"),
                   blank_grid(6, 6, 0.5, label=r"stops at the top right\\after 4 bounces")], gap=0.9)
+ vspace(0.35) + row([blank_grid(6, 6, 0.5, label=r"stops at the top left\\after 7 bounces"),
                      blank_grid(6, 6, 0.5, label=r"stops at the top right\\after 3 bounces")], gap=0.9)
