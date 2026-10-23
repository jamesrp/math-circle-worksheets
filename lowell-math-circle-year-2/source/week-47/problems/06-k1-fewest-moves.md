+++
id = "w47.k1-fewest-moves"
title = "Fewest one-level moves between two landscapes"
grades = ["K-1"]
route = "return"
kernel = "Moving one marker one level at a time, the fewest moves from 1,2,1,2,1 to 1,0,0,0,1 is the total change, 5, though lowering the middle first is illegal."
+++

## prompt
Move one white marker one level up or down in its own column each turn, keeping the rule. Reach the second landscape in as few moves as you can.

## figure
row(30,36,[1,2,1,2,1],(0,4),dx=25)+row(30,70,[1,0,0,0,1],(0,4),dx=25)+board(40,113,5,3,{0:1,4:1})
