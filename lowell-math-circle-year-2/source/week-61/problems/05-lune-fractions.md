+++
id = "w61.lune-fractions"
title = "Fractions of the ball from meridian gaps"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'A lune of angle g covers g/360 of the ball, so the pole triangle with gap g covers g/720: 1/16, 1/12 and 1/6 for gaps 45, 60 and 120 degrees.'
+++

## text
\band{3--5}
A \textit{lune} is the strip between two great-circle semicircles from $N$ to its opposite pole $S$. The strip's angle is the gap between them at $N$. Fractions refer to the ball's surface.

\begin{center}\begin{tabular}{ccc}
\luneexample &
\begin{tikzpicture}[x=.72in,y=.72in]\path[use as bounding box] (-1.15,-1.2) rectangle (1.15,1.2);\foreach \a in {0,40,...,320}{\draw[ink!65] (0,0)--(\a:1);}\fill[blue!22] (0,0)--(0:1) arc (0:40:1)--cycle;\draw[ink] (0,0) circle (1);\node[font=\small] at (20:.69) {$40^\circ$};\node[font=\scriptsize,anchor=north] at (0,-1.06) {View down toward $N$};\end{tikzpicture}&
\begin{tikzpicture}[x=.72in,y=.72in]\path[use as bounding box] (-1.15,-1.2) rectangle (1.15,1.2);\node[font=\normalsize] at (0,.18) {$360\div40=9$};\node[font=\normalsize] at (0,-.28) {One lune: $\frac19$ of the surface};\end{tikzpicture}\\
\small $40^\circ$ lune & \small 9 equal lunes fill the ball & \small Area record
\end{tabular}\end{center}

## prompt
Use the marked meridian pairs with gaps $45^\circ$, $60^\circ$, and $120^\circ$. For each pair, make a triangle with $N$ and the two equator points. What fraction of the ball's surface does each triangle cover?

## text
\begin{center}\begin{tabular}{>{\centering\arraybackslash}p{1.55in}|>{\centering\arraybackslash}p{1.55in}|>{\centering\arraybackslash}p{1.55in}}
$45^\circ$ gap & $60^\circ$ gap & $120^\circ$ gap\\[6pt]
\begin{tikzpicture}[x=.67in,y=.67in]\draw[ink!60] (0,0) circle (1);\path[use as bounding box] (-1.1,-1.1) rectangle (1.1,1.1);\end{tikzpicture}&
\begin{tikzpicture}[x=.67in,y=.67in]\draw[ink!60] (0,0) circle (1);\path[use as bounding box] (-1.1,-1.1) rectangle (1.1,1.1);\end{tikzpicture}&
\begin{tikzpicture}[x=.67in,y=.67in]\draw[ink!60] (0,0) circle (1);\path[use as bounding box] (-1.1,-1.1) rectangle (1.1,1.1);\end{tikzpicture}\\[22pt]
Fraction: \rule{.8in}{.3pt}&Fraction: \rule{.8in}{.3pt}&Fraction: \rule{.8in}{.3pt}\\[8pt]
\end{tabular}\end{center}
\writing{6}
