+++
id = "w56.gaps-of-four-solids"
title = "The gap at every vertex, and all the gaps together"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'A vertex gap is $360^\circ$ minus its face angles; on the cube, tetrahedron, prism and octahedron the gaps total $720^\circ$, two full turns.'
+++

## text
A full turn is $360^\circ$. An equilateral triangle corner is $60^\circ$; a square corner is $90^\circ$. A vertex's gap is $360^\circ$ minus its face-corner angles.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \draw[fill=blue!8] (-.8,0)--(.2,0)--(-.3,.866)--cycle;
 \draw[fill=blue!8] (.45,0)--(1.45,0)--(.95,.866)--cycle;
 \node at (.3,-.55) {$60^\circ+60^\circ$};
 \draw[-{Latex}] (1.85,.3)--(2.55,.3);
 \begin{scope}[shift={(4.1,.3)}]
  \draw[gray!55] (0,0) circle (1.08);
  \draw[fill=blue!8] (0,0)--(1,0)--(.5,.866)--cycle;
  \draw[fill=blue!8] (0,0)--(.5,.866)--(-.5,.866)--cycle;
  \draw[very thick,gray!65] (120:1.08) arc (120:360:1.08);
  \fill (0,0) circle (1.5pt);\node at (.1,-1.5) {corners use $120^\circ$};
 \end{scope}
 \draw[-{Latex}] (5.55,.3)--(6.2,.3);
 \node[align=center] at (8,.3) {$360^\circ-120^\circ$\\[4pt]gap $=240^\circ$};
\end{tikzpicture}
\end{center}

## prompt
Find the gap at every vertex of each closed model. How many full turns do all its gaps make together?

## text
\begin{center}\renewcommand{\arraystretch}{1.1}
\begin{tabular}{|m{3.1cm}|>{\centering\arraybackslash}m{2.6cm}|>{\centering\arraybackslash}m{3.6cm}|>{\centering\arraybackslash}m{2.7cm}|>{\centering\arraybackslash}m{3.2cm}|}
\hline Model & Vertices & Face corners at one vertex & Gap at one vertex & All gaps together\\\hline
Cube &&&&\\[43pt]\hline
Tetrahedron &&&&\\[43pt]\hline
Triangular prism &&&&\\[43pt]\hline
Octahedron &&&&\\[43pt]\hline
\end{tabular}\end{center}
\blank{.15cm}\workbox{4.2}
