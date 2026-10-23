+++
id = "w29.lengths-3-4"
title = "Which lengths 3-rods and 4-rods build"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = 'With 3-rods and 4-rods exactly 1, 2 and 5 are impossible; 6, 7 and 8 plus added 3-rods reach every longer length.'
+++

## prompt @5.7 [K-1]
Which lengths can you build with 3-rods and 4-rods?

## prompt @5.7 [2-3]
Use 3-rods and 4-rods. Find all the lengths from 1 through 16 that can be built, and mark the ones that cannot.

## prompt @5.7 [4-5]
For 3-rods and 4-rods, find every impossible positive length. Explain why your list is complete.

## figure [K-1]
draw(*[('strip', 0, 7.1 + i * 2.05, n) for i, n in enumerate([1, 2, 5, 6, 8, 9, 10])])

## figure [2-3]
draw(('targets', range(1, 17), 8, 8), ('ruler', 0, 13, 16), ('ruler', 0, 17, 16), ('ruled', 21, 2))

## figure [4-5]
draw(('targets', range(1, 21), 8, 7), ('ruled', 14, 9))

## key [K-1]
\emph{Print guide, p. 2.} Of the listed targets, 6=3+3, 8=4+4, 9=3+3+3, 10=3+3+4 work. The targets 1, 2, 5 do not. One rod is too long for 1 or 2; for 5, one rod is too short and two rods total at least 6.

## key [2-3]
\emph{Print guide, p. 3.} In 1-16, only 1,2,5 fail. The certificate 6,7,8 plus added 3-rods covers all later targets.

## key [4-5]
\emph{Print guide, p. 3.} Exactly 1,2,5. Check these small failures and use the three-build certificate above; a long tested list alone does not prove completeness.
