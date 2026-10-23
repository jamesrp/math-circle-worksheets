+++
id = "w23.45-zero-one-principle"
title = "Does sorting 0s and 1s guarantee sorting numbers?"
grades = ["4-5"]
route = "first"
kernel = "Zero-one principle: if a fixed machine left 9 above 4, the threshold t = 4 would give a 0-1 start that finishes 1 above 0, so a machine that sorts every 0-1 start sorts every start, repeats included."
+++

## prompt
A fixed four-lane machine sorts every start made of 0s and 1s. Could some other start finish with 9 in lane 2 and 4 in lane 3? Explain. Decide whether sorting every 0--1 start guarantees sorting every start made of numbers, including repeats.

## figure
network(4,[],y=5.5,gap=1.5,outs=['',9,4,''])
+ '\\draw[fill=white,line width=.7pt] (4.4,4.75) rectangle (13.65,10.75);\n'
+ txt(7.97,7.35,'?',width=2.0,size=25)
