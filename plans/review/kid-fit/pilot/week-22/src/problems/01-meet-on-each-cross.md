+++
id = "w22.meet-on-each-cross"
title = "Put D on each cross and make the regions meet"
grades = ["K-1", "2-3", "4-5"]
route = "first"
page = "same"
kernel = "For every position of D some split works (Radon): D inside triangle ABC gives D against A, B, C; otherwise two segments cross or a point lies on a segment."
+++

## prompt [K-1]
In each picture, make two groups whose regions meet. Draw both regions and mark a point they share.

## prompt
Move the D marker to each cross in turn. Each time, use the markers and your finger to find a split of A, B, C, and D whose two regions meet.

## figure [K-1]
recording_boards([k_tri+[('D',x,y,'above right=5pt')] for x,y in [(9,9),(4.3,4.7),(0.8,7.2)]],columns=2,size=7.4)

## figure [2-3]
board(m_tri,[(9,9),(4,5),(6,2.5),(6,1)])

## figure [4-5]
board(u_tri,[(9.8,9),(5,5),(6.25,2.5),(1,6)])

## text [2-3, 4-5]
\newpage

## prompt [2-3, 4-5]
Draw the split you found for each position of D, and mark a point its two regions share.

## figure [2-3]
recording_boards([m_tri+[('D',x,y,'above right=5pt')] for x,y in [(9,9),(4,5),(6,2.5),(6,1)]])

## figure [4-5]
recording_boards([u_tri+[('D',x,y,'above right=5pt')] for x,y in [(9.8,9),(5,5),(6.25,2.5),(1,6)]])
