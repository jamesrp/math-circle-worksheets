+++
id = "w44.k1-before-last"
title = "One draw back"
grades = ["K-1"]
route = "return"
kernel = "Removing one possible last copy gives each predecessor; a predecessor keeps both colors, so copying never loses a color."
+++

## prompt @0
Find every possible bag just before the last draw for each finish. Could copying ever lose all the blue counters?

## figure
k1_before_last()

## key
5R / 1B: 4R / 1B, R.

4R / 2B: 3R / 2B; 4R / 1B, R; B.

3R / 3B: 2R / 3B; 3R / 2B, R; B.

Each last draw adds exactly one counter of its own color, so remove one candidate last copy to find a predecessor. A predecessor must still contain at least one red and one blue. For example, removing the only blue from 5R/1B would make 5R/0B, which cannot have arisen from the required start.

Copying cannot lose all blue counters, or all red counters. Every drawn counter is returned, and each move only adds a counter. In particular, the original blue remains. This is a deterministic invariant, not an observation about which color seems to be winning.
