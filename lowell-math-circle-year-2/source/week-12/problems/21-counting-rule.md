+++
id = "w12.counting-rule"
title = "Five and six edges, and a counting rule"
grades = ["4-5"]
route = "return"
kernel = "With C(0) = 1, C(n) is the sum of C(i)C(n-1-i) for i from 0 to n-1, giving 1, 1, 2, 5, 14, 42, 132; the first-return split proves it."
+++

## prompt
Find the number of trees with five edges, then six edges. Give a counting rule that works for any number of edges, and explain why it counts each tree once.

## key
\emph{Print guide, p. 9.} Let C(0)=1, the one empty code or root-only tree. For n at least 1, C(n) is the sum of C(i)C(n-1-i) for i=0,...,n-1. The values C(0) through C(6) are 1,1,2,5,14,42,132. In particular C(4)=5+2+2+5=14; C(5)=14+5+4+5+14=42; C(6)=42+14+10+10+14+42=132. This is a disjoint, exhaustive decomposition, not extrapolation from a number pattern.

In a tree, remove the edge from the root to its first child. P describes that child's subtree; Q describes the remaining root branches. Conversely attach any P tree as the new leftmost child branch of any Q tree. These operations undo one another.
