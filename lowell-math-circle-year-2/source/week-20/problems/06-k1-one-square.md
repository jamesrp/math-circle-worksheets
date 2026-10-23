+++
id = "w20.k1-one-square"
title = "One square controls the board"
grades = ["K-1"]
route = "return"
kernel = "With one square on a connected board every circle equals the square."
+++

## prompt @9.86
Fill the circles. Can any circle have a different number of cubes from its square?

## figure
graph([('a',4.25,8.1,True,2),('u',2.9,6.3,False,None),('v',5.6,6.3,False,None)],[('a','u'),('a','v'),('u','v')]) + graph([('a',2.95,4.1,True,3),('u',5.55,4.1,False,None),('v',5.55,1.9,False,None),('w',2.95,1.9,False,None)],[('a','u'),('u','v'),('v','w'),('w','a')])
