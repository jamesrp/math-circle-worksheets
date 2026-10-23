+++
id = "w18.shortest-two"
title = "The shortest key for two pictures"
grades = ["K-1", "2-3"]
route = "return"
kernel = "Two pictures need rows of three counters: two-counter rows always share a possible received row."
+++

## prompt [K-1]
Make two two-counter rows for the pictures. Can you keep the changer from fooling the receiver?

## prompt [2-3]
Make a key for the two pictures with 1, 2, or 3 counters in each row. What is the shortest length that always works? Explain why no shorter key works.

## figure [K-1]
''.join(keyed(.35,y,'triangle','--')+keyed(9.7,y,'square','--') for y in [4,9,14,19])

## figure [2-3]
''.join(keyed(1,y,'triangle','-'*n,2,small=True)+keyed(10.2,y,'square','-'*n,2,small=True) for y,n in [(3.8,1),(9.6,2),(15.4,3)])
