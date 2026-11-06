+++
id = "w24.fixed-maxima"
title = "Keep 9, 8 and 7; place 1 to 6"
grades = ["2-3", "4-5"]
route = ["first", "return"]
kernel = "Exactly three arrangements make the cycle: Problem 1's decks, (1,5,9), (3,4,8), (2,6,7), and (2,3,9), (1,6,8), (4,5,7)."
+++

## prompt [2-3]
Keep 9 in A, 8 in B, and 7 in C. Place cards 1 to 6 so A wins more pairs than B, B more than C, and C more than A. Find two arrangements different from Problem 1.

## prompt [4-5]
Keep 9 in A, 8 in B, and 7 in C. Use cards 1 to 6 once each to finish the decks so A wins more than half its pairs against B, B against C, and C against A. Find every arrangement and explain why none are missing.

## figure [2-3]
art(pool(list(range(1,7)),7.7), decks([('A',[None,None,9]),('B',[None,None,8]),('C',[None,None,7])],5.95))

## figure [4-5]
art(pool(list(range(1,7)),7.5), decks([('A',[None,None,9]),('B',[None,None,8]),('C',[None,None,7])],5.75))
