+++
id = "w88.upper-bounds"
title = "Why no bigger ring in Problems 3-5"
grades = ["K-5"]
route = "return"
page = "new"
kernel = "Each neighbouring pair needs a least angle at the middle; adding the least angles round the ring proves the maxima 9, 4, 8 and 5."
+++

## prompt
For each of Problems 3--5, what is the largest possible ring? Explain why no ring can have more outside disks.

## text
\vspace{2mm}
\begin{center}\begin{tikzpicture}[x=1mm,y=1mm]
\foreach \x/\y/\r/\txt in {0/0/12/80,80/0/6/40,0/-80/12/80,80/-80/6/40}{
\draw[thick,fill=black!6] (\x,\y) circle (\r);
\fill (\x,\y) circle (.5);
\node[below] at (\x,{\y-\r-3}) {\txt\ mm middle};}
\node at (0,35) {40 mm outside};
\node at (80,35) {80 mm outside};
\node at (0,-45) {Both sizes outside};
\node at (80,-45) {Both sizes outside};
\node at (40,-115) {Sketches, not actual size};
\path[use as bounding box] (-35,40) rectangle (115,-118);
\end{tikzpicture}\end{center}
