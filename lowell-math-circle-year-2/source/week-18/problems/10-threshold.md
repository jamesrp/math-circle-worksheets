+++
id = "w18.threshold"
title = "How many differing places keep two pictures apart?"
grades = ["4-5"]
route = "return"
kernel = "Two rows can always be told apart after at most one change exactly when they differ in at least three places."
+++

## prompt
For each pair, could the receiver see the same row after either picture was sent? What is the smallest number of differing positions that keeps two pictures apart for rows of any length? Explain why that number is enough and why a smaller number fails.

## figure
''.join(keyed(x,4.4,'triangle',a,.85,.95,'number')+keyed(x,6.3,'square',b,.85,.95,'number') for x,a,b in [(.3,'000000','110000'),(9.6,'010010','101010')])
