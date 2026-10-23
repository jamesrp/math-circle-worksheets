+++
id = "w86.longer-rings"
title = "Escape on five- and six-dot rings"
grades = ["2-5"]
route = "first"
kernel = "On a bare ring of four or more dots R escapes forever by staying outside C's one-road reach."
+++

## prompt
Find an escape plan for R on each ring that keeps working however C moves. A long game is a test; your plan must work forever.

## figure
graph(*cycle(5, 36), 96, 78, label='R5') + graph(*cycle(6, 36), 96, 181, label='R6') + lines(238, 1)

## key
On both the five- and six-dot ring, R begins at a nonneighbor of C. Before each cop turn, keep R outside C's closed one-road neighborhood. After C moves, stay if still safe; otherwise C is now a neighbor, so R steps away along the other ring edge. For a bare ring of at least four vertices that neighbor is neither C nor adjacent to C, restoring safety. ``Opposite'' is not an adequate general rule on an odd ring. Ask a partner to challenge the suggested response by staying or choosing either direction.
