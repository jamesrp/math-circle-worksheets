+++
id = "w32.equal-squares"
title = "Covering with identical squares"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "return", "2-3" = "return", "4-5" = "first" }
kernel = "Identical s by s squares cover an a by b rectangle exactly when s divides both sides; the largest such s is the greatest common divisor."
+++

## prompt @0 [K-1]
Cover each rectangle with squares that are all the same size. Find the biggest square size that works.

## prompt @0 [2-3]
Cover each rectangle with identical squares. Find every whole-number square size that works, and decide which is biggest.

## prompt @0 [4-5]
For each rectangle, find every size of identical whole-grid square that can cover it. Explain why your list is complete.

## figure [K-1]
gridrect(1,3,6,4)+gridrect(1,12,9,6)

## figure [2-3]
gridrect(1,3,12,8)+gridrect(1,14,10,6)+answer_lines([4.5,6.5,15.5,17.5],14)

## figure [4-5]
gridrect(1,3,12,8)+gridrect(1,14,15,9)
