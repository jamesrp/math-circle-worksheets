+++
id = "w65.two-crossings-away"
title = "Rooms two door crossings from Home"
grades = ["3-5"]
route = "return"
kernel = "Two crossings from Home give 8 x 7 = 56 routes but only 48 rooms, since each of Home's 8 corners has one room reached two ways; on squares 4 x 3 - 4 = 8. The octagon floor grows much faster."
+++

## prompt @.65,10.13
On this octagon floor every room has 8 doors. Only the rooms around Home are drawn; the floor goes on. How many rooms can you reach from Home in 2 door crossings but not fewer? How many on this square floor, where every room has 4 doors?

## figure
first_ring(center=(2.95, 6.95), scale=2.3)

## text @.75,4.45 w=4.0
Octagon floor: \rule{1.0in}{0.35pt} rooms

## figure
square_floor(size=.45, center=(6.6, 6.95))

## text @5.45,4.45 w=2.5
Square floor: \rule{.8in}{0.35pt} rooms
