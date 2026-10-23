+++
id = "w43.changed-start"
title = "A different starting row"
grades = ["2-3", "4-5"]
route = { "2-3" = "return", "4-5" = "first" }
page = { "4-5" = "same" }
kernel = "Every target order still has exactly one story from any start: choose where its first card is, then its second."
+++

## prompt @0 [2-3]
Start with B A C and use the same two-swap rule. Can you still make every row? Find the ticket story for each target.

## prompt @15 [4-5]
Start with C B A instead. Explain whether the chance of each final order changes, without listing every story again.

## figure [2-3]
bac_targets()

## figure [4-5]
start_row_and_lines('CBA', 18, 3)

## key [2-3]
Starting with BAC changes the target-to-ticket correspondence, but all six rows remain possible and equally likely.\par
\begin{tabular}{llll}\toprule Target & Ticket story & Target & Ticket story\\\midrule
ABC & (2,2) & ACB & (2,3)\\
BAC & (1,2) & BCA & (1,3)\\
CAB & (3,2) & CBA & (3,3)\\\bottomrule\end{tabular}

## key [4-5]
Every order still has chance 1/6 from CBA. Relabel A and C throughout the original experiment: its start becomes CBA, the allowed ticket histories and their weights do not change, and the output labels are permuted bijectively. Alternatively, for any target choose its first card from the three current slots, then its second from the two remaining slots; this determines a unique story regardless of the starting order.
