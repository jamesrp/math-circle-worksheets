+++
id = "w12.k1-finish-a-drawn-pair"
title = "Finish an eight-dot pairing from a drawn pair"
grades = ["K-1"]
route = ["first", "return"]
kernel = "A fixed string can be completed without crossings exactly when it leaves an even number of dots on each side: 1-4 and 1-6 finish two ways each, 1-3 and 1-5 trap an odd group."
+++

## prompt size=13.5
Keep each drawn pair when you try it on the large circle. Find every way to finish it, or show why you cannot.

## figure
k1_mat_and_records(8,fixed=[(1,4),(1,4),(1,6),(1,6),(1,3),(1,5)])

## key
\emph{Print guide, p. 4.} Keep each supplied chord. For 14, completions are 14|23|56|78 and 14|23|58|67. For 16, they are 16|23|45|78 and 16|25|34|78. The 13 and 15 starts are impossible: they trap respectively one or three dots on one side, and a string cannot leave without crossing the fixed chord. The duplicated 14 and 16 frames are for the two completions of each, not different starting cases.
