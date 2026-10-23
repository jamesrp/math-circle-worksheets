+++
id = "w49.predecessors"
title = "Which rings can be the result of one move?"
grades = ["2-3", "4-5"]
route = "return"
kernel = "(2,0,2,0) and (1,1,1,1) have old rings; (1,1,1,0) cannot, since the gaps around a ring have an even total, and (0,0,0,2) cannot, since three zero gaps force a constant ring."
+++

## prompt @0
Could each ring be the result of one move? Find an old ring that makes it, or explain why no old ring can work.

## figure
ring(28,53,[2,0,2,0],40,8)+ring(120,53,[1,1,1,0],40,8)+ring(28,147,[1,1,1,1],40,8)+ring(120,147,[0,0,0,2],40,8)
