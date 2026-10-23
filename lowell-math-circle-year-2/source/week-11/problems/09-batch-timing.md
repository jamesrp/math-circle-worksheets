+++
id = "w11.batch-timing"
title = "Adding chips while sharing, or in batches"
grades = ["K-1", "2-3"]
route = "return"
kernel = "Once all the prescribed chips have arrived and sharing is finished, the finish does not depend on when the chips were added."
+++

## prompt [K-1]
For each row, start empty and add the chips shown, sharing whenever you choose. Can a different order of adding and sharing change the finish?

## prompt [2-3]
Start empty for each trial. Add the two batches together and finish, or finish one batch before adding the other. Try both orders of the batches. Can these choices change the final piles?

## figure [K-1]
k1_batches()

## figure [2-3]
batches_23()

## key [K-1]
For every timing of additions and legal sharing, $(3,3)$ finishes at $(1,1)$, and $(2,4)$ finishes at $(1,0)$. All three repeated rows for each total have the same answer. In a batch of 3 at A then 3 at B: $(3,0)\to(1,1)$, then $(1,4)\to(1,1)$. Reversing the batch order agrees. For 2 at A then 4 at B: $(2,0)\to(0,1)$, then $(0,5)\to(1,0)$. Reversing gives $(0,4)\to(0,1)$, then $(2,1)\to(1,0)$.

## key [2-3]
The batches are 2 at A and 4 at B on the four cycle. All three timing choices finish at $(1,1,1)$. Together, $(2,4,0)$ has total firing counts $(2,3,1)$. For A's batch first, $(2,0,0)\to(0,1,0)$, then $(0,5,0)\to(1,1,1)$. For B's batch first, $(0,4,0)\to(1,0,1)$, then $(3,0,1)\to(1,1,1)$.

## hints [K-1]
Reserve the not-yet-added chips off the board, away from the sink. Stop only after all scheduled chips have been added and no circle can share.

## hints [2-3]
Have the child name what is held back at each stage. Empty the sink between independent trials, never between the two batches of one trial.
