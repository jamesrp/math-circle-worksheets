+++
id = "w27.23-four-pairs"
title = "Four pairs in two blocks"
grades = ["2-3"]
route = "return"
# Card should 5, October 23, 2026: six boards, not four, so the page does not print the number of answers.
kernel = "A, B, W, X rank only each other ahead of the rest, and so do C, D, Y, Z; each block pairs stably in two ways, so exactly four of the 24 pairings stay, and none gives all eight letters their first choice."
+++

## prompt @0.93
Find every pairing that can stay. Can one pairing give all eight letters their first choice?

## figure
strips(2.00,*get('middle_four'),n=4,step=.65,d=.45,size=16)
+ ''.join(board(.70+col*2.55,5.25+row*2.55,'ABCD','WXYZ',step=.52,d=.41,size=15) for row in range(2) for col in range(3))
