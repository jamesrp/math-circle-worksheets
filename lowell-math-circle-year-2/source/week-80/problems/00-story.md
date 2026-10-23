+++
id = "w80.story"
kind = "setup"
title = "The midnight light and the fold"
grades = ["2-5"]
route = ["first", "return"]
+++

## text
A light is OFF at 11:00 p.m. At 11:30 it switches ON; at 11:45 it switches OFF. It keeps switching halfway from the previous switching time to midnight, forever before midnight.

Use the ON/OFF card for the light. Mark switching times on a paper strip from 11:00 p.m. to MIDNIGHT. Flip the card at every switching mark.

\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,-1) rectangle (184,54);
  % A single, non-task fold demonstrates how the remaining gap is halved.
  \node at (27,49) {Input};
  \draw[line width=0.6pt] (1,16) rectangle (53,34);
  \draw (1,25)--(53,25);
  \draw (1,22)--(1,28) (53,22)--(53,28);
  \node[anchor=west,font=\sffamily\scriptsize] at (1,8) {11:30};
  \node[anchor=east,font=\sffamily\scriptsize] at (53,8) {MIDNIGHT};
  \draw[-{Stealth[length=2mm]},gray] (57,25)--(62,25);

  \node at (92,49) {Fold};
  \draw[dashed,gray] (66,16) rectangle (118,34);
  \draw[line width=0.8pt,fill=gray!12] (66,16) rectangle (92,34);
  \draw[dashed] (92,14)--(92,36);
  \draw[-{Stealth[length=2mm]}] (116,36) to[out=135,in=45] (68,36);
  \node[anchor=west,font=\sffamily\scriptsize,align=left] at (66,5) {MIDNIGHT\ meets 11:30};
  \draw[-{Stealth[length=2mm]},gray] (122,25)--(127,25);

  \node at (157,49) {Unfold};
  \draw[line width=0.6pt] (131,16) rectangle (183,34);
  \draw (131,25)--(183,25);
  \draw (131,22)--(131,28) (183,22)--(183,28);
  \draw[line width=1.2pt] (157,18)--(157,32);
  \node[font=\sffamily\scriptsize] at (157,8) {11:45};
\end{tikzpicture}
\end{center}
