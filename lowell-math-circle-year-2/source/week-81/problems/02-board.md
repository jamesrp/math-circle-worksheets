+++
id = "w81.board"
kind = "setup"
title = "Three-bucket board"
grades = ["2-5"]
route = ["first", "return"]
page = "new"
+++

## text
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
 \foreach \x/\label in {0/1,61/2,122/3}{
  \node[font=\large] at (28+\x,161) {Bucket \label};
  \draw[rounded corners=3mm,line width=1pt] (\x,12) rectangle +(56,139);
 }
 \draw[line width=.75pt] (0,-43) rectangle (86,-3);
 \draw[line width=.75pt] (92,-43) rectangle (178,-3);
 \node[font=\large] at (43,-15) {Supply};
 \node[font=\large] at (135,-15) {Removed};
\end{tikzpicture}
\end{center}
