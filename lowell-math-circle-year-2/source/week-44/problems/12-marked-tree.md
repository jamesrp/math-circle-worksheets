+++
id = "w44.marked-tree"
title = "Every marked two-draw story"
grades = ["2-3"]
route = "first"
page = "same"
kernel = "The six marked histories are equally likely, two for each final bag, so all three bags have chance $1/3$."
+++

## prompt @5.2
Each counter in the bag has the same chance of being drawn. Complete every marked two-draw story. Ignore marks when comparing final bags: which red/blue counts have the most stories?

## figure
marked_tree(8)

## key
All six marked histories are listed below. Each first choice has chance 1/2; each second choice, conditional on the first, has chance 1/3. Thus every row has chance 1/6. “R2” or “B2” exists only in the corresponding first-draw branch.

R1: R1, 3R / 1B, 2.

R1: R2, 3R / 1B, 2.

R1: B1, 2R / 2B, 1.

B1: R1, 2R / 2B, 1.

B1: B1, 1R / 3B, 0.

B1: B2, 1R / 3B, 0.

All three compositions have two histories, so none has the most: each has probability 1/3. Notice that RR and BB each merge two marked histories, while RB and BR each merge one.
