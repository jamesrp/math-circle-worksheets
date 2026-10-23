+++
id = "w87.card-vote-rules"
title = "Card-vote rules and the D/E example"
kind = "setup"
grades = ["2-5"]
route = "first"
+++

## text @18,29 size=11
Keep the voter cards unchanged. For each pair, each voter chooses the higher of the two letters on their card. Put that voter's token beside their choice. More votes wins.

## figure
t(18, 52, 'Pair on offer: D and E', size=10) + cards(18, 61, ['DFE', 'EFD', 'FED'], 16, 38, 2) \
+ t(77, 61, 'Chosen from D/E', 51, 9) + t(80, 73, r'V1 $\to$ D\\V2 $\to$ E\\V3 $\to$ E', 40, 11) \
+ t(137, 61, 'All three votes', 60, 9) + tally(137, 70, ['D', 'E'], [['V1'], ['V2', 'V3']]) + t(140, 101, 'E wins, 2 to 1', 55, 10)
