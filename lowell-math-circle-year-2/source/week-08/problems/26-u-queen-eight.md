+++
id = "w08.u-queen-eight"
title = "The queen game on the 8-by-8 board"
grades = ["4-5"]
route = "return"
page = "new"
+++

## text
\noindent\begin{minipage}[t]{4.7in}\vspace{0pt}\raggedright

## prompt
In a new game, the token may also slide diagonally down and to the left, one or more
squares. Color every square of this 8-by-8 board except the star: green if the first
player can always win when the token starts there, red if the second player can
always win.

## text
\end{minipage}\hfill\begin{minipage}[t]{1.9in}\vspace{0pt}\raggedleft

## figure
queen_moves_picture(0.34)

## text
\end{minipage}

\vspace{0.3in}

## figure
centered(board(8, 0.6))
