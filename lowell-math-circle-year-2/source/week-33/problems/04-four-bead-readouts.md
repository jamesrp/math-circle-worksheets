+++
id = "w33.four-bead-readouts"
title = "Four-bead rings with one to four readouts"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "return", "2-3" = "first", "4-5" = "first" }
kernel = "A four-bead ring has 1, 2 or 4 readouts, never 3: the number of readouts divides the length."
+++

## prompt @0 [K-1]
Make four-bead rings with one, two, three or four different readouts. Which are possible?

## prompt @0 [2-3]
Make four-bead rings with exactly one, two, three or four different readouts. For each impossible number, explain why it cannot happen.

## prompt @0 [4-5]
Find four-bead rings with one, two, three or four different readouts, or explain why a requested number is impossible. What feature lets a mixed ring repeat early?

## figure
mats(4,8)+mats(4,18)
