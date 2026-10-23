+++
id = "w80.cut-outs"
kind = "setup"
title = "Strips and the ON/OFF card"
grades = ["2-5"]
route = ["first", "return"]
page = "new"
+++

## text
\renewcommand{\band}{Grades 2--5}

\begin{center}
\strip{11:00 p.m.}{MIDNIGHT}

\vspace{11mm}
\strip{START}{END}

\vspace{23mm}
\begin{tikzpicture}[x=1mm,y=1mm]
  \path[use as bounding box] (0,0) rectangle (184,57);
  \draw[dashed,line width=0.6pt] (12,0) rectangle (88,54);
  \draw[dashed,line width=0.6pt] (96,0) rectangle (172,54);
  \node[font=\sffamily\bfseries\fontsize{32}{36}\selectfont] at (50,27) {ON};
  \node[font=\sffamily\bfseries\fontsize{32}{36}\selectfont] at (134,27) {OFF};
\end{tikzpicture}
\end{center}
\vfill
