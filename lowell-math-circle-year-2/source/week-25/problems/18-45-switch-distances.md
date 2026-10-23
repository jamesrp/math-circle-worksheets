+++
id = "w25.45-switch-distances"
title = "Switch routes among the six pictures"
grades = ["4-5"]
route = "first"
kernel = "A switch trades one top column for another, so the six pictures are connected and the greatest shortest distance is 2."
+++

## prompt @27
A switch moves the two counters to the empty corners shown; other cells stay fixed. Any two rows and columns may be used. Can any picture from Problem 1 reach any other by switches? Find the greatest number needed if you always take a shortest route.

## figure
h_switch_distances('One switch:')

## key
\emph{Print guide, p. 12.} A legal switch exchanges one selected top column with one unselected top column. If two pictures are identical, distance is 0. If their top pairs share one column, switch the unwanted top column with the missing one; distance is 1. If the pairs are disjoint, replace one unwanted column, then the other; distance is 2.

The only distance-two pairs are \{1,2\} versus \{3,4\}, \{1,3\} versus \{2,4\}, and \{1,4\} versus \{2,3\}. Each needs at least two moves because one switch replaces just one top position. Every distinct pair fits one of these two cases, so all pictures communicate and the largest shortest distance is exactly 2.
