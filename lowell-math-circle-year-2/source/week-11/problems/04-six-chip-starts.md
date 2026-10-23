+++
id = "w11.six-chip-starts"
title = "Six-chip starts that finish at one and one"
grades = ["2-3"]
route = "first"
kernel = "Of the seven ways to place 6 chips on the triangle, exactly (0,6), (3,3) and (6,0) finish at (1,1); choosing A from 0 to 6 forces B, so the list is complete."
+++

## prompt
Put exactly 6 chips altogether on A and B. Find every start that finishes with one chip at A and one at B. Explain how you know you have found every start that works.

## figure
six_chip_starts()

## key
Exactly three starts of total six finish at $(1,1)$: $(0,6),(3,3),(6,0)$.
\begin{center}\begin{tabular}{cccccccc}\toprule
A initially&0&1&2&3&4&5&6\\
B initially&6&5&4&3&2&1&0\\\midrule
Finish&$(1,1)$&$(0,1)$&$(1,0)$&$(1,1)$&$(0,1)$&$(1,0)$&$(1,1)$\\\bottomrule\end{tabular}\end{center}
\textbf{Why complete.} There are seven possible values of A, 0 through 6. Once A is chosen, B is forced. Checking these seven starts leaves none untested. Order independence means no unsuccessful start can be rescued by a new firing order.

## hints
If the child finds $(3,3)$ and stops, ask whether an empty circle is permitted at the start. If the list is disorganized, ask how one could be certain it includes every possible A pile.
