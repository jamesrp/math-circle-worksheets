+++
id = "w18.row-from-either"
title = "A row the receiver could get from either picture"
grades = ["2-3"]
route = "first"
kernel = "Two rows that differ in one or two places share a possible received row; rows that differ in three or four places do not."
+++

## prompt
For each key, find a row that the receiver could get from either picture. If there is no such row, explain why.

## figure
''.join(keyed(x,y,'triangle',a,2,small=True)+keyed(x,y+2.6,'square',b,2,small=True) for x,y,a,b in [(0,3.1,'0000','0001'),(9.5,3.1,'0101','0110'),(0,13.7,'0001','1111'),(9.5,13.7,'0011','1100')])
