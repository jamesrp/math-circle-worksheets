+++
id = "w24.six-and-four-card-chances"
title = "Six-card and four-card chances"
grades = ["4-5"]
route = "return"
kernel = "Six-card decks keep every chance 20/36 = 5/9; the four-card decks give A over B 10/16, B over C 7/16 and C over A 10/16, so B no longer beats C."
+++

## prompt
Find each deck's chance of winning against each other deck, first with the six-card decks and then with the four-card decks. Which chances changed from Problem 1?

## figure
art(decks([('A',[2,2,4,4,9,9]),('B',[1,1,6,6,8,8]),('C',[3,3,5,5,7,7])],7.6), decks([('A',[2,2,4,9]),('B',[1,1,6,8]),('C',[3,3,5,7])],4.7))
