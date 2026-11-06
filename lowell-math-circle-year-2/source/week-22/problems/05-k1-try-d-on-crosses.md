+++
id = "w22.k1-try-d-on-crosses"
title = "Two meeting groupings for three places of D"
grades = ["K-1"]
route = "first"
page = "new"
kernel = "With D on segment AB, beyond B on that line, or between A and C, exactly two splits work each time (AB | CD and ABC | D; AD | BC and ACD | B; AC | BD and ABC | D)."
+++

## prompt
For each place of D, find two different ways to make two groups whose regions meet. Draw them.

## figure
recording_boards([k_edge+[('D',x,y,'above right=5pt')] for x,y in [(5,3),(11,3),(3.5,6.5)] for _ in range(2)],columns=2,size=6.9)
