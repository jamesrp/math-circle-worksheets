+++
id = "w93.tile-rectangles"
title = "Every rectangle from 24 tiles"
grades = ["3-5"]
route = "first"
kernel = 'The rectangles of area 24 are 1 by 24, 2 by 12, 3 by 8 and 4 by 6; 4 by 6, with the closest sides, is nearest a square.'
+++

## prompt
Use 24 square tiles to make every different rectangle you can. Draw your collection. Which rectangle comes closest to being a square?

## text
\vspace{3mm}
\begin{center}
\begin{tikzpicture}[x=0.7cm,y=0.7cm]
\draw[step=1,gray!40,very thin] (0,0) grid (24,20);
\draw[gray] (0,0) rectangle (24,20);
\end{tikzpicture}
\end{center}
\vfill
