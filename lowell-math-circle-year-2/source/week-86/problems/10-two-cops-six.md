+++
id = "w86.two-cops-six"
title = "Two cops from a on the six-ring"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "Two cops catch on a ring: one holds a dot as a blocker while the other sweeps the path that remains."
+++

## prompt @40
Start both cops at a. Use them to catch R on this ring. Find a plan that works however R starts and moves.

## figure
graph(*cycle(6, 42), 96, 129, label='Q6') + lines(202, 3)

## key
For the six-dot task both cops enter at a; the same start works for the eight-dot and general-ring question. Keep C1 at a as a blocker. On its first turn C2 moves to the adjacent b, then advances along the remaining path toward R. Deleting a turns the other ring vertices into that path. R cannot pass C1 to get around the far end, nor pass C2, so the path strategy captures. The same plan works on every finite cycle. If R chooses the occupied starting dot, capture is immediate; if it starts at b, C2 catches on its first move. Two cops are necessary on a bare cycle of length at least four because the one-cop escape invariant applies; the triangle only needs one.
