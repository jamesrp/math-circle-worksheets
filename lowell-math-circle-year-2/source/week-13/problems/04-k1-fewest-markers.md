+++
id = "w13.k1-fewest-markers"
title = "Stop every route with as few markers as you can"
grades = ["K-1"]
route = "first"
kernel = "Every route must lose an arrow: the diamond needs one marker on each branch, and the funnel needs one on the arrow every route shares."
+++

## prompt
Stop every route with as few markers as you can. Find another way with the same number of markers, if you can.

## figure
k1_fewest_markers()

## key
Upper diamond: minimum 2. All four minimum closures take one arrow from \{sA,At\} and one from \{sB,Bt\}: \{sA,sB\}, \{sA,Bt\}, \{At,sB\}, \{At,Bt\}. Each branch must be broken. Lower funnel: minimum 1; either CD or Dt stops both routes. There are no other one-arrow solutions because closing an earlier edge leaves the other branch.

## hints
Hint: trace both routes and look for an arrow they must both use.
