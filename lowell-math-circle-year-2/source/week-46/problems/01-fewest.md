+++
id = "w46.fewest"
title = "The fewest instructions to match"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "Two boards can be made to match with exactly as many instructions as slots where they differ: each differing slot needs one, and one per slot suffices."
+++

## prompt @6.5 [K-1]
Make these boards match using as few instructions as you can. Can any other starts need more instructions?

## prompt @6.5 [2-3]
Find the fewest instructions needed to make these boards match. Build pairs needing fewer instructions. Can any pair need more?

## prompt @6.5 [4-5]
How does the fewest number of instructions needed for a match depend on the starting pair? Develop a rule that works for every pair.

## figure [K-1]
board(3.5,10,'RBR',3.6,True) + board(3.5,15,'BRB',3.6,True) + box(0,21,18,2)

## figure [2-3]
board(3.5,10,'RBR',3.6,True) + board(3.5,15,'BRB',3.6,True) + space(21,3)

## figure [4-5]
cases(9)
