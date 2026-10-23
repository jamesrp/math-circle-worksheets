+++
id = "w48.small-triangle"
title = "The triangle with small squares"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "Small squares raise the triangle's inside count from 6 to 7 and lower its cover from 10 to 9 big-square units; refining never loosens either bound."
+++

## figure
legend()

## prompt @43 [K-1]
Do Problem 1 again with small squares.

## prompt @43
Use the smaller squares to trap the triangle's area more tightly. State both bounds in big-square units.

## figure [K-1]
shape(33,86,8,'triangle')

## figure
shape(33,76,8,'triangle')+blanks(207,True)
