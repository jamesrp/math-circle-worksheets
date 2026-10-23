+++
id = "w89.corner-piles"
title = "Corner piles"
grades = ["K-5"]
route = "return"
page = "new"
kernel = "Each pile is the previous pile on the next staircase, so its total follows the third tray."
+++

## prompt
Build these corner piles for steps 3, 4 and 5. Can they explain the third tray's totals when every input is 1?

## text
At step 1, use one cube. At step 2, stack the step-1 pile on a bottom layer of 2-row stairs. At step 3, stack the step-2 pile on a bottom layer of 3-row stairs. Continue in the same way, keeping the square corners aligned.

\begin{center}\begin{tikzpicture}[x=1cm,y=1cm]
\node at (1,3){step-1 pile};
\begin{scope}[shift={(.4,.3)},x={(7mm,0)},y={(3.5mm,2.6mm)},z={(0,7mm)}]
\filldraw[fill=black!6] (0,0,0)--(1,0,0)--(1,0,1)--(0,0,1)--cycle;
\filldraw[fill=black!20] (1,0,0)--(1,1,0)--(1,1,1)--(1,0,1)--cycle;
\filldraw[fill=black!10] (0,0,1)--(1,0,1)--(1,1,1)--(0,1,1)--cycle;
\end{scope}\draw[-{Latex}] (2.5,1.2)--(3.4,1.2);\node[align=center,font=\small] at (5,3){put it on the square corner\\of a 2-row bottom layer};\begin{scope}[shift={(4.2,.3)},x={(7mm,0)},y={(3.5mm,2.6mm)},z={(0,7mm)}]
\filldraw[fill=black!6] (0,1,0)--(1,1,0)--(1,1,1)--(0,1,1)--cycle;
\filldraw[fill=black!20] (1,1,0)--(1,2,0)--(1,2,1)--(1,1,1)--cycle;
\filldraw[fill=black!10] (0,1,1)--(1,1,1)--(1,2,1)--(0,2,1)--cycle;
\filldraw[fill=black!6] (0,0,0)--(1,0,0)--(1,0,1)--(0,0,1)--cycle;
\filldraw[fill=black!20] (1,0,0)--(1,1,0)--(1,1,1)--(1,0,1)--cycle;
\filldraw[fill=black!10] (0,0,1)--(1,0,1)--(1,1,1)--(0,1,1)--cycle;
\filldraw[fill=black!6] (1,0,0)--(2,0,0)--(2,0,1)--(1,0,1)--cycle;
\filldraw[fill=black!20] (2,0,0)--(2,1,0)--(2,1,1)--(2,0,1)--cycle;
\filldraw[fill=black!10] (1,0,1)--(2,0,1)--(2,1,1)--(1,1,1)--cycle;
\begin{scope}[shift={(0,0,1.8)}]\filldraw[fill=black!6] (0,0,0)--(1,0,0)--(1,0,1)--(0,0,1)--cycle;
\filldraw[fill=black!20] (1,0,0)--(1,1,0)--(1,1,1)--(1,0,1)--cycle;
\filldraw[fill=black!10] (0,0,1)--(1,0,1)--(1,1,1)--(0,1,1)--cycle;
\end{scope}\draw[dashed,-{Latex}] (.4,.4,1.7)--(.4,.4,1.05);\end{scope}\draw[-{Latex}] (6.7,1.2)--(7.6,1.2);\node at (9.3,3){step-2 pile};\begin{scope}[shift={(8.5,.3)},x={(7mm,0)},y={(3.5mm,2.6mm)},z={(0,7mm)}]
\filldraw[fill=black!6] (0,1,0)--(1,1,0)--(1,1,1)--(0,1,1)--cycle;
\filldraw[fill=black!20] (1,1,0)--(1,2,0)--(1,2,1)--(1,1,1)--cycle;
\filldraw[fill=black!10] (0,1,1)--(1,1,1)--(1,2,1)--(0,2,1)--cycle;
\filldraw[fill=black!6] (0,0,0)--(1,0,0)--(1,0,2)--(0,0,2)--cycle;
\filldraw[fill=black!20] (1,0,0)--(1,1,0)--(1,1,2)--(1,0,2)--cycle;
\filldraw[fill=black!10] (0,0,2)--(1,0,2)--(1,1,2)--(0,1,2)--cycle;
\filldraw[fill=black!6] (1,0,0)--(2,0,0)--(2,0,1)--(1,0,1)--cycle;
\filldraw[fill=black!20] (2,0,0)--(2,1,0)--(2,1,1)--(2,0,1)--cycle;
\filldraw[fill=black!10] (1,0,1)--(2,0,1)--(2,1,1)--(1,1,1)--cycle;
\draw (0,0,1)--(1,0,1)--(1,1,1);\end{scope}
\end{tikzpicture}\end{center}
\answer{20mm}
