+++
id = "w58.cut-the-strip"
title = "Cut a two-colour strip into two pieces of equal value to the cutter"
grades = ["shared"]
route = "first"
kernel = "Within one colour value follows length, so the cutter can make an exact equal-own-value cut and the chooser takes a better piece."
+++

## text
\newband{Grades 2--5}
On a paper strip, the numbers on A and B's preference cards give the value of a whole 120 mm color panel. Within one color, value follows length: half a panel has half its value.

\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \node[anchor=west,font=\small] at (0,31){Input: one panel worth 2};
  \draw[fill=black!10] (0,10) rectangle (49,23);
  \node[font=\small] at (24.5,16.5){120 mm};
  \draw[-{Stealth[length=2mm]}] (54,16.5) -- (64,16.5);
  \node[anchor=west,font=\small] at (69,31){Two equal lengths};
  \draw[fill=black!10] (69,10) rectangle (118,23);
  \draw[dashed] (93.5,8) -- (93.5,25);
  \node[font=\scriptsize] at (81.25,16.5){60 mm};
  \node[font=\scriptsize] at (105.75,16.5){60 mm};
  \draw[-{Stealth[length=2mm]}] (121,16.5) -- (129,16.5);
  \node[anchor=west,font=\small] at (132,31){Output: value 1 each};
  \draw[fill=black!10] (132,10) rectangle (156.5,23);
  \draw[fill=black!10] (160.5,10) rectangle (185,23);
  \node[font=\small] at (144.25,16.5){1};
  \node[font=\small] at (172.75,16.5){1};
\end{tikzpicture}
\end{center}

## prompt
Use the full-size strips. A cuts parallel to the color join into two pieces of equal value to A. B chooses a piece first; A gets the remainder. On fresh strips, swap the roles. Mark each cut on its sketch, write its distance from the left end, and circle the chooser's piece.

## text
\begin{center}\prefmini\end{center}
\begin{center}
\begin{tikzpicture}[x=1mm,y=1mm]
  \node[anchor=west,font=\small] at (0,100){A cuts};\strip{0}{70}
  \node[anchor=west,font=\small] at (0,60){Cut: \rule{20mm}{.25pt}\ mm from the left end};
  \node[anchor=west,font=\small] at (0,35){B cuts};\strip{0}{5}
  \node[anchor=west,font=\small] at (0,-5){Cut: \rule{20mm}{.25pt}\ mm from the left end};
\end{tikzpicture}
\end{center}
