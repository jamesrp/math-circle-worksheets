+++
id = "w26.k1-one-move"
title = "Move one tile to shorten the boundary"
grades = ["K-1"]
route = "return"
kernel = 'One move takes the middle start to the 2-by-3 rectangle (10) and the L to 12, which is best because 10 needs a 2-by-3 rectangle; the straight row cannot get shorter than 14.'
+++

## prompt
Move one tile in each shape and draw a result with the shortest boundary you can make. Which shapes can you make shorter?

## figure
k1_one_move()

## key
\emph{Print guide, p. 7.} \textbf{Exact answer:} only the middle and bottom starts can be made shorter. Their best boundaries are 10 and 12; the straight row stays at 14.

\textbf{Moves shown:} in the top row, move the right endpoint just below the left endpoint. In the middle start, move the rightmost tile of its four-tile row into the gap between the two tiles in the next row. In the bottom L, move the far end of its four-tile arm into the inside corner.
