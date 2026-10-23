+++
id = "w14.three-routes-45"
title = "Three starts to one hexagon fan"
grades = ["4-5"]
route = "return"
kernel = "The number of target-fan diagonals missing from a start is a lower bound on the flips, and here each bound (3, 1, 2) is met."
+++

## prompt
Change each of the three starting fillings into the fourth filling using as few flips as possible. Explain why no shorter routes can work.

## figure
three_routes()

## key
The three starts, left to right, are $\{BD,BE,BF\}$, $\{AC,AE,CE\}$, and $\{AD,BD,DF\}$. The fourth filling, where the arrows point, is the A fan $\{AC,AD,AE\}$. Their minimum distances are 3, 1, and 2. Left start. Use the three-flip route on page 7: replace BF by AE, BE by AD, then BD by AC. It is shortest because all three target diagonals were missing. Middle start. Replace CE by AD. Exactly one target diagonal was missing. Right start. Replace BD by AC, then DF by AE. Exactly two target diagonals were missing.

## hints
Have a child mark which A-fan diagonals are already present, without erasing them. Ask how much that count can rise in one flip. A successful short route alone is not a proof that it is shortest.
