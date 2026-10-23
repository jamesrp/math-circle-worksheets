+++
id = "w86.paths"
title = "Best cop start on two paths"
grades = ["2-5", "4-5"]
route = "first"
page = "same"
kernel = "On a path the middle dot is the best start: C walks toward R, and R on a farthest end forces about half the path's length in cop turns."
+++

## prompt @106
Play on both paths. Choose a starting dot for C that guarantees capture in the fewest C turns, even when R chooses its hardest starting dot and moves.

## figure
graph(*path(5), 32, 150, label='P5') + graph(*path(7, 28), 12, 197, 20, label='P7') + lines(232, 1)

## key
On the five-dot path start C at c; against the best escape choices capture takes at most two cop moves. On the seven-dot path start at d; at most three suffice. R at a farthest endpoint can stay, forcing the same lower bound. Any other start has a farther endpoint, so it cannot improve the worst case. C follows the unique path to R; R may move or stay but cannot cross C or pass the endpoint. Counting a round as two player turns instead of one cop move changes the reported number, so identify the quantity when discussing speed.
