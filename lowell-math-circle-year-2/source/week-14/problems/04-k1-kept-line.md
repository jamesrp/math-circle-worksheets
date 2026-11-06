+++
id = "w14.k1-kept-line"
title = "Completions that keep a printed line"
grades = ["K-1"]
route = "return"
kernel = "A kept diagonal splits the polygon into pieces filled independently, so the completions multiply: 2 for the pentagon, $2\\times 2$ for the hexagon."
+++

## prompt
Fill each shape with triangles, keeping the printed line. Find every way.

## figure
k1_kept_line()

## key
Keeping 13 in the pentagon leaves a quadrilateral with two choices. Keeping 14 in the hexagon leaves two quadrilaterals, each with two independent choices: four completions. Only two pentagon completions exist, so one of the three pre-lined pentagons stays empty, and two of the six pre-lined hexagons stay empty; the spares keep the boards from giving the count away.

## hints
The required diagonal is printed on every board; if a child erases it, redraw it on a spare board from the packet's last page. If one hexagon side is always filled the same way, ask whether its quadrilateral has another filling. Combining each left choice with each right choice proves completeness.
