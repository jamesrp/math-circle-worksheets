+++
id = "w25.45-farthest-pair"
title = "The two pictures farthest apart on a two-row grid"
grades = ["4-5"]
route = "return"
kernel = "On a 2-by-6 grid one switch fixes at most one wrong top column, and at most three top columns can be wrong, so two pictures are never more than three switches apart."
+++

## prompt @27
Make two pictures with the same counts on these grids that need as many switches as possible to change one into the other. Explain why no two pictures on these grids need more.

## figure
h_farthest_blanks()

## key
\emph{Added November 2026, before the guide's P5.} \textbf{Answer:} 3 switches, for example 111000 / 000111 and 000111 / 111000 (top row / bottom row), the endpoints of Problem 3. A pair can set this as a challenge for each other, with the third child checking counts and switches.

\textbf{Why no pair needs more:} columns with count 0 or 2 are the same in both pictures. Among the s columns with count 1, a wrong top column is one occupied in the start's top row and empty in the target's. If the top row holds k of them, at most k can be wrong and at most s - k can be missing, so at most min(k, s - k) are wrong, which is at most 3 when s is at most 6. One switch fixes at most one wrong top column (Problem 3), and the route of the next problem fixes one with every switch.
