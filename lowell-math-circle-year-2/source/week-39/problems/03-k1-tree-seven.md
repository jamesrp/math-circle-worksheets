+++
id = "w39.k1-tree-seven"
title = "Seven-step trips on the tree"
grades = ["K-1"]
route = "return"
kernel = 'Every seven-step trip from A to E shortens to A$\to$B$\to$D$\to$E, and every one from C to F to C$\to$B$\to$D$\to$F: the simple paths in the tree.'
+++

## prompt @27
Make a seven-step trip from A to E and a seven-step trip from C to F. Replay each one, removing out-and-back pairs until none remain.

## figure
graph(36, 77, 32, TREE, TEDGES) + blank(16, 162, 180, 90)

## key
Example seven-step A-to-E trip: ABABDFDE, reducing to ABDE. Example seven-step C-to-F trip: CBABDEDF, reducing to CBDF. Any valid constructions have these same respective reduced routes, the unique simple paths in the tree.
