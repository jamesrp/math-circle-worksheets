+++
id = "w16.routes"
title = "Doors and routes on a printed filling"
grades = ["2-3", "4-5"]
route = "first"
page = "new"
kernel = "Routes through R-B doors pair outside doors two at a time or end in a triangle with R, B and Y; an odd number of outside doors leaves one unpaired."
+++

## prompt [2-3]
An edge with R at one end and B at the other is a door. Mark every door. Draw every route that starts at an outside door. A route must leave a two-door triangle through its other door; it stops at a one-door triangle or outside. Which entrances lead back outside?

## prompt [4-5]
Call an edge with R at one end and B at the other a door. Mark every door. A route crosses through doors and uses no door twice. In a two-door triangle it must use both doors. Draw all the routes, including any that stay inside the big triangle. Can every route from outside return outside?

## figure [2-3]
door_example()+board(3,width=4.8,labels=R3)

## figure [4-5]
door_example()+board(4,width=4.8,labels=R4)
