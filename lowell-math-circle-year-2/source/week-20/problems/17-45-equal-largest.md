+++
id = "w20.45-equal-largest"
title = "Which circles can equal the largest square?"
grades = ["4-5"]
route = "return"
kernel = "Equality with the largest square spreads through circles and stops at a square, so a square junction allows it and a circle junction does not."
+++

## prompt @9.86
Fill the circles. Which circles can equal the largest square number on their own board? Explain what makes the two boards different.

## figure
graph([('a',1.15,7.6,True,0),('u',2.7,7.6,False,None),('b',4.25,7.6,True,8),('v',5.8,7.6,False,None),('w',7.35,7.6,False,None)],[('a','u'),('u','b'),('b','v'),('v','w')]) + graph([('a',1.3,4.3,True,0),('u',3.25,4.3,False,None),('v',5.2,4.3,False,None),('b',7.15,4.3,True,12),('w',5.2,2.55,False,None)],[('a','u'),('u','v'),('v','b'),('v','w')])
