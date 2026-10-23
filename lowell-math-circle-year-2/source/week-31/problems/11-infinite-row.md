+++
id = "w31.infinite-row"
title = "A row where every dot is visible"
grades = ["2-3"]
route = "return"
page = "same"
kernel = 'Row 1 is the only row where every dot is visible: a point between O and (x, 1) would have height strictly between 0 and 1.'
+++

## prompt @14
A grid continues as far as you like. Give a row where every dot is visible, and explain why each one is visible.

## figure
draw(('ruled', 17, 6))

## key
\emph{Print guide, p. 3.} Row y=1: every dot (x,1), $x\geq0$, is visible. Every interior point of the segment to (x,1) has height strictly between 0 and 1, so cannot be a lattice point. This is an exact geometric proof, not an inference from a finite row. It is the only such row: row 0 has the hidden dot (2,0), and each row $y\geq2$ has the hidden dot (0,y). Accept column x=1 as well.
