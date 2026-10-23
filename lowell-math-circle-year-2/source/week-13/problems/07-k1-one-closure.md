+++
id = "w13.k1-one-closure"
title = "Close one arrow and still fit two routes"
grades = ["K-1"]
route = "return"
kernel = "Closing an arrow before the meeting dot leaves two routes; closing one of only two exits, or a branch of the greedy board other than its middle arrow, does not."
+++

## prompt
Close just one arrow at a time. Find every arrow you could close and still fit two routes.

## figure
k1_one_closure()

## key
On the upper board, exactly six single closures preserve two routes: sA, sB, sC, AD, BD, CD. Each removes one of three approaches to D, leaving two intact. Any of DE, DF, Et or Ft removes one of only two exits and leaves at most one route. On the lower greedy board, only AB may be removed. Any other closure breaks one of the two disjoint branch routes. Reopen the arrow before each new trial.

## hints
Hint: sort arrows into “before the meeting dot” and “after it.”
