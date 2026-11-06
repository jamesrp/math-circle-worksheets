+++
id = "w12.three-edge-trees"
title = "Every ordered tree with three edges"
grades = ["4-5"]
route = "first"
page = "same"             # shares page 1 with the rules
kernel = "There are exactly five ordered rooted trees with three edges; sorting by the number of root children gives 2 + 2 + 1."
+++

## prompt @120
Draw all different trees with three edges, using these rules. How do you know your collection is complete?

## figure
roots([61,155],[146,185,224])

## key
\emph{Print guide, p. 8.} The five-edge example has two root children: the left has two leaf children, and the right has one. Exactly five three-edge trees; see page 6 and its root-child case split. A chain and a fork are different; changing edge lengths is irrelevant. Swapping unequal subtrees creates a different ordered tree.
