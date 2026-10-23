+++
id = "w41.shrink-to-h"
title = "Which trip shrinks to staying at H?"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "RRRUUULLLDDD finishes in copy (0,0) and shrinks to staying at H; RRR finishes in (1,0) and cannot."
+++

## prompt @146
Use tracing paper on the repeated map from page 2. Which trip can shrink all the way to staying at H? Show changes to the whole trip.

## figure
arrtrip(19,164,180,'RRRUUULLLDDD',14)+arrtrip(19,177,180,'RRR',14)+ruled(196,254,9.5)

## key
RRRUUULLLDDD can shrink to staying at H; RRR cannot. The first has zero lifted displacement. An explicit legal reduction is to commute each L leftward across each U, using nine square slides, producing RRRLLLUUUDDD. Cancel the three adjacent RL pairs and then the three UD pairs. The second finishes at H in copy (1,0). Every allowed move preserves the lifted endpoint, so it cannot become the empty path at the original H.
