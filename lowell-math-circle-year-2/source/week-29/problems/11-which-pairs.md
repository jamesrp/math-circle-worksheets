+++
id = "w29.which-pairs"
title = "Which pairs from 2, 3, 4 and 5 build every target 6 through 12"
grades = ["K-1"]
route = "return"
kernel = 'Of the six pairs, only 2 and 3, 2 and 5, and 3 and 4 build every target from 6 through 12.'
+++

## prompt
Choose two rod lengths from 2, 3, 4 and 5. Which pairs can build every target from 6 through 12?

## figure
draw(('rodkey', [2, 3, 4, 5], 2), ('targets', range(6, 13), 4, 7), ('ruler', 0, 7, 12), ('ruler', 0, 11, 12), ('ruled', 16, 6))

## key
\emph{Print guide, p. 2.} Exactly \{2,3\}, \{2,5\}, \{3,4\} cover every target 6-12. For \{2,3\}, use 2-rods for even targets and one 3 plus 2-rods for odd targets. For \{2,5\}, do the same with one 5 for odd targets. The failures are \{2,4\}: 7,9,11; \{3,5\}: 7; \{4,5\}: 6,7,11. This checks all six distinct pairs.
