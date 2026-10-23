+++
id = "w18.shortest-four"
title = "The shortest key for four pictures"
grades = ["4-5"]
route = "return"
kernel = "Four pictures need length five: four rows each with n+1 received rows need 4(n+1) at most 2 to the n, which fails for n up to 4."
+++

## prompt
What is the shortest row length for a key that always works for four pictures? Give a working key and explain why every shorter length is impossible.

## figure
''.join(shape(1.3,y+.35,s)+line(2.45,y+1,10.9) for y,s in zip([3.3,5.5,7.7,9.9],['triangle','square','star','diamond']))
