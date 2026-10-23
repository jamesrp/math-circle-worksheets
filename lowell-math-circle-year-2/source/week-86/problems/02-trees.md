+++
id = "w86.trees"
title = "A cop plan on two trees"
grades = ["2-5"]
route = "first"
kernel = "Every tree is cop-win: with C's dot removed, the piece of the tree holding R shrinks with every cop step toward R."
+++

## prompt
Find a cop plan that catches R on each map, wherever R starts and however R moves. Challenge your partner to escape.

## figure
graph(T1, T1_ROADS, 96, 110, label='T1') + graph(T2, T2_ROADS, 96, 151, label='T2') + lines(239, 1)

## key
Both maps are trees. C can start anywhere and repeatedly take the first edge of the unique path toward R. Starting at c in either supplied map catches within two cop moves, but the printed task asks for a guaranteed strategy, not the fastest count.

For the general reason, delete C's dot and shade the connected component containing R. C's next move goes into that component. Unless it captures R, deleting the new C dot leaves R in a strict subset of the former component. R's reply cannot leave this subset without crossing C. Repeated strict shrinking in a finite graph forces capture. Merely saying the distance decreases is insufficient: R can move away and restore the distance for a while. The territory cut off by C, not the current distance alone, is what accumulates.
