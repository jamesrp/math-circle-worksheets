+++
id = "w79.rule"
kind = "setup"
title = "Two cards in, one card moves"
grades = ["2-5"]
route = ["first", "return"]
+++

## text
Both bowls start empty. Each day, put the next two numbered cards in A, then move A's smallest card to B. Cards in B stay there.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
  \foreach \x/\t in {3/Before,9/{Add 1 and 2},15/{Move 1 to B}} {
    \node[font=\small] at (\x,3.4){\t};
    \draw[line width=0.6pt,rounded corners=4pt] (\x-2.3,1.25) rectangle (\x+2.3,2.75);
    \draw[line width=0.6pt,rounded corners=4pt] (\x-2.3,-0.65) rectangle (\x+2.3,0.85);
    \node[font=\bfseries\small,anchor=west] at (\x-2.12,2.5){A};
    \node[font=\bfseries\small,anchor=west] at (\x-2.12,0.6){B};
  }
  \draw[-{Stealth[length=2.5mm]},line width=0.7pt] (5.5,1.03)--(6.45,1.03);
  \draw[-{Stealth[length=2.5mm]},line width=0.7pt] (11.5,1.03)--(12.45,1.03);
  \card{8.45}{1.9}{1}
  \card{9.65}{1.9}{2}
  \card{15.3}{1.9}{2}
  \card{15.3}{0}{1}
\end{tikzpicture}
\end{center}
