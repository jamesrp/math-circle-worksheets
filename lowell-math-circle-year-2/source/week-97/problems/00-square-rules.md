+++
id = "w97.square-rules"
kind = "setup"
title = "Inputs, bundles and outputs"
grades = ["3-5"]
route = ["first", "return"]
+++

## text
An input of 3 means a $3\times3$ square of counters. Input 0 uses no counters. Remove complete bundles of the given size until fewer than one bundle's worth remain. The number left is the output; it can be 0. We compare outputs to find which square inputs they can hide.

\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth]
\node at(1.6,2.8){\small Input 3};
\foreach \x in {0,1,2} \foreach \y in {0,1,2} {\dotat{0.9+0.65*\x}{0.65+0.65*\y}}
\node at(1.6,0){\small $3\times3=9$ counters};
\draw[->,thick] (3.7,1.3)--(4.7,1.3);
\node at(7.25,2.8){\small Bundles of 4};
\foreach \a in {5.4,7.2} {
\draw[rounded corners=5pt] (\a,0.5) rectangle +(1.3,1.6);
\foreach \x in {0,1} \foreach \y in {0,1} {\dotat{\a+0.35+0.6*\x}{0.95+0.7*\y}}}
\dotat{9.2}{1.3}
\node at(7.35,0){\small $9=4+4+1$};
\draw[->,thick] (10.1,1.3)--(11.1,1.3);
\node at(13,2.8){\small Output 1};
\dotat{13}{1.3}
\node at(13,0){\small 1 counter left};
\end{tikzpicture}
\end{center}

With bundles of 4 and only inputs 0--3:
\begin{center}
\setlength{\tabcolsep}{15pt}
\begin{tabular}{r|cccc}
Input & 0 & 1 & 2 & 3\\
Output & 0 & 1 & 0 & 1
\end{tabular}
\end{center}
Output 1 hides two possible inputs: 1 and 3. There are two different outputs: 0 and 1.
