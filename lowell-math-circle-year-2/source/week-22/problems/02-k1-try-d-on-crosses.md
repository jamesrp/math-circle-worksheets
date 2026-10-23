+++
id = "w22.k1-try-d-on-crosses"
title = "Every meeting split for three places of D"
grades = ["K-1"]
route = "first"
page = "new"
kernel = "With D on segment AB, beyond B on that line, or between A and C, exactly two splits work each time (AB | CD and ABC | D; AD | BC and ACD | B; AC | BD and ABC | D)."
+++

## prompt
Try D on each cross. Find every split whose regions meet.

## figure
board(k_edge,[(5,3),(11,3),(3.5,6.5)])

## text
\newpage

## prompt
Find every split whose regions meet.

## figure
recording_boards([k_edge+[('D',x,y,'above right=5pt')] for x,y in [(5,3),(11,3),(3.5,6.5)] for _ in range(3)],columns=3,size=5.35)
