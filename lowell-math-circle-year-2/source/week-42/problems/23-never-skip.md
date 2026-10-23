+++
id = "w42.never-skip"
title = "A rule that never skips"
grades = ["4-5"]
route = "return"
page = "same"
kernel = "A fair color-only rule for three red and one blue must skip at least 10 of the 16 labeled pairs."
+++

## prompt @13
A different color-only rule must give a shape on every pair from the three-red, one-blue bag. Can it be fair? If skipping is allowed, what is the smallest number of the 16 labeled pairs it must skip?

## figure
lines(18,6)

## key
Always giving a shape is impossible: the RR class alone has weight 9 > 8. If skipping is allowed, RR must still be skipped because all other classes total only 7. The remaining weights are 3, 3, 1. Their only equal, nonempty, disjoint subset sums are the two 3s. Therefore BB must also be skipped. The minimum is 10 skipped labeled pairs, attained by the two usual rules. This claim is restricted to deterministic color-only rules, not rules using identity marks or extra randomness.
