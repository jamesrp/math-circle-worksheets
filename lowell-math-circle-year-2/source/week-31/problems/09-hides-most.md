+++
id = "w31.hides-most"
title = "Which first dot hides the most dots"
grades = ["K-1"]
route = "return"
kernel = 'On the 0-6 grid, (1, 0), (0, 1) and (1, 1) each hide five dots; every other visible dot hides at most two.'
+++

## prompt
Which first dot after O hides the most other dots? Find every first dot that ties for the most.

## figure
draw(('dots', 3, 4, 6, 2), ('ruled', 20, 3))

## key
\emph{Print guide, p. 2.} Three first dots tie: (1,0), (0,1), (1,1). Each hides five dots, its multiples 2 through 6. Every other primitive direction has some coordinate at least 2, so it reaches at most three dots within this grid and hides at most two.
