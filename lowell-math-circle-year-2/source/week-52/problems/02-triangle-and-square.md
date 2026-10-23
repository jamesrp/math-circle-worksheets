+++
id = "w52.triangle-and-square"
title = "Change a triangle and a square"
grades = ["K-5"]
route = "first"
kernel = 'Fixed bar lengths make a hinged triangle rigid; a hinged square shears into rhombi.'
+++

## prompt
Can you change the shape of the triangle and the square? Draw the shapes you can make.

## text
\vspace{12pt}
\begin{minipage}[t]{0.46\linewidth}\centering
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=2pt] (0,0)--(4,0)--(2,3.4641)--cycle;
\foreach \p in {(0,0),(4,0),(2,3.4641)}{\filldraw[fill=white,line width=0.8pt] \p circle (3pt);}
\end{tikzpicture}
\par\vspace{18pt}\spacebox{7.2}{5.6}
\end{minipage}\hfill
\begin{minipage}[t]{0.46\linewidth}\centering
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=2pt] (0,0) rectangle (4,4);
\foreach \p in {(0,0),(4,0),(4,4),(0,4)}{\filldraw[fill=white,line width=0.8pt] \p circle (3pt);}
\end{tikzpicture}
\par\vspace{18pt}\spacebox{7.2}{5.6}
\end{minipage}
