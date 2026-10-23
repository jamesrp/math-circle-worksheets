+++
id = "w64.two-right-one-up"
title = "Two right, one up: short and long trips"
grades = ["shared"]
route = "return"
kernel = 'In direction (2,1) the block permutation fixes one square and swaps the other two, so one start returns after one block and the others after two.'
+++

## figure
page_start('Grades 4--5')

## prompt @.48
Find the first closed trip from each dot in the marked direction. Which starting squares give the shortest trip? How many times as long are the other trips?

## text @0,1.32 w=7.30 size=12.5
The travel arrows go two small grid squares right and one up.

## figure
fig(lshape(3.70,2.00,2.52,[(sq,(.25,.5),'') for sq in 'ABC'],(2,1)), lines(7.64,5,.35))
