+++
id = "w08.m-two-piles"
title = "Two piles: first or second?"
grades = ["2-3"]
route = "first"
page = "new"
+++

## prompt
Play many games with two piles of counters from each start. Would you rather go
first or second?

## text
\vspace{0.3in}

## figure
"\\noindent " + "\\hfill".join(labelled_piles(p, f"{p[0]} and {p[1]}", maxk=7)
                               for p in [(4, 4), (6, 2), (5, 3), (7, 7)])
+ "\n\\vspace{0.6in}"   # in the paragraph of the row, as the old builder had it
