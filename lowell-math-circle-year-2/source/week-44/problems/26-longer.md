+++
id = "w44.longer"
title = "Five draws and more"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "After $n$ draws each red total from 0 to $n$ has chance $1/(n+1)$."
+++

## prompt @14
What do you predict about red-draw totals after five draws, or after more draws? Explore your prediction.

## figure
lines(18,6)

## key
Predict 1/6 for each red total after five draws, and 1/(n+1) after n draws. Proof: a word with r reds has probability r!(n-r)!/(n+1)!, since its red numerators are 1,...,r and its blue numerators 1,...,n-r. There are n!/[r!(n-r)!] such words. Multiplication gives 1/(n+1). A child’s observed pattern remains a conjecture until justified; the general proof is an optional endpoint invited by the problem.
