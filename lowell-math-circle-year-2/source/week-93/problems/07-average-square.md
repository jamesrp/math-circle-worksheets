+++
id = "w93.average-square"
title = "Is the average-side square always bigger?"
grades = ["3-5"]
route = "return"
page = "new"
kernel = '$m^2-ab=((b-a)/2)^2$: a cut-and-rearrange picture shows the extra square.'
+++

## text
\renewcommand{\band}{Grades 4--5, ready for general reasoning}

## prompt
For any rectangle, is the square whose side is the average of the rectangle's sides always at least as large in area? Explain with a cut-and-rearrange picture. How much extra area does the square have?

## text
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]
\draw[thick] (0,0) rectangle (7,3);
\node[below] at (3.5,0) {long side};\node[left,rotate=90,anchor=south] at (0,1.5) {short side};
\draw[thick] (10,-1) rectangle (15,4);
\node[below,align=center] at (12.5,-1) {average of\\the two sides};
\end{tikzpicture}
\end{center}
\vspace{19mm}
