+++
id = "w17.three-circle-rows"
title = "Which rows does a three-circle machine accept?"
grades = ["4-5"]
route = "first"
page = "same"
kernel = "The three-circle cycle accepts exactly the rows whose number of red cards is a multiple of three."
+++

## prompt @1.86 size=14.5
Find every five-card row this machine sends to YES. Describe exactly which rows it sends to YES, for any length.

## figure
three(3.5,labels=True)

## text @.8,4.74 w=6.9 size=11.5
Example R B: start 1 $\xrightarrow{\ R\ }$ 2 $\xrightarrow{\ B\ }$ 2; stop: NO.

## figure
''.join(line(x,y,1.85) for y in [5.45,5.95,6.45,6.95,7.45] for x in [.85,3.28,5.72])+lines(.85,[8.5,9.15,9.8],6.8)
