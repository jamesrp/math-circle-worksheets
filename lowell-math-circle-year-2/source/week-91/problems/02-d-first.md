+++
id = "w91.d-first"
title = "Four-exit tree: keep D first"
grades = ["2-5"]
route = "first"
kernel = "D first forces the root and right-child cards; the left child is free, so exactly two orders start with D."
+++

## figure
head('Grades 2--5')

## prompt @15,31
Use the four-exit tree. Choose starting arrows that send the first counter to D. Keep those cards and send seven more counters. Record the starting arrows and arrival order.

## figure
tree(60,79,2,1)+strip(15,135,8,15)

## text @15,162 w=186 size=14
What can you change in the starting arrows while keeping D first? Find every arrival order.

## figure
tree(60,184,2,1)+strip(15,240,8,15)
