+++
id = "w28.alternating-rule"
title = "Every other sector totals a half-turn"
grades = ["4-5"]
route = "first"
kernel = "Following the folded rays around the vertex gives an alternating sum that must be zero, so odd-position and even-position sectors each total 180 degrees (Kawasaki-Justin, necessity)."
+++

## prompt
Explain why every other sector must total $180^\circ$ in any flat-folding pattern with an even number of rays. Which patterns does your explanation rule out?

## figure
alternating_disks()

## key
\begin{tabular}{llll}
Case & Odd sectors & Even sectors & What the proof establishes\\
A & 45+90=135$^\circ$ & 90+135=225$^\circ$ & Ruled out\\
B & 30+60+90=180$^\circ$ & 30+60+90=180$^\circ$ & Not ruled out\\
C & 30+30+90=150$^\circ$ & 30+60+120=210$^\circ$ & Ruled out\\
D & 4$\times$45=180$^\circ$ & 4$\times$45=180$^\circ$ & Not ruled out\\
\end{tabular}

\textbf{Answer:} rule out A and C. Page 5 gives the complete requested proof, including why an apparent full-turn ambiguity cannot produce $\pm$360$^\circ$. In B and D, passing this test does not validate a particular M/V choice; none is prescribed here.
