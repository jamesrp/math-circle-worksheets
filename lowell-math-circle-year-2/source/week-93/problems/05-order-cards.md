+++
id = "w93.order-cards"
title = "Four stages of one rectangle"
grades = ["3-5"]
route = "return"
page = "new"
kernel = 'Each move nests the new bracket inside the old: B, D, A, C, with widths 4, 1, $1/14$ and $1/2716$.'
+++

## prompt
Cut out the four cards from a spare copy of this page. They show four stages of reshaping one rectangle, with exact side lengths. Put them in order so each card follows from one reshaping move. Which card gives the tightest guaranteed range for the side of a square of area 12? Show why that square's side cannot lie outside your range.

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) rectangle (7,2);\node at (.5,1.5) {A};\node at (3.5,1) {$\dfrac{24}{7}\quad\text{by}\quad\dfrac72$};
\draw (8,0) rectangle (15,2);\node at (8.5,1.5) {B};\node at (11.5,1) {$2\quad\text{by}\quad6$};
\draw (0,-2.5) rectangle (7,-.5);\node at (.5,-1) {C};\node at (3.5,-1.5) {$\dfrac{336}{97}\quad\text{by}\quad\dfrac{97}{28}$};
\draw (8,-2.5) rectangle (15,-.5);\node at (8.5,-1) {D};\node at (11.5,-1.5) {$3\quad\text{by}\quad4$};
\end{tikzpicture}
\end{center}
\vspace{29mm}
