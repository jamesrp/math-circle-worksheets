+++
id = "w27.k1-swap-one-strip"
title = "Swap one strip"
grades = ["K-1"]
route = "return"          # the route note: return to P3-4 once both wishes are checked against one pairing
kernel = "One blocker can be removed by reversing either of its two strips (top: A's or Y's); when two blockers share no letter, no single strip repairs the pairing (bottom)."
+++

## prompt @0.91
Swap the two choices on just one strip to make the drawn pairing stay. Circle every strip that works on its own, or cross out the pairing if none works.

## figure
kstrips(2.0,*get('k_one_blocker'))+kboard(2.68,2.0+2.27,(0,1))
+ kstrips(6.30,*get('k_unique_cross'))+kboard(2.68,6.30+2.27,(0,1))
+ ln(.6,5.99,7.9,5.99)
