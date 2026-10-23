+++
id = "w03.perfect-shuffles"
title = "Perfect shuffles of 4 to 12 cards"
grades = ["4-5"]
route = "first"
page = "new"
+++

## prompt
A perfect shuffle splits a deck into a top half and a bottom half of the same size, then puts the halves together one card from each half at a time, keeping the top card on top. Do the shuffles with the cards laid out in a row, top card on the left. Here is one perfect shuffle of eight cards.

\vspace{10pt}
{\centering
\begin{tikzpicture}[x=0.45in, y=0.45in,
  card/.style={draw, fill=slotfill, minimum width=0.36in, minimum height=0.4in, inner sep=0pt, font=\cardfont},
  lab/.style={anchor=east, inner sep=0pt}]
\foreach \c [count=\i] in {A,2,3,4,5,6,7,8} \node[card] at (\i,0) {\c};
\foreach \c [count=\i] in {A,2,3,4} \node[card] at (2*\i-1,-1.1) {\c};
\foreach \c [count=\i] in {5,6,7,8} \node[card] at (2*\i,-1.8) {\c};
\foreach \c [count=\i] in {A,5,2,6,3,7,4,8} \node[card] at (\i,-2.9) {\c};
\node[lab] at (0.4,0) {the deck};
\node[lab] at (0.4,-1.1) {top half};
\node[lab] at (0.4,-1.8) {bottom half};
\node[lab] at (0.4,-2.9) {after one shuffle};
\end{tikzpicture}\par}
\vspace{10pt}
How many perfect shuffles bring these eight cards back to their starting order? Find the number for 4, 6, 10 and 12 cards too, using the cards from A upward in one suit. Then draw the perfect shuffle of 8 cards as a machine.

## text
\vspace{18pt}
{\centering\renewcommand{\arraystretch}{2.2}%
\begin{tabular}{|l|*{5}{>{\centering\arraybackslash}p{0.75in}|}}
\hline
cards & 4 & 6 & 8 & 10 & 12 \\ \hline
shuffles & & & & & \\ \hline
\end{tabular}\par}

\fig[36pt]{u-p5}
