+++
id = "w70.shots-portals-and-shields"
kind = "setup"
title = "Shots, portal edges and shields"
grades = ["4-5"]
route = ["first", "return"]
+++

## text
A shot travels straight. At an X edge it reappears at the same height on the other X edge. Y edges work the same way, at the same left-to-right position. It keeps its direction. All four corners are the same S. Stop at the first T reached.

A shield is one exact point, away from S and T. A shot stops only if its line passes through that point. A counter marks the point at its center. On an unfolded map, a shield repeats at the same place in every large room-copy.

\begin{center}
\begin{tikzpicture}[scale=.47]
\draw[step=1,gray!25](0,0)grid(8,4);\draw[thick](0,0)rectangle(4,4);\draw[thick](4,0)rectangle(8,4);
\fill(3,1)circle(2.5pt);\draw[-{Stealth},very thick](3,1)--(5,2);\draw(4,1.5)circle(3.5pt);
\foreach\x in{1,5}{\draw[very thick](\x-.16,1.84)--(\x+.16,2.16);\draw[very thick](\x-.16,2.16)--(\x+.16,1.84);\node[above,font=\scriptsize]at(\x,2.2){P};}
\node[above,font=\scriptsize]at(3,1){start};\node[above,font=\scriptsize]at(4,4){X};
\node[below,font=\small]at(4,-.55){one shield P in two copies};
\end{tikzpicture}\hspace{.35in}
\begin{tikzpicture}[scale=.47]
\draw[step=1,gray!25](0,0)grid(4,4);\draw[thick](0,0)rectangle(4,4);
\fill(3,1)circle(2.5pt);\draw[-{Stealth},very thick](3,1)--(4,1.5);\draw[-{Stealth},very thick](0,1.5)--(1,2);
\draw[very thick](.84,1.84)--(1.16,2.16);\draw[very thick](.84,2.16)--(1.16,1.84);\node[above,font=\scriptsize]at(1,2.2){P};
\draw(0,1.5)circle(3.5pt);\draw(4,1.5)circle(3.5pt);
\node[above,font=\scriptsize]at(3,1){start};\node[left,font=\scriptsize]at(0,2){X};\node[right,font=\scriptsize]at(4,2){X};
\node[below,font=\small]at(2,-.55){the same shot in one room};
\end{tikzpicture}
\end{center}
