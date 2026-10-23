+++
id = "w41.predict-trips"
title = "Predict where four trips from H end"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "A step across an edge comes back in on the opposite edge at the same height or place across."
+++

## prompt @142
Start at H for each trip. Predict where it ends, then try it with your pawn.

## figure
predict_trips()

## key [K-1]
The four printed routes end, from top to bottom, at F, G, F, F. RRD: H $\to$ E $\to$ D $\to$ F. UU: H $\to$ B $\to$ G. LD: H $\to$ D $\to$ F. UURR: H $\to$ B $\to$ G $\to$ I $\to$ F.

Several different routes intentionally reach F. At a portal continue in the same arrow direction, and a seam crossing still counts as one ordinary step.

## key [2-3]
In printed order: RRD$\to$F, UU$\to$G, LD$\to$F, UURR$\to$F. Three different routes reach F; the path itself is more information than its final portal cell.

## key [4-5]
Destinations: F, G, F, F for RRD, UU, LD, UURR.
