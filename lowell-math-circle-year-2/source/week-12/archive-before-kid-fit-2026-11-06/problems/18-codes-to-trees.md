+++
id = "w12.codes-to-trees"
title = "Trees for four codes, and whether a code has two"
grades = ["4-5"]
route = ["first", "return"]
kernel = "Each legal code builds exactly one ordered tree: at U add a new rightmost child and move to it, at D move to the parent."
+++

## prompt
Draw a tree for each code. Can a code describe two different trees?

## figure
codes_to_trees()

## key
\emph{Print guide, p. 8.} No. For these ordered rooted trees, each legal complete code describes exactly one tree. UUDDUD: the root has two children; the left child has one child. UDUUDD: the root has two children; the right child has one child. UUDUDUDD: the root has one child, and that child has three leaf children. UUUDDUDD: the root has one child; that child has two children, the left of which has one child. At U there is one prescribed action: add a new rightmost child of the current vertex and move there. At D move to the parent. No choices remain, so there is exactly one ordered tree.
