+++
id = "w31.rows-and-99"
title = "A visible row, an infinite hidden set, 99 blockers"
grades = ["4-5"]
route = "return"
page = "same"
kernel = 'Row 1 is entirely visible, the diagonal (n, n) for n at least 2 is hidden behind (1, 1), and (100, 100) has exactly 99 blockers.'
+++

## prompt @14
Find an entire row of visible dots, an infinite collection of hidden dots, and a target with exactly 99 blockers. Explain each choice.

## figure
draw(('ruled', 17, 6))

## key
\emph{Print guide, p. 4.} Row y=1 is fully visible by the height argument on page 3. The points (n,n), $n\geq2$, form an infinite hidden collection, all behind (1,1). Target (100,100) has exactly 99 blockers, (k,k) for k=1,...,99; (100,0) is another valid example.
