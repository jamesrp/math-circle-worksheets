+++
id = "w43.k1-two-starts"
title = "One story, two starting rows"
grades = ["K-1"]
route = "return"
page = "same"
kernel = "A fixed swap story can be undone in reverse order, so it never sends two different starts to the same row."
+++

## prompt @18
Start with these two different rows and give both the same two-ticket story. Can they ever finish alike?

## figure
k1_two_starts()

## key
No. A swap is undone by repeating it. If the finishes matched, undoing the shared swaps would recover equal starts, contradicting ABC versus CBA. Here are all six comparisons.\par
\begin{tabular}{lll}\toprule Story & Finish from ABC & Finish from CBA\\\midrule
(1,2) & ABC & CBA\\
(1,3) & ACB & CAB\\
(2,2) & BAC & BCA\\
(2,3) & BCA & BAC\\
(3,2) & CBA & ABC\\
(3,3) & CAB & ACB\\\bottomrule\end{tabular}
