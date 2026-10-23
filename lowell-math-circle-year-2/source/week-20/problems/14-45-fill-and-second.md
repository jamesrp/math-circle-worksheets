+++
id = "w20.45-fill-and-second"
title = "Fill the boards and look for a second filling"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "The path (5,10), the tree (5,7) and the tied diamond (8,8) each have exactly one filling."
+++

## prompt @6.87
Fill all the circles. Can any board have a second filling with the same square numbers?

## figure
numeric_chain_example(8.32,8.98) + path(5.90,(0,15),2) + tree(3.65,4.25,(0,8,9)) + diamond(4.25,1.90,2,14,True,vertical=.78)
