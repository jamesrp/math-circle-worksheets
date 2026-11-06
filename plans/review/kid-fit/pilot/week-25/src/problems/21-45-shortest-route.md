+++
id = "w25.45-shortest-route"
title = "A shortest route on six columns"
grades = ["4-5"]
route = ["first", "return"]
kernel = "Three top counters sit where the target has none and a switch fixes at most one of them, so three switches are needed and enough."
+++

## prompt @27
Change the upper picture into the lower picture in as few switches as you can. Record a shortest route and explain why fewer switches cannot work.

## figure
h_route_endpoints()

## key
\emph{Print guide, p. 13.} \textbf{Answer:} exactly 3 switches. Student page 5 has three blank grids: a shortest route needs two for its intermediate pictures, and the third is spare. The route below switches column pairs 1,4; then 2,5; then 3,6. These are all legal two-row rectangles.

The target has no top counter in columns 1, 2, or 3. The start has one in each of those columns. One switch can remove a top counter from at most one of these three unwanted columns, so every route uses at least three switches. The displayed three-switch route meets this lower bound exactly.
