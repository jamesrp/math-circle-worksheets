+++
id = "w24.k1-a-empty-place"
title = "Change A's largest card"
grades = ["K-1"]
route = "return"
kernel = "With A = (2,4,x), A wins 2 + (number of B cards below x) pairs, so of 3, 5, 7 and 9 only 9 gives A more than half."
+++

## prompt
Try 3, 5, 7, and 9 in A's empty place. Which choices make A win more card pairs than B?

## figure
art(kdeck('A',[2,4,None],7.8), kdeck('B',[1,6,8],6.4), kpool([3,5,7,9],4.85))
