+++
id = "w31.ray-groups"
title = "Groups of dots on one straight line from O"
grades = ["2-3", "4-5"]
route = "return"
kernel = 'The dots on one ray from O are the multiples of its first dot, so every target belongs to exactly one group.'
+++

## prompt [2-3]
Which dots lie on the same straight line from O as (1, 1)? Make groups for (1, 1), (2, 1), (3, 2), (1, 2) and (1, 0).

## prompt [4-5]
List all the targets (a, b) whose two coordinates are each from 1 through 6 that have the same first visible dot as (6, 4). Repeat for (6, 3) and (6, 6). Explain why no target can belong to two different groups.

## figure [2-3]
draw(('dots', 3, 3, 6, 2), ('ruled', 19, 4))

## figure [4-5]
draw(('dots', 3, 3.5, 6, 2), ('ruled', 19, 4))

## key [2-3]
\emph{Print guide, p. 3.} Excluding O, the five groups on the 0-6 grid are:\\
(1,1): (1,1), (2,2), (3,3), (4,4), (5,5), (6,6).\\
(2,1): (2,1), (4,2), (6,3).\\
(3,2): (3,2), (6,4).\\
(1,2): (1,2), (2,4), (3,6).\\
(1,0): (1,0), (2,0), (3,0), (4,0), (5,0), (6,0).\\
These are all positive multiples of the named first point that fit in the grid.

## key [4-5]
\emph{Print guide, p. 4.} For (6,4), the group is \{(3,2), (6,4)\}. For (6,3), it is \{(2,1), (4,2), (6,3)\}. For (6,6), it is \{(1,1), (2,2), (3,3), (4,4), (5,5), (6,6)\}. Each nonzero target determines one ray and that ray has one first lattice point, so the groups are disjoint.
