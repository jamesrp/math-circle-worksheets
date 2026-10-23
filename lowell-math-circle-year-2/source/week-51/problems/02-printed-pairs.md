+++
id = "w51.printed-pairs"
title = "Which pairs keep the promise"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "A promise about a join holds exactly when both extreme joins keep it; one extreme setting defeats it otherwise."
+++

## prompt [K-1]
Try A with B, C with D, and E with F; which pairs always reach 8? Let a friend try to defeat your choices.

## prompt
Try only A with B, C with D, and E with F. Choose a pair whose join always reaches 8 and fits within 10. For each rejected pair, let a partner defeat one promise with allowed lengths.

## figure
printed_pairs()

## text @8,219 w=178 size=11 [K-1]
Reaching 8 includes ending at 8.

## text @8,219 w=178 size=11
Reaching 8 includes ending at 8. Fitting within 10 includes ending at 10.

## key
Use only the three printed row pairs, not arbitrary cross-pairings.\par
\begin{tabular}{llll}\toprule Printed pair & Tight sum & Always reaches 8 & Also fits within 10\\\midrule
A 4-6 with B 3-4 & [7,10] & No: 4+3=7 & Yes\\
C 4-5 with D 4-5 & [8,10] & Yes & Yes\\
E 6-8 with F 2-4 & [8,12] & Yes & No: 8+4=12\\\bottomrule\end{tabular}\par
K-1 asks only about reaching 8, so \textbf{C with D and E with F} both work. Grades 2-3 and 4-5 require both promises, so \textbf{C with D alone} works. Reaching exactly 8 and ending exactly 10 count as successes. The endpoint witnesses in the table defeat the rejected guarantees.
