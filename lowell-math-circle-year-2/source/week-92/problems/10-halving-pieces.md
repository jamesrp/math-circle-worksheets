+++
id = "w92.halving-pieces"
title = "Halves, quarters and eighths"
grades = ["shared"]
route = "return"
kernel = 'Each piece of width $16/2^n$ fills the whole track after exactly $n$ moves, by induction on $n$.'
+++

## figure
band('Grades 4--5')

## prompt @0
Move each labelled piece separately. Shade its possible places after the stated number of moves on the matching track. Does the pattern continue if you keep cutting every piece in half? Explain.

## figure
r'''\foreach \y/\n/\lab/\first in {-36/2/1 move/65,-65/4/2 moves/67,-94/8/3 moves/71}{
\node[anchor=south west,font=\scriptsize] at (8,\y+10){\lab};
\foreach \k in {1,...,\n}{\pgfmathsetmacro{\xa}{8+160*(\k-1)/\n}\pgfmathsetmacro{\xb}{8+160*\k/\n}
\fill[bandfill] (\xa,\y-1.3) rectangle (\xb,\y+1.3);
\fill[ink] (\xa,\y) circle(0.7);\fill[ink] (\xb,\y) circle(0.7);
\pgfmathtruncatemacro{\letter}{\first+\k-1}
\node[font=\scriptsize,anchor=south] at ({(\xa+\xb)/2},\y+2){\char\letter};}
\track{\y}{ }}
\foreach \col/\first in {0/65,1/72}{
\foreach \r in {0,...,6}{
\pgfmathtruncatemacro{\letter}{\first+\r}
\begin{scope}[shift={({8+88*\col},{-120-14*\r})}]
\node[anchor=east,font=\scriptsize] at (-2,0){\char\letter};
\draw[ink] (0,0)--(70,0);
\foreach \i in {0,...,16}{\draw[ink] (70*\i/16,-1)--(70*\i/16,1);}
\foreach \i in {0,4,8,12,16}{\node[anchor=north,font=\tiny] at (70*\i/16,-2){\i};}
\end{scope}}}'''
