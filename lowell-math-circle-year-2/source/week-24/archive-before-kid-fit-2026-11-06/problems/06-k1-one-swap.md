+++
id = "w24.k1-one-swap"
title = "One swap between A and B"
grades = ["K-1"]
route = "return"
kernel = "Exactly the five swaps in which A gives away a card bigger than the one it receives make B win: (2,1), (4,1), (9,1), (9,6), (9,8)."
+++

## prompt
Swap one A card with one B card. Find every swap that makes B win more card pairs than A. Start each swap from these decks.

## figure
art(kdeck('A',[2,4,9],7.9), kdeck('B',[1,6,8],6.45))
