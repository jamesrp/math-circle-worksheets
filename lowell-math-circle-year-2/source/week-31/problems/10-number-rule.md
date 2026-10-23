+++
id = "w31.number-rule"
title = "A number rule for visible dots"
grades = ["2-3"]
route = "return"
kernel = 'A dot is visible exactly when its coordinates have no common factor larger than 1; dividing by a common factor gives a smaller step along the same thread.'
+++

## prompt
Find a number rule that predicts whether a dot is visible from O. Use it to predict (12, 8), (10, 7), (15, 5) and (11, 1). Explain how the rule matches a straight thread.

## figure
draw(('ruled', 3, 8))

## key
\emph{Print guide, p. 3.} A dot is visible exactly when the two coordinates have no common divisor greater than 1. Thus (12,8) is hidden (first point (3,2), three blockers); (10,7) is visible; (15,5) is hidden (first (3,1), four blockers); (11,1) is visible. Dividing both coordinates by a common divisor gives a smaller step in the same straight direction. The converse needs the reasoning on page 4.
