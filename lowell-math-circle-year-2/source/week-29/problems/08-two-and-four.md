+++
id = "w29.two-and-four"
title = "Lengths 1 through 12 with 2-rods and 4-rods"
grades = ["K-1"]
route = "return"
kernel = '2-rods and 4-rods build exactly the even lengths, since both are made of whole pairs of units.'
+++

## prompt
Use 2-rods and 4-rods to build lengths from 1 through 12. Show why some lengths cannot be built.

## figure
draw(('rodkey', [2, 4], 1.8), ('targets', range(1, 13), 4, 6), ('ruler', 0, 9, 12), ('ruler', 0, 13, 12), ('ruled', 18, 4))

## key
\emph{Print guide, p. 2.} Exactly 2,4,6,8,10,12 work. Both rods are made of whole pairs of units; joining them always leaves an even length. Every positive even length is made from 2-rods.
