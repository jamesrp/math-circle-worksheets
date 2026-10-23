+++
id = "w81.forever"
title = "Can a game go on forever?"
grades = ["2-5"]
route = "return"
kernel = "Every game ends, from two buckets or three: the rightmost bucket never refills, so it stops changing, and the game left in the other buckets ends too."
+++

## text
\vspace{4pt}

## prompt
Start from each picture. Can you agree on moves that keep the game going forever? If you think every game ends, however big the refills, explain why.

## text
\begin{center}
\begin{tabular}{@{}c@{\hspace{.75in}}c@{}}
\begin{tikzpicture}[x=1cm,y=1cm]% the two-bucket start (0, 3), drawn like \smallstart
 \foreach \x/\count in {0/0,1.3/3}{
  \draw[rounded corners=2pt,line width=.65pt] (\x,0) rectangle +(1.1,1.15);
  \node[font=\small] at (\x+.55,-.28) {\pgfmathparse{int(\x/1.3+1)}\pgfmathresult};
  \ifnum\count>0
   \foreach \n in {1,...,\count}{
    \pgfmathsetmacro{\xx}{mod(\n-1,2)*.43+.33}
    \pgfmathsetmacro{\yy}{floor((\n-1)/2)*.4+.35}
    \node[fish] at (\x+\xx,\yy) {};
   }
  \fi
 }
\end{tikzpicture} & \smallstart{1}{1}{1}
\end{tabular}
\end{center}
\vspace{5pt}
\begin{tikzpicture}
 \draw[black!35] (0,0) rectangle (17.5,2.15);
\end{tikzpicture}
