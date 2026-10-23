+++
id = "w41.trips-home"
title = "Trips from H back to H"
grades = ["K-1", "2-3", "4-5"]
route = "first"
kernel = "K-1: every cell is exactly two steps from H. Older bands: trips home exist for some lengths and not others, and a trip home can finish in a different copy of H."
+++

## prompt @27 [K-1]
Start at H. Find every square you can reach in exactly two steps.

## prompt @27 [2-3]
Find different trips from H back to H using exactly three steps, then exactly six steps. Draw or replay as many as you can.

## prompt @27 [4-5]
Make four different trips from H back to H. Choose trips whose replays finish in different copies of H on the repeated map.

## figure
tile(18,71,180,True,True,True,15)

## key [K-1]
Every one of the nine cells is reachable in exactly two steps. A: LU. B: DD. C: RU. D: RR. H: RL. E: LL. F: LD. G: UU. I: RD.

This list is complete because it contains every cell in the map. The witnesses use wrapping: for example DD goes H$\to$G$\to$B, whereas UU goes H$\to$B$\to$G. Exactly two steps does not mean at most two.

## key [2-3]
Exactly three steps: the complete list is RRR, LLL, UUU, DDD. Exactly six steps: examples include RRRRRR, LLLLLL, UUUUUU, DDDDDD, RRRUUU, RURURU, RRRDDD, LLLUUU, LLLDDD, and RLRLRL.

A six-step word returns to H precisely when its small-step displacement is (0,0), ($\pm$6,0), (0,$\pm$6), or ($\pm$3,$\pm$3). There are 400 balanced strings, four straight six-step strings, and 20 for each of the four diagonal sign choices: 484 total.

## key [4-5]
Four examples returning to H in different copies: RRR$\to$(1,0), LLL$\to$($-$1,0), UUU$\to$(0,1), DDD$\to$(0,$-$1). Many other choices are valid; the copy pair must differ for each of the four.
