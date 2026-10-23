+++
id = "w09.u-chart"
title = "Every table up to 6 by 6, in a chart"
grades = ["4-5"]
route = "first"
page = "new"
+++

## prompt
Find where the ball stops and how many times it bounces on every table from 1 by 1 to 6 by 6. Record each table in the chart: put a dot in the corner of its box where the ball stops, and write the number of bounces inside the box.

## figure
vspace(0.2) + row([chart(6, 0.85)])

## text
\newpage

## figure
row([blank_grid(14, 16, 0.5, dot=False)])
