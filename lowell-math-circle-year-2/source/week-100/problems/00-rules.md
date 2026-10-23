+++
id = "w100.rules"
kind = "setup"
title = "Groups, labels and distance, with a worked example"
grades = ["3-5"]
route = ["first", "return"]
+++

## text
% Page 1: conventions, non-task example, concrete entry, reusable cards.
\txt{0}{0}{250}{Groups can sit inside one another or be separate. They never cross. One group contains all the cards. Each card is also a one-card group. A group may contain three or more smaller groups. Every larger group has a positive label, and labels increase as you go outward. A group's size and number of cards do not determine its label.}
\txt{0}{27}{250}{The distance between two different cards is the label of their smallest common group. A card's distance from itself is 0. We write A--B for the distance between A and B.}
% Worked visual: input, selected smallest common group, output.
\begin{scope}[shift={(2,51)}]
\draw[rounded corners=3mm,line width=1.7pt] (0,0) rectangle (111,39);\grouplabel{105}{0}{6}
\draw[rounded corners=3mm,line width=.7pt] (5,7) rectangle (66,31);\grouplabel{60}{7}{3}
\card{22}{21}{X}\card{48}{21}{Y}\card{88}{21}{Z}
\smalltxt{0}{44}{114}{X and Z $\longrightarrow$ the thick group is their smallest common group $\longrightarrow$ X--Z = 6.}
\smalltxt{0}{63}{114}{X--Y = 3.\qquad X--X = 0.}
\end{scope}
