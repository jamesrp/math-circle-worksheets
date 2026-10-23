+++
id = "w65.room-routes"
title = "Room routes from Home to the star"
grades = ["3-5"]
route = "return"
kernel = "Different door routes can end in the same room: two 2-crossing routes and eight 4-crossing routes lead from Home to the star."
+++

## text @.65,10.13
For room routes, put a coin inside a room. A door crossing moves it across one shared side into the next room. Crossing a corner is not allowed. Write the rooms in the order you visit them.

## figure
door_example(r'$C\ \rightarrow\ D\ \rightarrow\ E$\\[5pt]Two door crossings')

## prompt @.65,8.29
This is another view of the same geometry, showing four rooms around one corner. Find every room route from Home to $\star$ using exactly 2 door crossings. Then find every route using exactly 4 door crossings. Stay in these four rooms. You may visit a room or use a door more than once.

## figure
four_rooms()

## text @.65,.92 size=10.5
Keep the route sheet beside this board.
