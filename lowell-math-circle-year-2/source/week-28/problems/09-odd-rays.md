+++
id = "w28.odd-rays"
title = "Patterns with an odd number of rays"
grades = ["4-5"]
route = "first"
kernel = "Each fold flips which face is up, so a flat fold around one point needs an even number of creases."
+++

## prompt size=14
Can any of these patterns close flat along every ray? Explain an answer that covers all three patterns.

## figure
odd_ray_disks()

## key
\begin{tabular}{llll}
Case & Consecutive angles & Number of active rays & Answer\\
A & 120$^\circ$,120$^\circ$,120$^\circ$ & 3 & Impossible\\
B & 60$^\circ$,60$^\circ$,60$^\circ$,90$^\circ$,90$^\circ$ & 5 & Impossible\\
C & 30$^\circ$,30$^\circ$,60$^\circ$,60$^\circ$,60$^\circ$,60$^\circ$,60$^\circ$ & 7 & Impossible\\
\end{tabular}

The orientation-parity proof on page 5 covers all three. The sectors sum to 360$^\circ$ in each case, so a missing wedge is not the obstruction.
