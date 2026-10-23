+++
id = "w64.one-right-one-up"
title = "One right, one up: the order of the dots"
grades = ["shared"]
route = "return"
kernel = 'In direction (1,1) one block sends A to B to C and back, so each trip visits all three dots before returning.'
+++

## figure
page_start('Grades 4--5')

## prompt @.48
Find the first closed trip from each dot in the marked direction. In what order does each trip visit the three dots before returning to its starting dot?

## text @0,1.32 w=7.3 size=12.5
The travel arrows go one small grid square right and one up.

## figure
fig(lshape(3.70,2.00,2.52,[(sq,(.5,.25),'') for sq in 'ABC'],(1,1)), lines(7.64,5,.35))
