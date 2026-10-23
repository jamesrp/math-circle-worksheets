+++
id = "w08.k1-winning-move"
title = "The winning move on four 5-by-5 boards"
grades = ["K-1"]
route = "return"
page = "new"
+++

## prompt
It is your turn, and the token is on the dot. Color the square you should move it to
so that you can win.

## text
\vspace{0.3in}

## figure
grid2([board(5, 0.66, dots=[d]) for d in [(0, 3), (3, 1), (2, 4), (4, 3)]], vsep="0.45in")
