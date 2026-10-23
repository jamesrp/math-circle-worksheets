+++
id = "w12.k1-avoid-neighbors"
title = "Pair eight dots without joining neighbors?"
grades = ["K-1"]
route = "return"
kernel = "Every noncrossing pairing joins some two neighbors: an innermost string has no dots under it."
+++

## prompt
Can you pair eight dots without joining any two neighbors around the circle? Show why your answer is right.

## figure
k1_neighbor_records()

## key
\emph{Print guide, p. 4.} No. Every noncrossing complete pairing has a pair of circular neighbors. Proof: consider any chord and one side of it. If there are dots on that side, they must be paired entirely within that side. Choose a pair with the fewest intervening dots in the linear reading order 1,...,8. If it had any, those dots would have a pair between them with fewer intervening dots, a contradiction. Thus some consecutive numbered pair is joined, and it is also a pair of circular neighbors.
