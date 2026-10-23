+++
id = "w31.one-and-two-blockers"
title = "Every target with exactly one or exactly two blockers"
grades = ["K-1", "2-3"]
route = "return"
kernel = 'On the 0-6 grid, exactly one blocker means a greatest common factor of 2 (nine targets), exactly two means 3 (five targets).'
+++

## prompt [K-1]
Find every target with exactly one dot between it and O. Then find every target with exactly two.

## prompt [2-3]
Find all targets on this grid with exactly one blocker. Then find all targets with exactly two blockers.

## figure [K-1]
draw(('dots', 3, 4, 6, 2), ('ruled', 20, 3))

## figure [2-3]
draw(('dots', 3, 3, 6, 2), ('ruled', 19, 4))

## key [K-1]
\emph{Print guide, p. 2.} Exactly one blocker: (0,2), (2,0), (2,2), (2,4), (2,6), (4,2), (4,6), (6,2), (6,4). Exactly two: (0,3), (3,0), (3,3), (3,6), (6,3). Their gcds are 2 and 3 respectively. Use thread to check; children need not write these coordinate lists. An adult can write on the lines, or a child who does not write can mark the two kinds of target in two colours on the grid.

## key [2-3]
\emph{Print guide, p. 3.} The two complete target lists are exactly K P3 on page 2, including axis points. ``One blocker'' means gcd 2, not just ``both coordinates even'': (4,4) has three blockers and (6,6) has five.
