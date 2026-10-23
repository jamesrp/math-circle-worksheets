+++
id = "w79.move-day"
title = "The days a card enters A and moves to B"
grades = ["2-5"]
route = "first"
page = "new"
kernel = "Card k enters A on day k/2 rounded up; under the smallest-card rule A holds n+1 to 2n after day n, so card k moves on day k and its wait in A grows."
+++

## prompt
Restart. Find rules for the day any numbered card enters A and the day it moves to B. Test your rules on cards 3, 6, and 10, and predict both days for card 20 without running twenty days.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
  \foreach \x/\v in {2.3/3,6.8/6,11.3/10,15.8/20} {
    \draw[line width=0.8pt,rounded corners=2pt] (\x-0.85,1.1) rectangle (\x+0.85,2.8);
    \node[font=\fontsize{25}{28}\selectfont] at (\x,1.95){\v};
    \node[font=\normalsize,anchor=west] at (\x-1.75,0.25){Enters day};
    \draw[line width=0.5pt] (\x+0.55,-0.05)--(\x+1.85,-0.05);
    \node[font=\normalsize,anchor=west] at (\x-1.75,-0.75){Moves day};
    \draw[line width=0.5pt] (\x+0.55,-1.05)--(\x+1.85,-1.05);
  }
\end{tikzpicture}
\end{center}

\vspace{0.7cm}
