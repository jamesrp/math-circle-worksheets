+++
id = "w05.m-orders-of-three"
title = "Every order of three towers and its two numbers"
grades = ["2-3"]
route = "first"
+++

## prompt
Stand towers of 1, 2, and 3 cubes in a row. Find every order of the three towers, and write each one with the number of towers seen from each end. Which pairs of numbers can a row of three towers never show? Explain why.

## figure
close(gap(0.2) + pic(place([D.row_record(3, sq=1.2) for _ in range(8)], 2, 8.8, 1.95)), gap(3.2))
