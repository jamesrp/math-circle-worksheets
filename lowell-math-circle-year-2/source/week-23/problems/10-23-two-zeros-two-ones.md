+++
id = "w23.23-two-zeros-two-ones"
title = "Two 0s and two 1s"
grades = ["2-3"]
route = "return"          # the guide offers Problems 4-5 as a separate binary-certification route
kernel = "Bars (1,2), (1,3), (2,3), (2,4) sort all six orders of 0, 0, 1, 1 but fail 0010, 0100, 1000 and 1110, so passing one kind of 0-1 start is not enough."
+++

## prompt
Use the cards 0, 0, 1, 1. Find every different starting order and test it on this machine. Decide whether the machine also sorts every other four-card start made of 0s and 1s.

## figure
bank([0,0,1,1],x=4.9,y=3.5)
+ network(4,[(1,2),(1,3),(2,3),(2,4)],y=6.0,gap=1.3)
