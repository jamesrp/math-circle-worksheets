+++
id = "w10.k1-end-where-started"
title = "End on the island where you started"
grades = ["K-1"]
route = "return"
page = "new"
+++

## prompt
Pick up every counter and end on the island where you started.
Put a check in the box if you can and an X if you cannot.

## figure
figs([[k1_town(4, row_doubles('k4a'), below='side')],
      [k1_town(4, double_then_single('k4b'), below='side')],
      [k1_town(4, square_double_side('k4c'), below='side')]],
     [[k1_town(4, flower('k4d'), below='side')]],
     [[k1_town(4, ladder_double_rung('k4e'), below='side')]], vgap=1.0)
