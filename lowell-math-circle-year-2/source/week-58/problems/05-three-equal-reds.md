+++
id = "w58.three-equal-reds"
title = "Three equal reds for two people, whole or with one card cut"
grades = ["shared"]
route = "first"
kernel = "An odd number of whole equal cards cannot be shared without envy; splitting one card removes the obstruction."
+++

## text
\newband{Grades K--5}

## prompt
U and V each value every red card at 1. Divide all three cards between them, keeping each card whole, so that neither person would rather have the other's cards. If no division works, explain why. For a second trial, replace R3 with its paper copy; you may cut that copy. R1 and R2 must stay whole. Can you now make such a division?

## text
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \foreach \x/\name in {0/U,96/V}{
    \draw[rounded corners=2mm,fill=pale] (\x,0) rectangle ++(86,25);
    \node[anchor=west,font=\bfseries] at (\x+5,17){\name};
    \fill[redgood] (\x+26,14) circle (3mm);
    \node[font=\small] at (\x+38,14){1};\valuedots{\x+44}{14}{1}
  }
\end{tikzpicture}
\end{center}
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \good{38}{0}{1}{R1}\good{78}{0}{1}{R2}\good{118}{0}{1}{R3}
\end{tikzpicture}
\end{center}
In the second trial, R3's whole paper square is worth 1 to each person. Equal areas have equal value.

\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \foreach \x/\label in {0/U,96/V}{
    \draw[rounded corners=3mm,black!40] (\x,0) rectangle ++(86,56);
    \node[anchor=north west,font=\small] at (\x+4,52){\label};
  }
\end{tikzpicture}
\end{center}
\linearea{5}
