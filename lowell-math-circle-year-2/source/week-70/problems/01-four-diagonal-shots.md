+++
id = "w70.four-diagonal-shots"
title = "The fewest shields for the diagonal shots"
grades = ["4-5"]
route = "first"
kernel = "The four corner-to-centre shots share no point, so at least four shields are needed."
+++

## prompt
Finish the four diagonal shots. Choose one shield arrangement for the room that stops all six shots. Use as few shields as you can. Your partner checks the shot lines and shields.

## text
\begin{center}
\room[{\foreach\a/\b/\c/\d in{0/0/.65/.65,4/0/3.35/.65,0/4/.65/3.35,4/4/3.35/3.35}{\draw[-{Stealth[length=6pt]},very thick](\a,\b)--(\c,\d);}
\draw[thick,-{Stealth[length=5pt]}](0,0)--(4/3,4);\draw[thick,-{Stealth[length=5pt]},shorten >=4pt](4/3,0)--(2,2);
\draw[thick,-{Stealth[length=5pt]}](0,0)--(4,4/3);\draw[thick,-{Stealth[length=5pt]},shorten >=4pt](0,4/3)--(2,2);
\foreach\p in{(4/3,4),(4/3,0),(4,4/3),(0,4/3)}{\draw\p circle(3.5pt);}}]{1.9}{0}
\end{center}
\vfill
Our fewest shields: \rule{.9in}{.3pt}
