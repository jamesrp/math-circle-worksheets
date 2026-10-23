+++
id = "w31.rows"
title = "A row of visible dots, and a row of hidden dots?"
grades = ["K-1"]
route = "return"
kernel = 'Row 1 has only visible dots; no row has only hidden dots, since (1, y) is visible in every row.'
+++

## prompt
Find a row where every dot is visible. Is there a row where every dot is hidden?

## figure
draw(('dots', 3, 4, 6, 2), ('ruled', 20, 3))

## key
\emph{Print guide, p. 2.} Row y=1 is the only row where every dot is visible, from (0,1) to (6,1). Row 0 has the hidden dot (2,0), and each row y=2,...,6 has the hidden dot (0,y). No row is all hidden, since (1,y) is visible in every row, including (1,0). A child who turns the board may find column x=1, which is also all visible.
