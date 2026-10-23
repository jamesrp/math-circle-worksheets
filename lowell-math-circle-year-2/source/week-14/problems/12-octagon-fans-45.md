+++
id = "w14.octagon-fans-45"
title = "Fewest flips to two octagon fans"
grades = ["4-5"]
route = "return"
kernel = "From the printed octagon filling the fans at A and E need 3 and 5 flips, the number of their diagonals missing at the start."
+++

## prompt
A filling whose inside lines all meet at one corner is called a fan. Find the fewest flips from this filling to a fan at A, and to a fan at E. Explain why each route is shortest.

## figure
large_plus_copies(8,oct_start,'letters',topcy=4.4,copyy=7.7)

## key
The printed start is $S=\{AC,AD,DF,DG,DH\}$. A fan at A has five diagonals $\{AC,AD,AE,AF,AG\}$; a fan at E has $\{AE,BE,CE,EG,EH\}$. The minimum distances are 3 and 5, respectively. Three-flip route to the A fan
\begin{center}\begin{tabular}{rll}\toprule Step & Diagonals in the filling & Change just made\\\midrule
0 & AC, AD, DF, DG, DH & Start\\
1 & AC, AD, AG, DF, DG & DH $\to$ AG\\
2 & AC, AD, AF, AG, DF & DG $\to$ AF\\
3 & AC, AD, AE, AF, AG & DF $\to$ AE\\
\bottomrule\end{tabular}\end{center}
Five-flip route to the E fan
\begin{center}\begin{tabular}{rll}\toprule Step & Diagonals in the filling & Change just made\\\midrule
0 & AC, AD, DF, DG, DH & Start\\
1 & AC, AD, DG, DH, EG & DF $\to$ EG\\
2 & AC, AD, DH, EG, EH & DG $\to$ EH\\
3 & AC, AD, AE, EG, EH & DH $\to$ AE\\
4 & AC, AE, CE, EG, EH & AD $\to$ CE\\
5 & AE, BE, CE, EG, EH & AC $\to$ BE\\
\bottomrule\end{tabular}\end{center}
Optimality certificates. The start already has two of A's five diagonals and none of E's five. Each flip can add at most one target diagonal. Therefore at least $5-2=3$ and $5-0=5$ flips are required. Both tables achieve their lower bounds, always adding a target diagonal and never deleting one. The eight new pictures in the two routes fit the eight provided recording copies if the printed start is reused.

## hints
Ask the child to choose a target corner and point to every diagonal already meeting it. If a proposed flip removes one of those, ask whether a different choice can increase the count instead. The general reason that such a choice exists is on page 11.
