+++
id = "w24.k1-advantage-game"
title = "Choose the deck with the advantage and play"
grades = ["K-1"]
route = "return"
kernel = "Against A choose C, against B choose A, against C choose B; each chosen deck wins a round with chance 5/9, but it need not win more of six rounds."
+++

## prompt
Your partner takes A. Choose a deck that wins more card pairs against it, write its letter in the box, and play six rounds. Do the same for B and C. Must your chosen deck win more rounds?

## figure
art(ktracks([('A',None),('B',None),('C',None)],8.3,2.4))
