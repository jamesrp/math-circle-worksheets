+++
id = "w86.triangle-square"
title = "Triangle against square"
grades = ["2-5"]
route = "first"
kernel = "One cop catches on the triangle at once; on the square R stays opposite C forever."
+++

## prompt
Play on both rings. On which can C always catch R? On which can R keep escaping forever? Find a plan that works against every reply.

## figure
graph(*cycle(3, 34), 96, 77, label='R3') + graph(*cycle(4, 39), 96, 179, label='R4') + lines(238, 1)

## key
On the triangle C can start anywhere and capture the distinct starting R on its first move. On the square R starts opposite C. Whenever C stays, R stays; whenever C moves one edge, R moves one edge to the new opposite dot. Before every cop turn there are two roads between them, so the next cop move cannot capture. Every possible cop reply is accounted for; this explains perpetual escape, unlike a long lucky game.
