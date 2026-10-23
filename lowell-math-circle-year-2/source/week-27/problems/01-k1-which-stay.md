+++
id = "w27.k1-which-stay"
title = "Which pairing can stay?"
grades = ["K-1"]
route = "first"
page = "new"
kernel = "With two pairs, the pairing that can stay is the one with no blocker: in both cases only AX / BY stays, once because each letter has its first choice and once because A and X rank each other first."
+++

## prompt @1.97 size=15.5
Circle every pairing that can stay.

## figure
kcase(2.43,*get('k_unique_mutual'))+ln(.6,6.18,7.9,6.18)+kcase(6.41,*get('k_unique_shared'))
