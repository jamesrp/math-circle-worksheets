+++
id = "w20.k1-one-circle"
title = "One circle between two squares"
grades = ["K-1"]
route = "first"
page = "same"
kernel = "A circle joined to two squares is their fair share: 1, 3, 2 and 4, counting an empty square as a place."
+++

## prompt @6.65
Make the circle stacks on all four boards.

## figure
k1_sharing_example() + ''.join(graph([('a',x-.72,y+1.3,True,a),('b',x+.72,y+1.3,True,b),('c',x,y,False,None)],[('a','c'),('b','c')]) for x,y,a,b in [(2.25,4.35,0,2),(6.25,4.35,2,4),(2.25,1.67,0,4),(6.25,1.67,2,6)])
