+++
id = "w58.three-people-panels"
title = "Three people and three panels: proportional but not envy-free"
grades = ["shared"]
route = "return"
kernel = "For three people a division can be proportional while everyone envies someone; rearranging gives each a favourite."
+++

## text
\newband{Grades 3--5}
For three people, proportional means each person's own tray is worth at least one third of everything, using their own values. Envy-free means their own tray is worth at least as much as \emph{each} other tray. Ties pass both checks.

## prompt
Use the three-person preference cards below with panels X, Y and Z. A receives X, B receives Y, and C receives Z. Is this division proportional for everyone? Is it envy-free for everyone? Rearrange the whole panels to make the division envy-free.

## text
\begin{center}
\renewcommand{\arraystretch}{1.8}
\begin{tabular}{|p{37mm}|>{\centering\arraybackslash}p{36mm}|>{\centering\arraybackslash}p{36mm}|>{\centering\arraybackslash}p{36mm}|}
\hline
Observer & X & Y & Z\\\hline
A & 4 & 8 & 0\\\hline
B & 0 & 4 & 8\\\hline
C & 8 & 0 & 4\\\hline
\end{tabular}
\end{center}
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \foreach \x/\person/\panel in {0/A/X,64/B/Y,128/C/Z}{
    \draw[rounded corners=3mm,black!50] (\x,0) rectangle ++(54,54);
    \node[anchor=north west,font=\small] at (\x+4,50){\person};
    \draw[fill=pale] (\x+17,11) rectangle ++(25,25);
    \node[font=\large] at (\x+29.5,23.5){\panel};
  }
\end{tikzpicture}
\end{center}
\begin{center}
\renewcommand{\arraystretch}{1.65}
\begin{tabular}{|p{23mm}|p{31mm}|p{36mm}|p{36mm}|p{30mm}|}
\hline
\multicolumn{5}{|l|}{Initial allocation only: A has X, B has Y, C has Z}\\\hline
Observer & A's tray & B's tray & C's tray & One third of all\\\hline
A & & & &\\\hline
B & & & &\\\hline
C & & & &\\\hline
\end{tabular}
\end{center}
\linearea{3}
