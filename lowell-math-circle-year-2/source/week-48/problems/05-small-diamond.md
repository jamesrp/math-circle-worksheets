+++
id = "w48.small-diamond"
title = "The diamond with small squares"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = "return", "2-3" = "first", "4-5" = "first" }
kernel = "On the small grid the diamond's bounds become 6 and 10, so the uncertain area falls from 8 to 4 big-square units; K-1 changes the shape without changing its big-square marking."
+++

## figure
legend()

## prompt @43 [K-1]
Change the diamond so four outside small squares become partly gray. Keep every big square whole, partial, or outside as it was.

## prompt @43
Find new bounds for the diamond. Compare the area left uncertain on the big grid and on the small grid.

## figure [K-1]
shape(33,86,8,'diamond')

## figure
shape(33,76,8,'diamond')+blanks(207,True)
