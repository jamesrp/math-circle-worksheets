+++
id = "w51.fill-nine"
title = "Every whole-unit pair that fills 9"
grades = ["K-1", "2-3"]
route = "return"
kernel = "An exact total links the strips: B = 9 - A, so each whole A gives one pair, kept only if B fits its card."
+++

## prompt
A and B must fill 9 units exactly. Find every pair of whole-unit lengths that fits both cards.

## figure
band(12,47,4,6,'A')+band(12,91,3,5,'B')+nine_boards()

## key
With A from 4 to 6, B from 3 to 5, whole-unit lengths, and total 9, the complete list of ordered pairs (A,B) is \textbf{(4,5), (5,4), (6,3)}. These exhaust the three possible whole values of A, and each corresponding B=9-A fits its card. The exact-sum condition links the strips.
