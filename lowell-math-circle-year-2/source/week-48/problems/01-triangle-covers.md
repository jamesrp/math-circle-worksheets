+++
id = "w48.triangle-covers"
title = "Inside and cover for the triangle"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"             # shares page 1 with the rules
kernel = "On the 4-by-4 grid the half-square triangle has 6 whole cells and a cover of 10, so its area lies between 6 and 10."
+++

## prompt @65 [K-1]
Mark all the whole squares inside the triangle. Cover the triangle with as few grid-square tiles as you can.

## prompt @65
Find an inside cover and an outside cover for the triangle. Use as many whole inside squares and as few outside-cover squares as possible.

## figure
shape(33,96,4,'triangle')

## text @15,224 size=12
Inside: \rule{13mm}{.3pt} big squares \qquad Cover: \rule{13mm}{.3pt} big squares
