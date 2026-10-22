+++
id = "w50.fewest-turns"
title = "Fewest turns inside the strip"
grades = ["K-1", "2-3", "4-5"]
route = "return"
scale = "actual"
kernel = "Inside the ±15 mm strip the fewest turns is 8; a horizontal piece spans at most 40 mm (20 mm at either end)."
app = "Memory robot / Staircases group (docs/stairs/README.md in small-math-adventure)"
+++

## prompt [K-1]
Make a staircase inside the gray strip with as few turns as you can. Its pieces may follow the edge of the strip.

## prompt
Find the fewest turns possible for an S-to-F staircase inside the gray strip. Its pieces may follow the strip's boundary. Explain why fewer turns cannot work.

## figure
diagram(45, corridor=15)

## text @10,184 w=174 [2-3, 4-5]
The gray strip reaches 15 mm vertically above and below the dotted diagonal, clipped by the rectangle.

## figure
calibration()

## key
The fewest turns is \textbf{8}. A boundary-following witness, in millimeters from S, is (0,0), (20,0), (20,30), (60,30), (60,60), (100,60), (100,90), (140,90), (140,120), (160,120). Its nine nonzero segments make eight direction changes. All vertices have vertical gap in $[-15,15]$; linearity gives the same for the full path.

## key-figure
diagram(0, [(EIGHT_TURNS, 'line width=1.4pt')], corridor=15)

## key
\textbf{Why seven turns cannot work.} Inside the strip, a horizontal segment can span at most 40 mm: crossing a vertical-gap range of 30 takes $30/(3/4)=40$. A horizontal segment beginning at S or ending at F can span at most 20 mm. With at most seven turns, there are at most eight alternating horizontal/vertical segments. If there are four horizontal segments, at least one is an endpoint segment, so horizontal travel is at most $20+3\times40=140$ mm; if there are fewer, it is at most 120 mm. Neither reaches the required 160 mm.
