+++
id = "w24.k1-advantage-game"
title = "Choose the deck with the advantage and play"
grades = ["K-1"]
route = "return"
kernel = "Against A choose C, against B choose A, against C choose B; each chosen deck wins a round with chance 5/9, but it need not win more of six rounds."
+++

## prompt
Your partner takes A. Choose a deck that wins more card pairs against it and play six rounds. Do the same for B and C. Must your chosen deck win more rounds?

## figure
art(kdeck('A',[2,4,9],7.9), kdeck('B',[1,6,8],6.5), kdeck('C',[3,5,7],5.1))
