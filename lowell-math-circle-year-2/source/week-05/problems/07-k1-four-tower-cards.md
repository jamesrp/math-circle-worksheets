+++
id = "w05.k1-four-tower-cards"
title = "Four towers: a row for each card, or an X"
grades = ["K-1"]
route = "return"
page = "new"
+++

## prompt
Build a row of your four towers that shows the two numbers on each card, and draw it. If no row can, put an X on the card and tell why.

## figure
close(gap(0.3) + pic(place([D.card(4, a, b, box=0.85, pitch=1.05) for a, b in K_CARDS4], 2, 9.0, 5.2)))
