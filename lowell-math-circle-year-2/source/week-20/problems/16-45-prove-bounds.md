+++
id = "w20.45-prove-bounds"
title = "The maximum and minimum principle"
grades = ["4-5"]
route = "first"
kernel = "On a finite board where every shape reaches a square, every circle lies between the smallest and largest square it can reach."
+++

## prompt @9.86
A board has finitely many shapes and lines. Every shape can reach a square along the lines. Explain why no circle number can be below the smallest square number it can reach or above the largest one. Your explanation must work for every such board.

## figure
graph([('a',1.1,6.25,True,0),('u',2.6,6.25,False,None),('v',4.15,6.25,False,None),('w',5.7,6.25,False,None),('b',7.25,6.25,True,12),('c',4.15,4.65,True,6),('t',4.15,7.8,False,None)], [('a','u'),('u','v'),('v','w'),('w','b'),('v','c'),('u','t'),('t','w')])
