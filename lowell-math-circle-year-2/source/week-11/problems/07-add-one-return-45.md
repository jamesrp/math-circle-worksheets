+++
id = "w11.add-one-return-45"
title = "Return and merging when adding at A"
grades = ["4-5"]
route = "first"
kernel = "Adding one chip at A and finishing cycles (1,0), (0,1), (1,1) with period three; the empty start never returns, and (0,0) and (1,1) merge after one addition."
+++

## prompt
From each start, repeatedly add one chip to A and finish after each addition. Record the pairs you get. Which starts return to themselves? Can two different starts give the same pair after one addition?

## figure
add_one_45()

## key
The four stable starts have the following A-addition updates:
\begin{center}\begin{tabular}{ccccc}\toprule
Start&After 1&After 2&After 3&After 4\\\midrule
$(0,0)$&$(1,0)$&$(0,1)$&$(1,1)$&$(1,0)$\\
$(1,0)$&$(0,1)$&$(1,1)$&$(1,0)$&$(0,1)$\\
$(0,1)$&$(1,1)$&$(1,0)$&$(0,1)$&$(1,1)$\\
$(1,1)$&$(1,0)$&$(0,1)$&$(1,1)$&$(1,0)$\\\bottomrule\end{tabular}\end{center}
The three nonempty starts return after three additions and then at multiples of three. The empty start never returns. Starts $(0,0)$ and $(1,1)$ merge after one addition at $(1,0)$: the operation cannot be reversed uniquely. The state diagram on page 7 is complete.

## hints
Ask which arrows could be reversed without making a choice. Do not label all stable states a group.
