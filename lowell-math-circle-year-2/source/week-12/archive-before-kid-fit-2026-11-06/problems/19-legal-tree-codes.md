+++
id = "w12.legal-tree-codes"
title = "Rules for which codes come from trees"
grades = ["4-5"]
route = ["first", "return"]
kernel = "A U/D string comes from a tree exactly when every prefix has at least as many U's as D's and the totals are equal; the inverse construction then rebuilds the tree."
+++

## prompt
Which of these codes could come from a tree? Give rules that decide for any string of U's and D's, and explain why they work. Describe how to rebuild a tree from any code that follows your rules.

## figure
tree_codes()

## key
\emph{Print guide, p. 8.} Valid: UUUUDDDD, UDUDUUDD, UUUDUDDD. Invalid: UUDDDUUD first goes below zero at letter 5; DUUUDDUD does so at letter 1; UUDUDUDU finishes at height 2. Necessary and sufficient rules: every prefix has at least as many U as D, and total U equals total D. The empty code gives the root-only tree. The construction from P3 never asks for a parent above the root and finishes at the root. Walking its new children left-to-right gives back the code, which proves sufficiency and reversibility.
