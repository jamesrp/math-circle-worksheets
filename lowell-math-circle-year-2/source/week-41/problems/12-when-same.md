+++
id = "w41.when-same"
title = "When can two trips home be changed into each other?"
grades = ["4-5"]
route = "return"
kernel = "Two trips from H back to H change into each other by backtracks and square slides exactly when they finish in the same copy: loops on the torus are classified by pairs of whole numbers."
+++

## prompt @27
When can two trips from H back to H be changed into each other? Explain what their finishing copies decide, using the repeated map. Add copies if your journey leaves the page.

## figure
tiled(18,73,60,True)

## key
Exactly when their finishing copies agree. Necessity: a backtrack has zero displacement and either side of a square slide has the same endpoints in the tiled plane. Hence every allowed move preserves the endpoint copy. Sufficiency: square slides commute adjacent perpendicular steps, so a path can be rearranged into horizontal steps followed by vertical steps. Cancel adjacent opposite horizontal steps, then opposite vertical steps. It becomes the canonical path determined by its signed horizontal and vertical displacement. Equal endpoint copies for H-based routes give equal displacements and therefore the same canonical route. Reverse the second path's reduction, using backtrack insertions where needed, to connect the originals.
