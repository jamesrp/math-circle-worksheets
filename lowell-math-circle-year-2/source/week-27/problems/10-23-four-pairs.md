+++
id = "w27.23-four-pairs"
title = "Four pairs in two blocks"
grades = ["2-3"]
route = "return"
kernel = "A, B, W, X rank only each other ahead of the rest, and so do C, D, Y, Z; each block pairs stably in two ways, so exactly four of the 24 pairings stay, and none gives all eight letters their first choice."
+++

## prompt @0.93
Find every pairing that can stay. Can one pairing give all eight letters their first choice?

## figure
strips(2.00,*get('middle_four'),n=4,step=.65,d=.45,size=16)
+ ''.join(board(1.10+col*3.75,5.48+row*2.62,'ABCD','WXYZ',w=1.90,step=.52,d=.41,size=15) for row in range(2) for col in range(2))
