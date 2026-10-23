+++
id = "w25.k1-forced-or-not"
title = "When can two different pictures share the counts?"
grades = ["K-1"]
route = "first"
page = "same"             # on page 5 under the end of the problem before it
kernel = "A full or empty row or column can force every cell: two of these three sets of counts fit only one picture, the third fits five."
+++

## prompt @150
Can you make two different pictures for each pair of grids?

## figure
k1_forced_pair()

## key
\emph{Print guide, p. 6.} \textbf{Answers in printed order:} no, no, yes. The solution counts are 1, 1, and 5. A failure to find another picture is not yet a reason that none exists; use the forcing arguments below.

\textbf{Page 5:} row A needs all three cells. Column 1 needs two counters, so B1 is occupied; B2 and B3 must be empty. \textbf{Page 6 top:} row C and column 3 are empty. Column 1 needs two counters, forcing A1 and B1. B is now full, so the remaining counter in column 2 is A2. Each case forces every cell.
