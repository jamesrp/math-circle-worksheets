+++
id = "w11.batch-timing-45"
title = "Batches together or one at a time"
grades = ["4-5"]
route = "first"
kernel = "Adding two batches together, or finishing one before adding the other, ends at the same finish: S(S(x)+y) = S(x+y)."
+++

## prompt
Start empty. For each pair of batches, compare adding them together with finishing one before adding the other. Try both batch orders. Does the timing of additions change the finish?

## figure
batches_45()

## key
Together, first batch then second, and second then first all give the same finish for each row group:
\begin{center}\begin{tabular}{llll}\toprule
Batches & Together & First then second & Second then first\\\midrule
4 at B; 2 at A&$(1,1,1)$&$(1,1,1)$&$(1,1,1)$\\
3 at A; 3 at C&$(1,0,1)$&$(1,0,1)$&$(1,0,1)$\\\bottomrule\end{tabular}\end{center}
For the first pair, intermediate finishes are $(1,0,1)$ or $(0,1,0)$, as appropriate. For the second pair, $(3,0,0)\to(1,1,0)$, then $(1,1,3)\to(1,0,1)$; reversing A/C gives $(0,1,1)$ then $(3,1,1)\to(1,0,1)$. This does not claim the intermediate states agree.

## hints
Compare only after the same total additions have arrived and sharing is finished.
