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
Find the first closed trip from each dot in the marked direction. Which dots does each trip pass, and in what order, before it returns to its starting dot?

## figure
fig(lshape(3.70,2.00,2.52,[(sq,(.5,.25),'') for sq in 'ABC'],(1,1)), lines(7.64,5,.35))
