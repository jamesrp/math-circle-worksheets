+++
id = "w45.k1-three-tickets"
title = "Three tickets where red always hides blue"
grades = ["K-1"]
route = "return"
page = "same"
kernel = "Only ticket 3 shows red over blue, so the cup must hold 3 and no 1 or 2: {3,4,5}, {3,4,6}, {3,5,6}."
+++

## prompt @18
Choose three tickets so red sometimes shows and then always hides blue. Find every choice that works.

## figure
ticket_slots(21.2,3)
