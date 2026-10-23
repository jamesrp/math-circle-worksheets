+++
id = "w39.eight-counts"
title = "Same ring counts, different results"
grades = ["2-3", "4-5"]
route = "return"
page = "same"
kernel = "Going around each ring once each way does not decide whether a trip disappears; the order of the circuits does."
+++

## prompt @197 [2-3]
Make two trips from H back to H, each using both rings and at least 12 road steps. One must shorten to staying at H; the other must lose no steps.

## prompt @197 [4-5]
This trip goes around each ring once each way. Does that information alone tell whether a trip can disappear? Make another trip with those same counts and a different result.

## figure [2-3]
blank(16, 235, 180, 21)

## figure [4-5]
blank(16, 237, 180, 19)

## key [2-3]
A 12-step disappearing example is HABHBAHCDHDCH: left forward, left backward, right forward, right backward. A 12-step survivor is HABHCDHBAHDCH: left forward, right forward, left backward, right backward. Both use both rings. In the first, nested opposite traversals cancel within each round-trip pair. The second has no immediate reversal anywhere.

## key [4-5]
Equal net counts are insufficient. HABHBAHCDHDCH, or aa$^{-1}$bb$^{-1}$, goes around each ring once each way and reduces to H. It has exactly the same signed ring counts as the survivor in Problem 5. The difference is the order in which the inverse traversals occur.
