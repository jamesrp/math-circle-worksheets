+++
id = "w72.strip-and-cards"
kind = "setup"
title = "Memory strip and move cards to cut out"
grades = ["4-5"]
route = ["first", "return"]
page = "new"
+++

## text
Extra workspace for every problem. Cut out the memory strip and keep it beside your working page. If you need more numbers, tape on an extension, overlapping one tick, and continue numbering. Make more extensions with the same tick spacing when needed.
\vspace{.10in}
\begin{center}
\begin{tikzpicture}[x=.72cm,y=1cm]
\draw[dashed,gray](-10.55,-.85)rectangle(10.55,.9);
\draw[{Stealth}-{Stealth}](-10.35,0)--(10.35,0);
\foreach\x in{-10,...,10}{\draw(\x,-.10)--(\x,.10);\node[below,font=\small]at(\x,-.15){\x};}
\node[above]at(0,.35){memory};
\end{tikzpicture}\par\vspace{.22in}
\begin{tabular}{c@{\hspace{.20in}}c}
\begin{tikzpicture}[x=.72cm,y=1cm]
\draw[dashed,gray](-.55,-.85)rectangle(10.55,.7);
\draw(0,0)--(10,0);\foreach\x in{0,...,10}{\draw(\x,-.10)--(\x,.10);}
\end{tikzpicture}&
\begin{tikzpicture}[x=.72cm,y=1cm]
\draw[dashed,gray](-.55,-.85)rectangle(10.55,.7);
\draw(0,0)--(10,0);\foreach\x in{0,...,10}{\draw(\x,-.10)--(\x,.10);}
\end{tikzpicture}
\end{tabular}
\end{center}
\vspace{.15in}
Cut out the move cards. For a route longer than your cards allow, write its letters in order on paper.
\begin{center}
\begin{tikzpicture}[x=1.8cm,y=1.8cm]
\draw[dashed,gray,step=1](0,0)grid(8,4);
\foreach\x in{0,...,7}{
\node at(\x+.5,3.5){E $\rightarrow$};
\node at(\x+.5,2.5){W $\leftarrow$};
\node at(\x+.5,1.5){N $\uparrow$};
\node at(\x+.5,.5){S $\downarrow$};}
\end{tikzpicture}
\end{center}
