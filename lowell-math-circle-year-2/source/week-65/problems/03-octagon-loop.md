+++
id = "w65.octagon-loop"
title = "The octagon robot"
grades = ["3-5"]
route = "first"
page = "same"             # on page 2 under the bending-road example
kernel = "Moving and turning left around a right-angle octagon first returns to the start facing the same way after 8 moves, not 4."
+++

## prompt @.65,7.49
Start at A, facing along the road toward B. Move one edge and turn left, over and over. Mark where you are after 4 moves. How many moves make the first return to your starting place, facing the same way? Start toward H and try only right turns.

## figure
octagon_board()

## text @.65,1.08 size=12
Left turns: \rule{0.72in}{0.35pt} moves \hspace{0.5in} Right turns: \rule{0.72in}{0.35pt} moves
