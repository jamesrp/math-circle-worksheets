+++
id = "w28.ruled-out-labelings"
title = "Rule out the remaining labelings"
grades = ["4-5"]
route = "return"
kernel = "Stacking the four right-angle sectors shows that every flat fold has exactly one exceptional ray, which rules out the other eight of the sixteen labelings."
+++

## prompt
Can any of these labelings close flat? Explain why your folds from Problem 4 and the patterns you rule out account for every M/V labeling of the four-right-angle disk.

## figure
ruled_out_disks()

## key
\begin{tabular}{lll}
Printed case & Word & All cases represented by rotation\\
A & MMMM & MMMM\\
B & VVVV & VVVV\\
C & MMVV & MMVV, MVVM, VVMM, VMMV\\
D & MVMV & MVMV, VMVM\\
\end{tabular}

\textbf{None of A-D can close flat.} Page 6 proves that every legal four-right-angle stack produces exactly one exceptional ray. Consequently four equal labels and every 2-and-2 arrangement are impossible. The table shows that rotations of the printed cases cover all eight invalid words.
