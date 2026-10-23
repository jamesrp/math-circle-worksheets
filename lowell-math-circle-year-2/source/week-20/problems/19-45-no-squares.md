+++
id = "w20.45-no-squares"
title = "Five fillings and twenty-five fillings"
grades = ["4-5"]
route = "return"
kernel = "Each connected group of circles is constant, so the triangle has 5 fillings and the two separate pairs 5 x 5 = 25."
+++

## prompt @9.86
Use whole numbers from 0 to 4. Find every filling of the upper board and of the lower board. How many fillings does each board have? Explain why none are missing.

## figure
graph([('a',4.25,8.0,False,None),('b',2.8,6.05,False,None),('c',5.7,6.05,False,None)],[('a','b'),('b','c'),('c','a')],check=False) + dashed_group() + graph([('a',1.2,3.5,False,None),('b',3.0,3.5,False,None),('c',5.5,3.5,False,None),('d',7.3,3.5,False,None)],[('a','b'),('c','d')],check=False)
