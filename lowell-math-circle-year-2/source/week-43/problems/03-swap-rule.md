+++
id = "w43.swap-rule"
kind = "setup"
title = "The two-swap rule with tickets"
grades = ["K-1", "2-3", "4-5"]
route = { "K-1" = ["first", "return"], "2-3" = ["first", "return"], "4-5" = "first" }
+++

## text @0 size=13 [K-1]
Start A B C. Pick a ticket from 1, 2, 3 and swap that slot with slot 1. Then pick from 2, 3 and swap that slot with slot 2. A slot may swap with itself.

## text @0 size=13
Start A B C. Mix tickets 1, 2, 3 in the cup; draw and swap its slot with slot 1. Empty the cup, then mix tickets 2, 3; draw and swap its slot with slot 2. At each draw, all tickets in the cup have equal chances. Reset both sets for every new row. A slot may swap with itself.

## figure
swap_picture(0)
