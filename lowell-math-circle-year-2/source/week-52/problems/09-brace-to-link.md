+++
id = "w52.brace-to-link"
kind = "setup"
title = "From a brace to a link: worked example"
grades = ["K-5"]
route = "first"
page = "new"
+++

## text
\band{Grades 3--5}
\fontsize{13.5}{18}\selectfont
A brace becomes a link between its row dot and its column dot. Keep all the dots. Links may cross; a crossing is not a dot.
\vspace{5pt}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\node at (2.15,1.45) {frame};
\node at (7.0,1.45) {cell labels};
\node at (12.0,1.45) {links};
\node at (2.15,0) {\gridpic{1}{3}{11}{1/2}{0}};
\node at (7.0,0) {\gridpic{1}{3}{11}{1/2}{1}};
\node at (12.0,-0.15) {\linkpic{1}{3}{1.7}{1/2}};
\draw[-{Stealth[length=2.2mm]},line width=0.8pt] (4.15,0)--(4.8,0);
\draw[-{Stealth[length=2.2mm]},line width=0.8pt] (9.15,0)--(9.8,0);
\node[font=\fontsize{11}{13}\selectfont] at (7.0,-1.3) {R1 and C2};
\end{tikzpicture}
\end{center}
