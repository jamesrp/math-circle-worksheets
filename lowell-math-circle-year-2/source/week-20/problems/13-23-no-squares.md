+++
id = "w20.23-no-squares"
title = "Boards with no squares"
grades = ["2-3"]
route = "return"
kernel = "Without squares only constant fillings work: six on each board with numbers 0 to 5."
+++

## prompt @9.86
Use whole numbers from 0 to 5. Find every filling for each board, and explain how you know none are missing.

## figure
graph([('a',2.85,8.05,False,None),('b',5.65,8.05,False,None),('c',5.65,5.95,False,None),('d',2.85,5.95,False,None)],[('a','b'),('b','c'),('c','d'),('d','a')],check=False) + graph([('a',1.4,3.25,False,None),('b',4.25,3.25,False,None),('c',7.1,3.25,False,None)],[('a','b'),('b','c')],check=False)
