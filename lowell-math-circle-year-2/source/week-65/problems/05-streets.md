+++
id = "w65.streets"
title = "Two streets through P"
grades = ["3-5"]
route = "return"
kernel = "Two complete straight streets through P both miss the street R, which two ordinary straight lines through one point cannot do."
+++

## text @.65,10.13
A complete street goes straight through every crossing, taking the opposite branch. Streets continue forever. The dotted circle is the edge of the map; no number of moves reaches it. Only some streets are drawn.

## prompt @.65,8.99
Trace every drawn complete street through P in both directions. How many miss the heavy dashed street R? Can two different ordinary straight lines through one point both miss a third line? The ordinary lines also continue forever in both directions. Draw or explain below.

## figure
streets_board(r_at=(-0.66, 0))   # on R's mirror axis, nearer R than any other street (card could 5)
