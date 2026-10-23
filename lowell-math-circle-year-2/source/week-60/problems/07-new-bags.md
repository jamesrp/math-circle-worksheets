+++
id = "w60.new-bags"
title = "Best first-offer choices for new bags"
grades = ["shared"]
route = "first"
page = "new"
kernel = "For 0, 3, 6 taking or passing 3 ties at 36; for 0, 5, 6 take 5 or 6 first for 44; for 0, 2, 6 pass 0 and 2 and take 6 for 34."
+++

## text
\renewcommand{\band}{Grades K--5}

## prompt
For each new bag, find all the first-offer choices that give the highest total score on its nine two-offer cards.

## text
\vspace{0.07in}
\begin{tikzpicture}[x=1in,y=1in]
\node[font=\normalsize,anchor=west] at (0,3.23) {Bag: 0, 3, 6};
\foreach \a [count=\r from 0] in {0,3,6}{
\foreach \b [count=\c from 0] in {0,3,6}{
\cardtwo{\c*2.28}{(2-\r)*1.01}{\a}{\b}
}}
\end{tikzpicture}

Choices: \rule{4.32in}{0.3pt}\hspace{0.16in}Total: \rule{0.82in}{0.3pt}

\vspace{0.16in}
\begin{tikzpicture}[x=1in,y=1in]
\node[font=\normalsize,anchor=west] at (0,3.23) {Bag: 0, 5, 6};
\foreach \a [count=\r from 0] in {0,5,6}{
\foreach \b [count=\c from 0] in {0,5,6}{
\cardtwo{\c*2.28}{(2-\r)*1.01}{\a}{\b}
}}
\end{tikzpicture}

Choices: \rule{4.32in}{0.3pt}\hspace{0.16in}Total: \rule{0.82in}{0.3pt}
