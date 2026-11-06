+++
id = "w25.23-two-counter-move"
title = "Move two counters, keep the counts"
grades = ["2-3"]
route = "first"
page = "same"             # on page 3 under the end of the problem before it
kernel = "Moving two counters to the empty corners of a rectangle keeps every row and column count: the first picture allows one such move, the second three."
+++

## prompt @146
Move exactly two counters in each filled picture to make a different picture with the same counts. Find and draw every way.

## figure
m_two_counter_move()

## key
\emph{Print guide, p. 10.} \textbf{Page 3:} the only alternative moves A1 and C3 to A3 and C1. The selected rows and columns are nonadjacent. All of row B, column 2, and the other cells remain unchanged.

\textbf{Page 4 (added November 2026):} the filled picture A1, B2, C3 has exactly three two-counter moves, one for each pair of rows: A1, B2 to A2, B1 (giving 010/100/001); A1, C3 to A3, C1 (001/010/100); B2, C3 to B3, C2 (100/001/010), with slashes separating rows A/B/C. Moving two counters while keeping every count always uses the opposite corners of a rectangle, so a move needs two rows and the two columns their counters sit in. The other two pictures with counts 1, 1, 1 (010/001/100 and 001/100/010) move all three counters and are not answers.
