+++
id = "w64.trip-lengths"
title = "All the lengths of right-going trips"
grades = ["shared"]
route = "first"
kernel = 'Right-going trips are middle loops (one width) or outer loops whose two chords trade length, so every outer trip has the same total; starts in line with a corner hit it.'
+++

## figure
page_start()

## prompt @.48
Choose starting dots inside the octagon and head to the right. Find all the different lengths of a closed trip that you can. Mark the starting places that give each length, and the starting places whose paths hit a corner. Count only the lines inside the octagon when you measure a trip.

## figure
fig(octagon(3.7,4.80,5.35,ticks=True), lines(8.03,4,.36))
