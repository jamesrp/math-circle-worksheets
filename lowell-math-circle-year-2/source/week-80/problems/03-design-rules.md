+++
id = "w80.design-rules"
title = "A card that settles, a counter that does not"
grades = ["2-5"]
route = "first"
page = "new"
kernel = "A card settles exactly when it flips at only finitely many marks, and a counter whose moves never shrink below some fixed length cannot get closer and closer to one place."
+++

## prompt
Use the same switching marks. Make up a flipping rule for a second card that does settle on one side. Make up a moving rule for the counter that does not get closer and closer to one place.

## text
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (184,53);
  \draw[line width=0.9pt] (2,23)--(182,23);
  \draw[line width=0.9pt] (2,19)--(2,27) (182,19)--(182,27);
  \node[anchor=west] at (2,8) {START};
  \node[anchor=east] at (182,8) {END};
\end{tikzpicture}
\end{center}

\vspace{12mm}
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (184,109);
  \node[anchor=west] at (2,103) {Card rule};
  \node[anchor=west] at (98,103) {Counter rule};
  \draw[gray!50] (92,0)--(92,106);
\end{tikzpicture}
\end{center}
\vfill
