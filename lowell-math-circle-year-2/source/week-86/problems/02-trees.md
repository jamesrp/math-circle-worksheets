+++
id = "w86.trees"
title = "A cop plan on two trees"
grades = ["2-5"]
route = "first"
kernel = "Every tree is cop-win: with C's dot removed, the piece of the tree holding R shrinks with every cop step toward R, even when R runs ahead of C into another branch."
+++

## prompt
Find a cop plan that catches R on each map, wherever R starts and however R moves. On T1, C starts at h. Challenge your partner to escape.

## figure
graph(T1, T1_ROADS, 96, 110, label='T1', sides={'f': 'left', 'g': 'left'}) + graph(T2, T2_ROADS, 96, 151, label='T2', sides={'c': 'below-left'}) + lines(239, 1)

## key
Both maps are trees. C can start anywhere and repeatedly take the first edge of the unique path toward R. On T1, C must start at h, the end of the bent branch c--f--g--h. A robber that starts on f or g can then run ahead of C into the row and choose a side; C keeps walking toward R and traps it at the end of that side. From h the guarantee is five cop moves, the five roads from h to a or e. On T2, C chooses its start; from c it catches within two cop moves. The printed task asks for a guaranteed strategy, not the fastest count.

For the general reason, delete C's dot and shade the connected component containing R. C's next move goes into that component. Unless it captures R, deleting the new C dot leaves R in a strict subset of the former component. R's reply cannot leave this subset without crossing C. Repeated strict shrinking in a finite graph forces capture. Merely saying the distance decreases is insufficient: R can move away and restore the distance for a while. The territory cut off by C, not the current distance alone, is what accumulates.
