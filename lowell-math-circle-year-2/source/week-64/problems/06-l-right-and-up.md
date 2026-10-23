+++
id = "w64.l-right-and-up"
title = "Right and up trips on the L"
grades = ["shared"]
route = "return"
kernel = 'On the three-square L, rightward trips from A and B take two squares and from C one; upward trips from A and C take two and from B one.'
+++

## figure
page_start()

## prompt @.48
From each dot, make a closed trip to the right and a closed trip straight up. Which trips have the same length?

## text @0,1.30 w=7.35 size=12.5
Cross a shared side into the next square. The outside edges match by letters and arrows. Stop at any square corner.

## figure
fig(lshape(3.70,2.18,2.47,[(sq,(.5,.25),'') for sq in 'ABC'],[(1,0),(0,1)]), lines(7.74,4,.37))
