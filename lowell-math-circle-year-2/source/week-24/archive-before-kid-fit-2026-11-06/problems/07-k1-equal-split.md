+++
id = "w24.k1-equal-split"
title = "Two decks from 1 to 6 that tie"
grades = ["K-1"]
route = "return"
kernel = "Impossible: two three-card decks give nine pairs, each with one winner, and nine cannot be split equally."
+++

## prompt
Put these six cards into two decks of three so both decks win the same number of pairs. Find a way, or show why it cannot be done.

## figure
art(kpool(list(range(1,7)),7.9), kdeck('A',[None]*3,6.35), kdeck('B',[None]*3,4.9))
