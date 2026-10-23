+++
id = "w76.catch-repeating-strips"
title = "Catch the repeating AB and ABBA strips"
grades = ["3-5"]
route = "return"
page = "new"
kernel = "A repeating strip can pass every short ban yet hold a piece that decodes to ABABA or BABAB."
+++

## text
\promptat{0}

## prompt
One strip repeats AB forever. Another repeats ABBA forever. For each strip, find a finite piece that cannot occur in any row grown from A. Explain why your piece is impossible.

## text
\Strip{7}{38}{A,B,A,B,A,B,A,B,A,B,A,B,A,B,A,B}{9}
\node[anchor=west,font=\Large,inner sep=0pt] at (155,42.5) {$\cdots$};
\Strip{7}{108}{A,B,B,A,A,B,B,A,A,B,B,A,A,B,B,A}{9}
\node[anchor=west,font=\Large,inner sep=0pt] at (155,112.5) {$\cdots$};
