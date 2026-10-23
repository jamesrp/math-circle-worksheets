+++
id = "w89.one-tray-order"
title = "Does the order of inputs matter?"
grades = ["K-5"]
route = "return"
page = "new"
kernel = "A single tray keeps every counter, so every order of the inputs gives the same final total."
+++

## prompt
Can the order of these inputs change the final total? Use each shown input once. Try a tray starting at 0, then a tray starting at 3.

## text
\begin{center}\slips{0,1,2,3,4}\end{center}
Use the supplied input cards. An input tells how many counters to add. Keep the counters already in the tray. The number in the tray is its total. You may replace counters by one card showing their total.

\begin{center}\begin{tikzpicture}[x=1cm,y=1cm]
\tray{0}{0}{total before}{2}
\node[draw,minimum width=1cm,minimum height=.8cm] at (2.8,.6){3};
\node[font=\small] at (2.8,-.25){input};
\draw[-{Latex}] (3.5,.6)--(4.1,.6);
\draw[rounded corners=3pt] (4.4,0) rectangle (7,1.15);
\foreach \x in {4.8,5.2}{\filldraw[fill=white] (\x,.6) circle (.12);}
\foreach \x in {5.8,6.2,6.6}{\filldraw[fill=black!25] (\x,.6) circle (.12);}
\node[font=\small] at (5.7,-.25){2 kept + 3 added};
\draw[-{Latex}] (7.3,.6)--(7.9,.6);
\tray{8.3}{0}{total after}{5}
\node[font=\small,align=center] at (5,1.8){one turn: add 3 counters};
\end{tikzpicture}\end{center}
\answer{20mm}
