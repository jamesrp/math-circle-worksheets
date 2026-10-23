+++
id = "w41.trips-home"
title = "Trips from H back to H"
grades = ["K-1", "2-3"]
route = "first"
kernel = "K-1: every cell is exactly two steps from H. Grades 2-3: the three-step trips home are exactly RRR, LLL, UUU and DDD; six steps allow many more."
+++

## prompt @27 [K-1]
Start at H. Find every square you can reach in exactly two steps.

## prompt @27 [2-3]
Find as many different trips from H back to H as you can, using exactly three steps, then exactly six steps.

## figure [K-1]
tile(18,71,180,True,True,True,15)

## figure [2-3]
board_and_lines()

## key [K-1]
Every one of the nine cells is reachable in exactly two steps. A: LU. B: DD. C: RU. D: RR. H: RL. E: LL. F: LD. G: UU. I: RD.

This list is complete because it contains every cell in the map. The witnesses use wrapping: for example DD goes H$\to$G$\to$B, whereas UU goes H$\to$B$\to$G. Exactly two steps does not mean at most two.

Plain-board contrast for Problems 2 and 3: with no portals, two steps from H reach only H, A, C, F and I, and no odd trip returns to H, since each step changes checkerboard colour.

## key [2-3]
Exactly three steps: the complete list is RRR, LLL, UUU, DDD. Exactly six steps: examples include RRRRRR, LLLLLL, UUUUUU, DDDDDD, RRRUUU, RURURU, RRRDDD, LLLUUU, LLLDDD, and RLRLRL.

A six-step word returns to H precisely when its small-step displacement is (0,0), ($\pm$6,0), (0,$\pm$6), or ($\pm$3,$\pm$3). There are 400 balanced strings, four straight six-step strings, and 20 for each of the four diagonal sign choices: 484 total.
