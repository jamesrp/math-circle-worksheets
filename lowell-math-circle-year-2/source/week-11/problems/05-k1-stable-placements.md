+++
id = "w11.k1-stable-placements"
title = "Every placement where no circle can share"
grades = ["K-1"]
route = "return"
kernel = "A stable four-cycle placement has 0 or 1 chip at each circle: eight placements, and none uses 4 chips because three circles hold at most one each."
+++

## prompt
Find every way to put chips on A, B, and C so that no circle can share. Can any of these ways use 4 chips?

## figure
k1_stable_placements()

## key
Every stable four-cycle state has 0 or 1 chip at each circle. The complete set of eight is
\[
(0,0,0),\ (0,0,1),\ (0,1,0),\ (0,1,1),
\qquad
(1,0,0),\ (1,0,1),\ (1,1,0),\ (1,1,1).
\]
There cannot be a stable placement of four chips: three circles hold at most one each. This is a capacity proof, not merely a failed search.

## hints
Ask how many chips one circle can hold without sharing. Once the child has examples, sort them by whether A is empty; each half has the four B/C choices.
