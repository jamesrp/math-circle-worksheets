+++
id = "w12.every-six-step-path"
title = "Every six-step path, matched to the pairings"
grades = ["2-3"]
route = ["first", "return"]
kernel = "There are exactly five such paths, and the code and the stack rule undo each other, so paths and pairings match one to one."
+++

## prompt
Find every path with three up steps and three down steps that starts and ends on the dark line and never goes below it. Match your paths to your six-dot pairings.

## figure
six_path_grids()

## key
\emph{Print guide, p. 5.} Exactly five paths; see page 6. Match them to the pairings using the unique inverse just proved. A count of five in both lists alone is not a proof of a bijection: the rules in both directions must undo one another.
