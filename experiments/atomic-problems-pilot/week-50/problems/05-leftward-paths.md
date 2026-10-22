+++
id = "w50.leftward-paths"
title = "Paths that may go left"
grades = ["K-1", "2-3"]
route = "return"
scale = "actual"
kernel = "With total leftward travel L (and no downward travel) the length is 280 + 2L mm."
app = "Memory robot / Staircases group, exact-length paths with left steps"
+++

## prompt [K-1]
A path may now go left as well as right and up. Make two different S-to-F paths that use the same amount of string and more than a staircase.

## prompt
Allow leftward pieces as well as rightward and upward pieces. Make two very different S-to-F paths of length 360 mm. Could such a path be shorter than 280 mm? Explain your answer.

## figure [K-1]
diagram(40)

## figure
diagram(45)

## text @10,187 [2-3]
A straight diagonal is 200 mm long.

## figure [2-3]
calibration()

## key
Here are two distinct 360 mm routes, given as right (R), left (L), and up (U) distances in millimeters: \textbf{Route A:} R80, U40, L40, U40, R120, U40. \textbf{Route B:} R120, U90, L40, U30, R80. Both stay in the rectangle, end at F and travel left a total of 40 mm. Each length is $280+2\times40=\textbf{360 mm}$. K-1 needs only two equal longer paths, so these give a complete witness without requiring arithmetic.

## key [2-3]
The last question has the same answer as \emph{A leftward piece and less string} below: no path with a leftward piece is shorter than 280 mm.
