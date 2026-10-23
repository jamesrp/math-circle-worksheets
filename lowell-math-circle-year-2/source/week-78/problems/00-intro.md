+++
id = "w78.intro"
kind = "setup"
title = "The three-armed line and a worked crossing"
grades = ["4-5"]
route = ["first", "return"]
+++

## text
For a point $(x,y)$, compare $x$, $y$, and $2$. When the least number occurs at least twice, the point lies on this line.
\vspace{-2pt}
\begin{center}
\begin{minipage}[c]{.36\linewidth}\centering
\begin{tikzpicture}[x=.61cm,y=.61cm]
 \path[use as bounding box] (-.5,-.45) rectangle (5.3,5.3);
 \draw[step=1,gray!37,line width=.25pt] (0,0) grid (5,5);
 \foreach \v in {0,2,4}{\node[below,font=\fontsize{8}{9}\selectfont] at (\v,0){\v};\node[left,font=\fontsize{8}{9}\selectfont] at (0,\v){\v};}
 \draw[-{Stealth[length=4pt]},line width=1.1pt] (2,2)--(5.2,2);
 \draw[-{Stealth[length=4pt]},line width=1.1pt] (2,2)--(2,5.2);
 \draw[-{Stealth[length=4pt]},line width=1.1pt] (2,2)--(-.2,-.2);
 \fill (2,2) circle[radius=2.2pt];
 \node[below right,font=\fontsize{9}{11}\selectfont,inner sep=4pt,fill=white] at (2,2){junction};
 \fill (4,2) circle[radius=2.2pt];
 \node[above right,font=\fontsize{9}{11}\selectfont] at (4,2){$P$};
 \draw[line width=.8pt,fill=white] (4,4) circle[radius=2.4pt];
 \node[above right,font=\fontsize{9}{11}\selectfont] at (4,4){$Q$};
\end{tikzpicture}
\end{minipage}\hfill
\begin{minipage}[c]{.60\linewidth}
$P=(4,2):\quad 4,\ \underline{2},\ \underline{2}$\par
The least number is tied. $P$ is on the line.\par\vspace{5pt}
$Q=(4,4):\quad 4,\ 4,\ \underline{2}$\par
The least number occurs once. $Q$ is off the line.
\end{minipage}
\end{center}
\vspace{-5pt}
The arms point east, north, and diagonally southwest. They continue without end. Every line in this packet has this shape, moved without turning. Points between grid dots count too.

\vspace{10pt}
Here are two completed lines. Blue has junction $U=(1,4)$; orange has junction $V=(4,2)$. Their only shared point is circled: $(4,4)$.
\begin{center}
\begin{tikzpicture}[x=.65cm,y=.65cm]
 \draw[step=1,gray!35,line width=.25pt] (0,0) grid (8,7);
 \foreach \v in {0,2,4,6,8}{\node[below,font=\small] at (\v,0){\v};}
 \foreach \v in {0,2,4,6}{\node[left,font=\small] at (0,\v){\v};}
 \draw[blue!75!black,line width=1.5pt,-{Stealth[length=5pt]}] (1,4)--(8,4);
 \draw[blue!75!black,line width=1.5pt,-{Stealth[length=5pt]}] (1,4)--(1,7);
 \draw[blue!75!black,line width=1.5pt,-{Stealth[length=5pt]}] (1,4)--(0,3);
 \draw[orange!85!black,line width=1.5pt,dashed,-{Stealth[length=5pt]}] (4,2)--(8,2);
 \draw[orange!85!black,line width=1.5pt,dashed,-{Stealth[length=5pt]}] (4,2)--(4,7);
 \draw[orange!85!black,line width=1.5pt,dashed,-{Stealth[length=5pt]}] (4,2)--(2,0);
 \fill[blue!75!black] (1,4) circle(2.5pt);\node[above right,fill=white,inner sep=2pt] at (1,4){$U$};
 \fill[orange!85!black] (4,2) circle(2.5pt);\node[below right,fill=white,inner sep=2pt] at (4,2){$V$};
 \draw[black,line width=1pt] (4,4) circle(.22);
 \node[above right,fill=white,inner sep=2pt] at (4.3,4.3){$(4,4)$};
\end{tikzpicture}
\end{center}
In the next problem, try to make two lines share just one point, then try to make two lines overlap along a whole stretch. A shared stretch includes every point between its grid dots.
