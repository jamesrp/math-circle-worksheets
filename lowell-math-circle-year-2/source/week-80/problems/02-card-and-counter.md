+++
id = "w80.card-and-counter"
title = "The card and the counter"
grades = ["2-5"]
route = "first"
page = "new"
kernel = "The card flips forever and never settles, while the counter, halving its gap to END at the same marks, gets closer and closer to END."
+++

## prompt
Use the same switching marks. The card starts OFF. A counter starts at START. At each switching mark, flip the card and move the counter halfway from its present place toward END. As the rule keeps going, does the card settle on one side? What place does the counter approach?

## text
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (184,53);
  \draw[line width=0.9pt] (2,23)--(182,23);
  \draw[line width=0.9pt] (2,19)--(2,27) (182,19)--(182,27);
  \draw[line width=0.8pt,fill=white] (2,23) circle (3);
  \node[anchor=west] at (2,8) {START};
  \node[anchor=east] at (182,8) {END};
\end{tikzpicture}
\end{center}

\vspace{12mm}
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (184,109);
  \node[anchor=west] at (2,103) {Card};
  \node[anchor=west] at (98,103) {Counter};
  \draw[gray!50] (92,0)--(92,106);
\end{tikzpicture}
\end{center}
\vfill
