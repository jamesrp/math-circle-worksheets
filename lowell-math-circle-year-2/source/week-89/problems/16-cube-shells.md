+++
id = "w89.cube-shells"
title = "Grow solid cubes"
grades = ["K-5"]
route = "return"
page = "new"
kernel = "The shells from side 1 to 4 have 7, 19 and 37 cubes."
+++

## prompt
Grow a solid cube from side 1 to side 2, then to side 3, then to side 4. Each time keep the old cube in one corner. How many new cubes belong to each shell?

## text
\begin{center}\begin{tikzpicture}[x={(8mm,0)},y={(4mm,3mm)},z={(0,8mm)}]
\foreach \a/\xx in {1/0,2/4,3/9}{
\begin{scope}[shift={(\xx,0,0)}]
\fill[black!5] (0,0,0)--(\a,0,0)--(\a,0,\a)--(0,0,\a)--cycle;
\fill[black!18] (\a,0,0)--(\a,\a,0)--(\a,\a,\a)--(\a,0,\a)--cycle;
\fill[black!10] (0,0,\a)--(\a,0,\a)--(\a,\a,\a)--(0,\a,\a)--cycle;
\foreach \k in {0,...,\a}{\draw (\k,0,0)--(\k,0,\a)--(\k,\a,\a);\draw (0,0,\k)--(\a,0,\k)--(\a,\a,\k);\draw (0,\k,\a)--(\a,\k,\a)--(\a,\k,0);}
\node at (\a/2,0,-.65){side \a};
\end{scope}}
\end{tikzpicture}\end{center}
\answer{30mm}
