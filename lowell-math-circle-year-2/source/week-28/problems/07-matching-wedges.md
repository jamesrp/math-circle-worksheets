+++
id = "w28.matching-wedges"
title = "Do the shaded and white pairs make half-turns?"
grades = ["2-3"]
route = "first"
kernel = "On a four-ray disk, the alternating pairs of sectors either both make exact half-turns or one falls short by what the other exceeds."
+++

## prompt
Use the 16 separate loose wedges cut to match \mbox{A1--A4}, \mbox{B1--B4}, \mbox{C1--C4}, and \mbox{D1--D4}. For each disk, can the shaded pair fill a half-turn exactly, and can the white pair? For any disk that could not close in Problem 2, explain why.

## figure
matching_wedge_disks()

## key
\begin{tabular}{lllll}
Disk & Clockwise sectors 1,2,3,4 & Shaded 1+3 & White 2+4 & Both half-turns?\\
A & 90$^\circ$,90$^\circ$,90$^\circ$,90$^\circ$ & 180$^\circ$ & 180$^\circ$ & Yes\\
B & 45$^\circ$,90$^\circ$,90$^\circ$,135$^\circ$ & 135$^\circ$ & 225$^\circ$ & No\\
C & 60$^\circ$,120$^\circ$,120$^\circ$,60$^\circ$ & 180$^\circ$ & 180$^\circ$ & Yes\\
D & 30$^\circ$,60$^\circ$,150$^\circ$,120$^\circ$ & 180$^\circ$ & 180$^\circ$ & Yes\\
\end{tabular}

For B, the shaded pair falls short by 45$^\circ$ and the white pair exceeds a half-turn by 45$^\circ$. These are exact mismatches in the ideal pattern; imprecise cutting may blur the observation but cannot change the angle sums. The last sentence asks for this: B is the disk that could not close in Problem 2, and its pairs cannot both make a half-turn.
