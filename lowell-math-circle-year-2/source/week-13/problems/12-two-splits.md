+++
id = "w13.two-splits"
title = "Splits with two cut arrows and an arrow back"
grades = ["4-5"]
route = "first"
kernel = "Every route leaves the Start side at a first exit through an outgoing cut arrow, so closing the outgoing cut arrows stops travel; arrows pointing back do not count."
+++

## prompt
Split the dots into two sides, with Start on one side and Finish on the other. The arrows pointing from the Start side to the Finish side are called the cut arrows. Find two different splits with exactly two cut arrows and at least one arrow pointing back into the Start side. Explain why closing the cut arrows stops all travel.

## figure
two_splits()

## key
Any two of these three start-side sets work. All other dots are on the Finish side. They are the complete list satisfying both requested conditions.
\begin{center}\begin{tabular}{lll}\toprule Start-side set & Outgoing cut arrows & Arrows entering Start side\\\midrule
\{s,A\} & sB, AC & BA\\
\{s,A,B\} & AC, BD & CB\\
\{s,A,B,D\} & AC, Dt & CD, CB\\\bottomrule\end{tabular}\end{center}
Every directed route begins on the Start side and ends outside it, so at its first exit it must use an outgoing cut arrow. Closing all outgoing cut arrows therefore blocks travel. Incoming arrows do not allow an exit and are not counted. A route can later reenter the side, but that cannot avoid its first exit.

## hints
Hint: color the dots by side, then follow each arrowhead across the color boundary.
