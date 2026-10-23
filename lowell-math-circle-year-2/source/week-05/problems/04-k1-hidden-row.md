+++
id = "w05.k1-hidden-row"
title = "The hidden-row game"
grades = ["K-1"]
route = "first"
page = "new"
+++

## prompt
One partner hides a row of three towers behind a folder and says how many towers you can see from each end. The other builds a row that shows those numbers and draws it, and then you swap.

## figure
close(pic(D.folder_scene((2, 3, 1), cube=0.9, gap=0.45)) + gap(0.3)
      + pic(place([D.chart(3, box=0.85, pitch=1.05)[0] for _ in range(6)], 3, 6.15, 4.3)))
