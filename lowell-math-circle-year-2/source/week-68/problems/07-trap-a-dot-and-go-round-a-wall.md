+++
id = "w68.trap-a-dot-and-go-round-a-wall"
title = "Trap a dot, and go round a wall"
grades = ["3-5"]
route = "return"
kernel = "Blockers on the grid can trap finite pockets, but a finite wall can be walked round."
+++

## prompt
On the left grid, use four blockers to trap an open dot. On the right grid, the seven X dots are closed. Join P to Q by an open route. Which pieces on each map keep going forever?

## text
\vspace{.45in}
\begin{center}
\begin{tikzpicture}[x=1.2cm,y=1.2cm]\grid\end{tikzpicture}\hfill
\begin{tikzpicture}[x=1.2cm,y=1.2cm]\grid
\foreach \y in {-3,...,3}\node[fill=white,inner sep=0pt,font=\bfseries\large] at (0,\y){X};
\node[draw,circle,fill=white,inner sep=2pt] at (-2,0){P};\node[draw,circle,fill=white,inner sep=2pt] at (2,0){Q};
\end{tikzpicture}
\end{center}
\vspace{.2in}
