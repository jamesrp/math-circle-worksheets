+++
id = "w11.k1-four-and-five-chips"
title = "Every finish from 4 chips, then from 5"
grades = ["K-1"]
route = "first"
kernel = "Each total of 4 or 5 chips on the triangle reaches exactly the three finishes (1,0), (0,1) and (1,1); listing A = 0 to the total covers every start."
+++

## prompt [K-1]
Put 4 chips altogether on A and B in any way, and share until you must stop. Find every finish; then try 5 chips.

## figure
k1_four_and_five()

## key
Distribute 4 chips altogether, then 5 altogether. Each total has exactly three possible finishes: $(1,0),(0,1),(1,1)$. The following is a complete check, with A increasing by one.
\begin{center}\begin{tabular}{cc|cc}\toprule
4 chip start & Finish & 5 chip start & Finish\\\midrule
$(0,4)$&$(0,1)$&$(0,5)$&$(1,0)$\\
$(1,3)$&$(1,0)$&$(1,4)$&$(1,1)$\\
$(2,2)$&$(1,1)$&$(2,3)$&$(0,1)$\\
$(3,1)$&$(0,1)$&$(3,2)$&$(1,0)$\\
$(4,0)$&$(1,0)$&$(4,1)$&$(1,1)$\\
&&$(5,0)$&$(0,1)$\\\bottomrule\end{tabular}\end{center}
\textbf{Completeness.} A can hold 0 through the total; B must hold the rest. This lists every start, including empty circles. All legal orders from any listed start share its finish. With four or five chips, $(0,0)$ never occurs.

## hints
Keep the same four counters and move one from B to A between trials. Let the child decide how to keep the different finishes.
