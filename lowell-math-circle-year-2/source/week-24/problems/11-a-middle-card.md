+++
id = "w24.a-middle-card"
title = "Choose A's middle card"
grades = ["2-3"]
route = "return"
kernel = "With A = (2,x,9), only x = 2 or x = 4 keeps all three 5-to-4 advantages; 0 loses A over B, and 9 or 10 loses C over A."
+++

## prompt
Choose 0, 2, 4, 9, or 10 for A's empty card. Find every choice that makes A win more pairs than B, B more than C, and C more than A.

## figure
art(decks([('A',[2,None,9]),('B',[1,6,8]),('C',[3,5,7])],7.8), pool([0,2,4,9,10],6.05))
