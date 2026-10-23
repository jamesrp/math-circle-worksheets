+++
id = "w29.four-seven-last"
title = "The last impossible length for 4-rods and 7-rods"
grades = ["2-3"]
route = "return"
kernel = 'The last gap for 4/7 is 17; 18, 19, 20 and 21 plus added 4-rods settle every longer length.'
+++

## prompt
Use 4-rods and 7-rods. Find the last impossible length, and explain why there are no later gaps.

## figure
draw(('rodkey', [4, 7], 1.8), ('targets', range(12, 29), 4, 8), ('ruled', 10, 4))

## key
\emph{Print guide, p. 3.} Last gap 17. A certificate is 18=4+7+7, 19=4+4+4+7, 20=4+4+4+4+4, 21=7+7+7; then add 4-rods. For 17, using zero, one or two 7-rods leaves 17,10 or 3; none is divisible by 4.
