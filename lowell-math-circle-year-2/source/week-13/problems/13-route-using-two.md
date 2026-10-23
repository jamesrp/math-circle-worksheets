+++
id = "w13.route-using-two"
title = "A route that uses two closing arrows"
grades = ["4-5"]
route = "return"
kernel = "A route may cross a smallest cut more than once, so every route uses at least one cut arrow, not exactly one, and such a route cannot be in a largest collection."
+++

## prompt
Find a smallest set of closing arrows and a route that uses two of those arrows. Can that route belong to a largest collection on this board? Explain.

## figure
route_two_cut()

## key
Close AC and BD. This is a minimum two-arrow set: s-A-C-t and s-B-D-t are disjoint, so one closure is insufficient. The route s-A-C-B-D-t uses both AC and BD. It cannot belong to a largest collection: every other route must use AC or BD, both already reserved. The largest size is 2, but any collection containing this long route has size 1. This example refutes the claim that every route uses exactly one outgoing cut arrow; “at least one” is the correct bound. There are five smallest sets: \{sA,sB\}, \{sB,AC\}, \{AC,BD\}, \{AC,Dt\}, \{Ct,Dt\}. Only the middle three are used twice by one route (s-B-A-C-t, s-A-C-B-D-t, s-A-C-D-t). If a child chose the two Start or the two Finish arrows, ask for a different smallest set. The answer to the question is always no.

## hints
Hint: reserve the long route and test which cut arrows remain available.
