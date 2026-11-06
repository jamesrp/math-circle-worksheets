+++
id = "w12.trees-to-codes"
title = "Walk codes for four trees"
grades = ["4-5"]
route = "first"
page = "same"             # shares page 2 with the walk code
kernel = "A tree's walk code shows its edges (half the length), depth (greatest height), leaves (UD peaks) and root children (returns to zero)."
+++

## prompt @128
Write the walk code for each tree. Which features of a tree can you read from its code?

## figure
trees_to_codes()

## key
\emph{Print guide, p. 8.} The worked two-edge fork has code UDUD: visit the left leaf and return, then visit the right leaf and return. U is away from the root on the tree and upward on the path. For the four unanswered trees, reading top-left, top-right, bottom-left, bottom-right: UUUUDDDD, UDUDUDUD, UUDUDDUD, UDUUUDDD. Number of edges is half the code length. Maximum height is maximum root-to-vertex distance. A UD peak records a leaf. Every return to zero finishes a root child's branch, so the number of such returns is the root's number of children.
