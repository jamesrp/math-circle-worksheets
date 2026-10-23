+++
id = "w29.from-some-point-on"
title = "Every length from some point on"
grades = ["K-1", "2-3"]
route = "return"
kernel = 'Three consecutive builds with 3-rods (6, 7, 8 for 3/4; 8, 9, 10 for 3/5) grow by added 3-rods into every longer length.'
+++

## prompt [K-1]
Use 3-rods and 4-rods to build every length from 6 through 18. Could you keep going forever?

## prompt [2-3]
Can 3-rods and 4-rods build every length after 16? Can 3-rods and 5-rods build every length after 20? Explain how you know.

## figure [K-1]
draw(('targets', range(6, 19), 2, 7), ('ruler', 0, 7, 18), ('ruler', 0, 11, 18), ('ruled', 16, 5))

## figure [2-3]
draw(('rodkey', [3, 4], 2), ('ruled', 5, 6), ('rodkey', [3, 5], 13), ('ruled', 16, 6))


## key [K-1]
\emph{Print guide, p. 2.} Start with 6=3+3, 7=3+4, 8=4+4; add 3 to reach 9,10,11, then 12,13,14, then 15,16,17, then 18. These three chains keep going forever and cover every integer at least 6.

## key [2-3]
\emph{Print guide, p. 3.} Yes to both. Minimal consecutive certificates are 6,7,8 for 3/4 and 8,9,10 for 3/5: add 3-rods to each, so the gaps stop at 5 and 7. Any other finite collection that demonstrably covers every remainder and starts beyond the last gap is acceptable, such as 17,18,19 or 21,22,23.
