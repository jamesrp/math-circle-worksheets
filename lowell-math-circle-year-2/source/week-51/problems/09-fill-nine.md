+++
id = "w51.fill-nine"
title = "Every whole-unit pair that fills 9"
grades = ["K-1", "2-3"]
route = "return"
kernel = "An exact total links the strips: B = 9 - A, so each whole A gives one pair, kept only if B fits its card; A = 3 and A = 7 fail."
+++

## prompt
A and B must fill 9 units exactly. Find every pair of whole-unit lengths that fits both cards.

## figure
band(12,44,3,7,'A')+band(12,84,3,5,'B')+nine_boards()

## key
With A from 3 to 7, B from 3 to 5, whole-unit lengths, and total 9, the complete list of ordered pairs (A,B) is \textbf{(4,5), (5,4), (6,3)}. A=3 would need B=6 and A=7 would need B=2, both off B's card; for A=4, 5 and 6, B=9-A fits its card. Four boards are printed for three pairs, so the child decides when the list is complete. The exact-sum condition links the strips.
