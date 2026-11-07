+++
id = "w24.six-and-four-card-chances"
title = "Six-card and four-card chances"
grades = ["4-5"]
route = "return"
kernel = "Doubling every card keeps A's chance against B at 20/36 = 5/9; the four-card decks give A over B 10/16, B over C 7/16 and C over A 10/16, so B no longer beats C."
+++

## prompt
Find A's chance of beating B with the six-card decks. Then find each deck's chance of winning against each other deck with the four-card decks. Which chances changed from Problem 2?

## figure
art(decks([('A',[2,2,4,4,9,9]),('B',[1,1,6,6,8,8])],7.6), decks([('A',[2,2,4,9]),('B',[1,1,6,8]),('C',[3,3,5,7])],4.7))
