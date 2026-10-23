+++
id = "w20.23-match-extreme"
title = "Matching the biggest or smallest square"
grades = ["2-3"]
route = "first"
kernel = "A circle can equal an extreme square when a square stops the chain: equality spreads through circles, not through squares."
+++

## prompt @9.86
Fill all the circles. Can a circle match the biggest square on its board? Can a circle match the smallest square on its board?

## figure
graph([('a',1.15,7.4,True,0),('u',2.7,7.4,False,None),('b',4.25,7.4,True,6),('v',5.8,7.4,False,None),('w',7.35,7.4,False,None)],[('a','u'),('u','b'),('b','v'),('v','w')]) + graph([('v',1.15,4.0,False,None),('w',2.7,4.0,False,None),('a',4.25,4.0,True,0),('u',5.8,4.0,False,None),('b',7.35,4.0,True,6)],[('v','w'),('w','a'),('a','u'),('u','b')])
