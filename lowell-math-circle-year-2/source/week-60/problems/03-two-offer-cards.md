+++
id = "w60.two-offer-cards"
title = "Best first-offer choices on nine two-offer cards"
grades = ["shared"]
route = "first"
page = "new"
kernel = "All nine equally likely two-offer cards evaluate a fixed rule exactly; take 4 or 6 first and pass 0 for a total of 40."
+++

## text
\renewcommand{\band}{Grades 3--5}
A card lists offers in drawing order, including offers that would remain unseen after you take one. All complete cards of the same length have the same chance.

With practice tickets 1, 3, 5, this rule takes 3 or 5 and passes 1:
\begin{center}
\begin{tikzpicture}[x=1in,y=1in,>=Latex]
  \draw (0,0.06) rectangle (1.55,0.72);
  \node[font=\large] at (0.43,0.40) {3};
  \node[font=\large] at (1.12,0.40) {1};
  \draw[gray] (0.77,0.20) -- (0.77,0.60);
  \node[font=\small] at (0.78,-0.19) {complete card};
  \draw[->] (1.66,0.39) -- (2.30,0.39);
  \node[draw,align=center,minimum width=2.15in,minimum height=0.66in] at (3.46,0.39) {take the first offer: 3\\the later 1 is unseen};
  \draw[->] (4.62,0.39) -- (5.23,0.39);
  \node[draw,minimum width=1.15in,minimum height=0.66in] at (5.87,0.39) {score 3};
\end{tikzpicture}
\end{center}

## prompt
Find first-offer choices for 0, 4 and 6 that give the highest total score on all nine cards. Use the same choices on every card. The second offer must be taken if you reach it.

## text
\begin{center}
\begin{tikzpicture}[x=1in,y=1in]
\foreach \a [count=\r from 0] in {0,4,6}{
\foreach \b [count=\c from 0] in {0,4,6}{
\cardtwo{\c*2.28}{(2-\r)*1.01}{\a}{\b}
}}
\end{tikzpicture}
\end{center}

\vspace{0.15in}
\begin{tabular}{@{}p{2.06in}p{2.06in}p{2.06in}@{}}
First offer 0: & First offer 4: & First offer 6:\\[0.30in]
\rule{1.9in}{0.3pt} & \rule{1.9in}{0.3pt} & \rule{1.9in}{0.3pt}
\end{tabular}

\vspace{0.24in}
Total score on nine cards: \rule{1.55in}{0.3pt}
\blanklines{2}
