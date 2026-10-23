+++
id = "w29.claim"
title = "Does every pair eventually have no more gaps?"
grades = ["2-3"]
route = "return"
page = "same"
kernel = 'The claim is false: of the pairs from 2, 3, 4, 5 and 7, only 2 and 4 has gaps forever (every odd length); one counterexample refutes it.'
+++

## prompt @15
Someone says every pair of rod lengths eventually has no more gaps. Is the claim true? Use rods 2, 3, 4, 5 and 7 to decide.

## figure
draw(('ruled', 18, 5))

## key
\emph{Print guide, p. 3.} The claim is false: 2/4 misses every odd length. Of the ten pairs from 2, 3, 4, 5 and 7 it is the only one with gaps forever; the other nine share no divisor larger than 1. The pair 4/7 does eventually have no gaps, as P5 proves. One counterexample is enough to refute ``every pair.''
