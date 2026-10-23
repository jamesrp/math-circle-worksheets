+++
id = "w86.rules"
title = "Chasing-game rules and the star example"
kind = "setup"
grades = ["2-5", "4-5"]
route = { "2-5" = "first", "4-5" = ["first", "return"] }
+++

## text @0,0 w=192 size=11
One player controls C; the other controls R. C chooses a dot first, then R chooses. C takes the first turn. On your turn, stay or take one road to the next dot. Flip the turn tile even if you stay. Sharing a dot means immediate capture. Both counters stay visible. Swap jobs between games.

## figure
star_example([({'w': 'C', 'y': 'R'}, 'Start', 'C turn'),
              ({'x': 'C', 'y': 'R'}, 'C takes one road', 'R turn'),
              ({'x': 'C', 'y': 'R'}, 'R stays', 'C turn')])
