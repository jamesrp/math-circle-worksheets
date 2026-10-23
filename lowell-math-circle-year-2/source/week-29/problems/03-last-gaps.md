+++
id = "w29.last-gaps"
title = "Last impossible lengths for 3 and 5, and for 4 and 5"
grades = ["4-5"]
route = "first"
kernel = 'The last gaps are 7 for 3/5 and 11 for 4/5, each settled by a run of consecutive builds as long as the shorter rod.'
+++

## prompt
Find the last impossible length for each pair: 3 and 5; 4 and 5. For each pair, give a finite collection of builds that settles every longer target.

## figure
draw(*[step for i, s in enumerate(['3 and 5', '4 and 5']) for step in (('text', 0, 2.4 + i * 10, s, 18.5, 14, False), ('ruled', 4 + i * 10, 6))])

## key
\emph{Print guide, p. 3.} Last gaps: 3/5 $\to$ 7; 4/5 $\to$ 11. Certificates: 8,9,10 as above; 12=4+4+4, 13=4+4+5, 14=4+5+5, 15=5+5+5. For gap 11 with 4/5, zero, one, two 5-rods leave 11,6,1, none divisible by 4.
