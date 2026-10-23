+++
id = "w64.l-right-and-up"
title = "Right and up trips on the L"
grades = ["shared"]
route = "return"
page = "same"
kernel = 'On the three-square L, rightward trips from A and B take two squares and from C one; upward trips from A and C take two and from B one.'
+++

## prompt @1.05
From each dot, make a closed trip to the right and a closed trip straight up. Which trips have the same length?

## figure
fig(lshape(3.70,2.18,2.47,[(sq,(.5,.25),'') for sq in 'ABC'],[(1,0),(0,1)]), lines(7.74,4,.37))
