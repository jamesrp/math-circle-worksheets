+++
id = "w11.termination"
title = "Why sharing must stop on the four-cycle"
grades = ["4-5"]
route = "return"
kernel = "The score W = 3A + 4B + 3C drops by 2 at every legal share on the four-cycle and never goes below zero, so every run stops."
+++

## prompt
Try starts with all 12 chips at B, with 6 at A and 6 at C, and with 4 at each circle. Could any order of sharing continue forever? Explain why sharing must stop for any finite number of chips on this board.

## figure
termination_board()

## key
All three 12-chip starts stop. They happen to share one finish, although their share counts differ:
\begin{center}\begin{tabular}{llll}\toprule Start & Finish & Shares at each circle & Chips in sink\\\midrule
$(0,12,0)$ & $(1,0,1)$ & $(5,11,5)$ & 10\\
$(6,0,6)$ & $(1,0,1)$ & $(5,5,5)$ & 10\\
$(4,4,4)$ & $(1,0,1)$ & $(5,7,5)$ & 10\\
\bottomrule\end{tabular}\end{center}
\textbf{A finite score proves termination on this board.} Give each chip at A or C a score of 3, each at B a score of 4, and each at the sink a score of 0. The total $W=3A+4B+3C$ is a nonnegative integer. An A or C move removes two 3-point chips and creates one 4-point chip, decreasing $W$ by 2. A B move removes two 4-point chips and creates two 3-point chips, also decreasing $W$ by 2. Therefore infinitely many legal moves are impossible. This works for every finite start and every choice of legal moves on the four cycle. The three starts have scores 48, 36, 40; each finishes at score 6, so the total numbers of moves are 21, 15, 17.

## hints
First ask why ``a chip falls into the sink every move'' is false: B does not touch the sink. For a child who wants a numerical certificate, give the 3,4,3 weights and let them test each type of move.
