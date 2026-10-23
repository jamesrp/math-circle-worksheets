+++
id = "w14.fewest-flips-23"
title = "Fewest flips between two hexagon fans"
grades = ["2-3"]
route = "return"
kernel = "Each flip adds at most one target diagonal, so a target with all three diagonals missing needs at least three flips, and three suffice."
+++

## prompt
Change the first filling into the second using as few flips as you can. Find another route with a different number of flips, without visiting any filling twice.

## figure
hexagon_route_23()

## key
The printed start is the B fan $\{BD,BE,BF\}$ and the target is the A fan $\{AC,AD,AE\}$. The minimum is three flips. Here is one shortest route, read left to right:
\begin{center}\begin{tabular}{rll}\toprule Step & Diagonals in the filling & Change just made\\\midrule
0 & BD, BE, BF & Start\\
1 & AE, BD, BE & BF $\to$ AE\\
2 & AD, AE, BD & BE $\to$ AD\\
3 & AC, AD, AE & BD $\to$ AC\\
\bottomrule\end{tabular}\end{center}
Why three is best. None of the three target diagonals is present initially. One flip adds only one diagonal, so at least three flips are necessary. The displayed route achieves three. Counting missing target diagonals is a lower bound for arbitrary targets; it is always attainable for a fan target (page 11). A different simple route has four flips. The following five pictures are all different, so this meets the revised requirement to avoid visiting a filling twice.
\begin{center}\begin{tabular}{rll}\toprule Step & Diagonals in the filling & Change just made\\\midrule
0 & BD, BE, BF & Start\\
1 & BE, BF, CE & BD $\to$ CE\\
2 & AE, BE, CE & BF $\to$ AE\\
3 & AC, AE, CE & BE $\to$ AC\\
4 & AC, AD, AE & CE $\to$ AD\\
\bottomrule\end{tabular}\end{center}
Check the actual move. Two diagonal lists of length three are flip neighbors when they share exactly two diagonals. Merely rotating a page is not a move; nor may the child replace two diagonals at once.

## hints
For the shortest route, ask which target lines are missing and how many can appear in one move. For the second route, try a different first move. Undoing and redoing a move does not satisfy the no-repeated-fillings instruction.
