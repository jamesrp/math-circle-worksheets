+++
id = "w64.corner-groups"
title = "Which corners become one point"
grades = ["shared"]
route = "return"
kernel = "All eight octagon corners become one point; the square's four corners also become one point."
+++

## figure
page_start()

## prompt @.48
Match same-letter edges with their arrows pointing the same way. Which numbered corners become the same point? Put corners that meet in one group. Find all the groups for the octagon and for the square.

## figure
fig(octagon(2.50,4.05,4.02,numbers=True), square(6.08,3.55,1.72,numbers=True), lines(6.75,7,.36))
