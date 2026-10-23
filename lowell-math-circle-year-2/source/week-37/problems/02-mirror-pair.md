+++
id = "w37.mirror-pair"
title = "The mirror pair"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "A tetrahedron with four different corner labels cannot be turned to match its mirror image; with A on A, checking the three turns about A is a complete search."
+++

## prompt [K-1]
Build this pair with your adult. Can you turn the models to match every letter?

## prompt [2-3]
Build this model and its mirror twin. Can you match every letter by moving and turning one of them? If no turn has worked, does that mean no turn can work?

## prompt [4-5]
Build the model and its mirror twin. Can one be moved and turned to match the other? If not, explain why no turn can.

## figure [4-5]
mirror_pair(ruled=[17,19,21,23])

## figure
mirror_pair()

## key [K-1]
The printed A B C D versus A C B D pair cannot match under rigid translations and rotations. It swaps B and C while keeping A and D in place in the construction. Accept a complete check: A must go on A, and all three turns about A fail. A young child is not expected to produce it; the adult can demonstrate the stable reversed order after exploration.

## key [2-3]
The mirror pair cannot match. ``No turn has worked yet'' does not by itself establish ``no turn can work.'' Accept a complete check: A must go on A, and all three turns about A fail. The A-nearest-eye cyclic order is a second reason, covering every allowed turn.

## key [4-5]
No rigid matching motion exists for the four-distinct-label mirror pair. Page 5 gives both a geometric and an algebraic obstruction.
