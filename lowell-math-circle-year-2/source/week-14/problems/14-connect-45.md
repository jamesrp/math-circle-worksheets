+++
id = "w14.connect-45"
title = "Any two fillings are joined by flips"
grades = ["4-5"]
route = "return"
kernel = "Any two fillings of a convex polygon are joined by flips: send both to the same fan and reverse one route."
+++

## prompt
Find a route of flips between these two fillings. Can any two fillings of the same polygon be joined by flips? Explain why your answer works for any polygon with no inward-pointing corners.

## figure
octagon_route_45()

## key
The printed endpoints are $S=\{AC,AD,DF,DG,DH\}$ and $T=\{AE,BD,BE,EG,EH\}$. Here is a five-flip route.
\begin{center}\begin{tabular}{rll}\toprule Step & Diagonals in the filling & Change just made\\\midrule
0 & AC, AD, DF, DG, DH & Start\\
1 & AD, BD, DF, DG, DH & AC $\to$ BD\\
2 & AD, BD, DG, DH, EG & DF $\to$ EG\\
3 & AD, BD, DH, EG, EH & DG $\to$ EH\\
4 & AD, AE, BD, EG, EH & DH $\to$ AE\\
5 & AE, BD, BE, EG, EH & AD $\to$ BE\\
\bottomrule\end{tabular}\end{center}
This route is also shortest, although the problem does not ask for that: the endpoints share no diagonal, so all five target diagonals must be introduced and one move adds at most one. Why any two fillings can be joined. Choose one fixed corner, say A. Page 11's growing-fan procedure turns the first filling into the A fan and the second filling into the same A fan. Reverse the second route and place it after the first. Every reversed flip is legal, since exchanging the two diagonals of a convex quadrilateral is reversible. This gives a route between the original fillings. It need not be shortest. An upper bound, not an exact distance. Passing through one fan uses $(n-3-d_A(S))+(n-3-d_A(T))$ flips. For these endpoints A gives $3+4=7$, while the route above uses 5. This example shows why a connectivity construction should not automatically be called a shortest route.

## hints
If children can reach a fan but cannot connect arbitrary endpoints, ask whether a route can be followed backward. Be explicit that the same target corner must be used for both routes. A route can be recorded on the one working board as a list of changes, such as ``erase AC, draw BD'' from Problem 3's example, with only the final filling drawn.
