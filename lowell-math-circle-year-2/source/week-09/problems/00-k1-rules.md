+++
id = "w09.k1-rules"
kind = "setup"
title = "Rules: the ball, its bounces and the partner game"
grades = ["K-1"]
route = ["first", "return"]
+++

## figure
rules_block("""The ball rolls on a table. It starts at the dot and rolls across the squares from corner to corner. It bounces off the walls and stops when it gets to a corner of the table. Each time it hits a wall is one bounce. Stopping at the corner is not a bounce.

Partners take turns. One puts a counter on the corner where they think the ball will stop, and the other moves a counter along the path and draws it with a crayon.""",
            table(5, 3, 0.5, path_steps=4, arrow=True)) + vspace(0.15)
