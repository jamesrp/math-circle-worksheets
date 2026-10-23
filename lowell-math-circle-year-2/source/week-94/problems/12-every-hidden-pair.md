+++
id = "w94.every-hidden-pair"
title = "Every pair of hidden lengths"
grades = ["K-1", "2-3"]
route = "first"
page = "new"
kernel = 'Reports 7 and 10 fit six pairs, one for each extra: (6, 9), (5, 8), (4, 7), (3, 6), (2, 5), (1, 4). In K--1, towers that come out as 4 and 6 with extras 1--3 went in as (3, 5), (2, 4) or (1, 3); Q is always 2 taller.'
+++

## prompt [K-1]
P and Q went into the same machine: build and color every pair of towers that could have gone in. Could P be taller than Q?

## prompt
Two hidden strips give these reports. Find every possible pair of lengths.

## text [K-1]
\begin{center}\begin{tikzpicture}[x=7mm,y=7mm]
\node at(1.75,7.1){came out};
\tcubes{0}{0}{4}\node[below]at(.5,0){P};
\tcubes{2.5}{0}{6}\node[below]at(3,0){Q};
\draw[gray](4.75,-1)--(4.75,7.6);
\node at(13.25,7.1){could have gone in};
\foreach\s in{0,...,3}{\tcells{6+4*\s}{0}{6}\node[below]at(6.5+4*\s,0){P};\tcells{7.5+4*\s}{0}{6}\node[below]at(8+4*\s,0){Q};}
\end{tikzpicture}\end{center}

## text
\begin{center}\begin{tikzpicture}[font=\large]
\node[draw,minimum width=5cm,minimum height=1.8cm] at(0,0){P reports 7};
\node[draw,minimum width=5cm,minimum height=1.8cm] at(7,0){Q reports 10};
\end{tikzpicture}\end{center}
\begin{center}\begin{tabular}{|p{4.3cm}|p{4.3cm}|p{4.3cm}|}\hline
Length of P & Length of Q & Extra number \\\hline
\rule{0pt}{15mm}&&\\\hline\rule{0pt}{15mm}&&\\\hline\rule{0pt}{15mm}&&\\\hline\rule{0pt}{15mm}&&\\\hline\rule{0pt}{15mm}&&\\\hline\rule{0pt}{15mm}&&\\\hline\rule{0pt}{15mm}&&\\\hline
\end{tabular}\end{center}
