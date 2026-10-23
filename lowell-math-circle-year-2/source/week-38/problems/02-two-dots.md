+++
id = "w38.two-dots"
title = "Two dots one edge trip can or cannot reach"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "Two edge dots share a trip exactly when they lie on the same boundary circle; on B, with one circle, every pair does."
+++

## prompt @27 [K-1]
Put two dots on the edges of A so one edge trip reaches both, then try to place them so no one trip reaches both. Repeat with B.

## prompt @27 [2-3]
On A and B, find two edge dots that one edge trip can visit together, and two that it cannot. Which requests are impossible?

## prompt @27 [4-5]
One separate closed edge is a boundary component. Explain the number of boundary components of A and B from their seam recipes.

## text @16,60 w=180 size=14
Dots on one edge go in one ring.

## figure
washer_example()

## text @16,181 w=180 size=12
The rings record which dots share an edge.
