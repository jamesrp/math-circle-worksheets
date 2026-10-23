+++
id = "w56.sides-and-corners"
title = "Separate face sides and corners against the assembled solid"
grades = ["shared"]
route = "first"
page = "new"
kernel = 'Each assembled edge joins two face sides, so edges are half the separate sides; corners gather in different numbers, so the cube and octahedron both have 24 face corners but 8 and 6 vertices.'
+++

## prompt
Imagine cutting every face free. Find a rule that turns the number of separate face sides into the assembled edge count. Can the separate face-corner count alone tell you the vertex count?

## text
\begin{center}
\begin{tikzpicture}[x=.75cm,y=.75cm,font=\small]
 \draw[fill=blue!8] (0,0)--(1.3,0)--(.65,1.1258)--cycle;
 \draw[fill=blue!8] (1.6,0)--(2.9,0)--(2.25,1.1258)--cycle;
 \draw[very thick] (1.3,0)--(.65,1.1258) (1.6,0)--(2.25,1.1258);
 \node[below,align=center] at (1.45,-.15) {separate sides\\and corners};
 \draw[-{Latex}] (3.3,.55)--(4.1,.55);
 \draw[fill=blue!8] (4.6,0)--(5.9,0)--(5.25,1.1258)--cycle;
 \draw[fill=blue!18] (5.9,0)--(6.55,1.1258)--(5.25,1.1258)--cycle;
 \draw[very thick] (5.9,0)--(5.25,1.1258);\fill (5.9,0) circle (2pt);\fill (5.25,1.1258) circle (2pt);
 \node[below,align=center] at (5.55,-.15) {joined edge\\and endpoints};
\end{tikzpicture}
\end{center}

\begin{center}\renewcommand{\arraystretch}{1.1}
\begin{tabular}{|m{4.7cm}|>{\centering\arraybackslash}m{2.6cm}|>{\centering\arraybackslash}m{2.6cm}|>{\centering\arraybackslash}m{2.6cm}|>{\centering\arraybackslash}m{2.6cm}|}
\hline Faces before assembly & Separate sides & Assembled edges & Separate corners & Assembled vertices\\\hline
6 squares: cube &&&&\\[36pt]\hline
4 triangles: tetrahedron &&&&\\[36pt]\hline
2 triangles and 3 squares: prism &&&&\\[36pt]\hline
8 triangles: octahedron &&&&\\[36pt]\hline
\end{tabular}\end{center}
\blank{.2cm}\workbox{4.9}
