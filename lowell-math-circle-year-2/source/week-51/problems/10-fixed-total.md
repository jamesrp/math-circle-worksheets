+++
id = "w51.fixed-total"
title = "A known total narrows the gap"
grades = ["4-5"]
route = "return"
kernel = "A+B=12 with B in [3,7] forces A into [5,9], so A is in [7,9] and the gap 2A-12 runs from 2 to 6; A=10 is discarded."
+++

## prompt
A is 7 to 10 units and B is 3 to 7 units. You learn that their join is exactly 12 units. Align their starts at 0. Find the smallest and largest possible gap between their ends.

## figure
band(12,53,7,10,'A')+band(12,95,3,7,'B')+rect(12,142,120,14)+label(72,162,'A + B = 12 units',12)

## key
$A\in[7,10]$, $B\in[3,7]$ and A+B=12 imply B=12-A. The B card restricts A to [5,9]; intersecting with A's card gives \textbf{$A\in[7,9]$} and consequently $B\in[3,5]$. Since A is always larger, the end gap is A-B=2A-12, ranging from \textbf{2 to 6}. Witnesses are (A,B)=(7,5) and (9,3). The discarded choice A=10 would require B=2 and is not allowed.
