+++
id = "w20.45-thirteen"
title = "A circle of 13 or more?"
grades = ["4-5"]
route = "first"
kernel = "A greatest value on a finite board forces its neighbours to equal it, through circles to a square, so no circle exceeds the largest square."
+++

## prompt @9.86
Can either board have a circle number of 13 or more while all circles follow the rule? Find a filling, or explain why none can work.

## figure
graph([('a',1.3,7.6,True,0),('u',2.85,7.6,False,None),('v',4.4,7.6,False,None),('b',5.95,7.6,True,6),('w',4.4,5.9,False,None),('z',6.25,5.9,False,None),('c',7.35,4.55,True,11)], [('a','u'),('u','v'),('v','b'),('v','w'),('w','z'),('z','v'),('z','c')]) + diamond(4.25,2.65,2,10,True)
