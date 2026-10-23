+++
id = "w55.four-totals"
title = "Every two-card B with exactly four totals"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'Against $A=\{0,3,6\}$, a two-card B gives the minimum $3+2-1=4$ totals exactly when its gap is 3: seven choices from 0--9.'
+++

## prompt @0
Keep A fixed. Find every two-card B from 0--9 that gives exactly four different totals.

## text
\cards{9}{23}{A}{0,3,6}
\foreach \y in {45,70,95,120} {
  \cards{9}{\y}{B}{\phantom{0},\phantom{0}}
  \txt{47}{\y+1}{70}{\small Totals:}
  \draw (47,\y+13)--(116,\y+13);
  \cards{136}{\y}{B}{\phantom{0},\phantom{0}}
  \txt{174}{\y+1}{65}{\small Totals:}
  \draw (174,\y+13)--(239,\y+13);
}
\lane{9}{151}
