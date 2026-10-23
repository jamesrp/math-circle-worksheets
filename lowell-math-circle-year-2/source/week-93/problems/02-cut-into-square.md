+++
id = "w93.cut-into-square"
title = "Cut a rectangle into its average-side square"
grades = ["3-5"]
route = "first"
page = "new"
kernel = 'The square whose side is the average of the sides holds the rectangle with one square of side half the difference left over.'
+++

## prompt
Cut each rectangle into pieces and fit all its pieces inside the matching square, without overlaps. Can the uncovered part be a single square, of any size, in each case? Find its side length.

## text
\begin{center}
\begin{tikzpicture}[x=1.5cm,y=1.5cm]
\unitrect{0}{6}{6}{2}{A}
\unitrect{7}{5}{4}{4}{A}
\unitrect{0}{0.5}{4}{2}{B}
\unitrect{7}{0}{3}{3}{B}
\unitrect{0}{-3.5}{5}{1}{C}
\unitrect{7}{-4.5}{3}{3}{C}
\end{tikzpicture}
\end{center}
\vfill
