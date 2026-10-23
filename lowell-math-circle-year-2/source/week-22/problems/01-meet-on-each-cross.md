+++
id = "w22.meet-on-each-cross"
title = "Put D on each cross and make the regions meet"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "For every position of D some split works (Radon): D inside triangle ABC gives D against A, B, C; otherwise two segments cross or a point lies on a segment."
+++

## prompt [K-1]
Put D on each cross. Each time, make two regions that meet and mark a point they share.

## prompt
Put D on each cross. For each position, split A, B, C, and D so their two regions meet, and mark a shared point.

## figure [K-1]
board(k_tri,[(9,9),(4.3,4.7),(0.8,7.2)])

## figure [2-3]
board(m_tri,[(9,9),(4,5),(6,2.5),(6,1)])

## figure [4-5]
board(u_tri,[(9.8,9),(5,5),(6.25,2.5),(1,6)])

## text
\newpage

## prompt [K-1]
For each place of D, make two regions that meet and mark a point they share.

## prompt
For each position of D, split A, B, C, and D so their two regions meet, and mark a shared point.

## figure [K-1]
recording_boards([k_tri+[('D',x,y,'above right=5pt')] for x,y in [(9,9),(4.3,4.7),(0.8,7.2)]],columns=3,size=5.35)

## figure [2-3]
recording_boards([m_tri+[('D',x,y,'above right=5pt')] for x,y in [(9,9),(4,5),(6,2.5),(6,1)]])

## figure [4-5]
recording_boards([u_tri+[('D',x,y,'above right=5pt')] for x,y in [(9.8,9),(5,5),(6.25,2.5),(1,6)]])
