+++
id = "w82.matches"
kind = "setup"
title = "Complete matches that keep order"
grades = ["3-5"]
route = ["first", "return"]
+++

## text
There are two classes of kids, and each class lines up. A complete match gives each kid a partner in the other class, with nobody left out. It keeps order when any two kids in the first class appear in the same order as their partners in the second class.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]

\foreach \offset/\caption in {0/{Complete match\\keeps order},5.6/{Complete match\\does not keep order},11.2/{5 kids and 6\\no complete match possible}}{
 \node[align=center,font=\small] at (\offset+2.0,0.8) {\caption};
 \foreach \n/\letter in {1/A,2/B,3/C,4/D,5/E}{
  \node[draw,rounded corners=1pt,minimum width=.56cm,minimum height=.55cm,font=\small] at (\offset+.8*\n-.8,-.2) {\n};
  \node[draw,rounded corners=1pt,minimum width=.56cm,minimum height=.55cm,font=\small] at (\offset+.8*\n-.8,-1.9) {\letter};
 }
}
\foreach \n in {1,...,5}{\draw (.8*\n-.8,-.5)--(.8*\n-.8,-1.6);}
\foreach \n/\partner in {1/2,2/1,3/3,4/4,5/5}{\draw (5.6+.8*\n-.8,-.5)--(5.6+.8*\partner-.8,-1.6);}
\foreach \n in {1,...,5}{\draw (11.2+.8*\n-.8,-.5)--(11.2+.8*\n-.8,-1.6);}
\node[draw,rounded corners=1pt,minimum width=.56cm,minimum height=.55cm,font=\small] at (15.2,-1.9) {F};
\node[font=\scriptsize,anchor=north] at (15.2,-2.3) {left out};
\end{tikzpicture}
\end{center}
