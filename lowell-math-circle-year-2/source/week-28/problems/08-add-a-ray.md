+++
id = "w28.add-a-ray"
title = "Add one ray to make a flat pattern"
grades = ["2-3"]
route = "return"
kernel = "Given rays at 0, a and 180 degrees, the only fourth ray that balances the alternating sectors is at 360 minus a degrees."
+++

## prompt
Add one ray to each pattern so the two alternating groups of wedges both make a half-turn. Make a flat fold of each completed pattern.

## figure
add_ray_starts()

## key
\begin{tabular}{llll}
Case & Given rays clockwise from top & Add ray at & Final sectors clockwise\\
A & 0$^\circ$,90$^\circ$,180$^\circ$ & 270$^\circ$ & 90$^\circ$,90$^\circ$,90$^\circ$,90$^\circ$\\
B & 0$^\circ$,60$^\circ$,180$^\circ$ & 300$^\circ$ & 60$^\circ$,120$^\circ$,120$^\circ$,60$^\circ$\\
C & 0$^\circ$,30$^\circ$,180$^\circ$ & 330$^\circ$ & 30$^\circ$,150$^\circ$,150$^\circ$,30$^\circ$\\
D & 0$^\circ$,120$^\circ$,180$^\circ$ & 240$^\circ$ & 120$^\circ$,60$^\circ$,60$^\circ$,120$^\circ$\\
\end{tabular}

Each completion is a two-book-fold model of page 3 with the second fold at a; VVVM is a witness.
