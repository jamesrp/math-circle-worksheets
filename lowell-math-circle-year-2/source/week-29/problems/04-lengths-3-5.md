+++
id = "w29.lengths-3-5"
title = "Which lengths 3-rods and 5-rods build"
grades = ["K-1", "2-3"]
route = "first"
kernel = 'With 3-rods and 5-rods exactly 1, 2, 4 and 7 are impossible; 8, 9 and 10 plus added 3-rods reach every longer length.'
+++

## prompt [K-1]
Use 3-rods and 5-rods. Which lengths can you build?

## prompt [2-3]
Use 3-rods and 5-rods. Find all the impossible lengths from 1 through 20. Is there a last impossible length?

## figure [K-1]
draw(('rodkey', [3, 5], 1.65), *[('strip', 0, 3.4 + i * 2.6, n) for i, n in enumerate([4, 7, 8, 9, 10, 11, 12])])

## figure [2-3]
draw(('rodkey', [3, 5], 1.9), ('targets', range(1, 21), 4, 7), ('ruled', 10, 11))

## key [K-1]
\emph{Print guide, p. 2.} With 3 and 5, 4 and 7 are impossible. The others work: 8=3+5, 9=3+3+3, 10=5+5, 11=3+3+5, 12=3+3+3+3. For 7, no 5 leaves a multiple of 3: the possible remainders are 7 and 2.

## key [2-3]
\emph{Print guide, p. 3.} The impossible lengths in 1-20 are 1,2,4,7. The last is 7: 8=3+5, 9=3+3+3, 10=5+5, followed by added 3-rods, settle all later targets.
