+++
id = "w86.two-cops-any-ring"
title = "Two cops on the eight-ring and on every ring"
grades = ["4-5"]
route = "return"
kernel = "The blocker-and-sweeper plan works on every ring, whatever its number of dots."
+++

## prompt
Find a two-cop plan for this ring. Will your plan work on every ring, however many dots it has? Explain why.

## figure
graph(*cycle(8, 51), 96, 114, label='Q8') + lines(197, 4)

## key
Both cops may each take at most one road or stay, then R gets one turn. Two moves are not a pooled budget that one cop may spend. The six-dot example gives a concrete coordination attempt before the eight-dot/general question. A held hint is to ask whether one cop could make one part of the ring permanently unusable. A strategy in which both cops move can also be valid; require an explanation of the region R can still occupy.
