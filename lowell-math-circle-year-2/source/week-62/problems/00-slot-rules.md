+++
id = "w62.slot-rules"
title = "Cards, conflict lines and slots"
kind = "setup"
grades = ["shared"]
route = ["first", "return"]
+++

## text
Each circle is one activity card. A line means its two cards cannot share a slot. Put every card in one slot. A slot can hold any number of cards if none of them conflict. Only marked circles are activities; line crossings add none. Write a card's slot number in its circle.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,font=\small,card/.style={draw,minimum width=0.55cm,minimum height=0.7cm,fill=white},>=Stealth]
\node at (1.3,2) {conflicts};
\draw (0.1,1) -- (1.4,1);
\node[draw,circle,fill=white,minimum size=0.7cm] at (0.1,1) {X};
\node[draw,circle,fill=white,minimum size=0.7cm] at (1.4,1) {Y};
\node[draw,circle,fill=white,minimum size=0.7cm] at (2.7,1) {Z};
\draw[->] (3.4,1) -- (4.1,1);
\node at (5.7,2) {X and Y placed};
\node at (4.7,1.5) {slot 1}; \node[card] at (4.7,0.8) {X};
\node at (6,1.5) {slot 2}; \node[card] at (6,0.8) {Y};
\node[card] at (7.3,0.8) {Z}; \node at (7.3,0.1) {waiting};
\draw[->] (8,1) -- (8.7,1);
\node at (10.9,2) {one finished schedule};
\node at (9.8,1.5) {slot 1}; \node[card] at (9.45,0.8) {X}; \node[card] at (10.15,0.8) {Z};
\node at (11.5,1.5) {slot 2}; \node[card] at (11.5,0.8) {Y};
\draw (9.4,-0.4) -- (10.8,-0.4);
\foreach \x/\letter/\slot in {9.4/X/1,10.8/Y/2,12.2/Z/1}{
\node[draw,circle,fill=white,minimum size=0.9cm,inner sep=0pt] at (\x,-0.4) {};
\node[font=\scriptsize] at (\x,-0.2) {\letter};
\node[font=\scriptsize\bfseries] at (\x,-0.6) {\slot};
}
\end{tikzpicture}
\end{center}
