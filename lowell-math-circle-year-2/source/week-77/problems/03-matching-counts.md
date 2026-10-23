+++
id = "w77.matching-counts"
title = "Matching counts, different histories"
grades = ["4-5"]
route = "first"
page = "new"
kernel = "Equal hole counts at every stage do not determine when the first loop disappears."
+++

## text
\promptat{0}

## prompt
Start with the four solid edges. Add one dashed edge at stage 2 and the other at stage 4. Fill one triangle at stage 5 and the other at stage 8. Make one build where the first loop is gone at 5, and another where it first disappears at 8. Save the first loop's edges each time and record a schedule your partner can replay.

## text
\begin{scope}[shift={(3.25,5.45)}]
 \coordinate (A) at (0,0);\coordinate (B) at (0,5.8);\coordinate (C) at (5.8,2.9);\coordinate (D) at (11.6,0);\coordinate (E) at (11.6,5.8);
 \draw[line width=1.5pt] (A)--(C)--(B) (D)--(C)--(E);
 \draw[black!50,dash pattern=on 4pt off 4pt,line width=.9pt] (A)--(B) (D)--(E);
 \foreach \v/\pos in {A/above left,B/below left,C/below,D/above right,E/below right}{\fill (\v) circle(2.2pt);\node[\pos,inner sep=4pt,font=\large] at (\v) {\v};}
\end{scope}
\smallat{0}{12.45}{18.2}{First loop gone at stage 5:}
\lineat{0}{13.55}{18.2}\lineat{0}{14.85}{18.2}
\smallat{0}{16.0}{18.2}{First loop disappears at stage 8:}
\lineat{0}{17.1}{18.2}\lineat{0}{18.4}{18.2}
\textat{0}{19.55}{18.2}{Both builds have 0, 1, 2, 1, 0 holes after stages 0, 2, 4, 5, 8. Can those counts alone tell you when the first loop disappears?}
\lineat{0}{21.85}{18.2}
