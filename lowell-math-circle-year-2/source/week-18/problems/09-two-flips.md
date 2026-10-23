+++
id = "w18.two-flips"
title = "The shortest key when two counters may change"
grades = ["2-3"]
route = "return"
kernel = "With up to two hidden changes, two pictures need rows that differ in five places, so five counters."
+++

## prompt
This time the changer may turn over zero, one, or two counters. Make the shortest key you can for the two pictures, using at most five counters in each row. Explain why your length is the shortest.

## figure
''.join(shape(1.9,y+.7,s)+line(3.0,y+1.5,12.7) for y,s in [(4,'triangle'),(7.15,'square'),(13.5,'triangle'),(16.65,'square')])
