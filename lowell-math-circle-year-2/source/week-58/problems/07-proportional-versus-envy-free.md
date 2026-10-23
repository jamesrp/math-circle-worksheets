+++
id = "w58.proportional-versus-envy-free"
title = "Proportional versus envy-free for two and three people"
grades = ["shared"]
route = "return"
kernel = "Envy-free implies proportional for any number of people; the converse holds for two people and fails for three."
+++

## text
\newband{Grades 3--5}

## prompt
Every item goes to exactly one person, and tray values add. For two people, can a division be proportional but fail to be envy-free? Can it be envy-free but fail to be proportional? Explain your answers for any two-person division.

## text
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \node[anchor=west,font=\small] at (0,39){One observer's values};
  \draw[rounded corners=2mm] (0,0) rectangle (86,28);
  \draw[rounded corners=2mm] (96,0) rectangle (182,28);
  \node[font=\small] at (43,18){own tray};
  \node[font=\small] at (139,18){other tray};
\end{tikzpicture}
\end{center}
\linearea{4}

For three people, can a division be proportional but fail to be envy-free? Can it be envy-free but fail to be proportional? Give an example whenever the answer is yes, and explain why whenever the answer is no.

\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \node[anchor=west,font=\small] at (0,37){One observer's values};
  \foreach \x/\lab in {0/own tray,64/other tray,128/other tray}{
    \draw[rounded corners=2mm] (\x,0) rectangle ++(54,27);
    \node[font=\small] at (\x+27,17){\lab};
  }
\end{tikzpicture}
\end{center}
\linearea{3}
