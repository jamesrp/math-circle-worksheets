+++
id = "w64.must-it-close"
title = "Must every whole-number direction close or reach a corner?"
grades = ["shared"]
route = "return"
kernel = 'A whole-number direction repeats its position in a square after a fixed block, and the block permutes the three squares, so within three blocks the trip closes unless it reaches a corner first.'
+++

## figure
page_start('Grades 4--5')

## prompt @.48
Try each of these straight directions from S. Each arrow gives a number of grid squares right and up. Which paths close, and which reach a corner? Must every straight direction with positive whole-number right and up amounts eventually close or reach a corner? Explain your answer.

## figure
fig(direction_arrows(), lshape(3.7,2.89,2.20,[('A',(.5,.25),'S')],None), lines(7.78,5,.34))
