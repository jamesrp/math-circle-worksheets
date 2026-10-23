+++
id = "w05.k1-three-tower-cards"
title = "A row for each card, or an X"
grades = ["K-1"]
route = "first"
page = "new"
+++

## prompt
Build a row of your three towers that shows the two numbers on each card, and draw it. If no row can, put an X on the card and tell why.

## figure
close(gap(0.3) + pic(place([D.card(3, a, b, box=1.0, pitch=1.25) for a, b in K_CARDS3], 2, 9.0, 4.9)))
