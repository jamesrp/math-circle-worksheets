+++
id = "w77.matching-counts"
title = "Gone at stage 5? Two triangles and the square"
grades = ["4-5"]
route = "first"
page = "new"
kernel = "On two triangles meeting at a dot, either first loop can be gone at stage 5; on the square only a triangle rim can, since the outer rim needs both tiles. All these builds have the same hole counts, so counts do not tell when the first loop disappears."
+++

## text
\promptat{0}

## prompt
Start with the four solid edges. Add one dashed edge at stage 2 and the other at stage 4. Fill one triangle at stage 5 and the other at stage 8. Whichever dashed edge comes first, can the first loop be gone at stage 5? Answer the same question for the square in Problem 2. Save the first loop's edges each time, and record a schedule your partner can replay or explain why there is none.

## text
\begin{scope}[shift={(3.25,4.55)}]
 \coordinate (A) at (0,0);\coordinate (B) at (0,5.8);\coordinate (C) at (5.8,1.4);\coordinate (D) at (11.6,0);\coordinate (E) at (11.6,5.8);
 \draw[line width=1.5pt] (A)--(C)--(B) (D)--(C)--(E);
 \draw[black!50,dash pattern=on 4pt off 4pt,line width=.9pt] (A)--(B) (D)--(E);
 \foreach \v/\pos in {A/above left,B/below left,C/below,D/above right,E/below right}{\fill (\v) circle(2.2pt);\node[\pos,inner sep=4pt,font=\large] at (\v) {\v};}
\end{scope}
\smallat{0}{11.45}{8.7}{AB first:}
\lineat{0}{12.55}{8.7}\lineat{0}{13.85}{8.7}
\smallat{9.5}{11.45}{8.7}{DE first:}
\lineat{9.5}{12.55}{18.2}\lineat{9.5}{13.85}{18.2}
\smallat{0}{14.75}{18.2}{Square:}
\lineat{0}{15.85}{18.2}\lineat{0}{17.15}{18.2}
\textat{0}{18.0}{18.2}{Count each enclosed, unfilled region as one hole. Every build on these two boards has 0, 1, 2, 1, 0 holes after stages 0, 2, 4, 5, 8. Can those counts alone tell you when the first loop disappears?}
\lineat{0}{20.55}{18.2}\lineat{0}{21.85}{18.2}
