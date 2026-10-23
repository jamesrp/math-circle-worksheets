+++
id = "w41.k1-step-counts"
title = "Trips home with 2, 3, 4 and 5 steps"
grades = ["K-1"]
route = "return"
kernel = "A trip home with an odd number of steps must lap the board."
+++

## prompt @27
Find trips from H back to H with each number of steps. Look for more than one trip on each map.

## figure
k1_step_maps()

## key
Many answers are valid. Two examples at each requested length: 2 steps: RL and UD. 3 steps: RRR and UUU. 4 steps: RRLL and RULD. 5 steps: RRRUD and UUURL.

Every route listed finishes at H. A candidate is valid exactly when both signed coordinate displacements are multiples of three; adults may use that check without demanding arithmetic from the child.
