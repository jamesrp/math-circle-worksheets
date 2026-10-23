+++
id = "w58.rules"
kind = "setup"
title = "Trays, preference cards and the divide-and-choose turn"
grades = ["shared"]
route = ["first", "return"]
kernel = "A tray's value is the sum of one fixed observer's card values; the divider makes two trays and the chooser picks first."
+++

## text
\renewcommand{\Band}{Grades K--5}
Keep each person's preference card unchanged during a trial. A tray's value is the sum of its cards' values, using the same person's preferences for every tray. Use every card once. Cards stay whole unless the problem allows cutting. Ties are allowed.

\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \node[anchor=west,font=\small] at (0,39){Input};
  \node[anchor=west,font=\small] at (60,39){Divider makes two trays};
  \node[anchor=west,font=\small] at (131,39){Choice and remainder};
  \foreach \x in {2,16,30}{\draw[fill=black!12] (\x,25) circle (4mm);}
  \draw[-{Stealth[length=2mm]}] (46,25) -- (56,25);
  \draw[rounded corners=2mm] (61,17) rectangle (88,32);
  \draw[rounded corners=2mm] (94,17) rectangle (117,32);
  \foreach \x in {69,80}{\draw[fill=black!12] (\x,25) circle (3mm);}
  \draw[fill=black!12] (105,25) circle (3mm);
  \draw[-{Stealth[length=2mm]}] (120,25) -- (129,25);
  \draw[rounded corners=2mm] (133,17) rectangle (159,32);
  \draw[rounded corners=2mm] (166,17) rectangle (185,32);
  \foreach \x in {141,152}{\draw[fill=black!12] (\x,25) circle (3mm);}
  \draw[fill=black!12] (175.5,25) circle (3mm);
  \node[font=\scriptsize,align=center] at (146,8){Chooser takes\\this tray first};
  \node[font=\scriptsize,align=center] at (176,8){Divider takes\\the remainder};
\end{tikzpicture}
\end{center}
