+++
id = "w12.four-edge-trees"
title = "How many trees have four edges?"
grades = ["4-5"]
route = "return"
kernel = "There are 14 four-edge trees; splitting each code at its first return to zero counts every tree exactly once."
+++

## prompt
How many different trees have four edges? Organize the count so someone can check that every tree is counted exactly once.

## figure
roots([38,84,130,176],[68,112,156,200])

## key
\emph{Print guide, p. 9.} There are 14 four-edge trees. The page 7 gallery exhibits them; this argument certifies none are missed. A nonempty legal code has exactly one split U P D Q, with the displayed D being the first return to height zero. P and Q are themselves legal codes. If P has i pairs, Q has n-1-i pairs. Choosing them independently gives C(i) times C(n-1-i) choices, and different i or different smaller words cannot give the same whole word.
