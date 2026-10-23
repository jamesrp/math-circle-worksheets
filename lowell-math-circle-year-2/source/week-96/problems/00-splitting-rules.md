+++
id = "w96.splitting-rules"
kind = "setup"
title = "Split a card until every card is prime"
grades = ["2-3", "4-5"]
route = ["first", "return"]
+++

## text
A number card can split into two whole numbers greater than 1 that multiply to its value. These numbers are its factors. Keep splitting until every card is prime: a number greater than 1 with no factors except 1 and itself. The finished cards make a prime bag. Multiply its tokens to find its value.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth]
\node[draw,rounded corners,minimum width=1cm,minimum height=.7cm] at (0,0){20};
\draw[->] (.7,0)--(1.4,0);
\node[draw,minimum size=.7cm] at (2,0){4};\node at (2.6,0){$\times$};\node[draw,minimum size=.7cm] at (3.2,0){5};
\draw[->] (3.8,0)--(4.5,0);
\draw[rounded corners=9pt](4.8,-.48) rectangle(7.5,.48);
\foreach \v [count=\i from 0] in {2,2,5}{\node[draw,circle,minimum size=.55cm,inner sep=0pt] at(5.3+.85*\i,0){\v};}
\node at (0,-.85){card};\node at (2.6,-.85){$4\times5=20$};\node at (6.15,-.85){$2\times2\times5=20$};
\end{tikzpicture}
\end{center}
Token order does not matter. Equal tokens are interchangeable.
