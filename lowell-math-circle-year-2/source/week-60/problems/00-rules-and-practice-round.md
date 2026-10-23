+++
id = "w60.rules-and-practice-round"
kind = "setup"
title = "Draw rules, turn counters and a practice round"
grades = ["shared"]
route = ["first", "return"]
kernel = "Each offer is a fresh draw from a known bag (a die with each number on two faces draws the same way); take ends the round, a pass is permanent and the last offer must be taken."
+++

## text
\renewcommand{\band}{Grades K--5}
Each bag has one ticket marked 0, one marked 4 and one marked 6. Each has the same chance. Every offer is a fresh draw from the whole bag: roll the bag's die, or put the ticket back and mix.

Set the number of offers before a round, and put out one turn counter for each offer. Your partner shows each offer. Take it to end the round, or pass it forever. With one counter left, you must take the offer, even if it is 0. Remove one turn counter after deciding on each offer. Only the offer you take scores.

A practice round uses different tickets: 1, 2, 5.

\begin{center}
\begin{tikzpicture}[x=1in,y=1in,>=Latex]
  \node[draw,minimum width=1.34in,minimum height=0.83in,align=center] at (0.8,0.45) {offer 2\\two counters};
  \node[draw,minimum width=1.83in,minimum height=0.83in,align=center] at (3.02,0.45) {pass 2\\one counter left};
  \node[draw,minimum width=1.57in,minimum height=0.83in,align=center] at (5.55,0.45) {next offer 1\\must take 1};
  \draw[->] (1.48,0.45) -- (2.07,0.45);
  \draw[->] (3.96,0.45) -- (4.72,0.45);
  \node at (5.55,-0.19) {round score: 1};
\end{tikzpicture}
\end{center}
