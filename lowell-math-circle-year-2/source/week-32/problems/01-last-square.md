+++
id = "w32.last-square"
title = "The last square of two rectangles"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "The biggest-square rule ends with a square whose side is the greatest common divisor of the two sides."
+++

## prompt @6 [K-1]
Cover both rectangles with the biggest-square rule. Which square comes last?

## prompt @6 [2-3]
Use the biggest-square rule on both rectangles. Record the square sizes in the order you use them.

## prompt @6 [4-5]
Apply the biggest-square rule to both rectangles. Record every square size, including repeated sizes, and compare the last squares.

## figure [K-1]
gridrect(1,8.5,6,4)+gridrect(1,15.5,8,4)

## figure
gridrect(1,8.5,10,6)+gridrect(1,17,8,5)+answer_lines([10,12,18.5,20.5])
