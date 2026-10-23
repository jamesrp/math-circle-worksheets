+++
id = "w20.45-uniqueness"
title = "Two different fillings?"
grades = ["4-5"]
route = "return"
kernel = "The difference of two fillings obeys the rule with 0 at every square, so the maximum principle makes it 0 everywhere."
+++

## prompt @9.86
Can the same board, with the same square numbers, have two different fillings that both follow the rule? Explain your answer for every finite board where each shape can reach a square.

## figure
''.join(graph([('a',1.2,y,True,0),('u',2.7,y,False,None),('v',4.4,y+.75,False,None),('w',4.4,y-.75,False,None),('b',6.15,y+.75,True,16),('c',6.15,y-.75,True,8)], [('a','u'),('u','v'),('u','w'),('v','w'),('v','b'),('w','c')]) for y in [7.1,3.5])
