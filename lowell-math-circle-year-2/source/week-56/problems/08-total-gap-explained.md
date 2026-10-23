+++
id = "w56.total-gap-explained"
title = "Why every solid has the same total gap"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'Counting face angles face by face gives $180^\circ\sum(n_f-2)=360^\circ(E-F)$, so the total gap is $360^\circ(V-E+F)=720^\circ$.'
+++

## text
The angles of a triangle add to $180^\circ$. A polygon with $n$ sides can be divided into $n-2$ triangles, so its corner angles add to $180(n-2)^\circ$.
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \foreach \s/\x in {0/0,1/4.2}{
  \begin{scope}[shift={(\x,0)}]
   \foreach \i in {0,...,4}{\coordinate (P\i) at (90+72*\i:1.4);}
   \draw[fill=blue!8] (P0)--(P1)--(P2)--(P3)--(P4)--cycle;
   \ifnum\s=1\draw[very thick] (P0)--(P2) (P0)--(P3);\fi
  \end{scope}
 }
 \node at (0,-1.9) {five-sided face};\node at (4.2,-1.9) {three triangles};
 \draw[-{Latex}] (1.75,0)--(2.45,0);\draw[-{Latex}] (5.9,0)--(6.55,0);
 \node[align=center] at (8.35,0) {$3\times180^\circ$\\[4pt]angle sum $=540^\circ$};
\end{tikzpicture}\end{center}

## prompt
Explain why every closed convex solid with polygon faces has the same total gap, even when its vertex gaps are different.

## text
\blank{.3cm}\workbox{14.5}
