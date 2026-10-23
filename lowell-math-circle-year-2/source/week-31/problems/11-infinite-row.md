+++
id = "w31.infinite-row"
title = "A row with infinitely many visible dots"
grades = ["2-3"]
route = "return"
page = "same"
kernel = 'Every dot (x, 1) is visible: a point between O and it would have height strictly between 0 and 1.'
+++

## prompt @14
A grid continues as far as you like. Give a row containing infinitely many visible dots, and explain why each one is visible.

## figure
draw(('ruled', 17, 6))

## key
\emph{Print guide, p. 3.} Row y=1 has infinitely many visible dots (x,1) for $x\geq0$. Every interior point of the segment to (x,1) has height strictly between 0 and 1, so cannot be a lattice point. This is an exact geometric proof, not an inference from a finite row.
