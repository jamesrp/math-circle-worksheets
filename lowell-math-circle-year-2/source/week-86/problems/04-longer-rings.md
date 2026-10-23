+++
id = "w86.longer-rings"
title = "Escape on five- and six-dot rings"
grades = ["2-5"]
route = "first"
kernel = "On a bare ring of four or more dots R escapes forever by staying outside C's one-road reach."
+++

## prompt
Find an escape plan for R on each ring that keeps working however C moves. Your plan must work forever.

## figure
graph(*cycle(5, 36), 96, 78, label='R5') + graph(*cycle(6, 36), 96, 181, label='R6', sides={'b': 'right', 'f': 'left'}) + lines(238, 1)

## key
On both the five- and six-dot ring, R begins at a nonneighbor of C. Before each cop turn, keep R outside C's closed one-road neighborhood. After C moves, stay if still safe; otherwise C is now a neighbor, so R steps away along the other ring edge. For a bare ring of at least four vertices that neighbor is neither C nor adjacent to C, restoring safety. An odd ring has no single opposite dot; staying on one of the two dots across from C also works (on the pentagon these are exactly the dots outside C's neighborhood). Ask a partner to challenge the suggested response by staying or choosing either direction. A pair that finishes this problem can go on to upper Problem 2, adding roads.
