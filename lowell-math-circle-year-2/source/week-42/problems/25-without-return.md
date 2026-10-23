+++
id = "w42.without-return"
title = "Returning only after the pair"
grades = ["4-5"]
route = "return"
kernel = "Without return inside a pair, RB and BR still have equal counts (3 and 3 of 12 ordered labeled pairs)."
+++

## prompt @0
Return both counters only after drawing a pair. Then mix before the next pair. Does your rule still work with the three-red, one-blue bag? Explain using the labeled outcomes.

## figure
bag_and_pair()

## key
Yes. Without replacement there are 4 $\times$ 3 = 12 equally likely ordered pairs of distinct identities. RR has six, RB three, BR three, BB none. Reverse each kept pair to match its weight. Each shape has probability 3/12, and conditional on output it has chance 1/2. The within-pair draws are dependent, so the independent-draw product proof is inapplicable; the reversal proof still works. Return both counters and mix before the next pair.
