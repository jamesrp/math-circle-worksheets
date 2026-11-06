+++
id = "w12.every-eight-dot-pairing"
title = "Every pairing of eight dots in a row"
grades = ["2-3"]
route = "return"
kernel = "Eight dots have 14 noncrossing pairings: dot 1's partner splits them 5 + 2 + 2 + 5."
+++

## prompt
Draw every pairing of eight dots. How can you be sure that none are missing?

## figure
eight_dot_rows()

## key
\emph{Print guide, p. 5.} Exactly 14 pairings, page 7. The four cases for the partner of 1 give 5+2+2+5. Within each case, choices inside and after the first pair are independent. The forced-split proof on page 9 justifies completeness.
