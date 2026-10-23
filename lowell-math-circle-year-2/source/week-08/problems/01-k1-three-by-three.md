+++
id = "w08.k1-three-by-three"
title = "Two 3-by-3 boards: first or second?"
grades = ["K-1"]
route = "first"
+++

## prompt
Play many games from the dot on each board. Circle if you would rather go first or
second.

## text
\vspace{0.35in}

## figure
grid2([stack(board(3, 1.0, dots=[d]), choice(0.85, 0.42, 0.25), sep="0.2in")
       for d in [(2, 2), (1, 2)]], colw="3.3in")
