+++
id = "w25.k1-one-or-many"
title = "Counts that fit one picture, and counts that fit more"
grades = ["K-1"]
route = "return"
kernel = "A picture is the only one with its counts exactly when no two counters can trade opposite corners of a rectangle; a full row forces cells."
+++

## prompt @27
Draw a four-counter picture on each grid and write its counts. Choose pictures whose counts fit only one picture on the left grids and more than one picture on the right grids.

## figure
blank_pairs()

## key
\emph{Print guide, p. 7.} \textbf{P6:} the left grids must have unique reconstructions; the right grids must have more than one. The counts of the left and right grids need not match.

\textbf{Why the left pictures are unique:} A is full. On the 2-by-3 board, column 1 then forces B1, and B has no other counter. On the 3-by-3 board, C is empty and the same reasoning forces B1.

\textbf{Why the right pictures are ambiguous:} the adjacent alternative has exactly the same circled counts and is different in labeled cells. Two witnesses suffice to establish "more than one." Never accept "my partner could not find one" as the only uniqueness argument.
