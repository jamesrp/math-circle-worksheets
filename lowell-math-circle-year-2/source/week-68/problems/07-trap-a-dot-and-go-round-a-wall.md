+++
id = "w68.trap-a-dot-and-go-round-a-wall"
title = "Trap a dot, and go round a wall"
grades = ["3-5"]
route = "return"
kernel = "Blockers on the grid can trap finite pockets, but a finite wall can be walked round."
+++

## prompt
On the left grid, use four blockers to trap an open dot. On the right grid, the five X dots are closed. Join P to Q by an open route. Which pieces on each map keep going forever?

## text
\vspace{.2in}
\begin{center}
\begin{tikzpicture}[x=1cm,y=1cm]\grid\end{tikzpicture}\hfill
\begin{tikzpicture}[x=1cm,y=1cm]\grid
\foreach \y in {-2,...,2}\node[fill=white,inner sep=0pt,font=\bfseries\large] at (0,\y){X};
\node[draw,circle,fill=white,inner sep=2pt] at (-2,0){P};\node[draw,circle,fill=white,inner sep=2pt] at (2,0){Q};
\end{tikzpicture}
\end{center}
\vspace{.2in}
