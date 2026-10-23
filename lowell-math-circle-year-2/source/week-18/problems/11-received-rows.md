+++
id = "w18.received-rows"
title = "Every row the receiver might see from one row"
grades = ["4-5"]
route = "return"
kernel = "A row of length n can arrive as itself or with one of its n entries changed: n+1 received rows."
+++

## prompt
Find every row the receiver might see from each row below, and explain why none are missing. How many received rows can come from any one row of length 10?

## figure
''.join(strip(.7,y,bits,1,.95,'number') for y,bits in [(3.4,'010'),(9.5,'0110'),(15.6,'00111')])
