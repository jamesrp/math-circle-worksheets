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
two_cases_with_records(5,6,es((1,3)),es((1,4)),keep_edges=True)

## key
Keeping 13 in the pentagon leaves a quadrilateral with two choices. Keeping 14 in the hexagon leaves two quadrilaterals, each with two independent choices: four completions. Only two pentagon completions exist, so two of the four pre-lined pentagon copies stay empty; the spares keep the copies from giving the count away.

## hints
Keep the required printed diagonal visible on every tracing. If one hexagon side is always filled the same way, ask whether its quadrilateral has another filling. Combining each left choice with each right choice proves completeness.
