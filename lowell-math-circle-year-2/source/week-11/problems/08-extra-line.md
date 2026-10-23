+++
id = "w11.extra-line"
title = "Order on the board with an extra line"
grades = ["2-3", "4-5"]
route = "return"
kernel = "With the A-C line, A and C need 3 chips and B still needs 2; some finishes change, but every legal order from a start still agrees."
+++

## prompt [2-3]
Finish each start. Find another order wherever a choice is possible. After stopping, compare the final piles and count each letter in the sharing words.

## prompt [4-5]
Finish each start in two different orders, if possible. After stopping, compare the final piles and count each letter in the sharing words. Does the extra line change your conclusion about order?

## figure [2-3]
extra_line_23()

## figure [4-5]
extra_line_45()

## key [2-3]
On the extra-line board, A and C have degree 3, while B has degree 2. The complete answer rows are:
\begin{center}\begin{tabular}{llll}\toprule Start & Finish & Shares at each circle & One legal order\\\midrule
$(3,0,3)$ & $(2,0,2)$ & $(1,1,1)$ & ACB\\
$(0,6,0)$ & $(2,0,2)$ & $(1,4,1)$ & BBBACB\\
$(2,2,2)$ & $(2,0,2)$ & $(1,2,1)$ & BACB\\
$(4,1,2)$ & $(2,1,0)$ & $(2,2,2)$ & ABCABC\\
\bottomrule\end{tabular}\end{center}
Alternative legal orders, in the same row order, are CAB, BBBCAB, BCAB, and ACBABC. The added line changes thresholds and some finishes, but not the order-independence conclusion.

## key [4-5]
Extra-line answers: $(3,0,3)\to(2,0,2)$ with counts $(1,1,1)$; $(0,6,0)\to(2,0,2)$ with counts $(1,4,1)$; $(4,1,2)\to(2,1,0)$ with counts $(2,2,2)$. Orders from page 9 give two trials for each. Legal order still changes neither record.

## hints [2-3]
Before the first trial, let the child point to every destination for A's three outgoing chips. If they fire A at two chips, ask for a chip to match its third line.
