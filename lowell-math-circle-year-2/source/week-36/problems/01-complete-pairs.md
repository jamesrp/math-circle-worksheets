+++
id = "w36.complete-pairs"
title = "Complete each pair"
grades = ["K-1", "2-3", "4-5", "2-5"]
route = "first"
page = { "K-1" = "new", "2-3" = "same", "4-5" = "same", "2-5" = "same" }
kernel = "Any two different tiles have exactly one completing tile: for each attribute keep the shared value or use the missing one."
+++

## prompt [K-1]
Put a tile in each big box to make an allowed three. Your partner checks each three. Then give your partner new pairs.

## prompt @9 [2-3, 2-5]
Complete each pair to make an allowed three. Choose other pairs to give your partner; can any pair have two different answers?

## prompt @9 [4-5]
Complete the pairs. Can a pair of tiles have two completing tiles, or none? Explain.

## figure [K-1]
pairs_big()

## figure
pairs()
