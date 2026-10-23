+++
id = "w56.opened-drawing-tree"
title = "Why $V-E+F$ never changes: opened drawings and trees"
grades = ["shared"]
route = "return"
page = "new"
kernel = 'Erasing an edge on a loop lowers $E$ and the bounded faces by one each; a tree has $E=V-1$, so an opened drawing counts 1 and the closed solid 2.'
+++

## text
\renewcommand{\band}{Grades 4--5}
Convex means no dents. An opened drawing preserves the assembled edge and vertex connections. Count its bounded regions as faces; the outside is the removed face. A tree is a connected drawing with no closed loops.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \draw[fill=blue!8] (0,0)--(2.3,0)--(1.15,.7)--cycle;
 \draw[fill=blue!17] (2.3,0)--(1.15,.7)--(1.2,2.15)--cycle;
 \draw[dashed,gray] (0,0)--(1.15,.7)--(1.2,2.15);
 \draw (0,0)--(2.3,0)--(1.2,2.15)--cycle;
 \node[font=\scriptsize,fill=white,inner sep=1pt] at (1.12,1.04) {opening};
 \node[align=center] at (1.15,-.6) {tetrahedron with\\one face removed};
 \draw[-{Latex}] (2.8,1)--(3.5,1);
 \draw[fill=blue!8] (3.9,0)--(6.2,0)--(5.05,2)--cycle;
 \draw[very thick,red!60!black] (3.9,0)--(5.05,.67)--(6.2,0) (5.05,.67)--(5.05,2);
 \node[align=center] at (5.05,-.6) {same three faces\\viewed through the opening};
 \draw[-{Latex}] (6.65,1)--(7.35,1);
 \draw (7.85,0)--(9.0,.67)--(10.15,0) (9.0,.67)--(9.0,2);
 \foreach \p in {(7.85,0),(9.0,.67),(10.15,0),(9.0,2)}{\fill \p circle (1.5pt);}
 \node[align=center] at (9,-.6) {three boundary edges erased\\a tree remains};
\end{tikzpicture}\end{center}

## prompt
Explain why $V-E+F$ always has the same value for closed convex solids with polygon faces. Can an opened drawing be changed into a tree while keeping all its vertices connected?

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \draw[fill=blue!7] (0,0) rectangle (4.5,4.5);\draw[fill=blue!18] (1.4,1.4) rectangle (3.1,3.1);
 \draw (0,0)--(1.4,1.4) (4.5,0)--(3.1,1.4) (4.5,4.5)--(3.1,3.1) (0,4.5)--(1.4,3.1);
 \foreach \p in {(0,0),(4.5,0),(4.5,4.5),(0,4.5),(1.4,1.4),(3.1,1.4),(3.1,3.1),(1.4,3.1)}{\fill \p circle (1.5pt);}
 \node[below] at (2.25,-.1) {opened cube: five bounded faces};
\end{tikzpicture}\hspace{.7cm}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
 \draw[gray!50] (0,0) rectangle (4.5,4.5);\draw[gray!50] (1.4,1.4) rectangle (3.1,3.1);
 \draw[gray!50] (0,0)--(1.4,1.4) (4.5,0)--(3.1,1.4) (4.5,4.5)--(3.1,3.1) (0,4.5)--(1.4,3.1);
 \foreach \p in {(0,0),(4.5,0),(4.5,4.5),(0,4.5),(1.4,1.4),(3.1,1.4),(3.1,3.1),(1.4,3.1)}{\fill \p circle (1.5pt);}
 \node[below] at (2.25,-.1) {extra workspace};
\end{tikzpicture}\end{center}
\blank{.3cm}\workbox{6.8}
