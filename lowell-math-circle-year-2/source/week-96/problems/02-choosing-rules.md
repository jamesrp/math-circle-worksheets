+++
id = "w96.choosing-rules"
kind = "setup"
title = "Choose tokens from a bag"
grades = ["2-3", "4-5"]
route = ["first", "return"]
page = "new"
+++

## text
Choose some tokens from a bag, using each token at most once. The chosen tokens form a bag. You may choose all of them or none. An empty bag has value 1. A divisor of a whole number divides it with no remainder.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth]
\draw[rounded corners=9pt](-.5,-.45) rectangle(2.3,.45);
\node[draw,circle,minimum size=.55cm] at(0,0){2};
\node[draw,circle,minimum size=.55cm] at(.85,0){2};
\node[draw,circle,minimum size=.55cm] at(1.7,0){5};
\draw[->](2.6,0)--(3.2,0);
\draw[rounded corners=9pt](3.5,-.45) rectangle(6.3,.45);
\node[draw,circle,minimum size=.55cm,fill=gray!20] at(4,0){2};
\node[draw,circle,minimum size=.55cm] at(4.85,0){2};
\node[draw,circle,minimum size=.55cm,fill=gray!20] at(5.7,0){5};
\draw[->](6.6,0)--(7.2,0);
\draw[rounded corners=9pt](7.5,-.45) rectangle(9.6,.45);
\node[draw,circle,minimum size=.55cm] at(8,0){2};
\node[draw,circle,minimum size=.55cm] at(9.1,0){5};
\node at(.85,-.85){value 20};\node at(4.9,-.85){choose shaded tokens};\node at(8.55,-.85){value 10};
\node at(4.7,-1.45){$2\times5=10\qquad 20\div10=2$};
\end{tikzpicture}
\end{center}
