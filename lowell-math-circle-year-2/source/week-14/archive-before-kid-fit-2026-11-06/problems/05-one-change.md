+++
id = "w14.one-change"
title = "Every result of one change"
grades = ["K-1", "2-3", "4-5"]
route = {"K-1" = "return", "2-3" = "first", "4-5" = "first"}
kernel = "Erasing a diagonal leaves a convex quadrilateral with exactly one other diagonal, so a filling with $n-3$ diagonals has exactly $n-3$ one-change neighbours."
+++

## prompt [K-1]
Erase one inside line and draw a different one. Keep the shape full of triangles and find every possible result from each drawing.

## prompt
Erase one inside line and replace it with a different line so the polygon stays filled with triangles. Find every result of one such change from each drawing.

## figure [K-1]
two_cases_with_records(6,6,fan(6,0),hex_center,gray_edges=True)

## figure
two_cases_with_records(6,6,fan(6,0),hex_center,'letters')

## key [K-1]
Each printed hexagon has exactly three one-change results, one for each of its three interior diagonals. The original filling itself is not a new result. Each small copy prints its start's lines in light gray: the child crosses out the gray line that goes and draws the new one, so every copy differs from its start by one line. Show this once at the table. Four copies for three results keep the count open. Why the list is complete. Removing one interior diagonal merges exactly its two adjacent triangles into a convex quadrilateral. That quadrilateral has exactly one other diagonal. Everything outside it is unchanged. Thus each of the three original diagonals supplies exactly one neighbor, and there are no further legal one-line replacements.

## key [2-3]
First start $\{AC,AD,AE\}$ has neighbors $\{AC,AD,DF\}$, $\{AC,AE,CE\}$, and $\{AD,AE,BD\}$. Second start $\{AC,AE,CE\}$ has neighbors $\{AC,CE,CF\}$, $\{AE,BE,CE\}$, and $\{AC,AD,AE\}$. The six diagrams on page 5 show all results after replacing number labels by letters.

## key [4-5]
The two printed hexagon starts have the same six neighbors keyed in middle P3 and pictured in K--1 P5. Each start has exactly three possible flips. The two-triangle quadrilateral argument on page 5 proves completeness.

## hints [K-1]
Trace the two triangles touching the line a child wants to erase. Ask for the boundary of their combined piece before asking which other line fills it. Do not erase a second line.

## hints [2-3]
Choose one original diagonal; identify its two incident triangles. The other diagonal of their quadrilateral is the only legal replacement.

## hints [4-5]
A different-looking triangulation need not be one move away. Check that exactly one old diagonal disappeared and exactly one new one appeared.
