+++
id = "w58.two-reds-two-blues"
title = "Every envy-free division of two reds and two blues"
grades = ["shared"]
route = "first"
kernel = "For two people envy-free and proportional coincide; exactly five labelled divisions pass."
+++

## text
\newband{Grades 2--5}
For each person, a division is \emph{envy-free} when their own tray is worth at least as much as the other tray. It is \emph{proportional} when their own tray is worth at least half of all the cards. Use that person's preferences for each check.

## prompt
Use A and B's preference cards with R1, R2, B1 and B2. Find every way to give all four cards to A and B so that neither person envies the other. Which of these ways are proportional for both people? Different card labels count as different cards.

## text
\begin{center}\prefmini\end{center}
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \good{20}{0}{1}{R1}\good{55}{0}{1}{R2}\good{90}{0}{2}{B1}\good{125}{0}{2}{B2}
\end{tikzpicture}
\end{center}
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \foreach \x/\y/\n in {0/60/1,96/60/2,0/30/3,96/30/4,0/0/5,96/0/6}{
    \node[anchor=south west,font=\scriptsize] at (\x,\y+21){Record \n};
    \draw[rounded corners=2mm,draw=black!45,line width=.7pt] (\x,\y) rectangle ++(82,20);
    \node[anchor=north west,font=\small] at (\x+3,\y+18){A};
    \draw[black!25] (\x+41,\y+2) -- (\x+41,\y+18);
    \node[anchor=north west,font=\small] at (\x+44,\y+18){B};
  }
\end{tikzpicture}
\end{center}
