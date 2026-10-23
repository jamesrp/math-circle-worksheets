+++
id = "w17.k1-try-rows"
title = "Run a two-circle machine on rows of cards"
grades = ["K-1"]
route = "first"
page = "same"
kernel = "The machine says yes exactly when the number of red cards is even."
+++

## prompt @1.78 size=16
Try each row, starting fresh each time, and circle its answer. Make three different six-card rows that finish at \Y.

## figure
two('even',2.6,5.9,3.47,True,labels=True)

## text @.8,4.14 w=6.9 size=12
Example B R: start 1 $\xrightarrow{\ B\ }$ 1 $\xrightarrow{\ R\ }$ 2; stop at $\times$.

## figure
answer_rows(['','B','RBR','RRR','RRRR','BBBRB'],[4.85,5.35,5.85,6.35,6.85,7.35])+blank_rows([1.5],[8.15,8.9,9.65],6,.46,.65)
