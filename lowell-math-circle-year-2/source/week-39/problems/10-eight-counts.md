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

## prompt @150 [4-5]
Join the same four ring trips in every possible order. Which orders disappear?

## figure [2-3]
blank(16, 235, 180, 21)

## figure [4-5]
blank(16, 163, 180, 93)

## key [2-3]
A 12-step disappearing example is HABHBAHCDHDCH: left forward, left backward, right forward, right backward. A 12-step survivor is HABHCDHBAHDCH: left forward, right forward, left backward, right backward. Both use both rings. In the first, nested opposite traversals cancel within each round-trip pair. The second has no immediate reversal anywhere.

## key [4-5]
Of the 24 orders of a, b, a$^{-1}$, b$^{-1}$, 16 disappear and 8 survive. If two trips on the same ring are next to each other, they are a ring trip and its backward trip, which cancel; the other ring's two trips are then next to each other and cancel too. If the rings alternate, left, right, left, right or right, left, right, left, no out-and-back pair occurs anywhere, including at H: these 8 orders survive (two patterns, each with two ways to place each ring's two trips), such as ab a$^{-1}$ b$^{-1}$. Every order goes around each ring once each way, so equal net counts do not decide whether a trip disappears; the order does.
