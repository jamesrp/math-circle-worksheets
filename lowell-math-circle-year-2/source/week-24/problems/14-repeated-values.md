+++
id = "w24.repeated-values"
title = "A cycle with repeated values"
grades = ["4-5"]
route = "return"
kernel = "Repeated values allow cycles such as A = (1,4,4), B = (3,3,3), C = (2,2,5), winning 6, 6 and 5 of 9."
+++

## prompt
Write numbers from 1 to 6 on these nine cards. A number may repeat within one deck, but it cannot appear in two different decks. Make A win more than half its pairs against B, B against C, and C against A.

## figure
art(decks([('A',[None]*3),('B',[None]*3),('C',[None]*3)],7.65))
