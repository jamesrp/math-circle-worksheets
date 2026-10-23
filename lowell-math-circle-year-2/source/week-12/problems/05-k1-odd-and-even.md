+++
id = "w12.k1-odd-and-even"
title = "Which circles can be completely paired?"
grades = ["K-1"]
route = "first"
kernel = "An even number of dots can always be paired (join neighbors); an odd number never can, since each string removes two dots."
+++

## prompt
Pair all the dots in each circle if you can. If you cannot, show what gets in the way.

## figure
k1_parity_circles()

## key
\emph{Print guide, p. 4.} Ten, four and six dots are possible: join adjacent pairs (12,34,56,78,9-10 as far as the circle allows). Three, five and seven dots are impossible. Each string removes two unpaired dots, so an odd starting number always leaves an odd number; it cannot reach zero. A physical demonstration that repeatedly removes pairs is sufficient.
