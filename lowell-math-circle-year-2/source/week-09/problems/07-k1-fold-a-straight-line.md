+++
id = "w09.k1-fold-a-straight-line"
title = "Fold a straight line into a bouncing path"
grades = ["K-1"]
route = "return"
page = "new"
+++

## prompt
With a ruler, draw a straight line from the dot to the far corner of each big square. Cut out the square and fold it on the dashed lines, with the dot on top. Hold it up to the light, and draw the line you see on the small table next to it.

## figure
vspace(0.2) + row([sheet(2, 1, 1, 2, 0.75, dashed=True), table(1, 2, 0.75),
                   sheet(3, 1, 1, 3, 0.75, dashed=True), table(1, 3, 0.75)], gap=[0.35, 1.2, 0.35])
+ vspace(0.45) + row([sheet(2, 1, 2, 4, 0.75, dashed=True), table(2, 4, 0.75)], gap=0.5)
