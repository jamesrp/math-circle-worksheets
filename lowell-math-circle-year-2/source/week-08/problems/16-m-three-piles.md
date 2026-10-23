+++
id = "w08.m-three-piles"
title = "Small three-pile games"
grades = ["2-3"]
route = "return"
+++

## prompt
Play many games with three piles from each start. Would you rather go first or
second?

## text
\vspace{0.3in}

## figure
"\\noindent " + "\\hfill".join(labelled_piles(p, ", ".join(map(str, p)), gap=0.36)
                               for p in [(1, 1, 1), (1, 1, 2), (2, 2, 3), (1, 2, 3)])
