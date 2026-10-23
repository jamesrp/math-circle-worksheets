+++
id = "w39.tree-home"
title = "Trips home on the tree"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "return", "2-3" = "first", "4-5" = "first" }
kernel = "Every trip from A back to A on a tree shortens to staying at A: a farthest place visited is always left by the road just used."
+++

## prompt @27 [K-1]
Make trips from A back to A using 4, 6, 8, and 12 road steps. Which can you shorten to staying at A?

## prompt @27 [2-3]
Make three different 12-step trips from A back to A, each using every road. Can any trip home on this map survive after every immediate reversal is removed?

## prompt @27 [4-5]
On this map, can a trip from A back to A survive after every immediate reversal is removed? Explain why your answer holds for trips of any length.

## figure [K-1]
graph(30, 77, 49, TREE, TEDGES)

## figure [2-3]
graph(30, 72, 49, TREE, TEDGES) + blank(16, 184, 180, 71)

## figure [4-5]
graph(30, 69, 49, TREE, TEDGES) + blank(16, 179, 180, 34)

## key [K-1]
All 4-, 6-, 8-, and 12-step trips from A back to A shorten to staying at A. Explicit witnesses alternate A and B for 2, 3, 4, or 6 out-and-back pairs. Encourage less repetitive excursions when children are ready; the theorem covers all valid choices.

## key [2-3]
Three valid 12-step A-home trips covering every road are ABABCBDEDFDBA, ABABCBDFDEDBA, and ABABDEDFDBCBA. Every one reduces to A. A nonempty reduced closed walk in a tree would force a cycle; equivalently a farthest excursion forces a reversal. The claim holds for all finite lengths, not just the three examples.

## key [4-5]
No nonempty A-home trip on the tree survives. Root the tree at A. In any nonempty closed journey, take a visited vertex of greatest distance from A. Choose an occurrence reached from its parent. Since no deeper vertex is visited and a tree gives it only one neighbor closer to A, the next step returns along that same edge. There is a cancellable pair. Reapply after each deletion until only A remains.
