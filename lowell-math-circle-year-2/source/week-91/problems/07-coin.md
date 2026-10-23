+++
id = "w91.coin"
title = "A coin against the switch"
grades = ["2-5"]
route = "return"
kernel = "A coin can make every word, including XX; the switch makes only the two alternating words, so balance is not randomness."
+++

## figure
head('Grades 2--5')

## prompt @15,31
Make a second way to choose exits: toss a coin for each counter, sending heads to X and tails to Y. Compare 12 coin choices with 12 arrivals from the one-switch board.

## figure
strip(15,88,12,15,'Coin')+strip(15,135,12,15,'Switch')

## text @15,184 w=186 size=14
Find a six-counter arrival order that the coin could make but the switch could never make. Could the coin make every order that the switch can make?

## figure
strip(15,230,6,15,'')
