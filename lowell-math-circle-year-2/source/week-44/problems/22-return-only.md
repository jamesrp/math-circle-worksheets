+++
id = "w44.return-only"
title = "Return without a copy"
grades = ["4-5"]
route = "first"
kernel = "Without copies the totals have chances $1/4$, $1/2$, $1/4$ instead of $1/3$ each."
+++

## prompt @0
Keep the starting bag R1, B1, but return each draw without adding a copy. How does the chance of zero, one, or two red draws change? Explain the difference exactly.

## figure
box_lines(0,4,18,7)

## key
Without copies, the four histories are RR, RB, BR, BB, each with probability 1/4. The probabilities for zero, one, two reds become 1/4, 1/2, 1/4, compared with 1/3, 1/3, 1/3 under copying. In copying, the first color gains an extra identity for the second draw, giving RR and BB two marked histories each.
