+++
id = "w23.45-fewest-bars"
title = "The fewest bars"
grades = ["4-5"]
route = "return"
# Card could 12, October 23, 2026: "Count each bar, even when two bars could happen at the same
# time" is cut from the prompt; the guide keeps "Count bars, not parallel stages."          # the guide offers Problems 6-7 (records and minima) instead of 3-5
kernel = "Three lanes need 3 bars and four lanes need 5: a $k$-bar machine has at most $2^k$ records, each sorting at most one order, so $2^k$ must reach $3! = 6$ and $4! = 24$, and an exhaustive check rules out four bars."
+++

## prompt
Find the fewest bars a three-lane sorting machine can have and the fewest bars a four-lane sorting machine can have. Give a working machine for each and explain why fewer bars cannot work.

## figure
network(3,[],y=4.7,gap=1.25)
+ network(4,[],y=10.3,gap=1.25)
