+++
id = "w86.folds"
title = "Fold F1 and F2 down"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "A map is cop-win exactly when folds can shrink it to one dot; F1 folds to a dot, F2 sticks at a square."
+++

## prompt @121
Use boards F1 and F2 in the materials packet. Can each map fold down to one dot? Find a sequence of legal folds, or a remaining map with no legal fold. What does this suggest about the chasing game? Keep the original visible. On the working copy, cover each removed dot and its roads with removable opaque pieces. Leave surviving dots and roads visible.

## figure
lines(191, 4)

## key
Materials p.1 supplies F1 and its working copy; p.2 supplies F2 and its working copy. Keep the original visible, but test each fold in the current reduced graph. Staying counts among reachable places. Deleting a dot deletes its incident roads; do not create a replacement road through it.

F1 can fold e into d, then d into c, then f into a. The remaining triangle a,b,c folds a into b, then b into c. Each inclusion can be checked from the actual remaining board. Other legal orders work. Its one-dot reduction certifies that one cop has a strategy.

In F2 only b is initially removable: it can fold into a or c. Either removal leaves the bare square on a,c,d,e. No adjacent pair in a square has one closed neighborhood contained in the other, so no further fold is possible. F2 is robber-win by the projected-square strategy above. A single dead end in an arbitrary search would need justification; here both initial choices produce the same residual square. Children can stop at a checkable fold certificate; understanding the simultaneous real/shadow strategy is an additional readiness gate.
