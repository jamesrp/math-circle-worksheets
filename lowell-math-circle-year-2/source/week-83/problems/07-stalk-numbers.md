+++
id = "w83.stalk-numbers"
title = "Which card is each stalk?"
grades = ["2-5"]
route = "return"
page = "new"
kernel = "A stalk's number is the earliest card between the numbers Blue's cuts leave and those Red's cuts leave: BR is 1/2, BRR is 1/4, RB is -1/2."
+++

## text
\begin{sheet}

## prompt
An empty board is 0, B is 1 and R is $-1$. On each mat, put the numbers of the boards Blue's cuts can leave on the left and Red's on the right. Which card is BR? BRR? RB?

## text
\stalkmat{158}{BR}{B,R}{56}
\stalkmat{72}{BRR}{B,R,R}{78}
\stalkmat{8}{RB}{R,B}{56}
\end{sheet}
