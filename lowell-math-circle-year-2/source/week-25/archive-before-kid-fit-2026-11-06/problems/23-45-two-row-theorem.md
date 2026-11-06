+++
id = "w25.45-two-row-theorem"
title = "The fewest switches on any two-row board"
grades = ["4-5"]
route = "return"
kernel = "On two rows the fewest switches is the number of top counters in columns where the other picture has none: one switch fixes one, and pairing achieves it."
+++

## prompt @27
Take any two pictures on a two-row grid with the same row and column counts. Explain why switches can always turn one into the other. Give a rule for the fewest switches needed, using only the two pictures. Your explanation should work for any number of columns.

## figure
h_two_row_blanks()

## key
\emph{Print guide, p. 15.} \textbf{Rule:} the fewest switches equals the number of columns with a top counter in the start and no top counter in the target. Count unwanted top positions, not all differing cells. If there are none, the pictures already agree and the answer is zero.

\textbf{3. Match one of each.} Choose an unwanted top column u and a missing top column v. Currently the counters are at Au and Bv, while Bu and Av are empty. Switching those corners puts both columns in their target states. It does not disturb any other column. Repeat until there are no unwanted positions. If there were d initially, this supplies a route of d switches.

\textbf{4. No route can do better.} Any two-row switch removes only one top counter and adds only one top counter, so it can reduce the number of unwanted top columns by at most 1. That number must fall from d to 0. At least d switches are required. The constructed route uses exactly d, proving the rule and connectivity for every number of columns.
