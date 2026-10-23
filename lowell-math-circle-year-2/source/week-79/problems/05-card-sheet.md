+++
id = "w79.card-sheet"
kind = "setup"
title = "Cards 1 to 24"
grades = ["2-5"]
route = ["first", "return"]
page = "new"
+++

## text
\renewcommand{\level}{Grades 2--5}

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
  \foreach \r in {0,...,5} {
    \foreach \c in {0,...,3} {
      \pgfmathtruncatemacro{\v}{4*\r+\c+1}
      \draw[line width=0.6pt] (3*\c,-3*\r) rectangle (3*\c+3,-3*\r-3);
      \node[font=\fontsize{27}{30}\selectfont] at (3*\c+1.5,-3*\r-1.5){\v};
    }
  }
\end{tikzpicture}
\end{center}
