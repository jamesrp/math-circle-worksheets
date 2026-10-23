+++
id = "w73.halfway-hunt"
title = "Hunt with halfway dots for the surviving positions of O"
grades = ["4-5"]
route = "first"
page = "new"
kernel = "With triangles moved evenly, the side-midpoint tests rule out every O except the center, the only point inside both unit disks about (1,0) and (1,2)."
+++

## prompt
Your partner places O inside the square. Join it to all four corners. Each old triangle moves evenly onto its matching new triangle: straight segments stay straight, and halfway points stay halfway. Add halfway dots on triangle edges and hunt for a pair that stretches more than any pair of the original five dots. Swap jobs. Which positions for O survive your tests?

## text
\begin{center}\begin{tikzpicture}[x=.7in,y=.7in,font=\small,>=Stealth]
\draw(0,0)--(2,0)--(0,1.3)--cycle;
\fill(0,0)circle(2pt)node[below]{P};\fill(2,0)circle(2pt)node[below]{Q};\fill(0,1.3)circle(2pt)node[above]{R};
\fill(1,0)circle(2pt)node[below]{M};\fill(0,.65)circle(2pt)node[left]{N};\draw[dashed](1,0)--(0,.65);
\draw[->](2.6,.65)--(3.6,.65);
\draw(4.2,0)--(6.2,0)--(5.1,1.3)--cycle;
\fill(4.2,0)circle(2pt)node[below]{P};\fill(6.2,0)circle(2pt)node[below]{Q};\fill(5.1,1.3)circle(2pt)node[above]{R};
\fill(5.2,0)circle(2pt)node[below]{M};\fill(4.65,.65)circle(2pt)node[left]{N};\draw[dashed](5.2,0)--(4.65,.65);
\end{tikzpicture}\end{center}
\fanboard
\vspace{.1in}
O's position: \hrulefill
\answerline\answerline\answerline
