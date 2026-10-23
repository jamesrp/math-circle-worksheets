+++
id = "w62.first-slot-rule"
title = "The first-slot rule"
kind = "setup"
grades = ["shared"]
route = "return"
page = "new"
+++

## text
\gdef\band{Grades 3--5}
For Problems 7--8, choose an order for the cards. Place each card in the first numbered slot where it conflicts with no card already there. During the order, do not move a placed card.
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,card/.style={draw,minimum width=0.55cm,minimum height=0.7cm,fill=white},>=Stealth]
\node at (1.3,2.7) {order X, Y, W};
\draw (0.1,1.7) -- (1.3,0.5) -- (2.5,1.7);
\node[draw,circle,fill=white,minimum size=0.7cm] at (0.1,1.7) {X};
\node[draw,circle,fill=white,minimum size=0.7cm] at (2.5,1.7) {Y};
\node[draw,circle,fill=white,minimum size=0.7cm] at (1.3,0.5) {W};
\draw[->] (3.3,1.3) -- (4,1.3);
\node at (5.9,2.7) {after X and Y};
\node at (4.9,2) {slot 1}; \node[card] at (4.55,1.3) {X}; \node[card] at (5.25,1.3) {Y};
\node at (6.7,2) {slot 2}; \node at (6.7,1.3) {empty};
\node[card] at (5.9,0.2) {W}; \node at (7.2,0.2) {waiting};
\draw[->] (8,1.3) -- (8.7,1.3);
\node at (10.9,2.7) {W cannot use slot 1};
\node at (9.8,2) {slot 1}; \node[card] at (9.45,1.3) {X}; \node[card] at (10.15,1.3) {Y};
\node at (11.6,2) {slot 2}; \node[card] at (11.6,1.3) {W};
\draw (9.4,-0.1) -- (10.8,-1.1) -- (12.2,-0.1);
\foreach \x/\y/\letter/\slot in {9.4/-0.1/X/1,12.2/-0.1/Y/1,10.8/-1.1/W/2}{
\node[draw,circle,fill=white,minimum size=0.9cm,inner sep=0pt] at (\x,\y) {};
\node[font=\scriptsize,yshift=2mm] at (\x,\y) {\letter};
\node[font=\scriptsize\bfseries,yshift=-2mm] at (\x,\y) {\slot};
}
\end{tikzpicture}
\end{center}
