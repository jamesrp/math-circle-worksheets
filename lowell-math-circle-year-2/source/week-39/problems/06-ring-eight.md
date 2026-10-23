+++
id = "w39.ring-eight"
title = "What eight-step ring trips leave"
grades = ["K-1", "2-3"]
route = { "K-1" = "return", "2-3" = "first" }
kernel = "Eight-step trips home on the ring leave exactly five results: staying at A, or one or two circuits in either direction."
+++

## prompt @27 [K-1]
Make eight-step trips from A back to A and shorten each. Find every different result.

## prompt @27 [2-3]
Make every different trip from A back to A that can remain after shortening an eight-step ring trip. Find the fewest road steps in a surviving trip home.

## figure [K-1]
graph(50, 77, 53, RING, REDGES) + blank(16, 202, 180, 50)

## figure [2-3]
graph(55, 71, 48, RING, REDGES)

## key [K-1]
There are exactly five reduced home results from eight-step ring walks:\par
\begin{tabular}{lll}\toprule Remaining route & Length & One eight-step input\\\midrule
Stay at A & 0 & ABABABABA\\
ABCDA & 4 & ABABABCDA\\
ADCBA & 4 & ABABADCBA\\
ABCDABCDA & 8 & ABCDABCDA\\
ADCBADCBA & 8 & ADCBADCBA\\\bottomrule\end{tabular}\par
Completeness: on a degree-two ring, once a nonempty reduced route chooses a direction it cannot turn around. A home route has length a multiple of four. Deletions preserve parity and cannot increase length; among lengths 0 through 8 this gives 0, 4, or 8, with two directions for each nonzero length. The listed inputs prove attainability.

## key [2-3]
The complete eight-step ring result set is A (stay), ABCDA, ADCBA, ABCDABCDA, and ADCBADCBA. The fewest steps in a nonempty surviving trip home is four. A degree-two ring leaves a reduced walker no choice except continuing in its chosen direction; a closed route must complete full four-edge circuits. The construction table on page 3 provides eight-step witnesses for every result.
