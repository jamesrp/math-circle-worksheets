+++
id = "w50.closer-staircase"
title = "A staircase closer to the diagonal"
grades = ["K-1", "2-3", "4-5"]
route = "first"
scale = "actual"
kernel = "Staircases can get as close to the diagonal as you like, yet every one stays 280 mm long; the diagonal is 200 mm."
+++

## prompt [K-1]
Make a staircase that stays inside the gray strip, closer to the shortcut than this one reaches. Compare the staircase lengths with string.

## prompt
Make a staircase inside the gray strip, with a smaller greatest vertical gap from the diagonal than this path. Compare the two staircase lengths with the diagonal's length.

## figure
diagram(45, [(stairs(4), 'line width=1.1pt')], corridor=15)

## text @10,184 w=174 [K-1]
The straight diagonal is 200 mm long.

## text @10,184 w=174
The straight diagonal is 200 mm long. The strip reaches 15 mm vertically above and below it.

## figure
calibration()

## key
The given four-step staircase reaches a greatest vertical gap of \textbf{30 mm}. One improvement is eight repetitions of right 20, up 15, whose greatest gap is \textbf{15 mm}; it stays within the gray strip, including its boundary. Both staircases have length \textbf{280 mm}, whereas the diagonal is \textbf{200 mm}. Along each segment the signed gap is linear, so checking its endpoints controls the whole segment.
