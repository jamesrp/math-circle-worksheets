+++
id = "w20.k1-linked-circles"
title = "Two circles in a row"
grades = ["K-1"]
route = "return"
kernel = "Both circles must work on one unchanged board, which forces equal steps: (1,2), (2,1), (2,4) and (4,2)."
+++

## prompt @7.30
Make all the circle stacks. Both circles on a board must work at the same time.

## figure
k1_chain_example() + ''.join(path(y,ends) for y,ends in [(6.12,(0,3)),(4.60,(3,0)),(3.08,(0,6)),(1.56,(6,0))])
