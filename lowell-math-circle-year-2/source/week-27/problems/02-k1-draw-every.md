+++
id = "w27.k1-draw-every"
title = "Draw every pairing that can stay"
grades = ["K-1"]
route = "first"
kernel = "A profile can have two stable pairings (top: AX / BY and AY / BX) or one (bottom: only AY / BX)."
+++

## prompt @0.91 size=15.5
Draw every pairing that can stay.

## figure
kcase(1.80,*get('k_two_stable'),kinds=(None,None))+ln(.6,5.80,7.9,5.80)+kcase(6.25,*get('k_unique_cross'),kinds=(None,None))
