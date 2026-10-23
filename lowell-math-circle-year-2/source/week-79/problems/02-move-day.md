+++
id = "w79.move-day"
title = "The day a card moves to B"
grades = ["2-5"]
route = "first"
page = "new"
kernel = "Under the smallest-card rule A holds n+1 to 2n after day n, so card k moves on day k."
+++

## prompt
Restart. Find a rule for the day any numbered card moves to B. Test your rule on cards 3, 6, and 10, and predict the day for card 20 without running twenty days.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
  \foreach \x/\v in {2.3/3,6.8/6,11.3/10,15.8/20} {
    \draw[line width=0.8pt,rounded corners=2pt] (\x-0.85,1.1) rectangle (\x+0.85,2.8);
    \node[font=\fontsize{25}{28}\selectfont] at (\x,1.95){\v};
    \node[font=\normalsize,anchor=west] at (\x-1.1,0.25){Day};
    \draw[line width=0.5pt] (\x-0.15,-0.05)--(\x+1.3,-0.05);
  }
\end{tikzpicture}
\end{center}

\vspace{0.7cm}
