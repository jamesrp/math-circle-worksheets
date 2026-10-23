+++
id = "w51.card-for-b"
title = "A card for B that keeps the join in 7 to 9"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "With A in [3,4], B's card must start at least 4 (A might be 3) and end at most 5 (A might be 4), so [4,5] is the unique widest safe card."
+++

## prompt [K-1]
Pick a card for B so the join always reaches 7 and fits within 9. Try to break your choice with different allowed strips.

## prompt
A is 3 to 4 units long. Make a range card for B so every join reaches 7 and fits within 9. Make B's allowed range as wide as possible, and explain why it cannot be wider.

## figure [K-1]
k1_b_cards()

## figure
band(12,50,3,4,'A')

## text @12,97 size=13 [2-3, 4-5]
B:

## figure [2-3, 4-5]
target_card()

## text @12,222 size=11 [K-1]
Fitting within 9 includes ending at 9.

## key
Choose \textbf{B from 4 to 5}. With A from 3 to 4, all sums then lie in [7,9]. K-1's 3-4 card fails at 3+3=6; its 5-6 card fails at 4+6=10. In the older task, B's lower endpoint must be at least 4, because A might be 3; B's upper endpoint must be at most 5, because A might be 4. Hence [4,5] is the unique widest interval.
