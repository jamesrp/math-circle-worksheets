+++
id = "w79.settled"
title = "Where the cards settle, and whether a finite day shows it"
grades = ["2-5"]
route = "return"
page = "new"
kernel = "Under the smallest-card rule every card settles in B, yet card N+1 is in A on every day N: each card by some day is not all cards by one day."
+++

## text
\renewcommand{\level}{Grades 4--5}

## prompt
Imagine the numbered cards continuing forever, with two new cards each day. Call a card settled in a bowl if, after some day, it stays in that bowl forever. For each rule, decide where all the cards settle. Can that arrangement happen on a finite day?

## text
\vspace{0.7cm}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
  \node[font=\large] at (9.1,14.35){Move A's smallest card};
  \draw[line width=0.6pt] (0,7.4) rectangle (8.9,13.7);
  \draw[line width=0.6pt] (9.5,7.4) rectangle (18.4,13.7);
  \node[font=\Large,anchor=north west] at (0.25,13.45){A};
  \node[font=\Large,anchor=north west] at (9.75,13.45){B};
  \node[font=\large] at (9.1,6.65){Move the larger new card};
  \draw[line width=0.6pt] (0,0) rectangle (8.9,6);
  \draw[line width=0.6pt] (9.5,0) rectangle (18.4,6);
  \node[font=\Large,anchor=north west] at (0.25,5.75){A};
  \node[font=\Large,anchor=north west] at (9.75,5.75){B};
\end{tikzpicture}
\end{center}
