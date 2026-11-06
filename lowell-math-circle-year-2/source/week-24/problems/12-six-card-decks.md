+++
id = "w24.six-card-decks"
title = "Two copies of every card, or of some"
grades = ["2-3"]
route = "return"
kernel = "Doubling every card multiplies every pair count by four (A over B 20 of 36), so no winner changes; the four-card decks (2,2,4,9), (1,1,6,8), (3,3,5,7) give A over B 10 of 16 and C over A 10 of 16, but C now beats B 9 to 7."
+++

## prompt
How many possible card pairs does A win against B with the six-card decks, and how many does B win? Then find which deck wins more pairs in each comparison of the four-card decks. Does any winner change from Problem 2?

## figure
art(decks([('A',[2,2,4,4,9,9]),('B',[1,1,6,6,8,8])],7.65), decks([('A',[2,2,4,9]),('B',[1,1,6,8]),('C',[3,3,5,7])],4.75))
