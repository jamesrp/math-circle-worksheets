+++
id = "w60.plans-a-and-b"
title = "Compare two plans on 27 three-offer cards"
grades = ["shared"]
route = "first"
page = "new"
kernel = "With three offers, passing a first 4 does better: plan B totals 134 against plan A's 130."
+++

## text
\renewcommand{\band}{Grades 3--5}

## prompt
Which plan gives the higher total score on these 27 three-offer cards? Use every card for each plan, including cards with the same score.

## text
A: Take 4 or 6 whenever it appears. Pass 0.\par
B: Take only 6 on the first offer. On the second, take 4 or 6 and pass 0.\par
Both plans take the last offer if they reach it.

A's total: \rule{1.12in}{0.3pt}\hspace{0.45in}B's total: \rule{1.12in}{0.3pt}

\vspace{-0.02in}
\begin{center}
\begin{tikzpicture}[x=1in,y=1in]
\foreach \a [count=\r from 0] in {0,4,6}{
\foreach \b [count=\s from 0] in {0,4,6}{
\foreach \c [count=\t from 0] in {0,4,6}{
\cardthree{\t*2.28}{(8-3*\r-\s)*0.77}{\a}{\b}{\c}
}}}
\end{tikzpicture}
\end{center}
