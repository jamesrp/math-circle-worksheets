+++
id = "w12.paths-to-pairings"
title = "Pairings for four paths, and whether a path has two"
grades = ["2-3"]
route = ["first", "return"]
kernel = "Each path has exactly one noncrossing pairing: at every D, close the most recent open U (the stack rule), and closing an older one would force a crossing."
+++

## prompt
Draw a pairing for each path. Could a path come from two different pairings without crossings? Explain.

## figure
paths_to_pairings()

## key
\emph{Print guide, p. 5.} Top to bottom: UUDUDD gives 16|23|45; UDUUDD gives 12|36|45; UUDDUUDD gives 14|23|58|67; UUUDUDDD gives 18|27|34|56. No path has two noncrossing inverse pairings. At every D, close the most recently opened unclosed U. If an older opening were closed first, the more recent opening would have to close later, causing interleaving endpoints and a crossing. This is the stack rule, and it is forced, not merely a convenient algorithm.
