+++
id = "w31.rows"
title = "Visible and hidden dots in each row"
grades = ["K-1"]
route = "return"
kernel = 'In every row above O the dot (1, y) is visible; row 1 has only visible dots, so no row has only hidden dots.'
+++

## prompt
Find a visible dot in each row above O and a row with only visible dots. Can you also find a hidden dot in every row?

## figure
draw(('dots', 3, 4, 6, 2), ('ruled', 20, 3))

## key
\emph{Print guide, p. 2.} In each positive row y, (1,y) is visible. Row y=1 contains only visible dots, including (0,1), so there cannot be a hidden dot in \emph{every} positive row. Each row y=2,...,6 does have a hidden dot (0,y).
