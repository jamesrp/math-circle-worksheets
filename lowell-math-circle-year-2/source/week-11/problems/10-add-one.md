+++
id = "w11.add-one"
title = "Adding one chip at a time on the triangle"
grades = ["K-1", "2-3"]
route = "return"
kernel = "Adding one chip at A and finishing cycles through (1,0), (0,1), (1,1); the empty board never returns; adding at B runs the same cycle the other way."
+++

## prompt [K-1]
Start with empty circles, then add one chip to A at a time, finishing all the sharing after each chip. Can you ever get empty circles again?

## prompt [2-3]
Begin with empty circles. Add one chip to A and finish; keep repeating until you have added 12 chips. Begin again, adding to B instead. After at least one addition, which pairs of final piles can each rule reach?

## figure [K-1]
k1_add_one()

## figure [2-3]
add_one_23()

## key [K-1]
After adding 1 through 11 chips at A, the finishes are
\[
(1,0),(0,1),(1,1),(1,0),(0,1),(1,1),
(1,0),(0,1),(1,1),(1,0),(0,1).
\]
No later stable finish is empty. The entire update rule on the four stable states is pictured below, so the repeating claim is exhaustive, rather than inferred only from eleven trials.

## key-figure [K-1]
add_one_cycle()

## key [K-1]
Every arrow means add one at A and finish all sharing. Only the three states in the cycle occur after an addition. The initial empty state is outside the cycle.

## key [2-3]
The complete twelve-row table is below. Each rule reaches exactly $(1,0),(0,1),(1,1)$ after at least one addition. $(0,0)$ occurs only before the first addition.
\begin{center}\begin{tabular}{ccc}\toprule
Chips added & Add at A then finish & Add at B then finish\\\midrule
1&$(1,0)$&$(0,1)$\\2&$(0,1)$&$(1,0)$\\3&$(1,1)$&$(1,1)$\\
4&$(1,0)$&$(0,1)$\\5&$(0,1)$&$(1,0)$\\6&$(1,1)$&$(1,1)$\\
7&$(1,0)$&$(0,1)$\\8&$(0,1)$&$(1,0)$\\9&$(1,1)$&$(1,1)$\\
10&$(1,0)$&$(0,1)$\\11&$(0,1)$&$(1,0)$\\12&$(1,1)$&$(1,1)$\\\bottomrule\end{tabular}\end{center}
\textbf{Why the cycles persist.} The A-addition map is drawn on page 7. Interchanging the names A and B gives the B-addition map. Once the same pair recurs, the fixed rule repeats the same successors forever. The two rules traverse the three-cycle in opposite directions.

## hints [K-1]
Ask whether an arrangement has appeared before. Once it has, ask what the same next action must do from that same arrangement.

## hints [2-3]
An adult may turn a child's repeated rows into three state cards with arrows. Introduce the diagram after the repetition has a purpose.
